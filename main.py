import file_operations
from faker import Faker
from random import randint, sample


fake = Faker("ru_RU")
skills = [
                "Стремительный прыжок",
                "Электрический выстрел",
                "Ледяной удар",
                "Стремительный удар",
                "Кислотный взгляд",
                "Тайный побег",
                "Ледяной выстрел",
                "Огненный заряд"
        ]
runic_alphabet = {
        "а": "а͠", "б": "б̋", "в": "в͒͠",
        "г": "г͒͠", "д": "д̋", "е": "е͠",
        "ё": "ё͒͠", "ж": "ж͒", "з": "з̋̋͠",
        "и": "и", "й": "й͒͠", "к": "к̋̋",
        "л": "л̋͠", "м": "м͒͠", "н": "н͒",
        "о": "о̋", "п": "п̋͠", "р": "р̋͠",
        "с": "с͒", "т": "т͒", "у": "у͒͠",
        "ф": "ф̋̋͠", "х": "х͒͠", "ц": "ц̋",
        "ч": "ч̋͠", "ш": "ш͒͠", "щ": "щ̋",
        "ъ": "ъ̋͠", "ы": "ы̋͠", "ь": "ь̋",
        "э": "э͒͠͠", "ю": "ю̋͠", "я": "я̋",
        "А": "А͠", "Б": "Б̋", "В": "В͒͠",
        "Г": "Г͒͠", "Д": "Д̋", "Е": "Е",
        "Ё": "Ё͒͠", "Ж": "Ж͒", "З": "З̋̋͠",
        "И": "И", "Й": "Й͒͠", "К": "К̋̋",
        "Л": "Л̋͠", "М": "М͒͠", "Н": "Н͒",
        "О": "О̋", "П": "П̋͠", "Р": "Р̋͠",
        "С": "С͒", "Т": "Т͒", "У": "У͒͠",
        "Ф": "Ф̋̋͠", "Х": "Х͒͠", "Ц": "Ц̋",
        "Ч": "Ч̋͠", "Ш": "Ш͒͠", "Щ": "Щ̋",
        "Ъ": "Ъ̋͠", "Ы": "Ы̋͠", "Ь": "Ь̋",
        "Э": "Э͒͠͠", "Ю": "Ю̋͠", "Я": "Я̋",
        " ": " "
    }
stats = ["strength", "agility", "endurance", "intelligence", "luck"]


def roll_stat():
    stat_value = randint(1, 6) + randint(1, 6) + randint(1, 6)
    return stat_value


def runify(text: str):
    for letter in text:
        text = text.replace(letter, runic_alphabet[letter])
    return text


def main():
    for i in range(10):

        active_skills = sample(skills, 3)

        context = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "job": fake.job(),
            "town": fake.city(),
            "skill_1": runify(active_skills[0]),
            "skill_2": runify(active_skills[1]),
            "skill_3": runify(active_skills[2])
        }

        for stat in stats:
            context[stat] = roll_stat()

        file_name = f"result_{i+1}"
        file_operations.render_template(
            "charsheet.svg",
            f"Character_results\\{file_name}.svg",
            context
        )


if __name__ == "__main__":
    main()
