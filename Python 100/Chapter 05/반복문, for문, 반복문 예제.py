#0부터 9까지 숫자가 아래처럼 출력되도록 for 반복문 예제를 구현하시오.

#[1]: for 반복문
print('[출력 결과]')
print('-' * 100)

for i in range(10):
    print(i, end='')
print('\n')
    
for i in range(10):
    print(i, end=' ')
print('\n')
    
for i in range(10):
    print(i, end='\t')
print('\n')

for i in range(10):
    print(i, end=', ')
print()