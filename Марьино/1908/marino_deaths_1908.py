from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, OLD_AGE
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.279 д.8 (Сергиевская церковь с. Эммануиловка, 1908).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
marino_deaths_1908 = death_records(
    "ГАРО", "627", "279", "8", "Эммануиловка", "Сергиевская", 1908,
    *death_month(Month.FEBRUARY,
                 death(1, Gender.FEMALE, 4, 5, reviewed=False,
                       deceased=person("Анна"), age="1 нед",
                       relatives=[relative(person("Яковъ", "Егоровъ", "Калугинъ"), Relationship.FATHER)],
                       cause_of_death=COLIC, comment="родилась 30 января того же года (ч. 1 ж.№4)"),
                 death(3, Gender.FEMALE, 23, 25, reviewed=False,
                       deceased=person("Меланія"), age=1,
                       relatives=[relative(person("Иванъ", "Петровъ", "Моисеевъ"), Relationship.FATHER)],
                       cause_of_death=COLIC),
                 ),
    *death_month(Month.APRIL,
                 death(6, Gender.FEMALE, 3, 5,
                       deceased=person("Дарья"), age="3 нед",
                       relatives=[relative(person("Егор", "Иванов", "Мыльников"), Relationship.FATHER)],
                       cause_of_death=COLIC),
                 ),
    *death_month(Month.NOVEMBER,
                 death(9, Gender.MALE, 17, 19, reviewed=False,
                       deceased=person("Петръ", "Ѳеодоровъ", "Телѣгинъ"), age=85,
                       cause_of_death=OLD_AGE),
                 ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
