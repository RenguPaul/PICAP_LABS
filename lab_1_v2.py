from math import sqrt
import sys
import matplotlib.pyplot as plt
import numpy as np

class Equation:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c
        self.roots = None
        self.numeric_roots = None
    
    def set_coefficients(self):
        if len(sys.argv) > 4:
            print("Коэффициентов слишком много. Пожалуйста, перезапустите программу.")
            sys.exit(1)

        try:    
            try:
                self.a = float(sys.argv[1])
            except IndexError:
                self.a = float(input("Введите коэффициент a: "))
            try:
                self.b = float(sys.argv[2])
            except IndexError:
                self.b = float(input("Введите коэффициент b: "))
            try:
                self.c = float(sys.argv[3])
            except IndexError:
                self.c = float(input("Введите коэффициент c: "))
        except:
            print("Коэффициенты должны быть числами. Попробуйте ещё раз")
            self.set_coefficients()
        return self.a, self.b, self.c
    
    def calculate_equation(self):
        try:
            if self.a == 0:
                if self.b == 0:
                    if self.c == 0:
                        self.roots = "Уравнение имеет бесконечно много решений."
                        self.numeric_roots = None
                    else:
                        self.roots = "Уравнение не имеет решений."
                        self.numeric_roots = None
                else:
                    t = -self.c / self.b
                    if t < 0:
                        self.roots = "Действительных решений нет."
                        self.numeric_roots = None
                    elif t == 0:
                        self.roots = f"Одно решение: x = 0"
                        self.numeric_roots = [0]
                    else:
                        root1 = -sqrt(t)
                        root2 = sqrt(t)
                        self.roots = f"Два решения: x = {root1}, x = {root2}"
                        self.numeric_roots = [root1, root2]
                return
            D = self.b ** 2 - 4 * self.a * self.c
            if D < 0:
                self.roots = "Действительных решений нет."
                self.numeric_roots = None
            elif D == 0:
                t = -self.b / (2 * self.a)
                if t < 0:
                    self.roots = "Действительных решений нет."
                    self.numeric_roots = None
                elif t == 0:
                    self.roots = f"Одно решение: x = 0"
                    self.numeric_roots = [0]
                else:
                    root1 = -sqrt(t)
                    root2 = sqrt(t)
                    self.roots = f"Два решения: x = {root1}, x = {root2}"
                    self.numeric_roots = [root1, root2]
            else:
                t1 = (-self.b - sqrt(D)) / (2 * self.a)
                t2 = (-self.b + sqrt(D)) / (2 * self.a)
                
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
                    self.roots = "Действительных решений нет."
                    self.numeric_roots = None
                else:
                    roots = sorted(list(set(roots)))
                    if len(roots) == 1:
                        self.roots = f"Одно решение: x = {roots[0]}"
                    else:
                        roots_str = ", ".join([f"x = {r}" for r in roots])
                        self.roots = f"Решения: {roots_str}"
                    self.numeric_roots = roots
                
        except TypeError:
            print("Вы ввели некорректные коэффициенты. Перезапустите программу. Убедитесь, что вы ввели числа, а не другие типы данных")
            sys.exit()
    
    def plot_function(self):
        if self.numeric_roots is None:
            return
        
        if self.numeric_roots:
            x_min = min(self.numeric_roots) - 2
            x_max = max(self.numeric_roots) + 2
        else:
            x_min, x_max = -5, 5
            
        x = np.linspace(x_min, x_max, 400)
        
        y = self.a * x**4 + self.b * x**2 + self.c
        
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, label=f'y = {self.a}x**4 + {self.b}x**2 + {self.c}', color='blue')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        
        for root in self.numeric_roots:
            plt.scatter(root, 0, color='red', s=100, zorder=5, 
                       label=f'Корень: x = {root:.2f}')
        
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('График биквадратного уравнения')
        plt.legend()
        plt.grid(True)
        plt.show()
    
    def show_answer(self):
        print(self.roots)
        if self.numeric_roots is not None:
            try:
                self.plot_function()
            except ImportError:
                print("Для построения графика необходимо установить matplotlib: pip install matplotlib")
            except Exception as e:
                print(f"Ошибка при построении графика: {e}")


def main():
    e = Equation()
    e.set_coefficients()
    e.calculate_equation()
    e.show_answer()


if __name__ == "__main__":
    main()