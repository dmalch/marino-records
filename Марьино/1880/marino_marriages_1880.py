from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import PEASANT_DAUGHTER_MAIDEN, PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.255 д.260 (Сергиевская церковь с. Эммануиловка, 1880).
# Read in full for Марьино on 2026-09-27; records added by that sweep are reviewed=False.
# No marriage of the year has a bride or groom from Марьино; this one has a surety.
marino_marriages_1880 = marriage_records(
    "ГАРО", "627", "255", "260", "Эммануиловка", "Сергиевская", 1880,
    *marriage_month(Month.JUNE,
                    marriage(12, 9, reviewed=False,
                             groom=person("Ѳеодоръ", "Матвѣевъ", "Барсуковъ", residence="Мануилово"), groom_age=18, groom_marriage_num=1,
                             bride=person("Екатерина", "Алексѣева", "Епишкина", residence="Мануилово"), bride_age=19, bride_marriage_num=1,
                             witness1=person("Василій", "Ѳеофилактовъ", "Моисеевъ", side=Side.GROOM, comment="«крестьянинъ деревни Марьиной»"),
                             witness2=person("Михаилъ", "Арсеньевъ", "Дмитріевъ", residence="Мануилово", side=Side.GROOM),
                             witness3=person("Иванъ", "Яковлевъ", "Стародымовъ", residence="Мануилово", side=Side.BRIDE, comment="фамилия читается неуверенно; деревня не названа"),
                             witness4=person("Петръ", "Матвѣевъ", "Барсуковъ", residence="Мануилово", side=Side.BRIDE, comment="деревня не названа"),
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
