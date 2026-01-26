# SICP Homework 003 — While Loops

Практика циклов `while` и работы с цифрами чисел.

## Задания

### 1. sum_even.py
Сумма чётных чисел от 1 до n.

```python
sum_even(10)  # 30 (2+4+6+8+10)
sum_even(7)   # 12 (2+4+6)
```

### 2. count_digits.py
Количество цифр в числе.

```python
count_digits(12345)  # 5
count_digits(100)    # 3
```

### 3. factorial.py
Факториал числа n (n!).

```python
factorial(5)   # 120 (5*4*3*2*1)
factorial(0)   # 1
```

### 4. product_digits.py (бонус)
Произведение цифр числа.

```python
product_digits(12345)  # 120 (1*2*3*4*5)
product_digits(10)     # 0
```

## Подсказки

```python
n % 10   # последняя цифра (123 % 10 = 3)
n // 10  # число без последней цифры (123 // 10 = 12)
n % 2    # остаток от деления на 2 (чётность)
```

## Как сдать

1. Форкни репозиторий
2. Реализуй функции
3. Запусти тесты локально: `pytest tests/ -v`
4. Сделай commit и push
5. Проверь вкладку Actions на GitHub
