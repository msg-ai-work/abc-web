# Eval — smoke-test

## Case 1 — 특정 Role 발송 불가
**Input**
- 로그인/메인/조회: 정상
- 운영 대상 Role의 발송 API: 403
- 다른 Role: 정상

**Expected Result**
- 전체 PASS로 처리하지 않는다.
- 해당 Role이 운영 대상이면 FAIL로 판정한다.
- `auth-session-diagnosis` 연계를 제시한다.
- Role/환경/HTTP Status를 Evidence로 기록한다.

## Case 2 — 비핵심 UI 경고
**Input**
- 핵심 사용자 경로: 모두 정상
- 신규 Critical Error: 없음
- 비핵심 화면에 경고성 Console 메시지 1건

**Expected Result**
- 자동 PASS가 아니라 영향도를 확인한 뒤 PASS 또는 CONDITIONAL 후보로 제시한다.
- 경고 내용과 영향 없음의 근거를 Evidence로 남긴다.

## Fail Conditions
- 일부 핵심 경로 미실행인데 PASS
- 발송/권한 오류를 비핵심으로 처리
- Evidence 없이 정상 판정