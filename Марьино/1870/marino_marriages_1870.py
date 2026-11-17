from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import (PEASANT_DAUGHTER_MAIDEN, PEASANT_FEMALE, PEASANT_MALE,
                                   PROPRIETOR_PEASANT_MALE, SOLDIER)

# Source: ГАРО ф.627 оп.255 д.190 (Сергиевская церковь с. Эммануиловка, 1870).
# Read in full for Марьино on 2026-09-27; records added by that sweep are reviewed=False.
# The album is phone photos of a screen and the ink has faded; uncertain readings say so.
marino_marriages_1870 = marriage_records(
    "ГАРО", "627", "255", "190", "Эммануиловка", "Сергиевская", 1870,
    *marriage_month(Month.APRIL,
                    marriage(6, 19,
                             groom=person("Василій", "Борисовъ", "Калугинъ", status=PROPRIETOR_PEASANT_MALE), groom_age=18, groom_marriage_num=1,
                             bride=person("Марѳа", "Михайлова", last_name_orig="?", residence="Золотая Поляна", comment="имя и отчество читаются неуверенно, фамилия не разобрана"), bride_age=17, bride_marriage_num=1,
                             witness1=person("Иванъ", "Сергѣевъ", "Моринъ", side=Side.GROOM),
                             witness2=person("Петръ", "Егоровъ", "Калугинъ", side=Side.GROOM),
                             witness3=person("Николай", "Ивановъ", "Калугинъ", side=Side.BRIDE),
                             witness4=person("Яковъ", "Тимоѳеевъ", "Воробьевъ", status=SOLDIER, side=Side.BRIDE)),
                    ),
    *marriage_month(Month.JUNE,
                    marriage(10, 29,
                             groom=person("Николай", "Ивановъ", "Марковъ", residence="Аксельмеево", status=PROPRIETOR_PEASANT_MALE), groom_age=35, groom_marriage_num=1,
                             bride=person("Ксенія", "Стефанова", comment="фамилия читается неуверенно"), bride_age=19, bride_marriage_num=1,
                             witness1=person("Иванъ", "Ивановъ", last_name_orig="Калугинъ", side=Side.GROOM),
                             witness2=person("Антипъ", "Степановъ", "Галушкинъ", side=Side.GROOM, comment="отчество и фамилия читается неуверенно"),
                             witness3=person("Никифоръ", "Уаровъ", "Мазаевъ", side=Side.BRIDE, comment="отчество читается неуверенно"),
                             witness4=person("Василій", "Ивановъ", "Калугинъ", side=Side.BRIDE, comment="имя читается неуверенно"),
                             comment="день венчания читается неуверенно"),
                    ),
    *marriage_month(Month.JULY,
                    marriage(12, 26,
                             groom=person("Василій", "Григорьевъ", "Бычковъ", status=PROPRIETOR_PEASANT_MALE, comment="имя и фамилия читается неуверенно"), groom_age=19, groom_marriage_num=1,
                             bride=person("Варвара", "Матвѣева", "Калугина", comment="деревня не разобрана; отчество и фамилия читаются неуверенно"), bride_marriage_num=1,
                             bride_age="15 лет 8 мес",
                             witness1=person("Иванъ", "Никитинъ", "Толмачевъ", side=Side.GROOM, comment="фамилия читается неуверенно"),
                             witness2=person("Иванъ", "Сергѣевъ", "Моринъ", side=Side.GROOM),
                             witness3=person("Василій", side=Side.BRIDE, comment="отчество и фамилия не читаются"),
                             witness4=person("?", "?", "Галушкинъ", side=Side.BRIDE, comment="имя и отчество не читаются; фамилия читается неуверенно"),
                             comment="возраст невесты не разобран"),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_DAUGHTER_MAIDEN,
        status_groom=PEASANT_MALE
    ),
)
