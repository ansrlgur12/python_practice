'''
함수

개발 시에 기능이 많아지면, 특정한 기능을 함수로 만들고 필요할 때 마다 호출하여 사용할 수 있다.

함수 선언

파이썬에서 함수는 다음과 같이 선언한다

예시)
def 함수이름():
    기능
    return 반환값

def f(x) :
    y = x + 2
    return y

i = f(2)
print(y)

결과 : 4

'''

# def f(x) :
#     y = x + 3

#     return y

# print(f(5))

number = int(input('숫자를 입력하세요 : '))

def f(n) :
    if n % 2 == 0 :
        return '짝수 입니다.'
    elif n == 0 :
        return '0입니다.'
    else :
        return '홀수 입니다.'
    
print(f(number))