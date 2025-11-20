# 오른쪽 아래가 직각인 이등변 삼각형으로 * 출력하기

print('오른쪽 아래가 직각 이등변 삼각형을 출력합니다.')
n = int(input('짧은 변의 길이를 입력하세요 : '))

for i in range(n):
    for _ in range(n - i - 1):  
        print(' ', end='')      # 공백 출력
    for _ in range(i + 1):
        print('*', end='')
    print()
    
'''
1. 공백 출력 -> for _ in range(n - i - 1):
- 모든 행에서 공백과 * 개수 합하면 n
- 첫 줄 = i=0 -> *이 1개 = 공백이 (n-1)개 -> 즉, 공백은 n-1 -i 개!

'''