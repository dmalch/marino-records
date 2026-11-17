from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import (PEASANT_DAUGHTER_MAIDEN, PEASANT_FEMALE, PEASANT_MALE,
                                   PROPRIETOR_PEASANT_MALE, RETIRED_SOLDIER, SOLDIER, SOLDIER_WIDOW)

# Source: ГАРО ф.627 оп.255 д.252 (Сергиевская церковь с. Эммануиловка, 1879).
# Read in full for Марьино on 2026-09-27; records added by that sweep are reviewed=False.
marino_marriages_1879 = marriage_records(
    "ГАРО", "627", "255", "252", "Эммануиловка", "Сергиевская", 1879,
    *marriage_month(Month.APRIL,
                    marriage(1, 8, reviewed=False,
                             groom=person("Василій", "Даниловъ", "Гуляевъ", status=RETIRED_SOLDIER), groom_age=44, groom_marriage_num=1,
                             bride=person("Дарія", "Трофимова", "Вольнова", residence="Горбуновка", status=SOLDIER_WIDOW), bride_age=27, bride_marriage_num=2,
                             witness1=person("Косма", "Кириловъ", "Свищевъ", status=SOLDIER, side=Side.GROOM, comment="«Касма»"),
                             witness2=person("Тимоѳей", "Григорьевъ", "Воробьевъ", side=Side.GROOM),
                             witness3=person("Василій", "Захаровъ", "Зрюевъ", side=Side.BRIDE, comment="деревня не названа"),
                             witness4=person("Яковъ", "Яковлевъ", "Калугинъ", side=Side.BRIDE, comment="деревня не названа")),
                    marriage(6, 8, reviewed=False,
                             groom=person("Григорій", "Уваровъ", "Мазаевъ"), groom_age=19, groom_marriage_num=1,
                             bride=person("Евдокія", "Максимова", "Рындяева", residence="Алеменево", comment="фамилия читается неуверенно"), bride_age=19, bride_marriage_num=1,
                             witness1=person("Иванъ", "Никитинъ", "Толмачевъ", side=Side.GROOM),
                             witness2=person("Никита", "Михеевъ", "Мазаевъ", side=Side.GROOM),
                             witness3=person("Тимоѳей", "Борисовъ", "Калугинъ", status=SOLDIER, side=Side.BRIDE, comment="«той же деревни» — Марьиной"),
                             witness4=person("Даніилъ", "", "Головачевъ", side=Side.BRIDE, comment="отчество не записано")),
                    marriage(9, 9,
                             groom=person("Захар", "Яковлев", "Швейкин"), groom_age=18, groom_marriage_num=1,
                             bride=person("Евдокия", "Иванова", "Чекрышева", residence="Шарик"), bride_age=19,
                             witness1=person("Димитрий", "Григорьев", "Головачев"),
                             witness2=person("Сергей", "Яковлев", "Швейкин"),
                             witness3=person("Данил", last_name_orig="Головачев"),
                             witness4=person("Семен", "Иванов", "Мыльников")),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_DAUGHTER_MAIDEN,
        status_groom=PROPRIETOR_PEASANT_MALE
    ),
)
