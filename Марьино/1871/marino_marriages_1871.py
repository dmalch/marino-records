from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import (PEASANT_DAUGHTER_MAIDEN, PEASANT_FEMALE, PEASANT_MALE,
                                   PROPRIETOR_PEASANT_MALE)

# Source: ГАРО ф.627 оп.255 д.195 (Сергиевская церковь с. Эммануиловка, 1871).
# Read in full for Марьино on 2026-09-27; records added by that sweep are reviewed=False.
# The album is phone photos of a screen; the godparents' column is cut off at the spine.
marino_marriages_1871 = marriage_records(
    "ГАРО", "627", "255", "195", "Эммануиловка", "Сергиевская", 1871,
    *marriage_month(Month.APRIL,
                    marriage(1, 4,
                             groom=person("Михаилъ", "Михайловъ", "Воробьевъ"), groom_marriage_num=1, groom_age=19,
                             bride=person("Марія", "Яковлева", "Воронкина"),
                             witness1=person("Иванъ", "Григорьевъ", "Швейкинъ", side=Side.GROOM),
                             witness2=person("Данилъ", "Ѳеодоровъ", "Головачевъ", side=Side.GROOM),
                             witness3=person("Филипъ", "Яковлевъ", "Воронкинъ", side=Side.BRIDE),
                             witness4=person("Алексѣй", "Абрамовъ", "Мыльниковъ", side=Side.BRIDE)),
                    marriage(6, 4,
                             groom=person("Михаилъ", "Васильевъ", "Горынинъ", residence="Мануилово", comment="фамилия читается неуверенно"), groom_age=18, groom_marriage_num=1,
                             bride=person("Параскева", "Ананіева", last_name_orig="?", residence="Жданная", comment="имя читается неуверенно, фамилия обрезана у корешка; возраст невесты обрезан"), bride_marriage_num=1,
                             witness1=person("Петръ", "Егоровъ", "Калугинъ", side=Side.GROOM),
                             witness2=person("Димитрій", "Іосифовъ", "Грабинъ", residence="Мануилово", side=Side.GROOM),
                             witness3=person("Григорій", "Степановъ", "Калугинъ", residence="Мануилово", side=Side.BRIDE),
                             witness4=person("Ѳеодоръ", "Косминъ", "Калугинъ", residence="Жданная", side=Side.BRIDE)),
                    marriage(7, 18,
                             groom=person("Егоръ", "Павловъ", "Марочкинъ", residence="Жданная"), groom_age=18, groom_marriage_num=1,
                             bride=person("Дарія", "Иванова", "Жаркова"), bride_marriage_num=1,
                             witness1=person("Семенъ", "Алексѣевъ", "Кузнецовъ", residence="Жданная", side=Side.GROOM),
                             witness2=person("Василій", "Ивановъ", "Кочетовъ", residence="Жданная", side=Side.GROOM, comment="фамилия читается неуверенно"),
                             witness3=person("Василій", "Андреевъ", "Калугинъ", residence="Жданная", side=Side.BRIDE),
                             witness4=person("Ѳеофанъ", "Барисовъ", "Жарковъ", side=Side.BRIDE),
                             comment="возраст невесты обрезан у корешка"),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_DAUGHTER_MAIDEN,
        status_groom=PROPRIETOR_PEASANT_MALE
    ),
)
