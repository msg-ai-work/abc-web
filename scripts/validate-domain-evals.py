#!/usr/bin/env python3
"""Validate Top 3 Domain Skill/Eval structure."""
from pathlib import Path
import re, sys
ROOT = Path(__file__).resolve().parents[1]
TOP3 = ROOT / "skills" / "TOP3.md"

def main():
    errors=[]
    def err(m): errors.append(m); print(f"::error::{m}")
    if not TOP3.exists(): err("skills/TOP3.md is required"); return 1
    skills=[]
    for line in TOP3.read_text(encoding="utf-8").splitlines():
        if line.lstrip().startswith("|"):
            m=re.search(r"`([a-z0-9-]+)`", line)
            if m and m.group(1) not in skills: skills.append(m.group(1))
    skills=skills[:3]
    if len(skills)!=3: err(f"TOP3.md must define exactly 3 skills; found {len(skills)}: {skills}")
    for skill in skills:
        sf=ROOT/"skills"/skill/"SKILL.md"; ef=ROOT/"evals"/skill/"EVAL.md"
        if not sf.exists(): err(f"missing Skill: skills/{skill}/SKILL.md"); continue
        if not ef.exists(): err(f"missing Eval: evals/{skill}/EVAL.md"); continue
        st=sf.read_text(encoding="utf-8"); et=ef.read_text(encoding="utf-8"); el=et.lower()
        vm=re.search(r'^version:\s*["\']?([0-9]+)\.([0-9]+)', st, re.MULTILINE)
        ver=(-1,-1) if not vm else (int(vm.group(1)),int(vm.group(2)))
        if ver < (0,2): err(f"{skill}: Top3 Skill version must be >= 0.2; found {ver}")
        if "priority: top-3" not in st: err(f"{skill}: frontmatter must contain priority: top-3")
        for section in ["## 입력","## 절차","## 출력"]:
            if section not in st: err(f"{skill}: missing required Skill section '{section}'")
        for marker in ["case 1","case 2","expected result"]:
            if marker not in el: err(f"{skill}: EVAL.md missing '{marker}'")
        if "fail conditions" not in el and "hard fail" not in el: err(f"{skill}: EVAL.md must define Fail Conditions or Hard Fail")
        print(f"OK {skill}: version {ver[0]}.{ver[1]}")
    if errors: print(f"FAILED: {len(errors)} contract error(s)"); return 1
    print(f"PASS: validated {len(skills)} Top3 skills and eval contracts"); return 0
if __name__ == "__main__": sys.exit(main())
