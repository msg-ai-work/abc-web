---
name: auth-session-diagnosis
summary: 로그인, 인증, 인가, Session, Role 기반 권한 오류를 진단한다.
version: "0.1"
---
# Auth / Session Diagnosis
## 절차
1. 인증 실패인지 인가 실패인지 구분한다.
2. 사용자 Role과 요청 Resource 권한을 비교한다.
3. Session/Token 생성·만료·갱신 흐름을 확인한다.
4. Cookie/SameSite/CORS/Redirect 영향을 확인한다.
5. Backend 권한 검증과 Frontend 노출 제어를 분리한다.
6. 최근 인증서/SSO/정책 변경 여부를 확인한다.
## Guardrail
Token, Session ID, 개인정보 원문은 저장소에 기록하지 않는다.
