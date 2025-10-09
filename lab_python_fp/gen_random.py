import random

def gen_random(num_count, begin, end):
    for _ in range(num_count):
        yield random.randint(begin, end)


if __name__ == '__main__':
    print("Тест gen_random:")
    numbers = list(gen_random(5, 1, 3))
    print(f"gen_random(5, 1, 3) = {numbers}")

    print("\nТест с большим диапазоном:")
    numbers = list(gen_random(10, 10, 20))
    print(f"gen_random(10, 10, 20) = {numbers}")
