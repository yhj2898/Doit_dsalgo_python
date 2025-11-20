# 학생 5명의 점수를 입력받아 합계와 평균을 출력하기

print('학생 그룹 점수의 합계와 평균을 구합니다.')

score1 = int(input('1번 학생의 점수를 입력하세요.: '))
score2 = int(input('2번 학생의 점수를 입력하세요.: '))
score3 = int(input('3번 학생의 점수를 입력하세요.: '))
score4 = int(input('4번 학생의 점수를 입력하세요.: '))
score5 = int(input('5번 학생의 점수를 입력하세요.: '))

total = 0
total += score1
total += score2
total += score3
total += score4
total += score5


print(f'합계는 {total}점입니다.')
print(f'평균은 {total/5}점입니다.')

'''
1. 해당 코드로는 학생 수 변경/특정 학생의 시험점수 확인하거나 변경/정렬이 필요한 경우 등 처리가 어려움
-> 학생 점수는 하나의 값을 저장하는 변수가 아니라, 묶음 단위로 값을 저장하는 "배열"로 다뤄야 함.
'''