from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.255 д.518 (Сергиевская церковь с. Эммануиловка, 1902).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
marino_marriages_1902 = marriage_records(
    "ГАРО", "627", "255", "518", "Эммануиловка", "Сергиевская", 1902,
    *marriage_month(Month.FEBRUARY,
                    marriage(5, 13, reviewed=False,
                             groom=person("Іоаннъ", "Филимоновъ", "Оськинъ", residence="Важная"), groom_age=None, groom_marriage_num=1,
                             bride=person("Татіана", "Севастіанова", "Овсянкина"), bride_age=18, bride_marriage_num=1,
                             witness1=person("Григорій", "Зиновьевъ", "Кондаковъ", side=Side.GROOM, comment="деревня не названа"),
                             witness2=person("Іоаннъ", "Яковлевъ", "Оськинъ", side=Side.GROOM, comment="деревня не названа"),
                             witness3=person("Андрей", "Яковлевъ", "Оськинъ", side=Side.BRIDE, comment="деревня не названа"),
                             witness4=person("Михаилъ", "", "Иничковъ", side=Side.BRIDE, comment="отчество не записано"),
                             comment="возраст жениха читается «1?» — вторая цифра неясна"),
                    ),
    *marriage_month(Month.JUNE,
                    marriage(14, 3, reviewed=False,
                             groom=person("Іоаннъ", "Іоанновъ", "Свищовъ"), groom_age=18, groom_marriage_num=1,
                             bride=person("Екатерина", "Димитріева", "Лужкина", residence="Новоселки", comment="фамилия читается неуверенно («Луж…кина»)"), bride_age="15л 6м", bride_marriage_num=1,
                             witness1=person("Павелъ", "Петровъ", "Калугинъ"),
                             witness2=person("Михаилъ", "Косьминъ", "Свищовъ"),
                             witness3=person("Георгій", "Косьминъ", "Свищовъ"),
                             witness4=person("Никита", "Савельевъ", "Шапухинъ", comment="фамилия читается неуверенно; деревня не названа"),
                             comment="невесте «15½» — так в книге"),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_FEMALE,
        status_groom=PEASANT_MALE,
    ),
)
