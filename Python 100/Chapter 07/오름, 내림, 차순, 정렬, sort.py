#오름차순, 내림차순 정렬을 sort(), sorted() 함수로 구현하시오.
#sort(), sorted() 함수의 차이점을 아는지 묻는 문제이다.

#[1]: 리스트
lst = [100, 50, 40, 70, 90, 60, 80]

#[2]: sort() 함수를 이용한 오름차순, 내림차순 정렬
#sort()함수나 sorted()함수나 아무런 옵션이 없이 사용하면 디폴트 정렬 --> 오름차순
lst.sort() #오름차순
print(lst)

lst.sort(reverse=True)
print(lst)

#[2]: sorted() 함수로 정렬