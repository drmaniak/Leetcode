def factorial(n: int) -> int:
    if n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    while True:
        val = input("Enter an integer value to calculate the factorial of: ")
        try:
            num = int(val)
            print(f"You entered: {num}")
            out = factorial(num)
            print(f"{num}! = {out}")
        except:
            print(f"{val} is not a valid Integer")
