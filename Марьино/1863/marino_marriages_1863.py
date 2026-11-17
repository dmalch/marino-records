from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MAIDEN, PEASANT_MALE

# Source: ГАРО ф.627 оп.255 д.171 (Сергиевская церковь с. Эммануиловка, 1863).
# Read in full for Марьино on 2026-09-27; records added by that sweep are reviewed=False.
# All seven marriages of the year are dated 7 April.
marino_marriages_1863 = marriage_records(
    "ГАРО", "627", "255", "171", "Эммануиловка", "Сергиевская", 1863,
    *marriage_month(Month.APRIL,
                    marriage(1, 7,
                             groom=person("Романъ", "Аникѣевъ", "Воробьевъ"), groom_age=21, groom_marriage_num=1,
                             bride=person("Анна", "Ѳедорова", "Лозина", residence="Мануилово"), bride_age=19, bride_marriage_num=1,
                             witness1=person("Ѳеодоръ", "Захаровъ", "Зрюевъ", status="временно-обязанный крестьянин", side=Side.GROOM),
                             witness2=person("Яковъ", "Яковлевъ", "Калугинъ", status="временно-обязанный крестьянин", side=Side.GROOM),
                             witness3=person("Павелъ", "Ильинъ", "Колдешковъ", residence="Мануилово", status="временно-обязанный крестьянин", side=Side.BRIDE),
                             witness4=person("Артемъ", "Никифоровъ", "Воронкинъ", residence="Мануилово", status="временно-обязанный крестьянин", side=Side.BRIDE)),
                    marriage(4, 7,
                             groom=person("Тимофей", "Григорьевъ", "Воробьевъ"), groom_age=19, groom_marriage_num=1,
                             bride=person("Марья", "Иванова", "Гуляева", residence="Золотая Поляна"),
                             witness1=person("Алексѣй", "Ефимовъ", "Ласевичевъ", status="временно-обязанный крестьянин", side=Side.GROOM),
                             witness2=person("Ѳлоръ", "Григорьевъ", "Бычковъ", status="временно-обязанный крестьянин", side=Side.GROOM),
                             witness3=person("Кузма", "Ивановъ", "Гуляевъ", residence="Золотая Поляна", status="временно-обязанный крестьянин", side=Side.BRIDE, comment="деревня не названа"),
                             witness4=person("Николай", "Егоровъ", "Петелинъ", side=Side.BRIDE)),
                    marriage(6, 7,
                             groom=person("Василій", "Михайловъ", "Воробьевъ"), groom_age=21, groom_marriage_num=1,
                             bride=person("Марья", "Семенова", "Горина", residence="Ржавец"), bride_age=19,
                             witness1=person("Иванъ", "Сергѣевъ", "Фокинъ", status="временно-обязанный крестьянин", side=Side.GROOM),
                             witness2=person("Михаилъ", "Федоровъ", "Головачевъ", status="временно-обязанный крестьянин", side=Side.GROOM),
                             witness3=person("Павелъ", "Ильинъ", "Колдашовъ", residence="Мануилово", status="временно-обязанный крестьянин", side=Side.BRIDE),
                             witness4=person("Александръ", "Павловъ", "Казекинъ", residence="Мануилово", status="временно-обязанный крестьянин", side=Side.BRIDE)),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_MAIDEN,
        status_groom=PEASANT_MALE,
    ),
)
