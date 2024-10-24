#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Rational:
    def __init__(self, a: int = 0, b: int = 1):
        if b == 0:
            raise ValueError()
        self.__numerator = abs(int(a))
        self.__denominator = abs(int(b))
        self.__reduce()

    # Сокращение дроби
    def __reduce(self):
        # Функция для нахождения нибольшего общего делителя
        def gcd(a: int, b: int):
            if a == 0:
                return b
            elif b == 0:
                return a
            elif a >= b:
                return gcd(a % b, b)
            else:
                return gcd(a, b % a)

        c = gcd(self.__numerator, self.__denominator)
        self.__numerator //= c
        self.__denominator //= c

    @property
    def numerator(self) -> int:
        return self.__numerator

    @property
    def denominator(self) -> int:
        return self.__denominator

    # Прочитать значение дроби с клавиатуры. Дробь вводится
    # как a/b.
    def read(self, prompt: str = None):
        line = input(prompt) if prompt else input()
        parts = list(map(int, line.split('/', maxsplit=1)))

        if parts[1] == 0:
            raise ValueError()

        self.__numerator = abs(parts[0])
        self.__denominator = abs(parts[1])
        self.__reduce()

    # Вывести дробь на экран
    def display(self) -> str:
        return f"{self.__numerator}/{self.__denominator}"

    # Сложение обыкновенных дробей.
    def add(self, rhs):
        if isinstance(rhs, Rational):
            a = self.numerator * rhs.denominator + \
                self.denominator * rhs.numerator

            b = self.denominator * rhs.denominator
            return Rational(a, b)
        else:
            raise ValueError()

    # Вычитание обыкновенных дробей.
    def sub(self, rhs):
        if isinstance(rhs, Rational):
            a = self.numerator * rhs.denominator - \
                self.denominator * rhs.numerator

            b = self.denominator * rhs.denominator
            return Rational(a, b)
        else:
            raise ValueError()

    # Умножение обыкновенных дробей.
    def mul(self, rhs):
        if isinstance(rhs, Rational):
            a = self.numerator * rhs.numerator

            b = self.denominator * rhs.denominator
            return Rational(a, b)
        else:
            raise ValueError()

    # Деление обыкновенных дробей.
    def div(self, rhs):
        if isinstance(rhs, Rational):
            a = self.numerator * rhs.denominator

            b = self.denominator * rhs.numerator
            return Rational(a, b)
        else:
            raise ValueError()

    # Отношение обыкновенных дробей.
    def equals(self, rhs):
        if isinstance(rhs, Rational):
            return (self.numerator == rhs.numerator) and \
                (self.denominator == rhs.denominator)
        else:
            return False

    def greater(self, rhs):
        if isinstance(rhs, Rational):
            v1 = self.numerator / self.denominator
            v2 = rhs.numerator / rhs.denominator
            return v1 > v2
        else:
            return False

    def less(self, rhs):
        if isinstance(rhs, Rational):
            v1 = self.numerator / self.denominator
            v2 = rhs.numerator / rhs.denominator
            return v1 < v2
        else:
            return False


if __name__ == '__main__':
    r1 = Rational(3, 4)
    print(f'R1: {r1.display()}')

    r2 = Rational()
    r2.read('Введите обыкновенную дробь: ')
    print(f'R2: {r2.display()}')

    r3 = r2.add(r1)
    print(f'R3 (R2 + R1): {r3.display()}')

    r4 = r2.sub(r1)
    print(f'R4 (R2 - R1): {r4.display()}')

    r5 = r2.mul(r1)
    print(f'R5 (R2 * R1): {r5.display()}')

    r6 = r2.div(r1)
    print(f'R6 (R2 / R1): {r6.display()}')

    r7 = r1.equals(r2)
    print(f'R7 (R1 == R2): {r7}')

    r8 = r1.greater(r2)
    print(f'R8 (R1 > R2): {r8}')

    r9 = r1.less(r2)
    print(f'R9 (R1 < R2): {r9}')
