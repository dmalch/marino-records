from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.279 д.56 (Сергиевская церковь с. Эммануиловка, 1913).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
marino_marriages_1913 = marriage_records(
    "ГАРО", "627", "279", "56", "Эммануиловка", "Сергиевская", 1913,
    *marriage_month(Month.FEBRUARY,
                    marriage(1, 13,
                             groom=person("Иван", "Михайлов", "Свищов"), groom_age=18, groom_marriage_num=1,
                             bride=person("Ирина", "Семенова", "Мыльникова"), bride_age=18, bride_marriage_num=1,
                             witness1=person("Егор", "Косьмин", "Свищов"),
                             witness2=person("Иван", "Яковлев", "Рогулин"),
                             witness3=person("Феодор", "Васильев", "Моисеев"),
                             witness4=person("Семен", "Яковлев", "Рогулин")),
                    ),
    *marriage_month(Month.APRIL,
                    marriage(4, 21, reviewed=False,
                             groom=person("Матвѣй", "Петровъ", "Киселевъ", residence="Каргашино", comment="«села Каргашина Ананьевской волости, Спасскаго уѣзда»; в 1914–1915 гг. отец с женой Марѳой Ивановой записан «Ивашкинъ» / «Иванашкинъ»"), groom_age=22, groom_marriage_num=1,
                             bride=person("Марѳа", "Иванова", "Косицкова", residence="Польное Конобеево", comment="фамилия читается неуверенно"), bride_marriage_num=1,
                             witness1=person("Николай", "Павловъ", "Воробьевъ"),
                             witness2=person("Тимоѳей", "Ивановъ", "Свищовъ"),
                             witness3=person("Ѳеодоръ", "Васильевъ", "Черкасовъ"),
                             witness4=person("Николай", "Зотовъ", "Воробьевъ"),
                             comment="деревня у поручителей не названа; все четверо — марьинские (по жениху и по невесте); возраст невесты в корешке; венчали по разрешению епархиального начальства за №1904"),
                    marriage(6, 21, reviewed=False,
                             groom=person("Григорій", "Андреевъ", "Кузнецовъ", residence="Важная"), groom_age=18, groom_marriage_num=1,
                             bride=person("Евдокія", "Ѳеодорова", "Моисеева"), bride_age=20, bride_marriage_num=1,
                             witness1=person("Иванъ", "Андреевъ", "Кузнецовъ", residence="Важная", side=Side.GROOM, comment="«Иванъ и Алексѣй Андреевы Кузнецовы»"),
                             witness2=person("Алексѣй", "Андреевъ", "Кузнецовъ", residence="Важная", side=Side.GROOM),
                             witness3=person("Петръ", "Андреевъ", "Кузнецовъ", side=Side.BRIDE, comment="деревня не названа"),
                             witness4=person("Степанъ", "Григорьевъ", "Малютинъ", side=Side.BRIDE, comment="деревня не названа")),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_FEMALE,
        status_groom=PEASANT_MALE
    ),
)
