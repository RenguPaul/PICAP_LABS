data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    # Без lambda-функции
    result = sorted(data, key=abs, reverse=True)

    # С lambda-функцией
    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)

    print(f"Исходные данные: {data}")
    print(f"Без lambda: {result}")
    print(f"С lambda: {result_with_lambda}")
