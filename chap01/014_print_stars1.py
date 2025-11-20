# *를 n개 출력하되 w개마다 줄바꿈하기 1

print('*를 출력합니다.')
n = int(input('몇 개를 출력할까요? : '))
w = int(input('몇 개마다 줄바꿈할까요? : '))

for i in range(n):
    print('*', end='')
    if i % w == w-1:
        print()         # 줄바꿈

if n % w:
    print()             # 남은 별이 있을 때 깔끔하게 줄바꿈 (다음 출력을 위함?)
    
# for 문을 반복할 때마다 if문을 실행하므로 효율적이지 않음!

'''
1. i % w == w-1  -> w가 아니라 w-1
- range(n)에서 i는 0부터 시작
- → w번째 별을 출력하는 순간은 i = w-1
'''