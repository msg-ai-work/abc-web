---
name: api-incident-analysis
summary: 기업메시징 Web API 장애의 발생 구간과 영향 범위를 분석한다.
version: "0.1"
---
# API Incident Analysis
## 절차
1. Endpoint/Method/발생시간/HTTP Status를 확인한다.
2. Gateway/WAF/Load Balancer/Backend 중 실패 지점을 구분한다.
3. Correlation ID로 요청 흐름과 Exception을 연결한다.
4. DB/Cache/외부 API 의존성 지연을 확인한다.
5. 특정 Role/고객/기능/전체 영향인지 범위를 좁힌다.
6. 최근 배포/설정 변경과 비교한다.
## 출력
영향 범위, 최초 실패 구간, 근거, 원인 후보, 임시조치, 추가 확인 항목.
