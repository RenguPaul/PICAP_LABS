from math import sqrt
import sys
import matplotlib.pyplot as plt
import numpy as np
from typing import List


def get_coefficients():
    if len(sys.argv) > 4:
        print("Коэффициентов слишком много. Пожалуйста, перезапустите программу.")
        sys.exit(1)

    try:    
        try:
            a = float(sys.argv[1])
        except IndexError:
            a = float(input("Введите коэффициент a: "))
        try:
            b = float(sys.argv[2])
        except IndexError:
            b = float(input("Введите коэффициент b: "))
        try:
            c = float(sys.argv[3])
        except IndexError:
            c = float(input("Введите коэффициент c: "))
    except:
        print("Коэффициенты должны быть числами. Попробуйте ещё раз")
        return get_coefficients()
    return a, b, c


def calculate_answer(a: float, b: float, c: float):
    try:
        if a == 0:
            if b == 0:
                if c == 0:
                    return "Уравнение имеет бесконечно много решений.", None
                else:
                    return "Уравнение не имеет решений.", None
            else:
                t = -c / b
                if t < 0:
                    return "Действительных решений нет.", None
                elif t == 0:
                    return "Одно решение: x = 0", [0]
                else:
                    root1 = -sqrt(t)
                    root2 = sqrt(t)
                    return f"Два решения: x = {root1}, x = {root2}", [root1, root2]
        
        D = b ** 2 - 4 * a * c
        
        if D < 0:
            return "Действительных решений нет.", None
        elif D == 0:
            t = -b / (2 * a)
            if t < 0:
                return "Действительных решений нет.", None
            elif t == 0:
                return "Одно решение: x = 0", [0]
            else:
                root1 = -sqrt(t)
                root2 = sqrt(t)
                return f"Два решения: x = {root1}, x = {root2}", [root1, root2]
        else:
            t1 = (-b - sqrt(D)) / (2 * a)
            t2 = (-b + sqrt(D)) / (2 * a)
            
            roots = []
            
            if t1 >= 0:
                if t1 == 0:
                    roots.append(0)
                else:
                    roots.append(-sqrt(t1))
                    roots.append(sqrt(t1))
            
            if t2 >= 0:
                if t2 == 0:
                    if 0 not in roots:
                        roots.append(0)
                else:
                    roots.append(-sqrt(t2))
                    roots.append(sqrt(t2))
            
            if not roots:
                return "Действительных решений нет.", None
            else:
                roots = sorted(list(set(roots)))
                if len(roots) == 1:
                    return f"Одно решение: x = {roots[0]}", roots
                else:
                    roots_str = ", ".join([f"x = {r}" for r in roots])
                    return f"Решения: {roots_str}", roots
                
    except TypeError:
        print("Вы ввели некорректные коэффициенты. Перезапустите программу. Убедитесь, что вы ввели числа, а не другие типы данных")
        sys.exit()
    except ZeroDivisionError:
        print("Коэффициент a не может быть = 0. Попробуйте перезапустить программу и попробовать ещё раз")
        sys.exit()


def plot_function(a: float, b: float, c: float, roots: List):
    if roots is None:
        return
    
    if roots:
        x_min = min(roots) - 2
        x_max = max(roots) + 2
    else:
        x_min, x_max = -5, 5
        
    x = np.linspace(x_min, x_max, 400)
    
    y = a * x**4 + b * x**2 + c
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=f'y = {a}x**4 + {b}x**2 + {c}', color='blue')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    
    for root in roots:
        plt.scatter(root, 0, color='red', s=100, zorder=5, 
                   label=f'Корень: x = {root:.2f}')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График биквадратного уравнения')
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    a, b, c = get_coefficients()
    result, roots = calculate_answer(a, b, c)
    print(result)
    
    if roots is not None:
        try:
            plot_function(a, b, c, roots)
        except ImportError:
            print("Для построения графика необходимо установить matplotlib: pip install matplotlib")
        except Exception as e:
            print(f"Ошибка при построении графика: {e}")


if __name__ == "__main__":
    main()