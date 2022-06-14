#1부터 100까지의 수에서 짝수들만 출력하는 코드를 구현하시오.
#두 가지 방식을 생각해서 구현해보시오.

#[1]: if 조건문을 이용 --> 홀짝 판단 후 처리.
for i in range(1, 101):
    # print(i, end=' ')
    if i % 2 == 0:
        print(i, end=' ')
print()

#[2]: range() 함수의 step(간격) 옵션 값을 이용하여 처리.
for i in range(1, 101, 2):
    print(i, end=' ')
print()

for i in range(2, 101, 2):
    print(i, end=' ')
print()