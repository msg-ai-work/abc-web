---
name: frontend-browser-diagnosis
summary: 화면 오류를 Browser Console, Network, FE 상태와 API 호출 기준으로 진단한다.
version: "0.1"
---
# Frontend / Browser Diagnosis
## 절차
1. 재현 Browser/Version/URL/사용자 조건을 기록한다.
2. Console JavaScript 오류를 확인한다.
3. Network 요청의 Status, Timing, Payload 형식을 확인한다.
4. FE 상태/라우팅/Cache 문제인지 API 문제인지 분리한다.
5. 특정 Browser/해상도/환경에서만 발생하는지 비교한다.
6. Build/배포 Asset version과 Cache 상태를 확인한다.
