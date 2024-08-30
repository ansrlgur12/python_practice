import math

'''
입출력, 변수, 자료형

'''


# print(1+2)
# print(3+2, 1+2)

# 문자열 포매팅
# %d : 정수형
# %f : 실수형, %.2f : 소숫점 두자리 수 까지 출력
# %s : 문자열

# 옛날 문법
# print('%02d월 %d일 날씨는 %s이고, 기온은 %.2f 입니다.' %(8, 27, '흐림', 28.1225))

# 요즘 문법
# print(f'{8:02d}월 {27}일 날씨는 {"흐림"}이고, 기온은 {28.1225:.2f} 입니다.')

# format() 사용
# print('{:02d}월 {}일 날씨는 {}이고, 기온은 {:.2f} 입니다.'.format(8, 27, '흐림', 28.1225))


# input 함수로 받은 값은 문자열로 저장됨
# month = input('월 입력 : ')
# day = input('일 입력 : ')
# weather = input('날씨 입력 : ')
# temp = input('기온 입력 : ')

# print('{:02d}월 {}일 날씨는 {}이고, 기온은 {} 입니다.'.format(int(month), day, weather, temp))

# ------------------------------------------------------------------------------------------------

# 원의 둘레 길이 구하기

# pi = 3.14
# radius = input('원의 지름을 입력하세요 (cm) : ')

# print('원의 둘레는 {:.2f}cm 입니다.'.format(float(radius) * pi))

# circle = float(input('원의 지름을 입력하세요 (cm) : ')) * 3.14
# # print ('원의 둘레는 {:.2f}cm 입니다.'.format(circle))
# print (f'원의 둘레는 {circle:.2f}cm 입니다.')

# ------------------------------------------------------------------------------------------------

# 택시 미터기

# default_pay = 4000
# total_pay = 0
# calc_distance = 150
# calc_meter = 120

# distance = int(input('이동 거리 입력(m) : '))

# extra_distance = distance - 2000
# extra_pay =  math.ceil((extra_distance / calc_distance) * calc_meter) 

# if extra_distance < 0:
#  total_pay = default_pay
# else:
#  total_pay = default_pay + extra_pay

# print(f'기본 요금: {default_pay}')
# print(f'가산 거리: {distance - 2000}')
# print(f'가산 거리 당 추가 요금: {extra_pay}')
# print(f'고객님의 이동 거리: {distance}m')
# print(f'총 요금은 {total_pay}원 입니다.')

# ------------------------------------------------------------------------------------------------

'''
변수란? 

프로그램이 실행되는 동안 컴퓨터가 기억해야 할 값을 저장하는 공간,
변수 선언 시, 컴퓨터 메모리 안에 저장할 공간이 확보된다. 변수에 저장될 자료의 형태에 따라서 저장공간의 크기가 결정된다.

변수 선언 규칙

1. 숫자로 시작할 수 없다.
2. 띄어쓰기를 하지 않는다.
   대신 _로 구분한다. : py_prac 
3. 대문자와 소문자를 구분하여 사용한다.
4. 한글보단 영어 사용 권장

변수 선언 방법

1. 간단하고 기억하기 쉽게
2. 변수의 용도와 목적을 명확하게

'''

'''
자료형 이란?

변수에 저장할 데이터의 종류와 특징에 따라 구분

자료형은 크게 두가지
기본자료형, 컨테이너 자료형

기본자료형은 한 변수에 한 개의 값만 담을 수 있다.
컨테이너 자료형은 한 변수의 여러개의 값을 담을 수 있다.

컨테이너 자료형

1. 리스트
[] 안에 , 구분으로 여러 자료 넣는다. 다양한 자료형 넣을 수 있음
리스트 안에 리스트도 넣을 수 있음

리스트 내부 요소 접근법
예를들어 list = [1, 2, 3, 4, 5]
이렇게 있다고 했을 때, '2'라는 요소에 접근하려면 list[1] index로 접근한다.


'''

# list_a = [1, 2, 3, [10, 20, 30], 4]
# print(list_a[3][1])
# = 20

'''
2. 튜플

튜플 선언은 리스트와 달리, [] 가 아닌 () 소괄호로 묶어서 선언
소괄호를 생략하고 생성해도 튜플로 저장된다.
sample_tuple = (1, 2, 3, 4, 5)
sample_tuple2 = 1, 2, 3, 4, 5
만약 튜플로 선언할 자료의 개수가 한 개여도 뒤에 ,를 붙여줘야 일반 변수가 아닌 튜플로 생성이 된다.
sample_tuple3 = 1,

한번 선언된 튜플은 내부 요소를 바꿀 수 없다. (읽기 전용)
내부 요소에 각각 접근해서 수정, 삭제는 불가능하지만, 튜플 두개를 + 연산자로 더해서 연달아 나열하는건 가능하다.


'''

