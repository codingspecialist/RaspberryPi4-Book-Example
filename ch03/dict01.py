#딕셔너리 타입(Dictionary Type)
dict = {'번호':10, '성명':'장동건', '나이': 23, '사는곳':'서울'}
print(dict)
print(type(dict))
print(dict['나이'])
#특정항목 변경
dict['나이'] = 24
print(dict['나이'])
#특정항목 추가
dict['직업'] = '배우'
print(dict)
#키 및 값 전체 반환
print(dict.keys())
print(dict.values())
# 키값 존재 여부 및 삭제
print('사는곳' in dict)
del dict['사는곳']
print('사는곳' in dict)
print(dict)