def print_multiplication_table(number):
    for i in range(1, 10):
        result = number * i
        print(f"{number} x {i} = {result}")


if __name__ == "__main__":
    try:
        input_number = int(input("구구단을 출력할 숫자를 입력하세요: "))
        print_multiplication_table(input_number)
    except ValueError:
        print("유효한 숫자를 입력해주세요.")
