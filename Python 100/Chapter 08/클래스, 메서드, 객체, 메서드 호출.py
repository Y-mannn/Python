#클래스 메서드 안에서 다른 메서드를 호출하는 코드를 만들어보시오.
#이 문제는 self를 이용한 메서드 호출 형식에 대해서 아는지를 묻는 문제이다.
#참고로, self없이 메서드를 호출하면 --> 클래스 외부 함수 호출.

#[1]: 클래스 생성
#------------------------------------------------
class Person:

    def a_method(self):
        print('a_method가 호출되었습니다.')
    
    def b_method(self):
        self.a_method() #self 사용해서 a_method 호출
        
    def c_method(self):
        a_method() # 외부 a_method 호출
#------------------------------------------------
def a_method():
    print('클래스 외부에 정의된 a_method입니다.')

#[2]: 클래스 사용
p1 = Person()
p1.a_method() #바로 a_method를 호출하는건 당연히 가능
p1.b_method() #b_method를 통해서 a_method를 호출하는 것도 가능
p1.c_method()