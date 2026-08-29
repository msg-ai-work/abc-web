---
name: backend-exception-analysis
summary: Backend Exception의 최초 오류와 연쇄 오류를 구분하고 원인 구간을 찾는다.
version: "0.1"
---
# Backend Exception Analysis
## 절차
1. Exception 발생 시각과 요청 식별자를 확보한다.
2. 최초 Exception과 후속 연쇄 오류를 구분한다.
3. Controller → Service → Repository → External 호출 순서로 추적한다.
4. 입력값/Null/Timeout/Pool/DB 오류를 분류한다.
5. 동일 배포 버전의 정상 요청과 비교한다.
6. 재현 조건과 수정 후 회귀 테스트를 정의한다.
