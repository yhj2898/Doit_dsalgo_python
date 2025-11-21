# 뮤터블 시퀀스 원소를 역순으로 정렬

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n//2):
        a[i], a[n-i-1] = a[n-i-1], a[i]
        
if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬합니다.')
    nx = int(input('원소 수를 입력하세요. : '))
    x = [None] * nx
    
    for i in range(nx):
        x[i] = int(input(f'x[{i}]값을 입력하세요. : '))
        
    reverse_array(x)
    
    print('배열 원소를 역순으로 정렬했습니다.')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')

'''
1. reverse_array(a: MutableSequence) -> None:
- a는 리스트 같이 '수정 가능한 자료형'임 
- 이 함수는 값을 되돌려주지 않음(None), 대신 원본 자체를 변경함

2. for i in range(n//2):
- 절반만 바꾸면 전체가 뒤집힘

'''