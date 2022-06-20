#클래스 외부에서 클래스 변수의 초기 값을 변경하는 코드의 결과를 예상하여 말해보시오
#이 문제는 클래스 변수 사용시 주의점에 대해서 아는지를 묻는 문제이다.

#[1]: 클래스 생성
#------------------------------------------
class MyClass:
    
    #클래스 변수
    a_var = 0
    
    #클래스 메서드
    def a_method(self):
        self.a_var = 300
        
    def b_method(self):
        MyClass.a_var = 300
#------------------------------------------

#[2]: 클래스 사용
print('[1]최초 초기 값 --> ', MyClass.a_var)

MyClass.a_var = 100
print('[2]초기 값을 100으로 변경 --> ', MyClass.a_var)

m1 = MyClass()
m1.a_method()
print('[3-1]클래스 내 메서드 호출(a_method())을 통해서 변수 값을 300으로 변경 --> ', m1.a_var, MyClass.a_var)
m1.b_method()
print('[3-2]클래스 내 메서드 호출(b_method())을 통해서 변수 값을 300으로 변경 --> ', m1.a_var, MyClass.a_var)