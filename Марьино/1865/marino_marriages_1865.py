from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import (PEASANT_FEMALE, PEASANT_MAIDEN, PEASANT_MALE, PEASANT_SON,
                                   RETIRED_SOLDIER, WIDOW)

# Source: ГАРО ф.627 оп.255 д.173 (Сергиевская церковь с. Эммануиловка, 1865).
# Read in full for Марьино on 2026-09-27; records added by that sweep are reviewed=False.
# Godparents and sureties from Марьино are written without a village; the default residence stands for them.
marino_marriages_1865 = marriage_records(
    "ГАРО", "627", "255", "173", "Эммануиловка", "Сергиевская", 1865,
    *marriage_month(Month.APRIL,
                    marriage(2, 11,
                             groom=person("Дмитрий", "Михайлов", "Чеменев", residence="Мануилово"),
                             groom_age=19, groom_marriage_num=1,
                             bride=person("Агафия", "Степанова", "Морозова", residence="Инная Слобода"), bride_age=19,
                             witness1=person("Антон", "Федоров", "Лунин", residence="Екатериновка"),
                             witness2=person("Дмитрий", "Арефиев", "Мыльников"),
                             witness3=person("Игнат", "Васильев", "Воронкин"),
                             witness4=person("Василий", "Алексеев", "Сахаров", status=RETIRED_SOLDIER)),
                    ),
    *marriage_month(Month.MAY,
                    marriage(5, 9,
                             groom=person("Михаилъ", "Ѳеодоровъ", "Головачевъ", status=PEASANT_MALE), groom_age=32, groom_marriage_num=2,
                             bride=person("Евдокія", "Никандрова", "Галыничева", residence="Аксельмеево", status=WIDOW), bride_age=31, bride_marriage_num=2,
                             witness1=person("Иванъ", "Ивановъ", "Калугинъ", side=Side.GROOM),
                             witness2=person("Яковъ", "Яковлевъ", "Калугинъ", side=Side.GROOM),
                             witness3=person("Артемъ", "Никандровъ", "Воронкинъ", residence="Аксельмеево", side=Side.BRIDE),
                             witness4=person("Сергей", "Ѳедоровъ", "Лазинъ", residence="Аксельмеево", side=Side.BRIDE)),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_MAIDEN,
        status_groom=PEASANT_SON
    ),
)
