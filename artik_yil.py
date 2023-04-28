def is_leap(y):
    """Bu fonksiyon artık yıl olup olmadığını kontrol eder."""
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(y):
    """Yıldaki gün sayısını hesaplar"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(y):
        month_days[1] = 29
    return sum(month_days)


year = int(input("Yılı giriniz: "))
days = days_in_month(year)

if is_leap(year):
    print(f"{year} yılı artık yıldır ve o yıl {days} gün sürmektedir.")

else:
    print(f"{year} yılı artık yıl değildir ve o yıl {days} gün sürmektedir.")


