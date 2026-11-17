from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import (PEASANT_DAUGHTER_MAIDEN, PEASANT_FEMALE, PEASANT_MALE,
                                   PEASANT_WIDOW, SOLDIER)

# Source: ГАРО ф.627 оп.255 д.237 (Сергиевская церковь с. Эммануиловка, 1877).
# Read in full for Марьино on 2026-09-27; records added by that sweep are reviewed=False.
marino_marriages_1877 = marriage_records(
    "ГАРО", "627", "255", "237", "Эммануиловка", "Сергиевская", 1877,
    *marriage_month(Month.APRIL,
                    marriage(7, 3, reviewed=False,
                             groom=person("Егоръ", "Ѳеодоровъ", "Зрюевъ"), groom_age=18, groom_marriage_num=1,
                             bride=person("Анастасія", "Петрова", "Чуева", residence="Шаморга", comment="«Села Шамарги»; фамилия читается неуверенно"), bride_age=21, bride_marriage_num=1,
                             witness1=person("Василій", "Филатовъ", "Моисеевъ", side=Side.GROOM),
                             witness2=person("Гавріилъ", "Сергѣевъ", "Калугинъ", side=Side.GROOM),
                             witness3=person("Иванъ", "Никитинъ", "Толмачевъ", side=Side.BRIDE, comment="деревня не названа"),
                             witness4=person("Тимоѳей", "Борисовъ", "Калугинъ", status=SOLDIER, side=Side.BRIDE, comment="деревня не названа")),
                    ),
    *marriage_month(Month.JUNE,
                    marriage(14, 29, reviewed=False,
                             groom=person("Иванъ", "Андреевъ", "Буряковъ", residence="Мануилово"), groom_age=20, groom_marriage_num=1,
                             bride=person("Агафья", "Яковлева", "Посовинкина", residence="д. Коршинцы?", status=PEASANT_WIDOW, comment="деревня «Коршинцы(?)» и фамилия читаются неуверенно"), bride_age=23, bride_marriage_num=2,
                             witness1=person("Николай", "Ефимовъ", "Моисеевъ", residence="Мануилово", side=Side.GROOM),
                             witness2=person("Несторъ", "Косминъ", "Толмачевъ", residence="Мануилово", side=Side.GROOM, comment="«Нестеръ Касминъ»"),
                             witness3=person("Косма", "Кириловъ", "Свищевъ", status=SOLDIER, side=Side.BRIDE, comment="«Деревни Марьиной солдатъ Касма»"),
                             witness4=person("Семенъ", "Васильевъ", "Толмачевъ", residence="Мануилово", side=Side.BRIDE),
                             comment="из Марьина только поручитель"),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_DAUGHTER_MAIDEN,
        status_groom=PEASANT_MALE
    ),
)
