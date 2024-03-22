"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    grades = int(input())
    if grades>=90: print('A')
    elif grades>=80: print('B')
    elif grades>=70: print('C')
    elif grades>=60: print('D')
    else: print('F')
    return


if __name__ == '__main__':
    main()
