def isperfectsquare(num):
    if num < 2:
        return True

    x = num // 2
    while x * x > num:
        x = (x + num // x) // 2
    return x * x == num


if __name__ == "__main__":
    print(isperfectsquare(16))
    print(isperfectsquare(14))
    print(isperfectsquare(2000105819))
