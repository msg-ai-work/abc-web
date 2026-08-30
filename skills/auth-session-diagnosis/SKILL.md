---
name: auth-session-diagnosis
summary: 로그인, 인증, 인가, Session/Token, Role 기반 권한 오류를 계층별로 분리해 진단한다.
version: "0.2"
priority: top-3
---
# Auth / Session Diagnosis

## 목적
로그인 실패, 401, 403, Session 만료, Redirect Loop를 하나의 '인증 문제'로 묶지 않고 인증(Authentication)과 인가(Authorization), Browser 정책을 분리한다.

## 입력
- 사용자 Role(개인 식별정보 제외)
- 실패 URL/API와 HTTP Status
- Token/Session의 원문이 아닌 생성·만료 시각
- Cookie 속성, CORS/Redirect 설정 요약
- 최근 SSO/인증서/정책 변경

## 절차
1. Credential 검증 단계 실패인지 확인한다.
2. 인증 성공 후 Resource 접근 권한 실패인지 확인한다.
3. Session/Token 생성→전달→만료→갱신 흐름을 확인한다.
4. Cookie Domain/Path/Secure/SameSite와 Browser 차단 여부를 확인한다.
5. CORS/Redirect Loop 여부를 확인한다.
6. Frontend 메뉴 노출과 Backend 권한 검증을 별도로 확인한다.

## 판단 기준
- **401:** 인증정보 없음/만료/검증 실패 우선
- **403:** 인증은 됐지만 Role/Policy 인가 실패 우선
- **로그인 성공 후 즉시 로그아웃:** Cookie/Session 저장·전달 우선
- **특정 Browser만 실패:** SameSite/Secure/CORS 등 Browser 정책 우선

## 대표 Case
> 비식별 대표 사례이며 실제 장애 기록이 아니다.

**현상:** 로그인 API는 200이나 다음 화면 API가 401이며 Browser에서 Session Cookie가 전송되지 않는다.

**판단:** 계정 권한보다 Cookie Domain/Secure/SameSite와 환경별 HTTPS 설정을 우선 확인한다. Token/Session 값 자체는 수집하지 않는다.

## 출력
실패 단계, 재현 조건, 근거, 영향 Role/Browser, 수정 후보, 재검증 절차.

## Guardrail
Token, Session ID, 이름/전화번호 등 개인정보 원문을 Git·Skill·Eval에 기록하지 않는다.