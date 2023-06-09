"""
< 문제 >
    [2차] 문제7) 거스름돈 구하기

< 문제 설명 >
    한국에는 다음과 같이 8가지 종류의 화폐가 있습니다.
    - 동전 : 10원, 50원, 100원, 500원
    - 지폐 : 1,000원, 5,000원, 10,000원, 50,000원

    손님에게 거슬러줘야 하는 금액이 주어질 때, 거슬러주는 동전과 지폐 개수의 합이 최소가 되도록 하려고 합니다.
    예를 들어 거슬러줘야 할 금액이 2,760원 이라면, 1,000원짜리 2장, 500원짜리 1개,
    100원짜리 2개, 50원짜리 1개, 10원짜리 1개를 거슬러줄 때 동전과 지폐 개수의 합이 최소가 됩니다.
    손님에게 거슬러줘야 하는 금액 money가 매개변수로 주어질 때,
    거슬러 주는 동전과 지폐 개수합의 최솟값을 return 하도록 solution 함수를 작성하려 합니다. 빈칸을 채워 전체 코드를 완성해주세요.

< 매개변수 설명 >
    손님에게 거슬러줘야 하는 금액 money가 solution 함수의 매개변수로 주어집니다.
    - money는 10 이상 100,000 이하의 자연수입니다.
    - money는 10의 배수로만 주어집니다.

< return 값 설명 >
    거슬러 주는 동전과 지폐 개수합의 최솟값을 return 해주세요.
"""
def solution(money):
	coin = [10, 50, 100, 500, 1000, 5000, 10000, 50000]
	counter = 0
	idx = len(coin) - 1

    # money가 0이 될 때까지 반복
	while money:
		counter += money // coin[idx]   # 제일 큰 화폐부터 지폐를 거스름돈으로 반환
		money %= coin[idx]              # 반환된 금액은 제외하기 위해 나머지만 money에 저장
		idx -= 1                        # idx를 줄여 다음 화폐로 계산할 수 있도록 설정
	return counter


money = 2760
ret = solution(money)
print("solution 함수의 반환 값은", ret, "입니다.")