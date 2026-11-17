from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MAIDEN, PEASANT_MALE, SOLDIER

# Source: ГАРО ф.627 оп.255 д.350 (Сергиевская церковь с. Эммануиловка, 1888).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
marino_marriages_1888 = marriage_records(
    "ГАРО", "627", "255", "350", "Эммануиловка", "Сергиевская", 1888,
    *marriage_month(Month.FEBRUARY,
                    marriage(5, 14, reviewed=False,
                             groom=person("Иванъ", "Петровъ", "Моисеевъ"), groom_age=18, groom_marriage_num=1,
                             bride=person("Стефанида", "Тимоѳеева", "Колина", residence="Желанное"), bride_age=17, bride_marriage_num=1,
                             witness1=person("Михаилъ", "Михайловъ", "Воробьевъ", side=Side.GROOM),
                             witness2=person("Савостіанъ", "Ивановъ", "Овсянкинъ", side=Side.GROOM),
                             witness3=person("Иванъ", "Никитинъ", "Толмачевъ", side=Side.BRIDE, comment="«той же деревни» — Марьиной"),
                             witness4=person("Михаилъ", "Ефимовъ", "Воробьевъ", side=Side.BRIDE)),
                    marriage(6, 14, reviewed=False,
                             groom=person("Александръ", "Касминъ", "Свищевъ"), groom_age=18, groom_marriage_num=1,
                             bride=person("Дарія", "Ефимова", "Ольчева", residence="Желанное"), bride_age=18, bride_marriage_num=1,
                             witness1=person("Петръ", "Степановъ", "Моисеевъ", side=Side.GROOM),
                             witness2=person("Павелъ", "Петровъ", "Калугинъ", side=Side.GROOM),
                             witness3=person("Егоръ", "Ѳеодоровъ", "Калугинъ", side=Side.BRIDE, comment="«той же деревни» — Марьиной"),
                             witness4=person("Иванъ", "Михайловъ", "Свищевъ", side=Side.BRIDE)),
                    marriage(7, 14, reviewed=False,
                             groom=person("Василій", "Антиповъ", "Галушкинъ", status=SOLDIER), groom_age=23, groom_marriage_num=1,
                             bride=person("Наталія", "Иванова", "Скотникова", residence="Желанное"), bride_age=17, bride_marriage_num=1,
                             witness1=person("Иванъ", "Егоровъ", "Телегинъ", side=Side.GROOM),
                             witness2=person("Петръ", "Ѳеодоровъ", "Телегинъ", side=Side.GROOM),
                             witness3=person("Василій", "Ивановъ", "Мыльниковъ", side=Side.BRIDE, comment="«той же деревни» — Марьиной"),
                             witness4=person("Иванъ", "Ивановъ", "Калугинъ", side=Side.BRIDE)),
                    ),
    *marriage_month(Month.MAY,
                    marriage(19, 15, reviewed=False,
                             groom=person("Семенъ", "Петровъ", "Куликовъ", residence="Новая (Спасский у.)"), groom_age=19, groom_marriage_num=1,
                             bride=person("Екатерина", "Петрова", "Телегина"), bride_age=21, bride_marriage_num=1,
                             witness1=person("Николай", "Антиповъ", "Галушкинъ", side=Side.GROOM),
                             witness2=person("Михаилъ", "Михайловъ", "Воробьевъ", side=Side.GROOM),
                             witness3=person("Иванъ", "Егоровъ", "Телегинъ", side=Side.BRIDE),
                             witness4=person("Гавріилъ", "Сергѣевъ", "Толмачевъ", side=Side.BRIDE)),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_MAIDEN,
        status_groom=PEASANT_MALE
    ),
)
