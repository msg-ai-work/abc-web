# Enterprise Messaging Web AI Harness

`abc-web`은 AX채널개발팀 기업메시징의 **Web Domain AI Harness** 저장소입니다.

## 역할

기업메시징 고객/관리자 Web의 Frontend, Backend, API 운영·개발 지식을 Domain Skill로 관리합니다.

## Common Harness

공통 Agent / Workflow / Rule / Guardrail은 `msg-ai-work/abc`를 SSOT로 사용합니다.
이 저장소는 공통 Harness를 복사해서 독립 관리하지 않습니다.

## 주요 영역

- Frontend / Backend
- API
- Authentication / Authorization / Session
- DB Query
- Browser Console / Network
- 외부 연계 Timeout
- 배포 / Smoke Test

## 운영 원칙

> 팀장은 AI가 일하는 방법을 관리하고, Domain 담당자는 AI가 알아야 할 업무를 관리합니다.

Skill 변경은 Branch → Pull Request → Review → main Merge 순서로 관리합니다.
