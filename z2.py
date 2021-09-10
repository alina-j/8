#!/usr/bin/env python3
# -*- coding: utf-8 -*-from datetime import date
# в основной ветке программы вызывается функция cylinder(),
# которая вычисляет площадь цилиндра. В теле cylinder() определена функция circle(),
# вычисляющая площадь круга по формуле . В теле cylinder() у пользователя
# спрашивается, хочет ли он получить только площадь боковой поверхности цилиндра,
# которая вычисляется по формуле , или полную площадь цилиндра. В последнем
# случае к площади боковой поверхности цилиндра должен добавляться удвоенный результат
# вычислений функции circle().

import math

if __name__ == '__main__':
    def circle(r):
        sr = 2 * 3.14 * r
        return sr
    def cylinder():
        print('Если хотите получить только площадь боковой поверхности введите 1')
        print('Если хотите получить полную площадь цилиндра введите 2')
        q = input('Введите команду -->')
        r = int(input('Введите радиус -->'))
        h = int(input('Введите высоту -->'))
        s = 2 * 3.14 * r * h
        if q == '1':
            print(s)

        elif q == '2':
            circle(r)
            s = sr * 2 + s
            print(s)
    cylinder()