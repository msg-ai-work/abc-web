---
name: database-query-analysis
summary: Web Backend의 Query 지연, Lock, Connection Pool 및 데이터 접근 문제를 분석한다.
version: "0.1"
---
# Database Query Analysis
## 절차
1. API 응답시간과 Query 실행시간을 연결한다.
2. Slow Query, Scan 범위, Index 사용 여부를 확인한다.
3. Lock/Deadlock/Connection Pool 대기를 확인한다.
4. N+1/반복 Query 여부를 확인한다.
5. 데이터량 증가에 따른 성능 영향을 평가한다.
6. 개선 전후 실행계획과 응답시간을 비교한다.
## Guardrail
운영 데이터 변경/DDL/Session Kill은 자동 실행하지 않는다.
