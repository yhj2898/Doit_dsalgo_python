# a부터 b까지 정수의 합 구하기2
# -> sum_verbose1보다 효율↑  (for문 안의 if문 실행횟수 ↓)

print('a부터 b까지 정수의 합을 구합니다.')

a = int(input('정수 a를 입력하세요 : '))
b = int(input('정수 b를 입력하세요 : '))

if a>b:
    a,b = b,a

sum=0
for i in range(a, b):           # for문에서 a부터 b-1까지 값 뒤에 + 붙여 출력
    print(f'{i} + ', end='')
    sum += i

print(f'{b} = ', end='')        # b의 값 뒤에 =를 붙여 출력
sum += b

print(sum)