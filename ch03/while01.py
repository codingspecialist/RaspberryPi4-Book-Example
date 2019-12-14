str = "꿈은 이루어 진다."
i = 0
while i<3:
    print(str)
    i = i + 1
print("-----------------------------------")
#while문으로 입력한 숫자만큼 str을 반복 출력하시오.
i = int(input("반복 횟수 숫자를 입력하세요. "))
j = 1
flag = True
while flag:
    j = j + 1 
    if i < j:
        flag = False
    print(str)