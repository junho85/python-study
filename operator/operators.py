import math

# 거듭제곱 연산자 (**)
print(2**3)  # 8 - 2의 3제곱 = 2 × 2 × 2 = 8

# math.ceil() - 올림 함수 (천장 함수)
print(math.ceil(5.1))  # 6 - 5.1 이상의 가장 작은 정수

# math.floor() - 내림 함수 (바닥 함수)
print(math.floor(5.1))  # 5 - 5.1 이하의 가장 큰 정수

# round() - 반올림 함수 (기본적으로 소수점 첫째 자리에서 반올림)
print(round(5.1))  # 5 - 5.1을 가장 가까운 정수로 반올림
print(round(5.5))  # 6 - 5.5를 가장 가까운 정수로 반올림
print(type(round(5.5)))  # <class 'int'> - 정수를 반환

# round() 함수의 두 번째 매개변수로 소수점 자릿수 지정
print(round(5.555, 2))  # 5.55 - 소수점 둘째 자리까지 반올림
print(type(round(5.555, 2)))  # <class 'float'> - 부동소수점수를 반환

# 반올림의 세부 동작 예시
print(round(5.123, 2))  # 5.12 - 셋째 자리 3은 5 미만이므로 내림
print(round(5.125, 2))  # 5.12 - 셋째 자리 5일 때의 특별한 경우
print(round(5.126, 2))  # 5.13 - 셋째 자리 6은 5 초과이므로 올림


# Python의 round() 함수는 "Banker's Rounding" (은행원 반올림) 방식을 사용
# 이는 "사사오입"이 아닌 "오사오입" 방식입니다
# 0.5일 때 가장 가까운 짝수로 반올림하는 방식입니다
print(round(0.5))   # 0 - 0과 1 중 짝수인 0을 선택
print(round(1.5))   # 2 - 1과 2 중 짝수인 2를 선택
print(round(2.5))   # 2 - 2와 3 중 짝수인 2를 선택
print(round(3.5))   # 4 - 3과 4 중 짝수인 4를 선택
print(round(4.5))   # 4 - 4와 5 중 짝수인 4를 선택
print(round(5.5))   # 6 - 5와 6 중 짝수인 6을 선택
print(round(6.5))   # 6 - 6과 7 중 짝수인 6을 선택
print(round(7.5))   # 8 - 7과 8 중 짝수인 8을 선택
print(round(8.5))   # 8 - 8과 9 중 짝수인 8을 선택
print(round(9.5))   # 10 - 9와 10 중 짝수인 10을 선택
print(round(10.5))  # 10 - 10과 11 중 짝수인 10을 선택
