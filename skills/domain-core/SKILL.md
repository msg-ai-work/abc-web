---
name: web-domain-core
summary: 기업메시징 고객/관리자 웹의 운영·개발 공통 Skill. FE/BE, API, 인증/권한, 배포 및 웹 장애 분석에 사용한다.
owner-role: web-domain-owner
version: "0.1"
---
# 웹 도메인 Core Skill
## 적용 범위
- 기업메시징 고객/관리자 웹
- Frontend / Backend API
- 로그인, 인증, 권한, 세션
- 메시지 발송/조회 UI와 업무 API
- 배포, 운영점검, 웹 장애 분석
## 판단 순서
1. FE 표시 문제인지 BE/API 문제인지 분리한다.
2. Browser → Gateway/Backend → DB/외부 연계 순서로 추적한다.
3. 인증/인가/세션/권한 문제 여부를 별도 확인한다.
4. 입력 검증, 예외처리, Timeout, 재시도 영향을 확인한다.
5. 운영 장애이면 최근 배포·설정·인증서·외부 변경을 우선 확인한다.
6. 변경이면 사용자 영향, 하위 호환성, Rollback을 확인한다.
## 운영 체크
- [ ] URL/환경/사용자 Role 확인
- [ ] Console/Network 및 HTTP Status 확인
- [ ] Backend 로그와 Correlation ID 연결
- [ ] DB/외부 API 지연 확인
- [ ] 최근 배포/설정 변경 확인
- [ ] 주요 사용자 경로 Smoke Test
## Guardrail
운영 개인정보/Token 원문을 저장하지 않고, AI가 권한 변경·DB 수정·운영 배포를 직접 실행하지 않는다.
