class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.items = iter(items)
        self.seen = set()

    def __next__(self):
        while True:
            item = next(self.items)

            # Для сравнения учитываем регистр, если нужно
            if isinstance(item, str) and self.ignore_case:
                key = item.lower()
            else:
                key = item

            if key not in self.seen:
                self.seen.add(key)
                return item

    def __iter__(self):
        return self


if __name__ == '__main__':
    print("Тест 1 - числа:")
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print(f"Исходные данные: {data}")
    print(f"Уникальные: {list(Unique(data))}")

    print("\nТест 2 - строки (ignore_case=False):")
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(f"Исходные данные: {data}")
    print(f"Уникальные: {list(Unique(data))}")

    print("\nТест 3 - строки (ignore_case=True):")
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(f"Исходные данные: {data}")
    print(f"Уникальные: {list(Unique(data, ignore_case=True))}")

    print("\nТест 4 - с генератором:")
    from gen_random import gen_random
    data = gen_random(10, 1, 3)
    print(f"Уникальные из gen_random(10, 1, 3): {list(Unique(data))}")
