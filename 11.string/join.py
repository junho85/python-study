# 1. 문자열 리스트 연결
# join() 함수는 문자열을 연결해줍니다.

# 문자열로 구성된 리스트 생성
mylist = ["1", "2", "3", "4", "5", "6"]

# 쉼표를 구분자로 사용하여 리스트의 모든 요소를 연결
print(",".join(mylist))  # 1,2,3,4,5,6

# 구분자 없이 리스트의 모든 요소를 연결
print("".join(mylist))  # 123456

# 2. 숫자 리스트 처리
# 숫자로 된 리스트는 문자열로 바꿔줘야 합니다.
# 정수로 구성된 리스트 생성
mylist = [1, 2, 3, 4, 5, 6]

# TypeError 발생: join()은 문자열만 처리 가능
# print(",".join(mylist))  # TypeError: sequence item 0: expected str instance, int found
# map(str, mylist)로 각 정수를 문자열로 변환한 후 join() 적용
print(",".join(map(str, mylist)))  # 1,2,3,4,5,6
