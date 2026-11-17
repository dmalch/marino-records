from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.255 д.476 (Сергиевская церковь с. Эммануиловка, 1899).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
# Part 3 was photographed on the verso pages only: the recto with the causes of death
# is not in the album.
marino_deaths_1899 = death_records(
    "ГАРО", "627", "255", "476", "Эммануиловка", "Сергиевская", 1899,
    *death_month(Month.JANUARY,
                 death(1, Gender.MALE, 1, 3, reviewed=False,
                       deceased=person("Петръ"), age=2,
                       relatives=[relative(person("Севастіанъ", "Ивановъ", "Овсянкинъ"), Relationship.FATHER)]),
                 ),
    *death_month(Month.MAY,
                 death(11, Gender.MALE, 11, 13, reviewed=False,
                       deceased=person("Іоаннъ"), age="3 мес 2 нед",
                       relatives=[relative(person("Іаковъ", "Егоровъ", "Калугинъ"), Relationship.FATHER)],
                       comment="в книге «3½ мѣс»; родился 27 января 1899 г. (м.№6)"),
                 ),
    *death_month(Month.NOVEMBER,
                 death(21, Gender.MALE, 13, 15, reviewed=False,
                       deceased=person("Іаковъ"), age="3 нед",
                       relatives=[relative(person("Іаковъ", "Ѳеодотовъ", "Головачевъ"), Relationship.FATHER)],
                       comment="родился 21 октября 1899 г. (м.№34)"),
                 ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
    ),
)
