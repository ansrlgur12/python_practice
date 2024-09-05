import random


def guess_number():

    number = random.randint(0, 100)

    guess = int(input("0부터 100사이의 숫자를 입력하세요 : "))
    temp = 1

    while True:
        if guess > number:
            print("더 작은 수를 입력하세요.")
            guess = int(input("다시 입력하세요 : "))
        elif guess < number:
            print("더 큰 수를 입력하세요.")
            guess = int(input("다시 입력하세요 : "))
        else:
            print(f"시도횟수 : {temp}번")
            break

        temp = temp + 1

    
guess_number()
