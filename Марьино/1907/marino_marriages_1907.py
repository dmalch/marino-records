from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.255 д.578 (Сергиевская церковь с. Эммануиловка, 1907).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
marino_marriages_1907 = marriage_records(
    "ГАРО", "627", "255", "578", "Эммануиловка", "Сергиевская", 1907,
    *marriage_month(Month.FEBRUARY,
                    marriage(2, 18, reviewed=False,
                             groom=person("Николай", "Павловъ", "Калугинъ"), groom_age=18, groom_marriage_num=1,
                             bride=person("Евдокія", "Михайлова", "Сауткина", residence="Купля"), bride_age=18, bride_marriage_num=1,
                             witness1=person("Тимоѳей", "Ивановъ", "Свищовъ"),
                             witness2=person("Антонъ", "Егоровъ", "Зрюевъ"),
                             witness3=person("Петръ", "Егоровъ", "Калугинъ", side=Side.BRIDE, comment="деревня не названа"),
                             witness4=person("Иванъ", "Григорьевъ", "Воронкинъ", side=Side.BRIDE, comment="деревня не названа")),
                    marriage(6, 23,
                             groom=person("Василий", "Иванов", "Мыльников"), groom_age="17 лет 11 мес", groom_marriage_num=1,
                             bride=person("Евдокия", "Григорьева", "Стрышкова", residence="Алеменево"), bride_age=17, bride_marriage_num=1,
                             witness1=person("Феодор", last_name_orig="Моисеев"),
                             witness2=person("Григорий", last_name_orig="Воронкин"),
                             witness3=person("Игнат", "Иванов", "Рожков"),
                             witness4=person("Феодор", "Павлов", "Марышов"),
                             comment="возраст жениха в источнике «17л 11 ½ м»"),
                    ),
    *marriage_month(Month.APRIL,
                    marriage(9, 29,
                             groom=person("Степан", "Григорьев", "Головачев"), groom_age=19, groom_marriage_num=1,
                             bride=person("Анна", "Тимофеева", "Ермачкова", residence="Новоселки"), bride_age=16, bride_marriage_num=1,
                             witness1=person("Николай", "Егоров", "Мыльников"),
                             witness2=person("Феодор", last_name_orig="Моисеев"),
                             witness3=person("Василий", "Семенов", "Мыльников"),
                             witness4=person("Иван", last_name_orig="Головачев")),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_FEMALE,
        status_groom=PEASANT_MALE
    ),
)
