# Web 우선 적용 Top 3

운영 장애 대응과 배포 안정성에 즉시 사용할 수 있는 Skill을 우선한다.

| 순위 | Skill | 선정 이유 | 1차 성공지표 |
|---:|---|---|---|
| 1 | `api-incident-analysis` | Web 장애의 중심인 API 실패를 Gateway/Backend/DB/외부 연계로 구간 분리 | 최초 실패 구간과 의존성 근거 제시 |
| 2 | `auth-session-diagnosis` | 로그인/권한/Session 장애는 원인 혼동이 많고 보안 영향이 큼 | 401/403/Session/Browser 정책 분리 |
| 3 | `smoke-test` | 배포 직후 최소 시간으로 서비스 사용 가능 여부 판단 | PASS/CONDITIONAL/FAIL Evidence 확보 |

## 적용 원칙
- 운영 장애/배포 결과를 Eval에 추가해 회귀 검증한다.
- Token·Session·개인정보 원문을 Test/Eval에 저장하지 않는다.
- 운영 설정 변경과 Rollback은 Human Gate를 유지한다.