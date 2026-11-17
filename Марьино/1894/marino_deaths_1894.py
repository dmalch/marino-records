from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import HEADACHE, TYPHUS
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, SOLDIER

# Source: ГАРО ф.627 оп.255 д.411 (Сергиевская церковь с. Эммануиловка, 1894).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
marino_deaths_1894 = death_records(
    "ГАРО", "627", "255", "411", "Эммануиловка", "Сергиевская", 1894,
    *death_month(Month.FEBRUARY,
                 death(2, Gender.MALE, 5, 8, reviewed=False,
                       deceased=person("Антонъ", "Григорьевъ", "Головачевъ", status=SOLDIER), age=55,
                       comment="в графе причины — отметка о погребении по разрешению станового пристава"),
                 death(1, Gender.FEMALE, 26, 27, reviewed=False,
                       deceased=person("Александра"), age=12,
                       relatives=[relative(person("Петръ", "Степановъ", "Моисеевъ"), Relationship.FATHER)],
                       cause_of_death=HEADACHE, comment="цифра возраста у корешка, читается «12»"),
                 ),
    *death_month(Month.MARCH,
                 death(3, Gender.MALE, 20, 21, reviewed=False,
                       deceased=person("Василій"), age=18,
                       relatives=[relative(person("Петръ", "Степановъ", "Моисеевъ"), Relationship.FATHER)],
                       cause_of_death=HEADACHE),
                 ),
    *death_month(Month.OCTOBER,
                 death(21, Gender.MALE, 30, 31,
                       deceased=person("Леонтий"), age=10,
                       relatives=[relative(person("Димитрий", "Акимов", "Каржавин"), Relationship.FATHER)],
                       cause_of_death=TYPHUS),
                 ),
    *death_month(Month.DECEMBER,
                 death(23, Gender.MALE, 28, 29, reviewed=False,
                       deceased=person("Иванъ"), age="6 нед",
                       relatives=[relative(person("Иванъ", "Егоровъ", "Телѣгинъ", comment="в книге «Тельгинъ»"), Relationship.FATHER)],
                       comment="родился 9 ноября 1894 г. (м.№27)"),
                 ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
