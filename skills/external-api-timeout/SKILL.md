---
name: external-api-timeout
summary: 외부 API 연계 지연과 Timeout을 내부·네트워크·상대 시스템 구간으로 분리한다.
version: "0.1"
---
# External API Timeout
## 절차
1. 호출 시작/종료/Timeout 값을 확인한다.
2. DNS/TLS/Connection/Read Timeout 구간을 구분한다.
3. 외부 API 성공률과 Latency 추이를 확인한다.
4. 동일 시간 내부 API와 다른 외부 연계를 비교한다.
5. Retry가 부하를 증폭시키는지 확인한다.
6. 사용자 응답과 Fallback/Graceful degradation 가능성을 검토한다.
