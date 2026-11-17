from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import DECREPITUDE, DROPSY, PLEURISY, SUFFOCATION
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, PEASANT_WIDOW

# Source: ГАРО ф.627 оп.255 д.219 (Сергиевская церковь с. Эммануиловка, 1875).
# Read in full for Марьино on 2026-09-27; proofread in Verso on 2026-10-14.
# The album is phone photos of a screen with heavy moiré; uncertain readings say so.
marino_deaths_1875 = death_records(
    "ГАРО", "627", "255", "219", "Эммануиловка", "Сергиевская", 1875,
    *death_month(Month.JANUARY,
                 death(1, Gender.MALE, 1, 3,
                       deceased=person("Иванъ", comment="«пріемный сынъ»"), age=6,
                       relatives=[relative(person("Григорій", "Тимоѳеевъ", "Воробьевъ", comment="прочтение неуверенно"), Relationship.FATHER)],
                       comment="причина не разобрана"),
                 death(4, Gender.FEMALE, 2, 4,
                       deceased=person("Дарья", "Никитина?"), age=73,
                       relatives=[relative(person("Пантелеймон", "Никифоров", "Коржавенков"), Relationship.HUSBAND)],
                       cause_of_death=DECREPITUDE),
                 ),
    *death_month(Month.FEBRUARY,
                 death(4, Gender.MALE, 23, 26,
                       deceased=person("Иванъ"), age=4,
                       relatives=[relative(person("Никифоръ", "", "Мазаевъ", comment="отчество не записано"), Relationship.FATHER)],
                       cause_of_death=PLEURISY),
                 ),
    *death_month(Month.MARCH,
                 death(6, Gender.MALE, 14, 16,
                       deceased=person("Егоръ", "Ѳеодоровъ", "Калугинъ"), age=73,
                       cause_of_death=SUFFOCATION),
                 ),
    *death_month(Month.JULY,
                 death(13, Gender.FEMALE, 16, 18,
                       deceased=person("Марія", "Иванова", "Мазаева", status=PEASANT_WIDOW), age=55,
                       cause_of_death=DROPSY),
                 ),
    *death_month(Month.DECEMBER,
                 death(17, Gender.FEMALE, 2, 4,
                       deceased=person("Анна", "Иванова", "Свищева", status=PEASANT_WIDOW), age=74,
                       cause_of_death=DECREPITUDE),
                 ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
