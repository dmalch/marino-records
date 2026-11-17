from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import PEASANT_DAUGHTER_MAIDEN, PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.255 д.411 (Сергиевская церковь с. Эммануиловка, 1894).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
marino_marriages_1894 = marriage_records(
    "ГАРО", "627", "255", "411", "Эммануиловка", "Сергиевская", 1894,
    *marriage_month(Month.FEBRUARY,
                    marriage(8, 6,
                             groom=person("Митрофан", "Андреев", "Иничков", residence="Важная"), groom_age=18, groom_marriage_num=1,
                             bride=person("Анна", "Иванова", "Мыльникова"), bride_age=20,
                             witness1=person("Николай", last_name_orig="Кудимушкин", residence="Ямбирно"),
                             witness2=person("Михаил", "Андреев", "Иничков", residence="Важная"),
                             witness3=person("Василий", "Иванов", "Мыльников"),
                             witness4=person("Иван", "Петров", "Кукушкин")),
                    marriage(12, 16, reviewed=False,
                             groom=person("Михаилъ", "Михайловъ", "Воробьевъ"), groom_age=42, groom_marriage_num=2,
                             bride=person("Акилина", "Филиппова", "Хрящева", residence="Крутая", comment="«Спасскаго уѣзда, деревни Крутой»"), bride_age=24, bride_marriage_num=1,
                             witness1=person("Тимоѳей", "Борисовъ", "Калугинъ"),
                             witness2=person("Сергій", "Яковлевъ", "Швейкинъ"),
                             witness3=person("Петръ", "Степановъ", "Моисеевъ", side=Side.BRIDE, comment="«той же деревни» — Марьиной"),
                             witness4=person("Касма", "Кириловъ", "Свищевъ", side=Side.BRIDE)),
                    ),
    *marriage_month(Month.APRIL,
                    marriage(15, 24,
                             groom=person("Григорий", "Петров", "Моисеев"), groom_age=20, groom_marriage_num=1,
                             bride=person("Дария", "Акимова", "Каржавина"), bride_age=19,
                             witness1=person("Михаил", "Михайлов", "Воробьев"),
                             witness2=person("Феодор", "Васильев", "Моисеев"),
                             witness3=person("Димитрий", "Акимов", "Каржавин"),
                             witness4=person("Василий", "Степанов", "Черкасов")),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_DAUGHTER_MAIDEN,
        status_groom=PEASANT_MALE
    ),
)
