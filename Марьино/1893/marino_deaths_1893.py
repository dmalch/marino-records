from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, PEASANT_WIDOW

# Source: ГАРО ф.627 оп.255 д.396 (Сергиевская церковь с. Эммануиловка, 1893).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
marino_deaths_1893 = death_records(
    "ГАРО", "627", "255", "396", "Эммануиловка", "Сергиевская", 1893,
    *death_month(Month.FEBRUARY,
                 death(5, Gender.MALE, 6, 7,
                       deceased=person("Иван"), age="3 мес",
                       relatives=[relative(person("Василий", "Иванов", "Мыльников"), Relationship.FATHER)],
                       cause_of_death=COLIC),
                 death(18, Gender.MALE, 23, 27,
                       deceased=person("Василий", "Егоров", "Мыльников"), age=13,
                       cause_of_death="скоропостижною болезнью"),
                 ),
    *death_month(Month.MARCH,
                 death(8, Gender.FEMALE, 26, 27, reviewed=False,
                       deceased=person("Анна", "Егорова", "Калугина", status=PEASANT_WIDOW), age=69),
                 ),
    *death_month(Month.DECEMBER,
                 death(16, Gender.FEMALE, 3, 4, reviewed=False,
                       deceased=person("Марія", "Яковлева"), age=43,
                       relatives=[relative(person("Михаилъ", "Михайловъ", "Воробьевъ"), Relationship.HUSBAND)],
                       comment="вдовец венчан вторым браком 16.02.1894 (1894, ч. 2 №12)"),
                 death(19, Gender.FEMALE, 24, 26, reviewed=False,
                       deceased=person("Анастасія"), age="1 мес",
                       relatives=[relative(person("Иванъ", "Егоровъ", "Телѣгинъ", comment="в книге «Телегинъ»"), Relationship.FATHER)],
                       cause_of_death=COLIC, comment="родилась 22 октября 1893 г. (ж.№25)"),
                 ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
