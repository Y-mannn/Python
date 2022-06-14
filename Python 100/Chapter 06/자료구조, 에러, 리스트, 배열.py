#아래의 자료구조에 접근시 에러가 나는 것은 무엇이고 그 이유를 설명해보시오.
#이 문제는 리스트 타입과 집합 타입의 차이점을 이해하고 있는지를 묻는 문제이다.

#[1]: 리스트
a = ['dog', 'hippo', 'elephant', 'lion', 'tiger', 'alligator', 'hippo', 'lion']
print('[1]lion 출력하기: ', a[3])

#[2]: 집합
b = set(a)
# print('[2]lion 출력하기: ', b[3]) 집합은 인덱스로 접근할 수 없다. Error
print('[2]집합 출력하기: ', b)