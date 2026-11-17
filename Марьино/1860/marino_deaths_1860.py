from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLD, HERNIA, SUFFOCATION
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.255 д.165 (Сергиевская церковь с. Эммануиловка, 1860).
# Read in full for Марьино on 2026-09-27; records added by that sweep are reviewed=False.
marino_deaths_1860 = death_records(
    "ГАРО", "627", "255", "165", "Эммануиловка", "Сергиевская", 1860,
    *death_month(Month.MAY,
                 death(5, Gender.FEMALE, 16, 18,
                       deceased=person("Матрена", "Иванова", "Ласевичева"), age=66,
                       cause_of_death="отъ грудной боли"),
                 ),
    *death_month(Month.JULY,
                 death(5, Gender.MALE, 22, 24,
                       deceased=person("Григорій"), age="9 мес",
                       relatives=[relative(person("Павелъ", None, "Калугинъ", comment="отчество не записано"), Relationship.FATHER)],
                       cause_of_death=HERNIA),
                 ),
    *death_month(Month.AUGUST,
                 death(8, Gender.MALE, 8, 10,
                       deceased=person("Григорій"), age="6 мес",
                       relatives=[relative(person("Павелъ", None, "Калугинъ", comment="отчество не записано"), Relationship.FATHER)],
                       cause_of_death=COLD, comment="второй за две недели «Павла Калугина сынъ Григорій» (ср. м.№5 22.07.1860)"),
                 ),
    *death_month(Month.DECEMBER,
                 death(16, Gender.FEMALE, 1, 3,
                       deceased=person("Феврония", "Дмитриева"), age=61,
                       relatives=[relative(person("Арефий", last_name_orig="Мыльников"), Relationship.HUSBAND)],
                       cause_of_death=SUFFOCATION),
                 ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
