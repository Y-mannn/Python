#오름차순, 내림차순 정렬을 sort(), sorted() 함수로 구현하시오.
#sort(), sorted() 함수의 차이점을 아는지 묻는 문제이다.

#[1]: 리스트
lst = [100, 50, 40, 70, 90, 60, 80]

#[2]: sort() 함수를 이용한 오름차순, 내림차순 정렬
#sort()함수나 sorted()함수나 아무런 옵션이 없이 사용하면 디폴트 정렬 --> 오름차순
lst.sort() #오름차순 sort() = sort(reverse=False)
print('[원본-1]: ', lst)

lst.sort(reverse=True) #내림차순 --> 먼저 오름차순으로 정렬이 되고나서 내림차순으로 정렬 --> 원본을 오름차순으로 정렬하고 역순으로 정렬
print('[원본-2]: ', lst)

#[3]: sorted()
#reverse 옵션을 안쓰면 디폴트가 False가 되므로 기본 정렬 --> 오름차순 --> reverse=False
acs_lst = sorted(lst) #원본 배열인 lst 리스트는 그대로 유지
print('[변경]: ', acs_lst)
print('[원본-2]: ', lst)