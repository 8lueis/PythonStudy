print('주민번호 7자리 입력')

RRN = input()

year = RRN[:2]
month = RRN[2:4]
day = RRN[4:6]
# day = RRN[-3:-1]
gender = RRN[-1]

print("태어난 연도는 %s년, 달은 %s월, 날짜는 %s일이고, 성별은 "%(year, month, day), end='')

if gender == '1' or gender == '3':
    print('남성입니다.')
elif gender == '2' or gender == '4':
    print('여성입니다.')
