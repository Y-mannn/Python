#클래스의 인스턴스 객체가 생성될 때 마다 객체의 카운트를 1씩 증가시키는 클래스를 구현하시오.
#이 때 카운트 증가 함수는 클래스 내 메서드를 통해서 구현한다.

#[1]: 클래스 생성
#--------------------------------------
import random

class Person:
    
    #클래스 변수
    count_class_var = 0
    
    #생성자
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.power = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.increase_obj()
    
    #소멸자
    def __del__(self):
        Person.count_class_var -= 1
    
    #클래스 메서드
    def increase_obj(self):
        Person.count_class_var += 1
#--------------------------------------

#[2]: 클래스 사용
print('현재까지 생성된 인스턴스 객체의 갯수 --> ', Person.count_class_var) #0
print('-' * 70)

p1 = Person('홍길동', 20)
print('현재까지 생성된 인스턴스 객체의 갯수 --> ', Person.count_class_var) #1
print(f'인스턴스의 이름은 {p1.name}, 나이는 {p1.age}, 파워는 {p1.power}입니다.')
print('-' * 70)

p2 = Person('강감찬', 30)
print('현재까지 생성된 인스턴스 객체의 갯수 --> ', Person.count_class_var) #2
print(f'인스턴스의 이름은 {p2.name}, 나이는 {p2.age}, 파워는 {p2.power}입니다.')
print('-' * 70)

p3 = Person('을지문덕', 40)
print('현재까지 생성된 인스턴스 객체의 갯수 --> ', Person.count_class_var) #3
print(f'인스턴스의 이름은 {p3.name}, 나이는 {p3.age}, 파워는 {p3.power}입니다.')
print('-' * 70)

del p3
print('현재까지 생성된 인스턴스 객체의 갯수 --> ', Person.count_class_var) #2
print('-' * 70)

del p2
print('현재까지 생성된 인스턴스 객체의 갯수 --> ', Person.count_class_var) #1
print('-' * 70)

del p1
print('현재까지 생성된 인스턴스 객체의 갯수 --> ', Person.count_class_var) #0
print('-' * 70)
