#if문
a = 23
if a < 50:
    print('50보다 작군요')
#if else문
if a < 20:
    print('20보다 작군요')
else:
    print('20보다 크군요')
#elif문
age = int(input('현재 나이를 입력하세요. '))
if age < 10:
        print('유년층 입니다.')
elif age < 20:
        print('10대입니다.')
elif age < 30:
        print('20대입니다.')
elif age < 40:
        print('30대입니다.')
else:
    print('장년층입니다')


