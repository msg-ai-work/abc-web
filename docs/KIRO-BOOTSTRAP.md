# Kiro Bootstrap

`bootstrap-harness`는 `msg-ai-work/abc`를 `.ai-harness/common`에 로컬 checkout하고, `enterprise-messaging-web` Agent가 중앙 Steering/Rule/Common Skill과 이 Repository의 `skills/**/SKILL.md`를 함께 Resources로 읽게 한다.

## 실행
```powershell
./scripts/bootstrap-harness.ps1
```
또는
```bash
bash scripts/bootstrap-harness.sh
```

## Kiro
Agent picker에서 `enterprise-messaging-web`을 선택한다.

## Version
초기 `harness.yaml`은 `ref: main`. 안정화 후 `v1.0.0` 같은 Tag로 Pin한다.

## 원칙
`.ai-harness/`는 Git 미추적이며, Common Rule을 Domain Repo로 복사해 수정하지 않는다. Production 변경은 Human Gate를 유지한다.
