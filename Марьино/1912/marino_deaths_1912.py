from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import DROPSY
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, RETIRED_SOLDIER

# Source: ГАРО ф.627 оп.279 д.47 (Сергиевская церковь с. Эммануиловка, 1912).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
marino_deaths_1912 = death_records(
    "ГАРО", "627", "279", "47", "Эммануиловка", "Сергиевская", 1912,
    *death_month(Month.JANUARY,
                 death(1, Gender.FEMALE, 21, 23, reviewed=False,
                       deceased=person("Анна"), age=14,
                       relatives=[relative(person("Василий", "Васильевъ", "Калугинъ"), Relationship.FATHER)],
                       comment="«отъ простуды»; возраст «14» ясно, хотя у Василия Васильева Калугина с Татіаной Андреевой дочь Анна родилась в ноябре того же года (ч. 1 ж.№23) — вероятно, другой Василий Васильевъ"),
                 death(2, Gender.FEMALE, 27, 29, reviewed=False,
                       deceased=person("Анна"), age=1,
                       relatives=[relative(person("Алексѣй", "Васильевъ", "Калугинъ"), Relationship.FATHER)]),
                 ),
    *death_month(Month.MARCH,
                 death(3, Gender.MALE, 12, 14,
                       deceased=person("Гавриил", "Димитриев", "Коржавин"), age=22,
                       cause_of_death=DROPSY),
                 ),
    *death_month(Month.JULY,
                 death(6, Gender.MALE, 9, 11, reviewed=False,
                       deceased=person("Андрей", "Захаровъ", "Зрюевъ", status=RETIRED_SOLDIER), age=84,
                       comment="«отъ старости»"),
                 ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
