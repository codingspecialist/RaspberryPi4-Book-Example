def mydef01():
    i = 10
    j = 20
    print(i+j)
mydef01()
def mydef02(i, j):
    print(i+j)
mydef02(10, 20)
# 계산할 숫자를 두 개 입력하세요.
def mydef03(i, j , p):
    if p == '+':
        print(i+j)
    elif p == '-': 
        print(i-j)
    elif p == '*':  
        print(i*j) 
    elif p == '/':  
        print(i/j)   
n = int(input("첫 번째 숫자를 입력하세요."))
m = int(input("두 번째 숫자를 입력하세요."))
p = input("연산자를 입력하세요(+, -, *, /)")
mydef03(n, m, p)

