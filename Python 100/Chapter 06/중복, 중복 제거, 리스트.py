#리스트에 들어이는 동물 중 중복된 동물을 제거하여 출력하시오
#이 문제는 리스트에 중복된 값을 제거하는 방법에 대해서 아는지를 묻는 문제이다.

#[1]: 리스트
lst = ['dog', 'hippo', 'elephant', 'lion', 'tiger', 'alligator', 'hippo', 'lion']

#[2]: 중복 제거 --> set() --> 집합 --> 중복을 허용하지 않음.
lst2 = set(lst)
print(lst2, type(lst2)) #이 때 집합 타입은 요소가 순서없이 뒤죽박죽 정렬이 된다.
lst3 = list(set(lst))
print(lst3, type(lst3))