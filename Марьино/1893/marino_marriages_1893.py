from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import PEASANT_DAUGHTER_MAIDEN, PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.255 д.396 (Сергиевская церковь с. Эммануиловка, 1893).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
marino_marriages_1893 = marriage_records(
    "ГАРО", "627", "255", "396", "Эммануиловка", "Сергиевская", 1893,
    *marriage_month(Month.APRIL,
                    marriage(4, 4,
                             groom=person("Яков", "Федотов", "Оськин", residence="Сборная", status="рядовой, уволенный с военной службы по болезни"), groom_age=25, groom_marriage_num=1,
                             bride=person("Мария", "Данилова", "Головачева"), bride_age=16,
                             witness1=person("Василий", "Иванов", "Мыльников"),
                             witness2=person("Михаил", "Феодоров", "Головачев"),
                             witness3=person("Михаил", "Михайлов", "Воробьев"),
                             witness4=person("Тимофей", "Борисов", "Калугин")),
                    marriage(7, 4, reviewed=False,
                             groom=person("Иванъ", "Михайловъ", "Воробьевъ"), groom_age=18, groom_marriage_num=1,
                             bride=person("Анисія", "Петрова", "Данишина", residence="Желанное", comment="фамилия читается неуверенно"), bride_age=19, bride_marriage_num=1,
                             witness1=person("Петръ", "Степановъ", "Моисеевъ"),
                             witness2=person("Иванъ", "Михайловъ", "Воробьевъ", comment="так в книге — поручителем назван сам жених; вероятно, описка"),
                             witness3=person("Сергій", "Яковлевъ", "Швейкинъ", side=Side.BRIDE, comment="«той же деревни» — Марьиной"),
                             witness4=person("Иванъ", "Петровъ", "Моисеевъ", side=Side.BRIDE)),
                    ),
    *marriage_month(Month.SEPTEMBER,
                    marriage(9, 27, reviewed=False,
                             groom=person("Иванъ", "Яковлевъ", "Оськинъ", residence="Важная", status="уволенный в запас армии бомбардир"), groom_age=25, groom_marriage_num=1,
                             bride=person("Марія", "Макарова", "Камарова"), bride_age=19, bride_marriage_num=1,
                             witness1=person("Андрей", "Яковлевъ", "Оськинъ", residence="Важная"),
                             witness2=person("Иванъ", "Осиповъ", "Сосинъ", residence="Важная"),
                             witness3=person("Михаилъ", "Макаровъ", "Комаровъ", side=Side.BRIDE, comment="деревня не названа"),
                             witness4=person("Степанъ", "Матвѣевъ", "Черкасовъ", side=Side.BRIDE, comment="деревня не названа")),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_DAUGHTER_MAIDEN,
        status_groom=PEASANT_MALE
    ),
)
