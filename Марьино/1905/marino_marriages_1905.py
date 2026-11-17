from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.255 д.559 (Сергиевская церковь с. Эммануиловка, 1905).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
marino_marriages_1905 = marriage_records(
    "ГАРО", "627", "255", "559", "Эммануиловка", "Сергиевская", 1905,
    *marriage_month(Month.FEBRUARY,
                    marriage(5, 18, reviewed=False,
                             groom=person("Иванъ", "Александровъ", "Тарасовъ", residence="Важная"), groom_age=18, groom_marriage_num=1,
                             bride=person("Іуліанія", "Васильева", "Калугина"), bride_age=19, bride_marriage_num=1,
                             witness1=person("Иванъ", "Андреевъ", "Кузнецовъ", residence="Важная"),
                             witness2=person("Игнатъ", "Игнатовъ", "Дворцовъ", residence="Важная"),
                             witness3=person("Петръ", "Павловъ", "Кукушкинъ", residence="Важная", side=Side.BRIDE, comment="«Деревни Важной крестьяне» — на всех четверых"),
                             witness4=person("Петръ", "Андреевъ", "Кузнецовъ", residence="Важная", side=Side.BRIDE)),
                    ),
    *marriage_month(Month.APRIL,
                    marriage(6, 24, reviewed=False,
                             groom=person("Иванъ", "Михайловъ", "Свищовъ"), groom_age=48, groom_marriage_num=2,
                             bride=person("Татіана", "Иванова", "Косицкина", residence="Польное Конобеево", comment="фамилия читается неуверенно («Косицк…»); ср. 1913, ч. 2 №4 — Марѳа Иванова Косицкова того же села"), bride_age=35, bride_marriage_num=2,
                             witness1=person("Михаилъ", "Косьминъ", "Свищовъ"),
                             witness2=person("Павелъ", "Петровъ", "Калугинъ"),
                             witness3=person("Григорій", "Матвѣевъ", "Воронкинъ", residence="Мануилово"),
                             witness4=person("Петръ", "Павловъ", "Кукушкинъ", residence="Мануилово")),
                    marriage(7, 24, reviewed=False,
                             groom=person("Василий", "Андреевъ", "Иничковъ", residence="Важная"), groom_age=23, groom_marriage_num=1,
                             bride=person("Пелагія", "Димитріева", "Коржавина"), bride_age=18, bride_marriage_num=1,
                             witness1=person("Митрофанъ", "", "Иничковъ", residence="Важная", comment="отчество не записано"),
                             witness2=person("Николай", "", "Рожковъ", residence="Важная", comment="отчество не записано"),
                             witness3=person("Григорій", "", "Иничковъ", residence="Важная", side=Side.BRIDE, comment="отчество не записано"),
                             witness4=person("Андрей", "", "Рожковъ", residence="Важная", side=Side.BRIDE, comment="отчество не записано")),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_FEMALE,
        status_groom=PEASANT_MALE,
    ),
)
