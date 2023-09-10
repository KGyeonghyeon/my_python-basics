#방법 1
print("나는 %d살입니다." %14)
print("나는 %s을 좋아해요" %"파이썬")
print("나는 %c를 받았어요." %"A")

print("나는 %d살이고, %s를 좋아해요." %(4, "대머리"))

#방법 2
print("나는 {1}살이고, {0} 입니다.".format(20, "대머리"))

#방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))

#방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")