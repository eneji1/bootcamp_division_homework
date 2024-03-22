"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    A = input('알파벳 문자 하나를 입력하세요 :')
    a=['a','e','i','o','u']
    b=['q','w','r','t','y','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    if A in a: print('O')
    elif A in b : print('X')
    else: print('알파벳을 입력해주세요.')
    
    return


if __name__ == '__main__':
    main()
