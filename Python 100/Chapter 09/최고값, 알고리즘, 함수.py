#여러 값이 들어있는 리스트에서 최곳값을 출력하는 함수를 직접 구현하시오.
#이때, max() 함수를 사용해서는 안된다.

#[1]함수 작성 --> max()함수 사용X
#----------------------------------------------------------------------------------
def max_in_list(lst):
    
    #초기 최곳값을 0으로 설정
    first_max_number = 0
    
    #반복문을 돌면서 전달된 리스트 내 요소 중 초기 최곳값 보다 큰 값이 있으면 초기 최곳값을 바꾼다.
    for i in lst:
        if i > first_max_number:
            first_max_number = i
            
    #최종 first_max_number 값을 리턴
    return first_max_number
#----------------------------------------------------------------------------------

#[2]: 리스트
english_score = [33, 44, 55, 66, 77, 88 ,99, 11, 22, 60]

#[3]: 함수 호출 및 결과 출력하기
result = max_in_list(english_score)
print('[3-1]직접 구현한 max(): ', result)
print('[3-2]내장 max(): ', max(english_score))
