#for문을 이용하여 1에서 10까지 합을 구하시오.
sum = 0
for i in range(1, 11, 1):
    sum+=i
print("sum  : %d" % sum)
print("---------------")
#for문을 이용하여 1에서 10까지 식과 합을 구하시오.
sum = 0
for j in range(1, 11, 1):
    if j<10:
        print("%d + " % j, end="")
    elif j==10:
        print("%d = " % j, end="")
    sum+=j   
print("%d" % sum)