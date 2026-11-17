from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, CONSUMPTION, DROPSY, HEADACHE
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, PEASANT_WIFE, SOLDIER_WIFE

# Source: ГАРО ф.627 оп.255 д.169 (Сергиевская церковь с. Эммануиловка, 1862).
# Read in full for Марьино on 2026-09-27; records added by that sweep are reviewed=False.
marino_deaths_1862 = death_records(
    "ГАРО", "627", "255", "169", "Эммануиловка", "Сергиевская", 1862,
    *death_month(Month.FEBRUARY,
                 death(2, Gender.FEMALE, 3, 5,
                       deceased=person("Ксенія", "Ѳеодорова", status=PEASANT_WIFE), age=62,
                       relatives=[relative(person("Григорій", "Ивановъ", "Петелинъ"), Relationship.HUSBAND)],
                       cause_of_death=CONSUMPTION),
                 ),
    *death_month(Month.MAY,
                 death(5, Gender.FEMALE, 26, 28,
                       deceased=person("Пелагія", "Тимофѣева", status=PEASANT_WIFE), age=62,
                       relatives=[relative(person("Димитрій", "Максимовъ", "Калугинъ"), Relationship.HUSBAND)],
                       cause_of_death=DROPSY),
                 ),
    *death_month(Month.JUNE,
                 death(6, Gender.FEMALE, 15, 17,
                       deceased=person("Настасія", "Максимова"), age=12,
                       relatives=[relative(person("Васса", "Наумова", "Швейкина", status=SOLDIER_WIFE), Relationship.MOTHER)],
                       cause_of_death=COLIC),
                 ),
    *death_month(Month.AUGUST,
                 death(11, Gender.MALE, 6, 8,
                       deceased=person("Ѳеодоръ"), age="4 мес",
                       relatives=[relative(person("Татіана", "Маркова", status=SOLDIER_WIFE), Relationship.MOTHER)],
                       cause_of_death=COLIC),
                 death(8, Gender.FEMALE, 22, 24,
                       deceased=person("Ирина", "Васильева", status=PEASANT_WIFE), age=61,
                       relatives=[relative(person("Борисъ", None, "Жарковъ", comment="отчество не записано"), Relationship.HUSBAND)],
                       cause_of_death=HEADACHE),
                 ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
