#파이썬 리스트 생성 시 빈 리스트를 생성하는 코드를 2가지로 구현해보시오.

#[1]: 빈 리스트 생성 --> 첫 번째 방식
a = []
print('[1]빈 리스트 첫번재 방식: ', a, type(a))

#[2]: 빈 리스트 생성 --> 두 번째 방식
b = list()
print('[2]빈 리스트 첫번재 방식: ', b, type(b))

#[3]: 리스트 생성
c = [1, 2, 3, 3]
print('[3]리스트 생성: ', c, type(c))

#[4]: 리스트를 집합으로
d = set(c)
print('[4]리스트를 집합으로: ', d, type(d))