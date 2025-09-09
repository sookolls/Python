def leap_year(year):
    assert isinstance (year, int)
    if (year//100)!=0 and year // 4 or year//400:
        return "Год високосный"
    elif print ("not leap_year"):
        return "Год невисокосный"
try:
    year = int(input("Введите число: "))
    print(leap_year(year))
except ValueError:
    print("Некорректный тип")