from datetime import date

def calculateAge(age):
    today = date.today()
    birth_year = today.year - age
    try:
        birthday = date(today.year, today.month, today.day)
        if birthday > today:
            birth_year -= 1
    except ValueError:
        birth_year -= 1

    return birth_year

# Driver code
age_input = int(input("Enter your age: "))
birth_year = calculateAge(age_input)
print("Birth Year:", birth_year)
