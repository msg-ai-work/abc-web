# Eval — api-incident-analysis

## Case 1 — 외부 API 지연에 의한 504
**Input**
- Gateway: 504 증가
- Backend: 요청 처리 종료가 늦음
- DB P95: 정상
- 외부 API P95: 0.3s → 6s

**Expected Result**
- Gateway 자체보다 외부 API 지연에 따른 연쇄 Timeout을 우선 후보로 제시한다.
- DB를 원인으로 단정하지 않는다.
- 외부 연계 상태, Timeout Budget, Fail-fast/격리 여부를 추가 확인한다.

## Case 2 — 배포 직후 Backend 500
**Input**
- 특정 Endpoint만 500
- 신규 NullPointer 계열 Exception
- 배포 직후 시작
- DB/외부 API 정상

**Expected Result**
- Backend 변경 영향도를 우선 확인한다.
- 특정 Endpoint 영향 범위를 명시한다.
- 최근 Diff/입력 조건/Exception Stack을 연결한다.

## Fail Conditions
- 504를 무조건 Gateway 장애로 단정
- 최근 배포/의존성 확인 누락
- 운영 Timeout을 자동 변경