# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
# числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.


class ComplexNumber:
    def __init__(self, re, im=0.0):
        ComplexNumber.check_user_input(re)
        ComplexNumber.check_user_input(im)
        self.re = float(re)
        self.im = float(im)

    @staticmethod
    def check_user_input(value):
        if not isinstance(value, (float, int)):
            raise ValueError('Invalid value used!')

    @classmethod
    def create_complex_number(cls, re, im=0.0):
        try:
            return cls(float(re), float(im))
        except ValueError as e:
            print(f'Invalid value used: {e}')

    def __str__(self):
        if self.im == 0:
            return f'{self.re}'
        return f'{self.re:.2f} {"+" if self.im > 0 else "-"} {abs(self.im):.2f}i'

    def __add__(self, other):
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return ComplexNumber(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        new_re = self.re * other.re - self.im * other.im
        new_im = self.im * other.re + self.re * other.im
        return ComplexNumber(new_re, new_im)


num1 = ComplexNumber.create_complex_number(2, 5)
num2 = ComplexNumber(3.0, -5)
print(num2)

print(num1 + num2)
print(num1 * num2)

print(ComplexNumber.create_complex_number(2))
