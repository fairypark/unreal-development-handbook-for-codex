# PCG 학습 실험에서 무엇을 재사용할 것인가 — 한국어 검토본

대응 원문: [Chapter16 사례](16-case-studies.md#case-an-inspectable-pcg-learning-fixture-is-not-a-production-starter), [Chapter08 자동화 재사용](../../design-unreal-automation-and-pcg/references/08-automation-python.md#reuse-a-validation-contract-without-replaying-historical-mutations), [Chapter09 절차 관계 전이](../../design-unreal-automation-and-pcg/references/09-procedural-systems-pcg.md#reuse-a-proved-relationship-not-a-fixture-configuration), [Chapter12 증거 주장](../../validate-unreal-production/references/12-validation-testing-debugging.md#archive-validity-and-diagnostic-readability-are-separate-claims).

## 사례의 의도와 범위

Electric Dreams에서 배울 PCG 관계를 이해하는 일이 완성된 정글보다 우선이었다. 기존 네 분포·제외 구간은 보존하고 새 비 Partition fixture에 계층, 방향, 여러 점 지지 비교를 추가했다. UE5.8.3의 기본 도형과 명시적인 query 표면으로 관계를 격리했다.

2026-10-25 운영자가 보존한 자료를 근거로 한 **Editor 학습 진단의 관찰 사례**다. 원본 이미지·에셋·실행 영수증은 운영자의 프로젝트에 있으며 핸드북에 배포하지 않는다. 핸드북 개정이 Editor를 새로 실행했다거나 비교 가능한 시간 절감·runtime·production 승인을 입증했다는 뜻은 아니다.

## 대안과 선택

전체 샘플을 재구현하면 불필요한 콘텐츠·의존성이 따라오고, 바로 숲을 꾸미면 규칙 오류와 미술 문제를 구분하기 어렵다. 필요한 관계만 구성하고 지지 필터를 소유 복사본으로 격리했다. data-only 결과를 먼저 검증하고 그 뒤 실제 출력과 고정 화면의 설명력을 검토했다. 관계를 저렴하게 관찰하는 대신 실제 환경의 미술·장면·runtime 위험은 해결하지 않았다.

## 관찰과 그 의미

| 관찰 | 가져갈 판단 | 일반화 한계 |
|---|---|---|
| 부모 변화가 후손 TRS에 전달되고 필요한 부모를 제거하면9→6 | 부품을 독립 산포하지 말고 상대변환·의존성을 명시 | 시험용 도형 조합의 성공이며 production asset family 검증은 아님 |
| 대조군8개와 목표 방향8개가 선언한 local 축으로 비교되고 목표 변경에 방향·표식이 반응 | 실제 메시 축과 목표 좌표계를 먼저 확인 | 모든 메시가 같은 앞축·같은 방향 연산을 쓰는 것은 아님 |
| 중심 검사3개 중 네 모서리는 평탄·경사2개만 허용. 단차60cm가 fixture의5cm 기준을 초과. 높이 허용을 늘리거나 간격을 줄이면 다시 통과 | footprint에 맞는 샘플과 허용값을 사용하고 under-sampling을 드러낼 실패 대조군 유지 | 수치는 사례 값이며 복잡한 물체의 완전 지지를 증명하지 않음 |
| query 기록3개가 나왔어도 density·hit identity·높이가 유효하지 않았고 실제 query 의미와 source filter를 맞춘 뒤 복구 | 개수 대신 실제 hit 상태와 소비자의 의미를 점검 | 특정 엔진의 filter 수정값을 모든 trace에 복사하지 않음 |
| 13개 spawner에 의도된 재질이 있었지만 실제7개 component에는 override가 없었음. 한정된 output 설정 갱신 후 색이 나타나고 행렬은 같았음 | 설정값과 실제 생성 resource를 구분한 뒤 라이팅·기하를 진단 | cache 재사용은 유력 가설이며 단독 원인으로 입증하지 않음. 당시 갱신 동작은 범용 수리법이 아님 |
| 최초 시각 점수 hierarchy2/aim2/support3/annotation1. 의도된 오판이 성공처럼 보임 | 학습 비교는 수학뿐 아니라 실패·대조·목표의 의미가 해당 화면에서 읽혀야 함 | 진단용 색·설명을 production 미술 팔레트로 강제하지 않음 |

입력 포인트, 표면, 조명,8카메라는 고정하고 진단 표현만 보완했다. 이후 독립 검토에서 학습용 적용 시각 범주가 모두4/5 이상이었다. 원거리 overview 글씨와 일부 가장자리 글씨는 여전히 작지만 핵심 관계는 같은 역할의 근접 고정 화면에서 읽혀 비차단 한계로 기록됐다.

## 기술 근거와 남은 범위

13 managed resources와232 instances를 확인했다. 본체227개에는 목표 표식1개가 포함되고 별도 진단5개가 있었다. 보완 전후 두 번 생성과 실제 저장·재개방의 world matrices가 검증한 데이터와 같았다. 재생성 전에 재개방 원상태도 보존했다. 출력은 collision/nav/overlap이 없고 명시한 source fixture만 query collision을 제공했다. 검증 당시 보호한 원본은 불변이었다.

운영자 자료는 `S1-data-validation.json`, `S2-output-validation.json`, 실패·통과한 `independent-S2-review`, raw 생성/재개방 snapshot,8개 고정 PNG와 캡처·전달 검증 기록이다. 반복된 world-matrix digest는 `8a9a4947149777242f2c24fa71cd0fc961f4f1a66999bf60c5330adfe3fc6063`이다. 핸드북은 보존 관찰을 설명하며 이 프로젝트 자료를 재배포하거나 새로 실행하지 않는다.

원본 전체 Blueprint 구현과의 동등성, PIE, runtime scheduling, 성능, 패키징, 실제 환경 에셋 통합, 총 제작시간 절감은 미검증이다. 관계별로 분리한 범용 production subgraph 라이브러리도 완성된 상태가 아니다.

## 장별 반영

- **08:** 관계의 목적·사전/사후 조건·증거 연결을 먼저 재사용한다. 기존 builder는 빈 맵·정확한 identity·미사용 파일 경로를 전제할 수 있으므로 그대로 replay하지 않는다. archive recheck는 stdout 또는 별도 새 보고서를 사용하고 기존 승인 기록을 바꾸지 않는다. 실제 재개방 상태를 재생성 전에 남기며 전체 다음 판단 주기를 측정하기 전 속도 개선을 확정하지 않는다.
- **09:** 의미 있는 root·부모 키, 좌표계·메시 축, 최종 footprint, source authority, 단위 있는 기준과 기대 실패를 새 맥락에 맞게 교체한다. 하나의 parameter 변화나 실패 대조군으로 관계를 반증해 본다. 작은 샘플 간격이 단차를 놓칠 수 있고 느슨한 기준이 실패를 허용할 수 있으므로 이를 자동 개선으로 읽지 않는다. 실제 소비자·hit·world TRS·재질·유효 collision을 확인한다.
- **12:** 보관 증거의 무결성·반복성·기존 승인 범위 확인은 현재 소비자를 관찰하거나 새 장면을 승인하는 일이 아니다. 의도된 실패를 성공과 구분할 수 없으면 기술 개수가 맞아도 진단은 통과시키지 않는다. 비교 조건을 고정해 설명이나 실제 출력을 고치고 기술 불변 조건도 다시 확인한다.
- **16:** 위의 의도·대안·관찰·회복·미검증 범위를 연결한 사례로 보존한다. 기존 원칙을 구체화하며 별도 의무 gate나 문서를 추가하지 않는다.

## 다른 조건에서 생각해 볼 질문

다음 둘은 **구성한 학습 질문**이며 새로운 성공 사례가 아니다.

1. 메시의 앞축이 바뀌어도 기존 aim 연산이 같은 계약을 만족하는가? 축을 확인하고 작은 목표 변화에서 실제 방향을 관찰한다.
2. 중심 hit가 유효하지만 모서리 하나가 지지되지 않으면 이 물체의 support 책임을 만족하는가? 넓은 기반인지 좁은 anchor인지에 따라 필요한 검사를 다르게 선택한다.

관계·변화 예측·실패 신호·검증 범위를 재사용하고 구현 설정은 조건에 맞게 바꾼다. 이 글을 읽은 뒤 판단력이 좋아졌는지에 대한 held-out 평가나 시간 개선은 아직 측정하지 않았다.
