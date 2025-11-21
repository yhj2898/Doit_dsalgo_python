# 1. n 이하의 소수의 배열 & 갯수

n = int(input('양의 정수 n을 입력하세요 : '))

prime = []

for num in range(2, n+1):
    is_prime = True
    
    for p in prime:
        if p*p > num:
            break
        if num % p == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(num)
    
            


print(f'{n}이하의 소수 개수 : {len(prime)}개')
print(f'소수 목록 : {prime}')