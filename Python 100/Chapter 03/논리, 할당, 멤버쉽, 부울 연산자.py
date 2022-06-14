#논리 연산자 예제를 만들어보시오.

#[1]: 논리 연산자
a = True
b = False

print(a and b) #False
print(a or b) #True
print(a, not(a)) #True, False

if a or b:
	print('True')
else:
	print('False')
print('-' * 100)
	
#할당 연산자 예제를 만들어보시오.

#[1]: 산술, 관계, 논리
a = 100
a = a + 1
print(a) #101

b = 200
b += 1
print(b) #201

c = 300
c *= 2
print(c) #600
print('-' * 100)

#in(멤버쉽) 연산자 예제를 만들어보시오.

#[1]: in 연산자
lst = [1, 2, 3, 4, 5]
print(lst, type(lst))

d = 7 in lst
print(d) #False
e = 5 in lst
print(e) #True

tpl = 1, 2, 3
print(tpl, type(tpl))

f = 4 in tpl
print(f) #False

g = 3 in tpl
print(g) #True
print('-' * 100)

#부울(Boolean) 연산자 예제를 만들어보시오.
#그 외 비트 연산자, is 연산자(동일 객체 비교) 등 도 있다는 정도만 우선 참고하자

#[1]: 부울 연산자 --> True, False 결과가 반환
print(bool(1)) #파이썬에서 1은 참(True)을 의미
print(bool(0)) #파이썬에서 0은 거짓(False)을 의미
print('마이너스 결과는: ', bool(-1)) #참(True)

print(bool(None)) #파이썬에서 None 값은 거짓(False)을 의미
print('-' * 100)

#[2]: None 너는 대체 뭐냐? --> 말 그대로 아무것도 없다는 뜻 --> 하나의 type --> 타입체크를 하면 NoneType으로 나옴.
#아무것도 없기 때문에 부울 연산자로 출력하면 항상 거짓(False)을 출력.

a = None
print(a, type(a))
print(bool(a)) #False