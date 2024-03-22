"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    
    num=int(input('정수를 입력해주세요 :'))
    if num>12: print('12이하의 정수를 입력해주세요. ')
    else:
        sum=0
        rhq=1
        i=1
        while i <=num:
            sum+=i
            i+=1
        for a in range(1,num+1):
            rhq*=a
        print(sum)
        print(rhq)
    return


if __name__ == '__main__':
    main()
