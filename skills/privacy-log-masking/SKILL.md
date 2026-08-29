---
name: privacy-log-masking
summary: Web 로그와 오류 응답에서 개인정보, 인증정보, Token의 불필요한 노출을 점검한다.
version: "0.1"
---
# Privacy / Log Masking
## 확인 항목
1. 이름, 전화번호, 이메일 등 개인정보 원문 노출을 확인한다.
2. Authorization, JWT, Cookie, Session ID 노출을 확인한다.
3. Request/Response 전체 Body 로깅 여부를 확인한다.
4. Exception에 Credential/Connection 정보가 포함되는지 확인한다.
5. 필요한 식별자는 비식별/Masking 기준을 적용한다.
6. 운영 로그 보존 목적에 필요한 최소 정보만 남긴다.
## 판정
민감정보 원문이 불필요하게 저장되면 개선 필요로 판정한다.
