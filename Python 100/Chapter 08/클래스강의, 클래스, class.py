#파이썬 OOP에서 클래스란 무엇인지 설명해보시오.
#[클래스 강의1]: 변수와 리스트를 사용하여 캐릭터 정보를 저장하고 출력해보시오.
#[클래스 강의2]: 함수를 사용하여 각 캐릭터에 파워 레벨을 랜덤으로 부여하고 출력해보시오.
#[클래스 강의3]: 클래스를 만들어보시오.
#[클래스 강의4]: 만든 클래스를 사용해보시오. **

#[5]: 클래스 사용 --> 클래스 객체를 생성 --> 그것을 변수에 할당
#어려운말로 --> PersonInfo 클래스의 인스턴스 객체를 생성.
#선언적 의미의 클래스 --> 선언만 해놓은 클래스를 실제 코드에서 활용하기 위한 하나의 절차
#---------------------------------------
class PersonInfo:
    def hello(self): #클래스 내에서는 인자로 self를 넣어줘야 한다.
        print('안녕하세요')
#---------------------------------------

p = PersonInfo()
print(p, type(p))
p.hello()

a= [2, 6, 3, 1, 4]
print(a, type(a))
a.sort()
print(a)
#a.helle() Error