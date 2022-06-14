#for 반복문을 사용해서 4부터 21까지의 홀수들의 합을 구하는 코드를 구현하시오.

#[1]: 변수 선언 및 초기 데이터 값 설정
first = 4
last = 21

#[2]: for 반복문
sum_odd = 0
for i in range(first, last + 1):
    #홀수 판단
    if i % 2 == 1:
        sum_odd += i
   
sum = 0   
for i in range(4, 22):
    if i % 2 != 0:
        sum += i

#[3]: 출력
print('[결과 출력]')
print('-' * 100)
print(sum_odd)
print(sum)