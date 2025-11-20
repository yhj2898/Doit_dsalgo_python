# +와 -를 번갈아 출력하기 1

print('+와 -를 번갈아가며 출력합니다.')
n = int(input('몇 개를 출력할까요? : '))

for i in range(n):
    if i % 2:
        print('-', end='')  # i가 홀수면 - 출력
    else:
        print('+', end='')  # i가 짝수면 + 출력
        

# for문이 반복될 때마다 if 문도 수행되어 비효율적

# range(n) : 0부터 시작해서 n-1까지 총 n개를 만든다! => 원하는 횟수만큼 반복하려면 range(n) 써야 함!
# ㄴ range(n+1) 아님 주의!

"""
if i % 2:
ㄴ (if i % 2 == 1) = (if i % 2)
ㄴ 1 = True, 0 = False 라서 =1 생략하고 `if i % 2`만 써도 됨!
ㄴ i % 2의 결과가 1 = True = if 블록 실행

"""

