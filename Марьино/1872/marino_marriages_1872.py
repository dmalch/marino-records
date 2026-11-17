from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import (PEASANT_DAUGHTER_MAIDEN, PEASANT_FEMALE, PEASANT_MALE,
                                   RETIRED_SOLDIER, SOLDIER_WIFE)

# Source: ГАРО ф.627 оп.255 д.201 (Сергиевская церковь с. Эммануиловка, 1872).
# Read in full for Марьино on 2026-09-27; records added by that sweep are reviewed=False.
# The album is phone photos of a screen with heavy moiré; uncertain readings say so.
marino_marriages_1872 = marriage_records(
    "ГАРО", "627", "255", "201", "Эммануиловка", "Сергиевская", 1872,
    *marriage_month(Month.JUNE,
                    marriage(6, 9,
                             groom=person("Андрей", "Захаровъ", "Зрюевъ", status=RETIRED_SOLDIER), groom_age=None, groom_marriage_num=2,
                             bride=person("Дарія", "Павлова", "Трифонова", residence="Новоселки"), bride_age=32,
                             witness1=person("Ѳеодоръ", "Захаровъ", "Зрюевъ", side=Side.GROOM),
                             witness2=person("Косма", "Кирилловъ", "Свищевъ", status="бессрочноотпускной солдат", side=Side.GROOM),
                             witness3=person("Яковъ", "Яковлевъ", "Калугинъ", side=Side.BRIDE),
                             witness4=person("Михаилъ", "Кирилловъ", "Свищевъ", side=Side.BRIDE),
                             comment="возраст жениха не записан"),
                    ),
    *marriage_month(Month.SEPTEMBER,
                    marriage(8, 20,
                             groom=person("Косма", "Кирилловъ", "Свищевъ", status="билетный солдат"), groom_age=55, groom_marriage_num=2,
                             bride=person("Евдокія", "Павлова", "Грачкова", residence="Чернояр", status=SOLDIER_WIFE, comment="отчество и фамилия читаются неуверенно"), bride_age=26, bride_marriage_num=2,
                             witness1=person("Егоръ", "Ѳеодоровъ", "Калугинъ", side=Side.GROOM),
                             witness2=person("Григорій", "Мамонтовъ", "Бычковъ", side=Side.GROOM),
                             witness3=person("Иванъ", "Ивановъ", "Калугинъ", side=Side.BRIDE),
                             witness4=person("Яковъ", "Яковлевъ", "Калугинъ", side=Side.BRIDE)),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_DAUGHTER_MAIDEN,
        status_groom=PEASANT_MALE
    ),
)
