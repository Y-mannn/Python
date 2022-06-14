#0부터 9까지 숫자가 아래처럼 출력되도록 for 반복문 예제를 구현하시오.
#0부터 9까지 숫자를 가로출력 했을 때 마지막 콤마를 없애시오.
#0, 1, 2, 3, 4, 5, 6, 7, 8, 9

#[1]: for 반복문
print('[출력 결과]')
print('-' * 100)

n = 0
for i in range(10):
    if n < 9:
        print(i, '(', n, ')', end=', ') #end 옵션 뒤에는 값이 올수 없다. 앞은 가능
    else:
        print(i, '(', n, ')')
    n += 1
    
print()


for i in range(10):
    if i < 9:
        print(i, end=', ') #end 옵션 뒤에는 값이 올수 없다. 앞은 가능
    else:
        print(i)
    
print()