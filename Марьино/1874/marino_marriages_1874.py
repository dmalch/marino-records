from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import (PEASANT_DAUGHTER_MAIDEN, PEASANT_FEMALE, PEASANT_MALE,
                                   PROPRIETOR_PEASANT_MALE, SOLDIER)

# Source: ГАРО ф.627 оп.255 д.213 (Сергиевская церковь с. Эммануиловка, 1874).
# Read in full for Марьино on 2026-09-27; proofread in Verso on 2026-10-13.
# The album is phone photos of a screen with heavy moiré; uncertain readings say so.
marino_marriages_1874 = marriage_records(
    "ГАРО", "627", "255", "213", "Эммануиловка", "Сергиевская", 1874,
    *marriage_month(Month.APRIL,
                    marriage(4, 7,
                             groom=person("Никифоръ", "Уаровъ", "Мазаевъ"), groom_age=29, groom_marriage_num=2,
                             bride=person("Матрона", "Иванова", "Овсянкина"), bride_age=21,
                             witness1=person("Иванъ", "Никитинъ", "Толмачевъ", side=Side.GROOM),
                             witness2=person("Никита", "Михѣевъ", "Мазаевъ", side=Side.GROOM),
                             witness3=person("Димитрій", "Григорьевъ", "Головачевъ", side=Side.BRIDE),
                             witness4=person("Иванъ", "Сергѣевъ", "Моринъ", side=Side.BRIDE)),
                    marriage(9, 7,
                             groom=person("Алексей", "Михайлов", "Головачев"), groom_marriage_num=1, groom_age=18,
                             bride=person("Евдокия", "Димитриева", "Мыльникова"), bride_age=18,
                             witness1=person("Михаил", "Ефимов", "Воробьев"),
                             witness2=person("Иван", "Васильев", "Головачев", status=SOLDIER),
                             witness3=person("Даниил", "Феодоров", "Головачев"),
                             witness4=person("Антип", "Степанов", "Галушкин")),
                    marriage(10, 7,
                             groom=person("Семен", "Иванов", "Мыльников"), groom_marriage_num=1, groom_age=18,
                             bride=person("Наталья", "Васильева", "Моисеева"), bride_age=18,
                             witness1=person("Иван", "Спиридонов", last_name_orig="?", residence="Мануилово"),
                             witness2=person("Иван", "Григорьев", "Швейкин"),
                             witness3=person("Петр", "Степанов", "Моисеев"),
                             witness4=person("Степан", "Михайлов?", "Черкасов")),
                    ),
    *marriage_month(Month.JUNE,
                    marriage(17, 30,
                             groom=person("Иванъ", "Михайловъ", last_name_orig="Сахаровъ", residence="Золотая Поляна", status=SOLDIER), groom_age=28, groom_marriage_num=1,
                             bride=person("Анисья", "Иванова", last_name_orig="Гаврилова", residence="Золотая Поляна"), bride_age=18,
                             witness1=person("Иванъ", "Степановъ", "Червоновъ", residence="Золотая Поляна", side=Side.GROOM),
                             witness2=person("Трафимъ", "Михайловъ", "Сахаровъ", residence="Золотая Поляна", side=Side.GROOM),
                             witness3=person("Василій", "Павловъ", "Жа?", residence="Золотая Поляна", side=Side.BRIDE, comment="фамилия читается неуверенно"),
                             witness4=person("Василій", "Григорьевъ", "Бычковъ", side=Side.BRIDE),
                             comment="из Марьина только поручитель по невесте; фото экрана с муаром"),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_DAUGHTER_MAIDEN,
        status_groom=PROPRIETOR_PEASANT_MALE
    ),
)
