def leap_year(year: int) -> str:
    assert isinstance (year, int)
    if (year%4==0 and (year%100)!=0) or year%400==0:
        return "Год високосный"
    else: return"Год невисокосный"
try:
    print(leap_year(year))
except ValueError:
    print("Некорректный тип")
except Exception as e:
    print(f"Неверное значение: {e}")