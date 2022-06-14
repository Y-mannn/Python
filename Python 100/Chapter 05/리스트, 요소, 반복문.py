#리스트 요소의 값을 반복문을 사용하여 모두 출력하시오.
#이 때 가로로 값을 출력시키시오.
#값을 모두 출력한 후에는 끝에 요소의 갯수를 함께 출력시키시오.

#[1]: 리스트
lst = ['dog', 'hippo', 'elephant', 'lion', 'tiger', 'alligator']

#[2]: 반북문 --> 출력
for i in range(len(lst)):
    print(lst[i], end='\t')
print('총', len(lst), ' 개 요소')
print()