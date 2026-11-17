from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.statuses import MAIDEN, PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.279 д.56 (Сергиевская церковь с. Эммануиловка, 1913).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
# Ages stand in a narrow column at the gutter of the verso; a bare number is years.
marino_deaths_1913 = death_records(
    "ГАРО", "627", "279", "56", "Эммануиловка", "Сергиевская", 1913,
    *death_month(Month.JANUARY,
                 death(1, Gender.MALE, 1, 3, reviewed=False,
                       deceased=person("Терентій"), age=4,
                       relatives=[relative(person("Марія", "Севастіанова", "Овсянкина", status=MAIDEN), Relationship.MOTHER)]),
                 ),
    *death_month(Month.FEBRUARY,
                 death(3, Gender.MALE, 3, 5, reviewed=False,
                       deceased=person("Иванъ", "Михайловъ", "Свищовъ"), age=59,
                       comment="не жених Иванъ Михайловъ Свищовъ 18 лет, венчанный 13 февраля того же года"),
                 ),
    *death_month(Month.APRIL,
                 death(6, Gender.MALE, 25, 27, reviewed=False,
                       deceased=person("Никита"), age="1 мес",
                       relatives=[relative(person("Иванъ", "Ивановъ", "Телѣгинъ"), Relationship.FATHER)],
                       comment="крещён 31 марта того же года (ч. 1 м.№8)"),
                 ),
    *death_month(Month.MAY,
                 death(5, Gender.FEMALE, 14, 16, reviewed=False,
                       deceased=person("Евдокія", "Никандрова", "Головачева"), age=None,
                       comment="графа возраста пробита дырой от переплёта; «отъ старости»"),
                 ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
