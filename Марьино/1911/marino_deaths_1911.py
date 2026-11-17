from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import FEVER
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.279 д.37 (Сергиевская церковь с. Эммануиловка, 1911).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
marino_deaths_1911 = death_records(
    "ГАРО", "627", "279", "37", "Эммануиловка", "Сергиевская", 1911,
    *death_month(Month.JANUARY,
                 death(1, Gender.FEMALE, 6, 8,
                       deceased=person("Анна", "Егорова"), age=None,  # возраст в записи неразборчив
                       relatives=[relative(person("Алексей", "Акимов", "Коржавин"), Relationship.HUSBAND)],
                       cause_of_death=FEVER,
                       comment="возраст в источнике неразборчив: «3?»"),
                 ),
    *death_month(Month.FEBRUARY,
                 death(3, Gender.FEMALE, 13, 15, reviewed=False,
                       deceased=person("Марія"), age=None,
                       relatives=[relative(person("Леонтій", "Тимоѳеевъ", "Кузюковъ"), Relationship.FATHER)],
                       comment="графа возраста ушла в корешок"),
                 ),
    *death_month(Month.MARCH,
                 death(1, Gender.MALE, 11, 13, reviewed=False,
                       deceased=person("Иванъ", "Никитинъ", "Мазаевъ"), age=35,
                       comment="«отъ горячки»; в других годах марьинский Иванъ Никитинъ Толмачевъ, здесь ясно «Мазаевъ»"),
                 ),
    *death_month(Month.APRIL,
                 death(6, Gender.FEMALE, 6, 8, reviewed=False,
                       deceased=person("Стефанида", "Николаева"), age=None,
                       relatives=[relative(person("Егоръ", "Ивановъ", "Калугинъ"), Relationship.HUSBAND)],
                       comment="«отъ паралича»; графа возраста ушла в корешок"),
                 ),
    *death_month(Month.JULY,
                 death(5, Gender.MALE, 7, 9, reviewed=False,
                       deceased=person("Стефанъ"), age="полгода",
                       relatives=[relative(person("Григорій", "Петровъ", "Моисеевъ"), Relationship.FATHER)],
                       comment="в книге «½»; родился 1 января того же года (ч. 1 м.№1)"),
                 ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
