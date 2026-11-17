from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MAIDEN, PEASANT_MALE

# Source: ГАРО ф.627 оп.255 д.169 (Сергиевская церковь с. Эммануиловка, 1862).
# Read in full for Марьино on 2026-09-27; records added by that sweep are reviewed=False.
# The sureties' village is not written in this book; the default residence stands for them.
marino_marriages_1862 = marriage_records(
    "ГАРО", "627", "255", "169", "Эммануиловка", "Сергиевская", 1862,
    *marriage_month(Month.APRIL,
                    marriage(6, 18,
                             groom=person("Петръ", "Ѳеодоровъ", "Телегинъ"), groom_age=19, groom_marriage_num=1,
                             bride=person("Акилина", "Анисимова", "Тезина", residence="Золотая Поляна"), bride_age=18, bride_marriage_num=1,
                             witness1=person("Иванъ", "Никитинъ", "Толмачевъ", side=Side.GROOM),
                             witness2=person("Николай", None, "Петелинъ", side=Side.GROOM, comment="отчество не записано"),
                             witness3=person("Артемъ", "Михайловъ", "Матыкинъ", side=Side.BRIDE, comment="деревня не названа"),
                             witness4=person("Николай", "Даниловъ", "Шелиповъ", side=Side.BRIDE, comment="деревня не названа")),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_MAIDEN,
        status_groom=PEASANT_MALE,
    ),
)
