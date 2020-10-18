# BRUMP

BRUMP는 bangtal 라이브러리를 이용하여 개발한 간단한 게임입니다. 체스와 같은 전략 보드 게임과 캐릭터 성장형 게임 그리고 트럼프 카드의 특성을 조합하여 개발한 게임입니다. 게임의 자세한 규칙은 아래에서 확인하실 수 있습니다.

01. BRUMP는 Board-Trump의 약자로 캐릭터 성장형 전략 보드 게임입니다.
02. 보드는 13 X 13으로 전체 169칸으로 이루어지며, 말은 트럼프 카드를 이용합니다.
03. 플레이어는 스페이드, 클로버, 하트, 다이아몬드 중에서 각각 겹치지 않게 배정됩니다.
04. 플레이어는 13개의 말(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K)과 함께 시작합니다.
05. 플레이어 1과 플레이어 2의 말은 각각 보드의 1번째 줄과 13번째 줄에 정렬되어 있습니다.
06. 숫자를 가진 말은 한 번에 최대 1칸, 알파벳을 가진 말은 한 번에 최대 2칸 씩 이동할 수 있습니다.
07. 숫자를 가진 말은 공격력 1, J를 가진 말은 공격력 5, Q와 K를 가진 말은 공격력 10을 가지고 있습니다.
08. 아군, 적군, 블랙 조커와 컬러 조커를 공격하면 대상의 공격력을 얻을 수 있습니다.
09. 대상의 공격력이 선택한 말보다 높으면 공격할 수 없습니다. 단, 블랙 조커와 컬러 조커는 공격력이 낮아도 공격할 수 있습니다.
10. 블랙 조커와 컬러 조커가 7번째 줄에 겹치지 않게 랜덤으로 배치됩니다.
11. 숫자를 가진 말이 블랙 조커 또는 컬러 조커를 공격하면 공격력 10을 얻고 A를 가진 말로 변화합니다.
12. 알파벳을 가진 말이 블랙 조커 또는 컬러 조커를 공격하면 공격력 10을 얻습니다.
13. 상대 플레이어의 모든 말을 섬멸할 때까지 게임은 끝나지 않습니다.
