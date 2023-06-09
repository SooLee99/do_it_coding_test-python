"""
< 문제설명 >
    주어진 배열의 순서를 뒤집으려고 합니다.
    예를 들어 주어진 배열이 [1, 4, 2, 3]이면, 순서를 뒤집은 배열은 [3, 2, 4, 1]입니다.
    정수가 들어있는 배열 arr와 arr의 길이 arr_len이 매개변수로 주어졌을 때, arr를 뒤집어서 return 하도록 solution 함수를 작성하려 합니다. 빈칸을 채워 전체 코드를 완성해주세요.

< 매개변수 설명 >
    정수가 들어있는 배열 arr와 arr의 길이 arrlen이 solution 함수의 매개변수로 주어집니다.
    * arrlen은 1 이상 100 이하의 자연수입니다. * arr의 원소는 -100 이상 100 이하의 정수입니다.

< return 값 설명 >
    배열 arr의 순서를 뒤집어서 return 해주세요.
"""

def solution(arr):
    left, right = 0, len(arr)-1

    # while 문의 조건은?
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

arr = [1, 4, 2, 3]
ret = solution(arr)

print("solution 함수의 반환 값은", ret, "입니다.")