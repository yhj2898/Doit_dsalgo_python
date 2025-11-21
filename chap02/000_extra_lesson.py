# [2C-2] 리스트의 모든 원소를 enumerate() 함수로 스캔 스캔 (원소 수 미리 파악)
x = ['지수','민규','이찬','용복','현진']
for i, name in enumerate(x):
    print(f'x[{i}] = {name}')


# [2C-3] 리스트의 모든 원소를 enumerate() 함수로 스캔(1부터 카운트)
for i, name in enumerate(x,1):
    print(f'{i}번째 = {name}')

'''
enumerate(x,1) : 인덱스를 1부터 시작
'''

# [2C-1] 리스트의 모든 원소 스캔 (원소 수 미리 파악)

