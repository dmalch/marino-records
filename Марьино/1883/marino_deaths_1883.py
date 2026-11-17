from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLD, COLIC
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.255 д.292 (Сергиевская церковь с. Эммануиловка, 1883).
# Read in full for Марьино on 2026-09-27; records added by that sweep are reviewed=False.
# Part 3 was photographed on the verso pages only.
marino_deaths_1883 = death_records(
    "ГАРО", "627", "255", "292", "Эммануиловка", "Сергиевская", 1883,
    *death_month(Month.JANUARY,
                 death(5, Gender.MALE, 30, 31, reviewed=False,
                       deceased=person("Игнатій"), age="6 нед",
                       relatives=[relative(person("Савостіанъ", "Ивановъ", "Овсянкинъ", comment="«Совостіана»"), Relationship.FATHER)],
                       cause_of_death=COLIC),
                 ),
    *death_month(Month.AUGUST,
                 death(13, Gender.FEMALE, 2, 3, reviewed=False,
                       deceased=person("Анисія"), age="8 мес",
                       relatives=[relative(person("Иванъ", "Михайловъ", "Свищевъ"), Relationship.FATHER)],
                       cause_of_death=COLIC, comment="в графе «8 м…» у корешка; над страницей месяца нет — продолжение августа; родилась 1 января 1883 г. (ж.№3)"),
                 ),
    *death_month(Month.DECEMBER,
                 death(18, Gender.MALE, 2, 3, reviewed=False,
                       deceased=person("Яковъ", "Яковлевъ", "Калугинъ"), age=61,
                       cause_of_death=COLD),
                 ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
