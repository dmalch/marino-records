from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, OLD_AGE
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.255 д.563 (Сергиевская церковь с. Эммануиловка, 1906).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
marino_deaths_1906 = death_records(
    "ГАРО", "627", "255", "563", "Эммануиловка", "Сергиевская", 1906,
    *death_month(Month.JULY,
                 death(7, Gender.MALE, 1, 3, reviewed=False,
                       deceased=person("Георгій"), age="3 мес",
                       relatives=[relative(person("Егоръ", "Косьминъ", "Свищовъ"), Relationship.FATHER)],
                       cause_of_death=COLIC, comment="крещён 1 апреля того же года (ч. 1 м.№6)"),
                 ),
    *death_month(Month.SEPTEMBER,
                 death(11, Gender.MALE, 5, 7, reviewed=False,
                       deceased=person("Михаилъ", "Ѳеодоровъ", "Головачевъ"), age=88,
                       cause_of_death=OLD_AGE),
                 ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