# test_tuple1 = (1, 2, 3, 4, '5')
# test_tuple2 = '6', 7, 8, 9, '10'
# test_tuple3 = 11,

# print(type(test_tuple1))
# print(type(test_tuple2))
# print(type(test_tuple3))

# # 튜플끼리 더해서 새로운 튜플에 할당
# test_tuple4 = test_tuple1 + test_tuple2
# print(test_tuple4, type(test_tuple4))

'''
3. 딕셔너리

연관된 정보를 key, value 로 묶어서 사용
{} 중괄호로 감싼다.

한 개의 키에 여러개의 value를 배열 형식으로 묶어서 사용할 수 있음

sample_dict = {'name': 'John', 'age': 25, 'address': 'Seoul', 'own_car': ['bmw', 'benz', 'audi']}


'''

# sample_dict = {'name': 'John', 'age': 25, 'address': 'Seoul', 'own_car': ['bmw', 'benz', 'audi']}
# print(sample_dict['own_car'])

'''
리스트 활용법

1. list() 함수
list 함수는 입력받은 자료형을 리스트로 만들어 반환한다.
이때 range() 함수를 함께 사용하면, 일정한 간격을 가진 정수 리스트를 만들 수 있다.

list(range(start, stop, step))

위 예시에서 start는 범위의 시작값, stop은 끝 값 다음의 값 (만약 10 이라했으면 9까지), step은 증감 간격

역순으로 입력되는 리스트를 만들기 위해서는
시작값 10, 종료값 0 만으로는 안된다.
증가는 상관없는데 감소는 step값을 -1 이나 음수값으로 지정해줘야한다.

'''

# 2. 리스트 슬라이스 (잘라내기)
# slice_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(slice_list[:1])
# # 0, 1 인덱스 출력
# print(slice_list[3:5])
# # 3, 4 인덱스 출력

# # [:] 앞의 숫자의 인덱스 부터, 뒤 숫자-1 인덱스를 가진 범위를 출력
# # [1:] 앞에만 있으면 앞의 숫자 인덱스 부터 끝까지
# # [:1] 뒤에만 숫자 있으면 처음부터 뒤에 숫자-1 인덱스까지 출력
# # [:] 둘 다 없으면 처음부터 끝까지 출력

'''
3. list 끼리 연산 가능 (+, *) 
더하기는 이어붙여주고,
곱하기는 뒤에 수만큼 list를 반복생성


4. list 요소 추가

4-1. append() 함수를 사용하면, 리스트의 가장 마지막에 해당 요소가 추가된다.

예시)
sample_list = [1, 2, 3, 4, 5]
sample_list.append('6')

print(sample_list)
결과: [1, 2, 3, 4, 5, '6']

4-2. extend() 함수를 사용하면, 리스트의 가장 마지막에 여러 요소를 한번에 추가한다.

예시)
sample_list = [1, 2, 3, 4, 5]
sample_list.extend(['6', 7, '8'])

print(sample_list)
결과: [1, 2, 3, 4, 5, '6', 7, '8']

만약 
sample_list.append(['6', 7, '8']) 이렇게 쓰면 ['6', 7, '8'] 이라는 값을가진 배열이 리스트에 추가된다.

4-3. insert() 함수를 사용하면, 리스트 내부 원하는 위치에 요소를 추가한다. 기존 요소들은 그 뒤로 밀려난다.

예시)
sample_list = [1, 2, 3, 4, 5]
sample_list.insert(2, '3')

print(sample_list)
결과: [1, 2, '3', 3, 4, 5]


5. 리스트 요소 삭제

remove() 함수는 리스트의 특정 요소를 삭제한다.

예시)
sample_list = [1, 2, 3, 4, 5]
sample_list.remove(2)

print(sample_list)
결과: [1, 3, 4, 5]


pop() 함수는 인덱스를 지정해서 해당 인덱스를 가진 요소를 삭제한다. 인덱스 없으면 가장 마지막 요소 삭제

예시)
sample_list = [1, 2, 3, 4, 5]
sample_list.pop(1)

print(sample_list)
# 결과: [1, 3, 4, 5]

sample_list.pop()
print(sample_list)
# 결과: [1, 3, 4]

이 외에도 리스트의 요소를 모두 제거하는 clear() 함수와, del 명령어가 있다.

clear() 예시)
sample_list = [1, 2, 3, 4, 5]
sample_list.clear()

print(sample_list)
# 결과: []


del 명령어는 특정 인덱스만 삭제한다. 범위를 지정할 수 있다.

del 예시)
sample_list = [1, 2, 3, 4, 5]
del sample_list[0:2] :: 인덱스 범위 지정

print(sample_list)


6. 기타 함수

sort() 함수 : 
    정렬할때 사용, 기본적으로 오름차순이지만, .sort(reverse = True) 로 사용하면 내림차순으로 정렬
    같은 타입의 자료형만 list 의 요소로 가지고 있을때만 정렬 가능

max(), min() 함수 :
    list 내의 요소 중 가장 큰 값/작은 값을 구한다, max(sample_list), min(sample_list)
    마찬가지로 같은 타입만

sum() 함수 : 
    list 내의 모든 요소의 합을 구한다, sum(sample_list)
    int 타입만 sum함수를 사용할 수 있다.


7. 특정 값 있는지 확인

list 내부에 특정 값이 있는지 확인하려면 in 을 쓴다. 없는지 확인할 때는 not in

예시)
sample_list = [1, 2, 3, 4, 5]
print(2 in sample_list)

# 결과: True


8. for in 반복문

리스트 내부 요소를 순환하면서 특정 명령을 수행
파이썬에서는 다음과 같이 선언, 들여쓰기한다.

sample_list = [1, 2, 3, '4', '5', '6', '7', 8]

for i in sample_list :
    print(i)


참고사항

 * 문자열 인덱싱

 문자열을 저장하면, 각 문자를 하나의 요소로 갖는 또 하나의 리스트형태로 저장이 된다.
 만약 sample_list = ['hello', 'world']
 이렇게 선언된 list가 있을 때,
 sample_list[0][0] 은 'h' 가 된다.

'''

