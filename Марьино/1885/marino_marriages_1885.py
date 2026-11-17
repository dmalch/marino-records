from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import PEASANT_DAUGHTER_MAIDEN, PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.255 д.315 (Сергиевская церковь с. Эммануиловка, 1885).
# Read in full for Марьино on 2026-09-27; records added by that sweep are reviewed=False.
marino_marriages_1885 = marriage_records(
    "ГАРО", "627", "255", "315", "Эммануиловка", "Сергиевская", 1885,
    *marriage_month(Month.MAY,
                    marriage(13, 13, reviewed=False,
                             groom=person("Николай", "Антиповъ", "Галушкинъ"), groom_age=24, groom_marriage_num=1,
                             bride=person("Марѳа", "Гаврилова", residence="Печкиряский Майдан", comment="«Спасскаго уѣзда, села Печкиряскаго(?) Майдана»; фамилия не записана; погребена 16.04.1888, 22 лет"), bride_age=19, bride_marriage_num=1,
                             witness1=person("Егоръ", "Ѳеодоровъ", "Телегинъ", side=Side.GROOM),
                             witness2=person("Петръ", "Ѳеодоровъ", "Телегинъ", side=Side.GROOM),
                             witness3=person("Иванъ", "Никитинъ", "Толмачевъ", side=Side.BRIDE, comment="«той же деревни» — Марьиной"),
                             witness4=person("Иванъ", "Ивановъ", "Калугинъ", side=Side.BRIDE)),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_DAUGHTER_MAIDEN,
        status_groom=PEASANT_MALE
    ),
)
