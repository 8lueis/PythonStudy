##for문 while문 비교
print("-- for문 --")

for i in range(0,3,1):
  print("%d : 안녕하세요 for문 공부 중입니다."%i)

print("-- while --문")

##while
i = 0
while i < 3:
  print("%d: 안녕하세요 while문 공부 중입니다."%i)
  i = i + 1


##Code06-09
i, hap = 0,0
i = 1
while i < 11:
  hap = hap + i
  i = i + 1

print("1에서 10까지의 합계: %d"%hap)



##Code06-10
hap = 0
a, b = 0, 0
while True:
  a = int(input("더할 첫 번째 수를 입력하세요: "))
  b = int(input("더할 두 번째 수를 입력하세요: "))
  hap = a + b
  print("%d + %d = %d"%(a,b,hap))
  break



#Code06-11
##0을 입력하면 종료
ch = ""
a, b = 0, 0

while True:
  a = int(input("계산할 첫 번째 수를 입력하세요: "))
  b = int(input("계산할 두 번째 수를 입력하세요: "))
  ch = input("계산할 연산자를 입력하세요: ")

  if(ch == "+"):
    print("%d + %d = %d"%(a,b,a+b))
  elif(ch == "-"):
    print("%d - %d = %d"%(a,b,a-b))
  elif(ch == "*"):
    print("%d * %d = %d"%(a,b,a*b))
  elif(ch == "/"):
    print("%d / %d = %d"%(a,b,a/b))
  elif(ch == "%"):
    print("%d %% %d = %d"%(a,b,a%b))
  elif(ch == "//"):
    print("%d // %d = %d"%(a,b,a//b))
  elif(ch == "**"):
    print("%d ** %d = %d"%(a,b,a**b))
  else:
    print("연산자를 잘못 입력했습니다.")
  break


##마름모 만들기

i, k = 0,0
i = 0
while i < 9:
  if i < 5:
    k = 0
    while k < 4 - i:
      print(' ', end='')
      k += 1
    k = 0
    while k < i * 2 + 1:
      print('\u2665',end='')
      k += 1
  else:
      k = 0
      while k < i - 4:
        print(' ',end='')
        k += 1
      k = 0
      while k < (9 - i) * 2 - 1:
        print('\u2665',end='')
        k += 1
  print()
  i += 1