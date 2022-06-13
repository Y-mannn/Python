#아래 코드의 is 연산자 결과 및 각각의 print 결과를 예상하여 말해보시오.

#[1]
a = "korea"
print('[1]', a, id(a))

b = "korea"
print('[2]', b, id(b))
print('a is b = ', a is b)

b += "!"
print('[3]', b, id(b))
print('a is b = ', a is b)

#korea!
c = b[:-1]
print('[4]', c, id(c))
print('a is c = ', a is c)
