"""
< 문제 >
    [1차][구현] 문제1) 단체 티셔츠를 주문하기 - Python3

< 문제 설명 >
    A 학교에서는 단체 티셔츠를 주문하기 위해 학생별로 원하는 티셔츠 사이즈를 조사했습니다.
    선택할 수 있는 티셔츠 사이즈는 작은 순서대로 "XS", "S", "M", "L", "XL", "XXL" 총 6종류가 있습니다.
    학생별로 원하는 티셔츠 사이즈를 조사한 결과가 들어있는 리스트 shirt_size가 매개변수로 주어질 때,
    사이즈별로 티셔츠가 몇 벌씩 필요한지 가장 작은 사이즈부터 순서대로 리스트에 담아 return 하도록 solution 함수를 완성해주세요.

< 매개변수 설명 >
    학생별로 원하는 사이즈를 조사한 결과가 들어있는 리스트 shirtsize가 solution 함수의 매개변수로 주어집니다.
    *shirtsize 의 길이는 1 이상 100 이하입니다.
    * shirt_size 에는 치수를 나타내는 문자열 "XS", "S", "M", "L", "XL","XXL" 이 들어있습니다.

< return 값 설명 >
    티셔츠가 사이즈별로 몇 벌씩 필요한지 가장 작은 사이즈부터 순서대로 리스트에 담아 return 해주세요.
    * return 하는 리스트에는 [ "XS" 개수, "S" 개수, "M" 개수, "L" 개수, "XL" 개수, "XXL" 개수] 순서로 들어있어야 합니다.
"""

def solution(shirt_size):
    answer = []
    ## 여기부터 코드 작성 ##
    size = ["XS", "S", "M", "L", "XL", "XXL"]
    for i in range(len(size)):
        answer.append(shirt_size.count(size[i]))
    ## 여기까지 코드 작성 ##
    return answer

shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size);

print("solution 함수의 반환 값은", ret, "입니다.")