'''
튜플

튜플을 선언하는건, 패킹 이라고도 한다.

튜플 안에 튜플을 패킹할 수 있다.

예시 ) 
sample_tuple1 = ('hello', 8, True)
sample_tuple2 = ('hello', 8), True
sample_tuple3 = 'hello', (8, True)

* 언패킹

튜플에 저장된 여러개의 요소를 다시 변수에 한 개씩 나누어 담는 것
언패킹을 할 때, 튜플 내부의 요소의 갯수만큼 변수가 있어야 한다.
비구조화랑 비슷

예시)

sample_tuple = ('hello', 8, True)
sample_text, sample_number, sample_bool = sample_tuple

print(sample_text, type(sample_text))
print(sample_number, type(sample_number))
print(sample_bool, type(sample_bool))

결과
hello <class 'str'>
8 <class 'int'>
True <class 'bool'>

'''


'''
딕셔너리


1. 요소추가

딕셔너리 내부에도 딕셔너리 선언 가능, (튜플, 리스트 마찬가지)

sample_dict = {'name': 'kim', 'age': 28, 'car': {'model': 'audi', 'color': 'black'}}
print(sample_dict['car']['color'])

위와 같이 접근함


2. 요소 삭제

del 명령어를 사용해서 key 이름으로 삭제

del sample_dict['age']
print(sample_dict)


3. 함수 사용

* get() 함수 사용
    get함수를 사용해서 딕셔너리의 특정 키의 value를 가져온다.

예시)
sample_dict = {'name': 'kim', 'age': 28, 'car': {'model': 'audi', 'color': 'black'}}

print(sample_dict.get('name'))
print(sample_dict['name'])

위 두 print는 동일한 값을 출력한다.
# 결과 : kim

* keys() : 딕셔너리의 key를 모두 출력한다.
* values() : 딕셔너리의 value를 모두 출력한다.
* items() : 딕셔너리의 key와 value를 모두 출력한다.

예시)
sample_dict = {'name': 'kim', 'age': 28, 'car': {'model': 'audi', 'color': 'black'}}

print(sample_dict.keys())
print(sample_dict.values())
print(sample_dict.items())

# 결과 :
dict_keys(['name', 'age', 'car'])
dict_values(['kim', 28, {'model': 'audi', 'color': 'black'}])
dict_items([('name', 'kim'), ('age', 28), ('car', {'model': 'audi', 'color': 'black'})])

실행 결과 함수 앞에 dict_ 가 붙는다.
keys()와 value()는 리스트 안에 담겨서 나오고,
items() 는 리스트 안에 튜플로 감싸져 나온다.



4. for in 반복문

딕셔너리의 요소를 for 문으로 출력하는 방법

sample_dict = {'name': 'kim', 'age': 28, 'car': {'model': 'audi', 'color': 'black'}}

for key in sample_dict:
    # key와 value를 모두 출력
    print(key, sample_dict[key])
    # key를 출력, end = ' '를 통해서 줄나눔이 아닌 공백기준으로 출력
    print(key, end = ' ')
    # value만 출력, end = ' '를 통해서 줄나눔이 아닌 공백기준으로 출력
    print(sample_dict[key], end = ' ')

'''

