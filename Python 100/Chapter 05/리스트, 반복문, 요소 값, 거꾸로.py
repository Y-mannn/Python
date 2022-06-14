#리스트 요소의 값을 반복문을 사용하여 거꾸로 출력시키시오.
#이 문제는 리스트의 값들을 거꾸로 출력시킬 때 필요한게 무엇인지를 아는지 묻는 문제이다.

#[1]: 리스트
lst = ['dog', 'hippo', 'elephant', 'lion', 'tiger', 'alligator']

#[2]: 반복문 --> 거꾸로 출력
for i in lst[::-1]:
    print(i, end='\t\t')
print()

#[3]: 반복문 --> 정방향 출력
for i in lst[::1]: #lst[시작:끝:step]
    print(i, end='\t\t')
print()

#[4]: 반복문 --> 2칸 간격으로 출력
for i in lst[::2]: #lst[시작:끝:step]
    print(i, end='\t\t')
print()