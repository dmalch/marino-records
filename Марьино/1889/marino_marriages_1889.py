from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MAIDEN, PEASANT_MALE, PEASANT_WIDOW

# Source: ГАРО ф.627 оп.255 д.359 (Сергиевская церковь с. Эммануиловка, 1889).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
marino_marriages_1889 = marriage_records(
    "ГАРО", "627", "255", "359", "Эммануиловка", "Сергиевская", 1889,
    *marriage_month(Month.JANUARY,
                    marriage(1, 29, reviewed=False,
                             groom=person("Николай", "Антиповъ", "Галушкинъ"), groom_age=27, groom_marriage_num=2,
                             bride=person("Анисія", "Никифорова", "Бочарова", residence="Завидная", status=PEASANT_WIDOW, comment="в апреле 1889 г. (рожд. ж.№14) восприемница «Анисія Никифорова Галушкина»"), bride_age=20, bride_marriage_num=2,
                             witness1=person("Петръ", "Ѳеодоровъ", "Телегинъ", side=Side.GROOM),
                             witness2=person("Иванъ", "Егоровъ", "Телегинъ", side=Side.GROOM),
                             witness3=person("Иванъ", "Григорьевъ", "Швейкинъ", side=Side.BRIDE, comment="«той же деревни» — Марьиной"),
                             witness4=person("Иванъ", "Ивановъ", "Калугинъ", side=Side.BRIDE)),
                    ),
    *marriage_month(Month.FEBRUARY,
                    marriage(4, 10,
                             groom=person("Степан", "Максимов", "Швейкин"), groom_age=18, groom_marriage_num=1,
                             bride=person("Христиния", "Васильева", "Иваненкова", residence="Боковой Майдан"),
                             bride_age=18,
                             witness1=person("Иван", "Григорьев", "Швейкин"),
                             witness2=person("Иван", "Никитин", "Толмачев"),
                             witness3=person("Иван", "Иванов", "Мыльников"),
                             witness4=person("Николай", "Антипов", "Галушкин")),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_MAIDEN,
        status_groom=PEASANT_MALE
    ),
)
