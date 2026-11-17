from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import (PEASANT_DAUGHTER_MAIDEN, PEASANT_FEMALE, PEASANT_MALE,
                                   UNTER_OFFICER)

# Source: ГАРО ф.627 оп.255 д.292 (Сергиевская церковь с. Эммануиловка, 1883).
# Read in full for Марьино on 2026-09-27; records added by that sweep are reviewed=False.
marino_marriages_1883 = marriage_records(
    "ГАРО", "627", "255", "292", "Эммануиловка", "Сергиевская", 1883,
    *marriage_month(Month.JANUARY,
                    marriage(2, 23, reviewed=False,
                             groom=person("Иванъ", "Павловъ", "Клинковъ", residence="Золотая Поляна", comment="фамилия сверено владельцем 27.09.2026"), groom_age=20, groom_marriage_num=1,
                             bride=person("Елена", "Зеновіева", "Епишкина"), bride_age=19, bride_marriage_num=1,
                             witness1=person("Егоръ", "Павловъ", "Жнакинъ", residence="Золотая Поляна", side=Side.GROOM),
                             witness2=person("Василій", "Ивановъ", "Козловъ", residence="Золотая Поляна", side=Side.GROOM),
                             witness3=person("Косма", "Филипповъ", "Горинъ", residence="Золотая Поляна", side=Side.BRIDE, comment="«Касма»; «той же деревни» — Золотой Поляны"),
                             witness4=person("Косма", "Анисимовъ", "Тезинъ", residence="Золотая Поляна", side=Side.BRIDE, comment="«Касма»")),
                    ),
    *marriage_month(Month.APRIL,
                    marriage(9, 24, reviewed=False,
                             groom=person("Павелъ", "Зотовъ", "Воробьевъ"), groom_age=19, groom_marriage_num=1,
                             bride=person("Анастасія", "Захарова", "Шустова", residence="Важная"), bride_age=21, bride_marriage_num=1,
                             witness1=person("Павелъ", "Петровъ", "Калугинъ", side=Side.GROOM),
                             witness2=person("Иванъ", "Григорьевъ", "Швейкинъ", side=Side.GROOM),
                             witness3=person("Косма", "Захаровъ", "Шустовъ", residence="Важная", side=Side.BRIDE, comment="«Касма»"),
                             witness4=person("Василій", "Степановъ", "Климовъ", residence="Важная", side=Side.BRIDE, comment="фамилия читается неуверенно")),
                    marriage(12, 24, reviewed=False,
                             groom=person("Даніилъ", "Зеновіевъ", "Епишкинъ", comment="так в книге; в 1884 г. (рожд. ж.№14) с той же женой Екатериной Михайловой — «Даніилъ Леонтіевъ Епишкинъ». Предположение владельца (27.09.2026): одно из двух — отчество по деду, а не по отцу"), groom_age=22, groom_marriage_num=1,
                             bride=person("Екатерина", "Михайлова", "Минаева", residence="Краснохолм"), bride_age=17, bride_marriage_num=1,
                             witness1=person("Иванъ", "Никитинъ", "Толмачевъ", side=Side.GROOM),
                             witness2=person("Савостіанъ", "Ивановъ", "Овсянкинъ", side=Side.GROOM),
                             witness3=person("Степанъ", "Матвѣевъ", "Черкасовъ", side=Side.BRIDE, comment="«той же деревни» по тексту — Краснохолма, но Черкасовы и Свищевы марьинские"),
                             witness4=person("Косма", "Кириловъ", "Свищевъ", status=UNTER_OFFICER, side=Side.BRIDE, comment="«Касма»")),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_DAUGHTER_MAIDEN,
        status_groom=PEASANT_MALE
    ),
)
