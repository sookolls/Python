def marks (mark):
    assert isinstance (mark, int) , "Оценка должна быть целым числом"
    assert 0 <= mark <= 100, "Оценка должна быть между 0 и 100"
    if mark <0 or mark > 100:
        return 'incorrect value'
    elif mark >=90:
        return 'A'
    elif 80<= mark <= 89:
        return 'B'
    elif  70<= mark <= 79:
        return 'C'
    elif 60<= mark <= 69:
        return 'D'
    elif mark <= 59:
        return 'E'
try:
    mark = int(input("Введите число: "))
    print(marks(mark))
except ValueError:
    print("Некорректный тип")
except AssertionError as e:
    print(f"Неверное значение: {e}")

