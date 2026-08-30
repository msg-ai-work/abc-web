---
name: smoke-test
summary: 배포 후 기업메시징 Web의 핵심 사용자 경로를 짧은 시간에 검증하고 배포 지속 여부의 근거를 만든다.
version: "0.2"
priority: top-3
---
# Web Smoke Test

## 목적
Smoke Test는 전체 회귀시험이 아니다. **서비스 사용 가능 여부를 빠르게 확인하는 최소 핵심 경로**만 검증한다.

## 입력 / 사전 정보
환경, 배포 버전, 배포 완료 시각, 대상 기능, 테스트 계정 Role, 관련 외부 연계 상태.

## 절차 / 핵심 경로
- [ ] 로그인 및 정상 Session 유지
- [ ] 권한별 메인 화면 진입
- [ ] 메시지 발송 화면 진입/필수값 Validation
- [ ] 비식별 테스트 발송 1건의 요청→결과 확인(가능 환경에서만)
- [ ] 주요 조회/검색 API
- [ ] 관리자 핵심 조회 기능
- [ ] 변경 기능이 포함된 대표 사용자 경로
- [ ] Browser Console의 신규 JS Error 확인

## 판정
- **PASS:** 핵심 경로 정상 + 신규 Critical Error 없음
- **CONDITIONAL:** 비핵심 오류가 있으나 고객 핵심 흐름 정상, Owner가 위험 수용
- **FAIL:** 로그인/핵심 API/발송/권한 중 하나라도 사용 불가 또는 데이터 오류

## 대표 Case
> 비식별 대표 사례이며 실제 배포 기록이 아니다.

**상황:** 메인 화면과 조회는 정상이나 특정 Role에서 발송 화면 API가 403이다.

**판정:** 전체 Smoke PASS로 처리하지 않는다. 해당 Role이 운영 대상이면 FAIL이며 `auth-session-diagnosis`로 연결한다.

## 출력 / Evidence
실행시각, 환경, 버전, Role, 테스트 항목별 결과, HTTP Status/오류 요약, 최종 판정.

## Human Gate
Smoke FAIL 시 배포 지속 또는 Rollback 판단은 승인권자가 수행한다.