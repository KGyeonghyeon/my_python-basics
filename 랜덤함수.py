from random import *

#0.0 ~ 1.0미만의 임의의 값 생성
print(random()) 

#0.0 ~ 10.0미만의 임의의 값 생성
print(random() * 10)

#소수점 뒤를 없애는 법
print(int(random() * 10))

#1부터 10 이하의 임의의 값 생성
print(int(random() * 10) + 1) 

print(int(random() * 10))

print(randrange(1, 46)) # 1~ 46 미만의 임의의 값 생성

#randint : 양끝을 모두 추가
print(randint(1, 45))