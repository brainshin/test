"""
구구단 출력 프로그램 (Python)

- 인자 없이 실행: 2단 ~ 9단 전체 출력
- 인자로 숫자 지정: 해당 단만 출력 (예: python gugudan.py 3)
- 범위 지정: python gugudan.py 2 5  -> 2단 ~ 5단 출력
"""


def print_dan(dan: int) -> None:
    """지정한 단(dan)의 구구단을 출력한다."""
    print(f"=== {dan}단 ===")
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")
    print()


def gugudan(start: int = 2, end: int = 9) -> None:
    """start단 부터 end단까지 구구단을 출력한다."""
    for dan in range(start, end + 1):
        print_dan(dan)


def main() -> None:
    import sys

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
