#대문자 A, B, C 3개 문자에 대해서 아스키 코드로 출력하는 코드를 작성하시오.

#[1]: 대문자 A --> 넌 정체가 뭐냐?
print('A', type('A'))
print(ord('A')) #ord() 함수는 문자를 입력받아 해당 문자에 해당하는 아스키코드 값을 반환(ordinal number)
print(ord('B'))
print(ord('C'))
print(ord('Z')) #A(65) + 알파벳문자(26개 - 1) = Z(90)

#[2]: 소문자 a --> 넌 정체가 뭐냐?
print('a', type('a'))
print(ord('a')) #97
print(ord('b'))
print(ord('c'))
print(ord('z')) #a(97) + 알파벳문자(26개 - 1) = z(122)

#사용자로 부터 숫자(아스키 코드)를 입력받아 그에 해당하는 문자를 출력하는 프로그램을 구현하시오.

#[1]: 사용자 입력
a = input('숫자를 입력하면 해당하는 문자를 출력해드려요 = ')
print(a, type(a)) #타입이 str

#[2]: 정수형으로 자료형을 반환
a = int(a)
print(a, type(a)) #타입이 int

#[3]: 해당하는 값을 출력하기 --> chr() 함수 사용
chr_ = chr(a)
print('당신이 입력한 숫자의 문자는: ', chr_)
print(f'당신이 입력한 숫자의 문자는 {chr_}입니다.') #f문자열