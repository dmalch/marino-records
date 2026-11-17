from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.279 д.8 (Сергиевская церковь с. Эммануиловка, 1908).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
marino_marriages_1908 = marriage_records(
    "ГАРО", "627", "279", "8", "Эммануиловка", "Сергиевская", 1908,
    *marriage_month(Month.FEBRUARY,
                    marriage(6, 11, reviewed=False,
                             groom=person("Даніилъ", "Николаевъ", "Оськинъ", residence="Важная", comment="«Даніилъ /по крестному отцу/ Николаевъ»"), groom_age=20, groom_marriage_num=1,
                             bride=person("Параскева", "Сергѣева", "Швейкина"), bride_age=17, bride_marriage_num=1,
                             witness1=person("Николай", "Андреевъ", "Спицынъ", side=Side.GROOM, comment="деревня не названа"),
                             witness2=person("Андрей", "Яковлевъ", "Оськинъ", side=Side.GROOM, comment="деревня не названа"),
                             witness3=person("Иванъ", "", "Оськинъ", side=Side.BRIDE, comment="отчество не записано"),
                             witness4=person("Яковъ", "", "Оськинъ", side=Side.BRIDE, comment="отчество не записано")),
                    ),
    *marriage_month(Month.APRIL,
                    marriage(11, 20,
                             groom=person("Гавриил", "Димитриев", "Коржавин"), groom_age=18, groom_marriage_num=1,
                             bride=person("Варвара", "Николаева", "Суслякова", residence="Николаевка"), bride_age=19, bride_marriage_num=1,
                             witness1=person("Алексей", last_name_orig="Коржавин"),
                             witness2=person("Алексей", last_name_orig="Головачев"),
                             witness3=person("Иван", last_name_orig="Телегин"),
                             witness4=person("Василий", last_name_orig="Пенчиков")),
                    ),
    *marriage_month(Month.JUNE,
                    marriage(12, 6, reviewed=False,
                             groom=person("Ѳеодоръ", "Никифоровъ", "Мазаевъ"), groom_age=25, groom_marriage_num=1,
                             bride=person("Ѳеодосія", "Иванова", "Бирючкова", residence="Важная"), bride_age=20, bride_marriage_num=1,
                             witness1=person("Иванъ", "Никифоровъ", "Мазаевъ", side=Side.GROOM, comment="в погребении 1911 г. (м.№1) — «Иванъ Никитинъ Мазаевъ»"),
                             witness2=person("Тимоѳей", "", "Бирючковъ", side=Side.GROOM, comment="отчество не записано"),
                             witness3=person("Ѳеодоръ", "Ивановъ", "Бирючковъ", side=Side.BRIDE, comment="деревня не названа"),
                             witness4=person("Василий", "Михайловъ", "Хохловъ", side=Side.BRIDE, comment="фамилия читается неуверенно")),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_FEMALE,
        status_groom=PEASANT_MALE
    ),
)
