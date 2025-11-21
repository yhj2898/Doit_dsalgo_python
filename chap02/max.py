# 시퀀스 원소의 최댓값 출력하기


from typing import Any, Sequence

# max_of() 함수 정의
def max_of(a: Sequence) -> Any:
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

# max_of() 함수 실행
if __name__ == '__main__':
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요. : '))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요. : '))
        
    print(f'최댓값은 {max_of(x)}입니다.')
    
'''
1. max_of(a:Sequence) -> Any:
- Any : 제약이 없는 임의의 자료형 (아무 타입이든 반환 받을 수 있음)
- Sequence : 리스트, 튜플, 문자열 등 순서가 있는 자료형
- 건네 받는 매개 변수 a의 자료형은 Sequence임
- 반환하는 것은 임의의 자료형인 Any임

2. if __name__ == '__main__':
- 이 파일을 ‘직접 실행할 때만’ 실행 코드가 작동하게 하고, import될 때는 작동하지 않도록 막아주는 장치
- 즉, 함수로 정의한 max_of()를 다른 파일에서 실행할 때 'max_of()함수의 실행'부분이 실행되지 않게 하기 위함

3. x = [None] * num
- 길이가 num인 리스트 미리 만들어 놓기
- 처음에는 아무 값도 없으니까 None으로 빈 자리 채움
- x = [] * num으로 할 경우, 항상 빈 리스트가 생성되어 적절하지 않음!
'''