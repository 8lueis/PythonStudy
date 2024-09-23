sample = input('문자열 입력')


print('k 문자 개수: ', sample.count('k'))
print('문자 길이', len(sample))

print('a가 몇 번 인덱스에 있나용 -> ',sample.find('a'))

print(sample.upper())
print(sample.lower())

print(sample.lstrip())
print(sample.rsplit())

print('----아래로는 name list----')

name = ['Lee', 'Jung', 'Choi','Kim']

a = ','

string = a.join(name)
print(string)

lst = string.split(',')
print(lst)

