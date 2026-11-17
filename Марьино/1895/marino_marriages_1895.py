from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import (PEASANT_DAUGHTER_MAIDEN, PEASANT_FEMALE, PEASANT_MALE,
                                   PEASANT_WIDOW)

# Source: ГАРО ф.627 оп.255 д.425 (Сергиевская церковь с. Эммануиловка, 1895).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
marino_marriages_1895 = marriage_records(
    "ГАРО", "627", "255", "425", "Эммануиловка", "Сергиевская", 1895,
    *marriage_month(Month.JULY,
                    marriage(13, 9, reviewed=False,
                             groom=person("Ѳеодоръ", "Васильевъ", "Моисеевъ"), groom_age=24, groom_marriage_num=2,
                             bride=person("Евдокія", "Егорова", "Чумакина", residence="Желанное", status=PEASANT_WIDOW), bride_age=26, bride_marriage_num=2,
                             witness1=person("Петръ", "Степановъ", "Моисеевъ"),
                             witness2=person("Михаилъ", "Михайловъ", "Воробьевъ", comment="отчество перенесено, видно «…иловъ»"),
                             witness3=person("Иванъ", "Петровъ", "Моисеевъ", side=Side.BRIDE, comment="«той же деревни» — Марьиной"),
                             witness4=person("Савостіанъ", "Ивановъ", "Овсянкинъ", side=Side.BRIDE)),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_DAUGHTER_MAIDEN,
        status_groom=PEASANT_MALE
    ),
)
