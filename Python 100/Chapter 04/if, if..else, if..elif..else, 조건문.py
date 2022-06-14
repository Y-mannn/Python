#파이썬의 기본적인 if .. else 조건문과 if .. elif .. else 조건문 예제를 구현하시오.

#[1]: if .. else 조건문
a = 110

if a > 120:
    print('a는 120보다 크다.')
else:
    print('a는 120보다 작다.')

#[2]: if..elif 조건문 --> 청년(~39세 미만), 중년(40세~59세), 장년(60세~79세), 노년(80세~)
age = 80

if age < 40:
	print('당신은 청년이에요..')
elif age < 60:
	print('당신은 중년이에요..')
elif age < 80:
	print('당신은 장년이에요..')
else:
	print('당신은 노년이에요..')
