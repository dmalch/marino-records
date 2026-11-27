from verso.ru.dsl import Month, RecordDefaults, marriage, marriage_month, marriage_records, person
from verso.ru.dsl.statuses import (PEASANT_DAUGHTER_MAIDEN, PEASANT_FEMALE, PEASANT_MALE,
                                   RETIRED_SOLDIER, SOLDIER_WIDOW)

# Source: ГАРО ф.627 оп.255 д.368 (Сергиевская церковь с. Эммануиловка, 1890).
# Read in full for Марьино on 2026-09-26: no other marriage names a party from Марьино.
marino_marriages_1890 = marriage_records(
    "ГАРО", "627", "255", "368", "Эммануиловка", "Сергиевская", 1890,
    *marriage_month(Month.APRIL,
                    marriage(5, 8,
                             groom=person("Петр", "Степанов", "Черкасов", status=RETIRED_SOLDIER, comment="отставной рядовой"),
                             groom_marriage_num=1, groom_age=44,
                             bride=person("Дария", "Трафимова", "Гуляева", status=SOLDIER_WIDOW, comment="вдова солдатка"),
                             bride_marriage_num=3, bride_age=39,
                             witness1=person("Петр", "Степанов", "Моисеев"),
                             witness2=person("Иван", "Димитриев", "Мыльников"),
                             witness3=person("Павел", "Петров", "Калугин"),
                             witness4=person("Гавриил", "Сергеев", "Калугин")),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_DAUGHTER_MAIDEN,
        status_groom=PEASANT_MALE
    ),
)
