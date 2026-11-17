from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COUGH
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.255 д.518 (Сергиевская церковь с. Эммануиловка, 1902).
marino_deaths_1902 = death_records(
    "ГАРО", "627", "255", "518", "Эммануиловка", "Сергиевская", 1902,
    *death_month(Month.APRIL,
                 death(6, Gender.FEMALE, 9, 11,
                       deceased=person("Варвара"), age=2,
                       relatives=[relative(person("Николай", "Георгиев", "Мыльников"), Relationship.FATHER)],
                       cause_of_death=COUGH),
                 ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
