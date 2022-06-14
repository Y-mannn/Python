#for 반복문을 사용해서 구구단 전체(2단 ~ 9단)를 출력하는 코드를 구현하시오.
#이 문제는 이중 반복문을 사용할 수 있는지를 묻는 문제이다.

#[1]: 구구단
for i in range(2, 10):
    print(i,'단')
    for j in range(1, 10):
        print(i, ' x ', j, ' = ', i * j)
    print()
    
print('-' * 100)

for i in range(0, 10):
    for j in range(2, 10):
        if i == 0:
            print(j, '단', end='\t\t')
        else:
            print(j, ' x ', i, ' = ', j * i, end='\t')
    print()
  