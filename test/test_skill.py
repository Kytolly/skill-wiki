#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Automated tests for skill-tutorial-wiki tooling."""
import json
import os
import shutil
import yaml
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIX = os.path.join(ROOT, "test", "fixtures")
PY = shutil.which("python3") or sys.executable
os.makedirs(os.path.join(ROOT, "build"), exist_ok=True)
MODES = ["course", "project-docs", "lab-sop", "technical-tutorial"]


def run(cmd, cwd=ROOT):
    return subprocess.run(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)


def run_validate(root):
    return run([PY, "script/validate.py", "--wiki-root", root, "--out", "qa-test.json"])


def run_coverage(root):
    return run([PY, "script/coverage.py", "--wiki-root", root, "--out", "coverage-test.json"])


def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def fixture(name):
    return os.path.join(FIX, name)


def copy_fixture(name, tmp):
    dst = os.path.join(tmp, name)
    shutil.copytree(fixture(name), dst)
    return dst


class TestValidFixtures(unittest.TestCase):
    def test_validators_pass_on_all_fixtures(self):
        for mode in MODES:
            with self.subTest(mode=mode):
                r = run_validate(fixture(mode))
                self.assertEqual(r.returncode, 0, r.stdout)
                rep = read_json(os.path.join(fixture(mode), "build", "qa-test.json"))
                self.assertEqual(rep["summary"]["error"], 0)

    def test_coverage_pass_on_all_fixtures(self):
        for mode in MODES:
            with self.subTest(mode=mode):
                r = run_coverage(fixture(mode))
                self.assertEqual(r.returncode, 0, r.stdout)
                rep = read_json(os.path.join(fixture(mode), "build", "coverage-test.json"))
                self.assertEqual(rep["summary"]["missing"], 0)

    def test_build_produces_docs(self):
        root = fixture("course")
        r = run([PY, "script/build.py", "--wiki-root", root])
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertTrue(os.path.exists(os.path.join(root, "build", "preview", "docs", "index.md")))


class TestNegative(unittest.TestCase):
    def _run_find_status(self, root, check_id):
        r = run_validate(root)
        rep = read_json(os.path.join(root, "build", "qa-test.json"))
        checks = {c["id"]: c for c in rep["checks"]}
        return r.returncode, checks.get(check_id, {})

    def test_unsupported_claim_detected(self):
        with tempfile.TemporaryDirectory(dir=os.path.join(ROOT, "build")) as tmp:
            root = copy_fixture("technical-tutorial", tmp)
            # remove evidence from the only claim
            path = os.path.join(root, "_meta", "claims.yaml")
            data = yaml.safe_load(open(path, encoding="utf-8"))
            data["claims"][0]["evidence_ids"] = []
            with open(path, "w", encoding="utf-8") as f:
                yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False)
            rc, check = self._run_find_status(root, "unsupported_claim")
            self.assertEqual(check.get("status"), "error")
            self.assertNotEqual(rc, 0)

    def test_figure_explanation_missing_detected(self):
        with tempfile.TemporaryDirectory(dir=os.path.join(ROOT, "build")) as tmp:
            root = copy_fixture("course", tmp)
            path = os.path.join(root, "_meta", "figures.yaml")
            text = open(path, encoding="utf-8").read()
            import re
            text = re.sub(r"explanation:.*\n", "explanation: null\n", text)
            open(path, "w", encoding="utf-8").write(text)
            rc, check = self._run_find_status(root, "figure_explanation")
            self.assertEqual(check.get("status"), "error")

    def test_broken_wiki_link_detected(self):
        with tempfile.TemporaryDirectory(dir=os.path.join(ROOT, "build")) as tmp:
            root = copy_fixture("technical-tutorial", tmp)
            page = os.path.join(root, "page", "basics", "示例页面.md")
            open(page, "a", encoding="utf-8").write("\n[[不存在的页面]]\n")
            rc, check = self._run_find_status(root, "dead_wiki_links")
            self.assertEqual(check.get("status"), "error")

    def test_meta_completeness_detected(self):
        with tempfile.TemporaryDirectory(dir=os.path.join(ROOT, "build")) as tmp:
            root = copy_fixture("technical-tutorial", tmp)
            meta = os.path.join(root, "page", "_META.md")
            open(meta, "a", encoding="utf-8").write("")  # no-op
            # remove a required field line
            lines = open(meta, encoding="utf-8").read().splitlines()
            lines = [ln for ln in lines if "- completeness_policy:" not in ln]
            open(meta, "w", encoding="utf-8").write("\n".join(lines) + "\n")
            rc, check = self._run_find_status(root, "meta_completeness")
            self.assertEqual(check.get("status"), "error")

    def test_terminology_preservation_warn(self):
        with tempfile.TemporaryDirectory(dir=os.path.join(ROOT, "build")) as tmp:
            root = copy_fixture("technical-tutorial", tmp)
            page = os.path.join(root, "page", "basics", "示例页面.md")
            text = open(page, encoding="utf-8").read().replace("Example Protocol", "示例协议")
            open(page, "w", encoding="utf-8").write(text)
            rc, check = self._run_find_status(root, "terminology_preservation")
            self.assertEqual(check.get("status"), "warn")


class TestMigration(unittest.TestCase):
    def test_legacy_wiki_migrated(self):
        with tempfile.TemporaryDirectory(dir=os.path.join(ROOT, "build")) as tmp:
            root = copy_fixture("technical-tutorial", tmp)
            # remove _meta to simulate legacy
            shutil.rmtree(os.path.join(root, "_meta"))
            r = run([PY, "script/migrate.py", "--wiki-root", root])
            self.assertEqual(r.returncode, 0)
            self.assertTrue(os.path.exists(os.path.join(root, "_meta", "status.yaml")))
            meta = open(os.path.join(root, "page", "_META.md"), encoding="utf-8").read()
            self.assertIn("provenance: legacy-unverified", meta)
            # idempotent
            r2 = run([PY, "script/migrate.py", "--wiki-root", root])
            self.assertIn("already present", r2.stdout)


if __name__ == "__main__":
    unittest.main()
