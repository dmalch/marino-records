from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.255 д.542 (Сергиевская церковь с. Эммануиловка, 1904).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
marino_marriages_1904 = marriage_records(
    "ГАРО", "627", "255", "542", "Эммануиловка", "Сергиевская", 1904,
    *marriage_month(Month.APRIL,
                    marriage(5, 4, reviewed=False,
                             groom=person("Стефанъ", "Георгіевъ", "Калугинъ"), groom_age=18, groom_marriage_num=1,
                             bride=person("Татіана", "Михайлова", "Милютина", residence="Важная"), bride_age=18, bride_marriage_num=1,
                             witness1=person("Георгій", "Ѳеодоровъ", "Зрюевъ"),
                             witness2=person("Антоній", "Георгіевъ", "Зрюевъ"),
                             witness3=person("Павелъ", "Зотовъ", "Воробьевъ", side=Side.BRIDE, comment="деревня не названа"),
                             witness4=person("Николай", "Григорьевъ", "Воронинъ", side=Side.BRIDE, comment="деревня не названа")),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_FEMALE,
        status_groom=PEASANT_MALE,
    ),
)
