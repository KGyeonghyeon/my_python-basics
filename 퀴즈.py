# 1번째 퀴즈 변수를 이용하여 다음 문장을 출력하시오

station = "사당"
print("%s행 열차가 들어오고 있습니다." %station)

# 2번째 퀴즈 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오
'''조건 1 : 랜덤으로 날짜를 뽑아야 함
조건 2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
조건 3 : 매월 1~3일은 스터디 준비를 해야하므로 제외'''

from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 %s 일로 선정되었습니다." %date)

# 3번째 퀴즈 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오
url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]

print(my_str[0:3] + str(len(my_str)) + str(my_str.count("e")) + "!")