def divide(dividend: int, divisor: int) -> int:
    sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0
    while (dividend >= divisor):
        dividend -= divisor
        quotient += 1

    if sign == -1:
        quotient = -quotient

    return quotient


if __name__ == "__main__":
    first_number: int = int(input('Enter your first number : '))
    second_number: int = int(input('Enter your second number : '))
    print(f"result : {divide(dividend=first_number, divisor=second_number)}")
