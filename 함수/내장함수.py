"""
    파이썬에는 기본적으로 제공되는 내장 함수가 있다.

    * enumerate()
        - 리스트에 저장된 요소의 순서와 값을 확인
        - 리스트의 요소가 몇 번째인지 알려주는 (순서, 요소)로 이루어진 튜플 형태로 리턴

        예시 )

        sample_list = ['red', 'green', 'blue', 'yellow']

        for i in enumerate(sample_list):
            print(i)

        # 결과값
        # (0,'red')
        # (1, 'green')
        # (2, 'blue')
        # (3, 'yellow')


    * map()
        - 반복문을 사용하지 않고도 컨테이너 자료형의 요소를 특정 함수에 한 개씩 입력한 후, 함수의 실행 리턴값을 받아 다시 컨테이너 자료형으로 리턴하는 함수
        - 사용법: map(함수 이름, 컨테이너 자료형의 이름)

        예시 )

        def plus(num1) :
            total = num1 + 2
            return total

        list_a = [1, 2, 3, 4]
        result = map(plus, list_a)

        print(list(result)) # map 결과는 list에 담아서 출력한다.

        # 결과값
        # [3, 4, 5, 6]


    * zip()
        - 여러 개의 컨테이너 자료형의 요소를 묶어 튜플 형태로 출력해준다.
        - 인자값으로 튜플형태로 출력하고 싶은 컨테이너 자료형의 이름을 여러 개 입력할 수 있다.

        예시 ) 
            x = [1, 2, 3, 4] # 리스트
            y = (5, 6, 7, 8) # 튜플
            z = {'a':1, 'b':2, 'c':3, 'd':4}

            for result in zip(x,y,z):
                print result

            # 결과값 :
            # (1, 5, 'a')
            # (2, 6, 'b')
            # (3, 7, 'c')
            # (4, 8, 'd')

"""

# def plus(num1) :
#     total = num1 + 2
#     return total

# list_a = [1, 2, 3, 4]
# result = map(plus, list_a)

# print(list(result))
# # print(result)


# x = [1, 2, 3, 4, 'a']  # 리스트
# y = (5, 6, 7, 8, 9, 10)  # 튜플
# z = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}

# for result in zip(x, y, z):
#     print(result)


#-----------------------------------------------------------------------------------------

# 예제

value = 1
mul_value = 0

def f(x) :
    list = []

    global value
    global mul_value

    global target

    target = x

    while True :
        
        mul_value = target * value 
        
        if mul_value > 100 : break

        list.append(mul_value)
        value = value + 1

    return list

num = int(input('입력하세요 : '))

list1 = f(num)

print(list1)
