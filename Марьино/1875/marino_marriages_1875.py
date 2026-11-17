from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import (PEASANT_DAUGHTER_GIRL, PEASANT_DAUGHTER_MAIDEN, PEASANT_FEMALE,
                                   PEASANT_MAIDEN, PEASANT_MALE, PEASANT_WIDOW,
                                   PROPRIETOR_PEASANT_MALE, SOLDIER)

# Source: ГАРО ф.627 оп.255 д.219 (Сергиевская церковь с. Эммануиловка, 1875).
# Read in full for Марьино on 2026-09-27; proofread in Verso on 2026-10-14.
# The album is phone photos of a screen with heavy moiré; uncertain readings say so.
marino_marriages_1875 = marriage_records(
    "ГАРО", "627", "255", "219", "Эммануиловка", "Сергиевская", 1875,
    *marriage_month(Month.APRIL,
                    marriage(3, 20,
                             groom=person("Гавріилъ", "Сергѣевъ", "Калугинъ", status=PROPRIETOR_PEASANT_MALE), groom_age=22, groom_marriage_num=1,
                             bride=person("Пелагія", "Иванова", "Толмачева", status=PEASANT_DAUGHTER_GIRL), bride_age=17,
                             witness1=person("Косма", "Кириловъ", "Свищевъ", status=SOLDIER, side=Side.GROOM),
                             witness2=person("Иванъ", "Яковлевъ", "Воронкинъ", residence="Краснохолм", side=Side.GROOM),
                             witness3=person("Зотъ", "Аникѣевъ", "Воробьевъ", side=Side.BRIDE),
                             witness4=person("Петръ", "Степановъ", "Моисеевъ", side=Side.BRIDE)),
                    marriage(4, 20,
                             groom=person("Василій", "Григорьевъ", "Бычковъ", status=PROPRIETOR_PEASANT_MALE), groom_marriage_num=2, groom_age=23,
                             bride=person("Марва", "Герасимова", "Тарасова", residence="Новоселки", status=PEASANT_WIDOW),
                             bride_marriage_num=2, bride_age=28,
                             witness1=person("Иванъ", "Сергѣевъ", "Моринъ", side=Side.GROOM),
                             witness2=person("Иванъ", "Ивановъ", "Мыльниковъ", side=Side.GROOM),
                             witness3=person("Василій", last_name_orig="Мазаевъ", side=Side.BRIDE, comment="отчество неразборчиво"),
                             witness4=person("Семенъ", "Ивановъ", "Мыльниковъ", side=Side.BRIDE)),
                    marriage(12, 27,
                             groom=person("Степанъ", "Петровъ", "Кузнецовъ", residence="Мануилово"), groom_age=17, groom_marriage_num=1,
                             bride=person("Ксенія", "Степанова", "Усадина", status=PEASANT_DAUGHTER_MAIDEN), bride_age=18,
                             witness1=person("Иванъ", "Савельевъ", "Грикинъ", residence="Мануилово", side=Side.GROOM),
                             witness2=person("Иванъ", "Савостьяновъ", "Смирновъ", residence="Краснохолм", side=Side.GROOM),
                             witness3=person("Даніилъ", "?", "Жарковъ", residence="Мануилово", side=Side.BRIDE),
                             witness4=person("Захаръ", "Ѳеодоровъ", "Петинъ", residence="Мануилово", side=Side.BRIDE)),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_MAIDEN,
        status_groom=PEASANT_MALE
    ),
)
