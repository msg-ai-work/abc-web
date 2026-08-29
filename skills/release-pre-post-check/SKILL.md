---
name: release-pre-post-check
summary: 기업메시징 Web 배포 전후 사용자 영향과 서비스 상태를 점검한다.
version: "0.1"
---
# Web Release Pre/Post Check
## 배포 전
- [ ] 변경 화면/API/DB 영향 확인
- [ ] 하위 호환성과 설정 변경 확인
- [ ] Rollback 절차 확인
- [ ] 주요 Dashboard/Alarm 정상 확인
## 배포 후
- [ ] Error rate/Latency 확인
- [ ] 로그인/권한 확인
- [ ] 주요 API 확인
- [ ] Smoke Test 실행
- [ ] DB/외부 연계 상태 확인
## Human Gate
배포와 Rollback 결정은 승인권자가 수행한다.
