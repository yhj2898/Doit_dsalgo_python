# 가로, 세로 길이가 정수이고 넓이가 area인 직사각형에서 변의 길이 나열하기

area = int(input('직사각형의 넓이를 입력하세요. : '))

for i in range(1, area+1):      
    if i * i > area: break      # i가 area의 제곱근보다 커지는지 확인 -> 커지면 이후론 짝이 이미 앞과 중복되므로 의미 없음
    if area % i: continue       # area가 i로 나누어 떨어지지 않으면 for문의 다음 반복으로 진행(아래 print문 무시하고 다음 i 검사로 넘어감)
    print(f'{i} x {area // i}') # 짧은 변, 긴변의 순서로 출력
