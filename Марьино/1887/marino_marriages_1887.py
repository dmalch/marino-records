from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MAIDEN, PEASANT_MALE

# Source: ГАРО ф.627 оп.255 д.338 (Сергиевская церковь с. Эммануиловка, 1887).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
marino_marriages_1887 = marriage_records(
    "ГАРО", "627", "255", "338", "Эммануиловка", "Сергиевская", 1887,
    *marriage_month(Month.APRIL,
                    marriage(8, 12,
                             groom=person("Василий", "Иванов", "Мыльников"), groom_age=18, groom_marriage_num=1,
                             bride=person("Анастасия", "Данилова", "Головачева"), bride_age=19,
                             witness1=person("Семен", "Иванов", "Мыльников"),
                             witness2=person("Иван", "Димитриев", "Мыльников"),
                             witness3=person("Григорий", "Данилов", "Головачев"),
                             witness4=person("Андрей", "Михайлов", "Головачев")),
                    marriage(9, 26, reviewed=False,
                             groom=person("Петръ", "Филипповъ", "Воронкинъ"), groom_age=18, groom_marriage_num=1,
                             bride=person("Дарія", "Никитина", "Мазаева"), bride_age=17, bride_marriage_num=1,
                             witness1=person("Димитрій", "Никифоровъ", "Бычковъ", residence="Мануилово", side=Side.GROOM),
                             witness2=person("Михаилъ", "Михайловъ", "Воробьевъ", side=Side.GROOM),
                             witness3=person("Сергій", "Яковлевъ", "Швейкинъ", side=Side.BRIDE),
                             witness4=person("Иванъ", "Егоровъ", "Телегинъ", side=Side.BRIDE)),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_MAIDEN,
        status_groom=PEASANT_MALE
    ),
)
