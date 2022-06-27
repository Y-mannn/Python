#학생 5명의 수학 점수를 입력 받아 60점 이상만 합계를 구하는 코드를 구현하시오.

#[1]: 사용자 입력
scores = input('학생 5명의 수학 점수를 입력하세요: ').split()

#[2]: 입력 받은 값 --> 리스트
print(scores, type(scores))

#[3]: 필요한 변수 선언 후 반복문 돌면서 조건을 처리
sum = 0
scores_num = len(scores)

for i in range(0, 5):
    if int(scores[i]) >= 60:
        sum += int(scores[i])

#[4]: 출력
print('[결과 출력]')
print('-' * 100)
print(f'학생 {scores_num}명의 입력 점수 중 60점 이상 합계는? {sum}점 입니다.')
print('-' * 100)