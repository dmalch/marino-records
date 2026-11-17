from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import DIARRHEA, SUFFOCATION
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.255 д.436 (Сергиевская церковь с. Эммануиловка, 1896).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
# The age column runs into the gutter: the figure is visible, its unit often is not.
marino_deaths_1896 = death_records(
    "ГАРО", "627", "255", "436", "Эммануиловка", "Сергиевская", 1896,
    *death_month(Month.JANUARY,
                 death(1, Gender.MALE, 2, 3, reviewed=False,
                       deceased=person("Андрей", "Тимоѳеевъ", "Воробьевъ"), age=77,
                       cause_of_death=SUFFOCATION,
                       comment="«Коренные жители крестьяне. Деревни Марьиной Андрей Тимоѳеевъ Воробьевъ»"),
                 ),
    *death_month(Month.FEBRUARY,
                 death(3, Gender.FEMALE, 21, 22, reviewed=False,
                       deceased=person("Пелагія"), age=None,
                       relatives=[relative(person("Егоръ", "Ѳеодоровъ", "Зрюевъ"), Relationship.FATHER)],
                       cause_of_death=DIARRHEA,
                       comment="в графе лет видна «4», единица в корешке"),
                 death(4, Gender.FEMALE, 28, 29, reviewed=False,
                       deceased=person("Анна"), age="3 нед",
                       relatives=[relative(person("Иванъ", "Михайловъ", "Свищевъ"), Relationship.FATHER)],
                       comment="в графе лет видна «3», единица в корешке; родилась 8 февраля 1896 г. (ж.№2), так что — недели"),
                 ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
    ),
)
