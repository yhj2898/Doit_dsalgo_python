# 10 ~ 99 사이의 난수 n개 생성하기 (13이 나오면 중단)

import random

n = int(input('난수의 개수를 입력하세요 : '))

for _ in range(n):
    r = random.randint(10,99)            # 10부터 99사이의 난수 생성
    print(r, end=' ')                    # 띄어쓰기로 구분 
    if r == 13:
        print('\n 프로그램을 중단합니다.')  # \n = 줄바꿈
        break
    
else:
    print('\n난수 생성을 종료합니다.')
    
'''
1. random.randint(a,b) : a 이상 b 이하 정수 가운데 무작위로 1개 반환
'''