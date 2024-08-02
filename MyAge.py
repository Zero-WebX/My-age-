
from datetime import datetime

def get_user_birthday():
    day = int(input("Введите день вашего рождения: "))
    month = int(input("Введите месяц вашего рождения: "))
    year = int(input("Введите год вашего рождения: "))
    return datetime(year, month, day)

def day_of_week(birthday):
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return days[birthday.weekday()]

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_age(birthday):
    today = datetime.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return age

def print_birthday_stars(birthday):
    date_str = birthday.strftime("%d %m %Y")
    star_map = {
        '0': [" *** ", "*   *", "*   *", "*   *", " *** "],
        '1': ["  *  ", " **  ", "  *  ", "  *  ", " *** "],
        '2': ["**** ", "*   *", "   * ", "  *  ", "*****"],
        '3': [" *** ", "    *", " *** ", "    *", " *** "],
        '4': ["   * ", "  ** ", " * * ", "*****", "   * "],
        '5': ["*****", "*    ", "**** ", "    *", "**** "],
        '6': [" **** ", "*    ", "**** ", "*   *", " *** "],
        '7': ["*****", "    *", "   * ", "  *  ", " *   "],
        '8': [" *** ", "*   *", " *** ", "*   *", " *** "],
        '9': [" **** ", "*   *", " ****", "    *", " *** "]
    }
    for row in range(5):
        line = ""
        for char in date_str:
            if char == ' ':
                line += "     "
            else:
                line += star_map[char][row] + " "
        print(line)

def get_year_word(age):
    if 11 <= age % 100 <= 19:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif 2 <= age % 10 <= 4:
        return "года"
    else:
        return "лет"

# Основная программа
birthday = get_user_birthday()
age = calculate_age(birthday)
print(f"День недели вашего рождения {day_of_week(birthday)}.")
print(f"Год вашего рождения {'високосный' if is_leap_year(birthday.year) else 'не високосный'}.")
print(f"Вам сейчас {age} {get_year_word(age)}.")
print("Дата вашего рождения:")
print_birthday_stars(birthday)

