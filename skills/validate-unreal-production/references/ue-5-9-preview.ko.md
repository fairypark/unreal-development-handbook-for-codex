# UE 5.8에서 확인한 결과와 5.9 프리뷰에서 확인할 것

2026년 11월 14일 기준으로 공개된 빌드는 11월 9일 발표된 **UE 5.9 MegaJam Preview**다. Epic은 검증 기간이 평소보다 짧았다고 밝혔다. 5.8에서 승인한 프로젝트를 보존하고, 도입하려는 기능이 실제 제작 결정에 영향을 줄 때 복사본에서 시험한다. [Epic 발표](https://forums.unrealengine.com/t/unreal-engine-5-9-megajam-preview/2852840) · [핸드북 13장 원문](13-production-pipeline.md#ue-59-megajam-preview)

## 5.8에서 실제로 관찰한 결과

| 당시 작업 | 확인한 것 | 증거가 닿는 범위 |
| --- | --- | --- |
| 5.8 초지 레벨 | 저장 후 다시 연 레벨의 화면을 확인했다. 에디터 플레이 모드(PIE)에서 17개 지점을 잇는 경로를 걸었고, 기록한 336개 표본에서 추락이 없었다. | 해당 경로와 장면에서 확인한 결과다. 배포 빌드, 다른 GPU에서의 성능, 식생의 바람 반응은 별도 시험이 필요하다. [초지 사례](../../analyze-unreal-development-cases/references/meadow-reuse-review.ko.md) |
| 5.8.3 PCG 학습 장면 | 가운데 점만 검사하면 계단 모서리에 뜬 물체를 놓쳤고, 네 모서리를 검사하면 잡아냈다. 두 번 생성하고 에디터에서 다시 열었을 때 실제 생성물의 위치·회전·크기도 검증 데이터와 일치했다. | 단순한 메시로 접지와 생성 규칙을 확인했다. 실제 숲의 배치나 런타임 비용은 측정하지 않았다. [PCG 사례](../../analyze-unreal-development-cases/references/pcg-learning-reuse.ko.md) |

두 사례에서 가져갈 것은 확인 방법이다. 신규 빌드의 저장·재생성 결과는 그 빌드에서 다시 관찰해야 한다. 11장과 13장의 Horde 인용은 당시 문서를 다시 읽을 수 있도록 5.8판에 연결했다. [Epic Horde Automation Hub 5.8](https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-automation-hub-for-unreal-engine?application_version=5.8)

## 이번에 5.9 프리뷰에서 직접 확인한 한 가지

Windows의 **UE 5.9.0 CL 60351404**에서 별도 빈 프로젝트를 만들었다. 명령줄 에디터에서 Python으로 Actor Blueprint를 복제하고 복제본에 빈 함수 그래프 하나를 추가해 컴파일·저장했다. 첫 프로세스를 종료하고 새 에디터 프로세스에서 두 에셋을 열었다. **함수는 복제본에만 남았고 다시 컴파일됐다.** 이 시험은 직접 Python으로 편집한 그래프의 저장 범위를 확인했다. MCP를 통한 편집, 루트 컴포넌트 교체, 게임 플레이는 시험하지 않았다. [6장 원문](../../design-unreal-blueprint-and-cpp/references/06-blueprint.md#scripted-graph-edits-in-ue-59-preview)

## Epic이 공지한 변화와 아직 실행하지 않은 프로젝트 시험

| 판단할 문제 | Epic이 문서화한 내용 | 프로젝트에서 해 볼 가장 작은 확인 |
| --- | --- | --- |
| **AI 화면으로 실제 숲의 밀도를 판단할 수 있을까?** | 5.9 프리뷰에는 뷰포트 화면을 AI로 실시간 가공하는 기능이 있다. [프리뷰 릴리즈 노트](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-5-9-release-notes?application_version=5.9) | 같은 장면·게임 카메라로 AI 가공을 끈 원본을 함께 찍는다. 가공본은 원하는 분위기를 고를 때 쓰고, 나무 사이의 실제 빈틈은 원본에서 확인한다. [10장](10-rendering.md#evidence-strategy) · [12장](12-validation-testing-debugging.md#evidence-integrity) |
| **에이전트가 이 Blueprint를 편집할 수 있을까?** | Preview 1의 새 프로젝트에서는 MCP 연결이 성공해도 편집 도구가 빠질 수 있다(UE-412135). Python으로 Blueprint 루트 컴포넌트를 바꿀 때 충돌할 수 있다는 보고도 있다(UE-411502). [Epic 알려진 문제](https://forums.unrealengine.com/t/unreal-engine-5-9-megajam-preview/2852840/3) | 연결한 에디터가 맞는지, 필요한 도구가 실제로 보이는지, 요청에서 해당 편집을 허용했는지 확인한다. 그 경로로 복제본 하나를 편집하고 컴파일·저장·다시 열기를 확인한 뒤 일괄 적용을 판단한다. [8장](../../design-unreal-automation-and-pcg/references/08-automation-python.md#python-as-an-option) · [15장](../../guide-unreal-ai-development/references/15-ai-assisted-development.md#evidence-and-independent-evaluation) |
| **Lumen 조명과 성능이 달라진 원인은 무엇일까?** | 새 World Cache는 기본값이 꺼져 있고 Lumen 하드웨어 레이 트레이싱에서 쓴다. 장면을 실행하는 동안 조명 정보를 채운다. [Epic World Cache 문서](https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-world-cache-in-unreal-engine?application_version=5.9) | 같은 5.9 빌드·GPU·해상도·조명·카메라 동선에서 캐시만 끄고 켠다. 처음 진입한 화면과 조명이 안정된 화면, 각각의 GPU 프레임 시간을 비교한다. 5.8 장면과 새 장면만 비교하면 캐시 효과를 분리하기 어렵다. [11장](11-performance-scalability.md#comparing-lumen-world-cache-in-ue-59-preview) |
| **웹 게임이 새로고침 뒤에도 진행도를 유지할까?** | Preview 1의 Launcher 기반 C++ 웹 게임에서 새로고침 후 저장·설정이 사라지는 문제(UE-412003)가 보고됐다. [Epic 알려진 문제](https://forums.unrealengine.com/t/unreal-engine-5-9-megajam-preview/2852840/3) | 시험용 저장 슬롯으로 등대에 도착해 보상을 받고 저장한다. 같은 브라우저 프로필과 사이트 주소에서 새로고침한다. 등대에서 이어지고 보상을 두 번 받을 수 없는지 확인한다. [13장](13-production-pipeline.md#can-players-keep-progress-made-after-an-update) |
| **Mesh Terrain이나 Nanite를 쓰면 식생 비용까지 줄어들까?** | 5.9에서 Mesh Partition과 PCG 연동이 개선됐다. Mesh Terrain은 실험 기능이며, Nanite의 내부 가시성 계산 개선과 별개로 문서는 뷰별 거리 컬링을 미지원으로 표기한다. [Mesh Terrain](https://dev.epicgames.com/documentation/en-us/unreal-engine/crafting-mesh-terrain-in-unreal-engine?application_version=5.9) · [Nanite](https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.9#rendering) | 돌출 지형이 필요하면 한 구간에서 아래쪽 보행과 위·아래 식생의 접지를 확인한다. 단순한 언덕이라면 기존 Landscape로도 충분할 수 있다. 같은 식생 동선에서 화면에 보이는 변화, 실제 생성 수, 메모리와 프레임 시간을 각각 본다. [4장](../../design-unreal-worlds-and-levels/references/04-world-level-design.md#terrain-representation-review-before-broad-terrain-mutation) · [9장](../../design-unreal-automation-and-pcg/references/09-procedural-systems-pcg.md#version-sensitive-rendering-and-culling-decisions) |
| **PCG Paint가 칠하는 즉시 갱신될까?** | 5.8.4에는 한 번 칠한 결과가 즉시 보이지 않는 문제(UE-401568)가 있었다. 검토한 5.9 프리뷰 노트에서 수정 여부는 확인되지 않았다. [5.8.4 공지](https://forums.unrealengine.com/t/5-8-4-hotfix-released/2842775) · [5.9 프리뷰 노트](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-5-9-release-notes?application_version=5.9) | 복사한 장면에 한 번 칠하고 다른 조작을 하기 전에 출력이 바뀌는지 본다. 재생성 및 저장 후 다시 열어서 배치가 남는지도 따로 확인한다. |
