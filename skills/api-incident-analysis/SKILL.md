---
name: api-incident-analysis
summary: 기업메시징 Web API 장애의 최초 실패 구간, 영향 범위, 의존성 병목을 증적 기반으로 분석한다.
version: "0.2"
priority: top-3
---
# API Incident Analysis

## 입력
- Endpoint / Method / 발생시간 / 환경
- HTTP Status와 Response 요약
- Correlation/Trace ID(비식별)
- Gateway/Backend/DB/외부 API Metric
- 최근 배포·설정 변경

## 절차
1. Browser/Client가 요청을 실제 전송했는지 확인한다.
2. WAF/Gateway/LB/Backend 중 최초 실패 지점을 찾는다.
3. Correlation ID로 Backend Exception과 호출 흐름을 연결한다.
4. DB/Cache/외부 API Latency와 Timeout을 같은 시간축으로 비교한다.
5. 특정 Endpoint/Role/기능/전체 영향인지 범위를 좁힌다.
6. 최근 배포/설정 변경 전후로 Error 유형을 비교한다.

## 판단 기준
| 관찰 | 우선 확인 |
|---|---|
| 4xx 집중 | 요청값/인증/인가/정책 |
| 5xx + Backend Exception | Application/DB/의존성 |
| Gateway 504 + Backend 장시간 처리 | Backend 또는 Downstream Latency |
| 일부 Role만 실패 | 권한/데이터 범위 |
| 배포 직후 신규 Error 증가 | 변경 영향 우선 |

## 대표 Case
> 비식별 대표 사례이며 실제 장애 기록이 아니다.

**현상:** 특정 조회 API의 504가 증가하고 Backend 로그에는 응답 완료 기록이 늦게 남는다. DB P95는 정상이나 외부 연계 API P95가 0.3초→6초로 상승했다.

**판단:** Gateway 자체보다 외부 API 지연이 Backend 처리시간을 늘린 연쇄 Timeout을 1순위로 본다. Timeout 설정만 즉시 늘리지 말고 외부 연계 상태와 호출 격리/Fail-fast 가능성을 확인한다.

## 출력
영향 범위, 최초 실패 구간, 근거 Metric/Log, 원인 후보, 추가 확인, 임시/근본조치.

## Human Gate
운영 설정 변경, Timeout 상향, 트래픽 우회, Rollback은 승인 후 수행한다.