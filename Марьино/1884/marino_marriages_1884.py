from verso.ru.dsl import Month, RecordDefaults, marriage, marriage_month, marriage_records, person
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MAIDEN, PEASANT_MALE, SOLDIER, WIDOW

# Source: ГАРО ф.627 оп.255 д.305 (Сергиевская церковь с. Эммануиловка, 1884).
marino_marriages_1884 = marriage_records(
    "ГАРО", "627", "255", "305", "Эммануиловка", "Сергиевская", 1884,
    *marriage_month(Month.APRIL,
                    marriage(6, 15,
                             groom=person("Иван", "Степанов", status=SOLDIER, residence="Желанное"),
                             groom_marriage_num=2, groom_age=36,
                             bride=person("Пелагея", "Александрова", "Мыльникова", status="вдова солдатка"),
                             bride_marriage_num=2, bride_age=36,
                             witness1=person("Димитрий", "Арефьев", "Мыльников"),
                             witness2=person("Павел", "Иванов", "Калугин"),
                             witness3=person("Иван", "Иванов", "Мыльников"),
                             witness4=person("Семен", "Иванов", "Мыльников")),
                    ),
    *marriage_month(Month.JUNE,
                    marriage(10, 1,
                             groom=person("Максим", "Григорьев", "Швейкин", status=SOLDIER),
                             groom_marriage_num=2, groom_age=61,
                             bride=person("Агрипина", "Афанасьева", "Морина", status=WIDOW),
                             bride_marriage_num=2, bride_age=67,
                             witness1=person("Иван", "Иванов", "Мыльников"),
                             witness2=person("Димитрий", "Арефьев", "Мыльников"),
                             witness3=person("Иван", "Иванов", "Калугин"),
                             witness4=person("Сергей", "Яковлев", "Швейкин")),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_MAIDEN,
        status_groom=PEASANT_MALE,
    ),
)
