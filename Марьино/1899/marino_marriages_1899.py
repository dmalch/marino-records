from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import (PEASANT_DAUGHTER, PEASANT_DAUGHTER_MAIDEN, PEASANT_FEMALE,
                                   PEASANT_MALE)

# Source: ГАРО ф.627 оп.255 д.476 (Сергиевская церковь с. Эммануиловка, 1899).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
marino_marriages_1899 = marriage_records(
    "ГАРО", "627", "255", "476", "Эммануиловка", "Сергиевская", 1899,
    *marriage_month(Month.JANUARY,
                    marriage(4, 12,
                             groom=person("Андрей", "Егоров", "Зрюев"), groom_age=18, groom_marriage_num=1,
                             bride=person("Анастасия", "Иванова", "Мыльникова"), bride_age=18,
                             witness1=person("Иаков", "Егоров", "Калугин"),
                             witness2=person("Михаил", "Космин", "Свищев"),
                             witness3=person("Григорий", "Павлов", "Морин"),
                             witness4=person("Михаил", "Зотов", "Воробьев")),
                    ),
    *marriage_month(Month.APRIL,
                    marriage(9, 25, reviewed=False,
                             groom=person("Іоаннъ", "Григорьевъ", "Воронинъ", residence="Важная"), groom_age=18, groom_marriage_num=1,
                             bride=person("Марія", "Васильева", "Черкасова", status=PEASANT_DAUGHTER_MAIDEN), bride_age=None, bride_marriage_num=1,
                             witness1=person("Михаилъ", "Андреевъ", "Милютинъ", residence="Важная"),
                             witness2=person("Романъ", "", "Дворцовъ", residence="Важная", comment="отчество не записано"),
                             witness3=person("Василій", "Григорьевъ", "Воронинъ", residence="Важная", side=Side.BRIDE, comment="деревня названа одна на всех поручителей — «крестьяне деревни Важной»"),
                             witness4=person("Сергій", "Павловъ", "Шилевъ", residence="Важная", side=Side.BRIDE, comment="фамилия читается неуверенно; деревня названа одна на всех поручителей"),
                             comment="возраст невесты читается «1?» — вторая цифра похожа на «1», не записан"),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_DAUGHTER,
        status_groom=PEASANT_MALE
    ),
)
