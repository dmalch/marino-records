from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLD, DROPSY, SUFFOCATION
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, SOLDIER, SOLDIER_WIDOW

# Source: ГАРО ф.627 оп.255 д.305 (Сергиевская церковь с. Эммануиловка, 1884).
# Read in full for Марьино on 2026-09-27; records added by that sweep are reviewed=False.
marino_deaths_1884 = death_records(
    "ГАРО", "627", "255", "305", "Эммануиловка", "Сергиевская", 1884,
    *death_month(Month.MARCH,
                 death(4, Gender.FEMALE, 20, 21, reviewed=False,
                       deceased=person("Васса", "Наумова"), age=None,
                       relatives=[relative(person("Максимъ", "Григорьевъ", "Швейкинъ", status=SOLDIER), Relationship.HUSBAND)],
                       cause_of_death=COLD, comment="в графе «5…» — вторая цифра в корешке; вдовец венчался вторично 1 июня 1884 г. (ч. 2 №10)"),
                 ),
    *death_month(Month.MAY,
                 death(5, Gender.FEMALE, 12, 14, reviewed=False,
                       deceased=person("Матрона", "Васильева", "Головачева", status=SOLDIER_WIDOW), age=58,
                       cause_of_death=DROPSY),
                 ),
    *death_month(Month.JULY,
                 death(12, Gender.MALE, 1, 2, reviewed=False,
                       deceased=person("Иванъ", "Григорьевъ", "Марковъ"), age=65,
                       cause_of_death=DROPSY),
                 ),
    *death_month(Month.OCTOBER,
                 death(14, Gender.MALE, 2, 3, reviewed=False,
                       deceased=person("Степанъ", "Ивановъ", "Личардинъ", comment="фамилия сверено владельцем 27.09.2026; в корпусе больше не встречается"), age=65,
                       cause_of_death=SUFFOCATION),
                 ),
    *death_month(Month.NOVEMBER,
                 death(8, Gender.FEMALE, 22, 25,
                       deceased=person("Варвара"), age=9,
                       relatives=[relative(person("Иван", "Иванов", "Мыльников"), Relationship.FATHER)],
                       cause_of_death="от боли в животе"),
                 ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
