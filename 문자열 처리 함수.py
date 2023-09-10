python = "Python is Amazing"

#모두 소문자로 출력
print(python.lower())

#모두 대문자로 출력
print(python.upper())

#첫 번째 값이 대문자, 소문자인지 확인
print(python[0].isupper())
print(python[2].islower())

#문자의 길이를 알아낼때
print(len(python))

#특정문자를 바꾸고 싶을 때
print(python.replace("Python", "Java"))

#특정 문자의 위치 확인
index = python.index("n")
print(index)

index = python.index("n", index + 1)
print(index)

print(python.find("n"))

#index와 find의 차이점 : 값이 없을 때 
#index는 시스템을 종료, find는 -1을 표기하고 계속 실행

#count : 문자가 몇 번 나오는지
print(python.count("Python"))