"""
구구단 출력 프로그램 (Python)

[개요]
이 스크립트는 2단부터 9단까지의 구구단을 콘솔에 출력합니다.
명령행 인자(Command Line Argument)를 통해 출력 범위를 자유롭게 지정할 수 있습니다.

[실행 방법]
    python gugudan.py            # 인자 없이 실행  -> 2단 ~ 9단 전체 출력
    python gugudan.py 3          # 숫자 1개 지정   -> 3단만 출력
    python gugudan.py 2 5        # 숫자 2개 지정   -> 2단 ~ 5단 출력 (순서 무관)

[인자 규칙]
    - 인자를 주지 않으면 기본값으로 2단 ~ 9단을 출력합니다.
    - 숫자를 1개만 주면 해당 단(dan)만 출력합니다.
    - 숫자를 2개 주면 두 수 사이의 모든 단을 출력합니다.
      (예: '5 2' 와 같이 거꾸로 입력해도 자동으로 2 ~ 5단으로 정렬됩니다.)
    - 숫자가 아닌 값은 무시되므로, '--help' 같은 플래그도 안전하게 스킵됩니다.

[작동 원리]
    - 각 단은 1부터 9까지 곱해서 'dan x i = dan*i' 형식으로 출력합니다.
    - print_dan(): 특정 한 단을 출력하는 단위 함수입니다.
    - gugudan(): start단부터 end단까지 print_dan()을 반복 호출합니다.
    - main(): sys.argv 로 받은 인자를 해석해 적절한 범위로 gugudan()을 호출합니다.
"""


def print_dan(dan: int) -> None:
    """
    지정한 단(dan)의 구구단을 출력합니다.

    Parameters
    ----------
    dan : int
        출력할 단의 숫자 (예: 3 이면 3단).

    Returns
    -------
    None
        결과는 콘솔(stdout)에 직접 출력되며, 반환값은 없습니다.
    """
    print(f"=== {dan}단 ===")
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")
    print()
    if len(args) == 0:
        # 인자가 없으면 2단 ~ 9단 전체 출력
        gugudan(2, 9)
    elif len(args) == 1:
        # 단 하나만 지정
        gugudan(args[0], args[0])
    else:
        # 범위 지정 (작은 수 ~ 큰 수)
        start, end = sorted(args[:2])
        gugudan(start, end)

def gugudan(start: int = 2, end: int = 9) -> None:
    """
    start단 부터 end단까지 구구단을 연속해서 출력합니다.

    Parameters
    ----------
    start : int, optional
        시작 단 (기본값 2).
    end : int, optional
        끝 단 (기본값 9).

    Returns
    -------
    None
    """
    for dan in range(start, end + 1):
        print_dan(dan)


def main() -> None:
    """
    명령행 인자를 해석하여 구구단 출력 범위를 결정하고 실행합니다.

    인자 개수에 따라 다음과 같이 동작합니다.
        - 0개: 2단 ~ 9단 전체
        - 1개: 해당 단만
        - 2개 이상: 정렬된 두 수 사이의 범위
    """
    import sys

    # 숫자로 변환 가능한 인자만 추려낸다 (플래그/문자열은 무시)
    args = [int(a) for a in sys.argv[1:] if a.lstrip("-").isdigit()]

    if len(args) == 0:
        # 인자가 없으면 2단 ~ 9단 전체 출력
        gugudan(2, 9)
    elif len(args) == 1:
        # 단 하나만 지정
        gugudan(args[0], args[0])
    else:
        # 범위 지정 (작은 수 ~ 큰 수)
        start, end = sorted(args[:2])
        gugudan(start, end)


if __name__ == "__main__":
    main()
