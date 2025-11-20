# a부터 b까지 정수의 합 구하기1

print('a부터 b까지 정수의 합을 구합니다.')

a = int(input('정수 a를 입력하세요 : '))
b = int(input('정수 b를 입력하세요 : '))

if a>b:
    a,b = b,a

sum=0
for i in range(a, b+1):
    if i<b:                         # i가 b보다 작으면 합을 구하는 과정 출력
        print(f'{i} + ', end='')    # ★ end='': 덧셈 과정에서 줄바꿈 없이 한 줄에 이어서 보여주기 위함
    else:
        print(f'{i} = ', end='')
    sum += i
print(sum)

# 해당 코드는 b가 큰 수일 경우, if문이 많이 반복되어 비효율적! -> for문 안에 있는 if문을 제외하여 별도로 두는 것이 더 좋음!

# print() -> 자동으로 줄바꿈
# `end =  ` 쓰면 줄바꿈 하지 않고 출력 뒤에 내가 지정한 걸 붙여줌! 
