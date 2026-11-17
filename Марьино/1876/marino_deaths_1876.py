from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import CONSUMPTION, DECREPITUDE, OLD_AGE
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, PEASANT_WIDOW

# Source: ГАРО ф.627 оп.255 д.227 (Сергиевская церковь с. Эммануиловка, 1876).
# Read in full for Марьино on 2026-09-27; proofread in Verso on 2026-10-17.
# The scans are phone photos of a screen (moiré).
marino_deaths_1876 = death_records(
    "ГАРО", "627", "255", "227", "Эммануиловка", "Сергиевская", 1876,
    *death_month(Month.FEBRUARY,
                 death(3, Gender.FEMALE, 6, 8,
                       deceased=person("Екатерина", "Иванова", "Головачева", status=PEASANT_WIDOW), age=84,
                       cause_of_death=OLD_AGE),
                 ),
    *death_month(Month.MARCH,
                 death(4, Gender.MALE, 28, 30,
                       deceased=person("Григорій"), age=18,
                       relatives=[relative(person("Стефанъ", "Ивановъ", "Епишкинъ"), Relationship.FATHER)],
                       cause_of_death=CONSUMPTION),
                 ),
    *death_month(Month.MAY,
                 death(4, Gender.FEMALE, 5, 7,
                       deceased=person("Ксенія", "Феофанова"), age=46,
                       relatives=[relative(person("Егоръ", "Феодоровъ", "Телегинъ"), Relationship.HUSBAND)],
                       cause_of_death=CONSUMPTION),
                 ),
    *death_month(Month.JUNE,
                 death(7, Gender.MALE, 29, 30,
                       deceased=person("Аникѣй", "Васильевъ", "Воробьевъ"), age=75,
                       cause_of_death=DECREPITUDE),
                 ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
