"""
< 문제 >
    [2차] 문제5) 언제까지 오르막길이야..?!

< 문제 설명 >
    자연수가 들어있는 배열이 있습니다. 이 배열에서, 숫자가 연속해서 증가하는 가장 긴 구간의 길이를 구하려 합니다.
    단, 바로 전 숫자와 현재 숫자가 같은 경우는 증가한 것으로 보지 않습니다.
    예를 들어 배열에 순서대로 [3, 1, 2, 4, 5, 1, 2, 2, 3, 4]가 들어있는 경우,
    [1, 2, 4, 5]가 들어있는 구간이 숫자가 연속해서 증가한 가장 긴 구간이며, 길이는 4입니다.
    자연수가 들어있는 배열 arr와 arr의 길이 arr_len이 매개변수로 주어질 때,
    숫자가 연속해서 증가하는 가장 긴 구간의 길이를 return 하도록 solution 함수를 완성해주세요.

< 매개변수 설명 >
    자연수가 들어있는 배열 arr와 arr의 길이 arr_len이 solution 함수의 매개변수로 주어집니다.
    - arr_len은 2 이상 200,000 이하입니다.
    - arr의 원소는 1 이상 1,000,000 이하의 자연수입니다.

< return 값 설명 >
    숫자가 연속해서 증가하는 가장 긴 구간의 길이를 return 해주세요.
    길이가 2 이상인 증가하는 구간이 없다면 1을 return 해주세요.
"""

def solution(arr):
    answer = 0

    # 전달된 리스트와 동일한 크기의 리스트 생성
    temp = [0 for x in range(len(arr))]
    idx = 0

    # 리스트의 크기 -1만큼 반복 순회
    for i in range(len(arr) - 1):

        # 현재 리스트의 크기보다 다음 리스트의 요소가 더 크면
        if arr[i] < arr[i + 1]:
            temp[idx] += 1  # temp 리스트에 누적

        # 만약 작을 경우
        else:
            idx += 1        # 새롭게 누적해야하기 때문에 idx 증가

    # 비교할 때 자신까지 포함하기 때문에 +1를 해줘야 함.
    answer = max(temp) + 1

    # answer가 2보다 작은 경우는 1 반환
    if answer < 2:
        return 1

    # 연속된 큰 요소가 발견된 경우에는 최대 누적된 값인 answer 반환
    return answer

# temp = [0, 3, 1, 0, 2]
# max(temp) => 3
# answer = max(temp) + 1
arr = [3, 1, 2, 4, 5, 1, 2, 2, 3, 4]
ret = solution(arr)
print("solution 함수의 반환 값은", ret, "입니다.")