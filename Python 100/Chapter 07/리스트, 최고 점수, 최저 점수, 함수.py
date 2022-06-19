#한 반의 학생들 10명에 대한 영어 점수표가 리스트로 있다.
#최고 점수를 출력하는 함수를 만들어 영어 점수표를 함수로 전달하면 최고 점수가 나오도록 구현해보시오.

#[1]: 함수 작성
def max_in_list(lst):
    return max(lst) #max() 함수는 전달받은 리스트내 요소 중 가장 큰 숫자를 반환

def min_in_list(lst):
    return min(lst) #in() 함수는 전달받은 리스트내 요소 중 가장 작은 숫자를 반환
#[2]: 영어 점수표
english_score = [35, 55, 87, 98, 48, 88, 77, 65, 91, 79]

#[3]: 함수 호출 및 결과 출력하기
result_max = max_in_list(english_score)
print(result_max)

result_min= min_in_list(english_score)
print(result_min)
