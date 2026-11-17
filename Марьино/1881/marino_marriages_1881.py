from verso.ru.dsl import Month, RecordDefaults, marriage, marriage_month, marriage_records, person
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MAIDEN, PEASANT_MALE

# Source: ГАРО ф.627 оп.255 д.272 (Сергиевская церковь с. Эммануиловка, 1881).
# Read in full for Марьино on 2026-09-27: no other marriage of the year has a participant from Марьино.
marino_marriages_1881 = marriage_records(
    "ГАРО", "627", "255", "272", "Эммануиловка", "Сергиевская", 1881,
    *marriage_month(Month.APRIL,
                    marriage(6, 19,
                             groom=person("Василий", "Степанов", "Черкасов"), groom_age=27, groom_marriage_num=1,
                             bride=person("Татьяна", "Акимова", "Коржавенкова"), bride_age=19,
                             witness1=person("Иван", "Никитин", "Толмачев"),
                             witness2=person("Тимофей", "Григорьев", "Воробьев"),
                             witness3=person("Егор", "Николаев", "Мыльников"),
                             witness4=person("Гаврил", "Сергеев", "Калугин")),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_MAIDEN,
        status_groom=PEASANT_MALE,
    ),
)
