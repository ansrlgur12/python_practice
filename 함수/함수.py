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



"""
    변수 스코프

    함수 내부에서 선언한 변수를 지역변수,
    함수 외부에서 정의한 변수를 전역 변수라고 한다.

    함수 내에서 외부에서 선언됐던 전역변수를 사용하려면 global을 사용한다.

    예시)

    num = 10 # 전역변수
    def plus() :
        global num # 전역 변수를 갖다 쓰겟다 선언
        num = num + 10
        print('전역변수 num : ', num)

    plus()
    plus()



"""