from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import MESHCHANIN_FEMALE, PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.279 д.74 (Сергиевская церковь с. Эммануиловка, 1915).
marino_marriages_1915 = marriage_records(
    "ГАРО", "627", "279", "74", "Эммануиловка", "Сергиевская", 1915,
    *marriage_month(Month.MARCH,
                    marriage(1, 29, reviewed=False,
                             groom=person("Василий", "Петровъ", "Маринъ", residence="Мануилово"), groom_age=30, groom_marriage_num=2,
                             bride=person("Ксенія", "Данилова", "Головачева"), bride_age=25, bride_marriage_num=1,
                             witness1=person("Данилъ", "Петровъ", "Маринъ", residence="Мануилово", comment="деревня у поручителей не названа; ж.№21 того же года — «Села Мануилова» Данилъ Петровъ Маринъ"),
                             witness2=person("Егоръ", "Сидоровъ", "", comment="фамилия и деревня в книге не записаны"),
                             witness3=person("Романъ", "Ивановъ", "Мыльниковъ"),
                             witness4=person("Николай", "Егоровъ", "Мыльниковъ")),
                    marriage(2, 29,
                             groom=person("Феодоръ", "Сергѣевъ", "Швейкинъ"), groom_age=18, groom_marriage_num=1,
                             bride=person("Екатерина", "Димитриева", "Кузнецова", status=MESHCHANIN_FEMALE), bride_age=17, bride_marriage_num=1,
                             witness1=person("Иванъ", "Семеновъ", "Мыльниковъ"),
                             witness2=person("Семенъ", "Савельевъ", "Кухтенковъ"),
                             witness3=person("Иванъ", "Димитріевъ", "Кузнецовъ"),
                             witness4=person("Афанасій", "Никитинъ", "Зубрильчевъ")),
                    marriage(3, 29,
                             groom=person("Василий", "Иванов", "Моисеев"), groom_age=18,
                             groom_marriage_num=1,
                             bride=person("Акилина", "Васильева", "Матюнькина", residence="Краснохолм"), bride_age=None,  # возраст в записи неразборчив
                             bride_marriage_num=1,
                             witness1=person("Григорий", "Петров", "Моисеев"),
                             witness2=person("Феодор", "Васильев", "Моисеев"),
                             witness3=person("Иван", "Васильев", "Матюнькин"),
                             witness4=person("Григорий", "Николаев", "Мыльников")),
                    ),
    *marriage_month(Month.APRIL,
                    marriage(4, 5, reviewed=False,
                             groom=person("Иванъ", "Леонтьевъ", "Кузюковъ"), groom_age=18, groom_marriage_num=1,
                             bride=person("Татіяна", "Трофимова", "Носкова", residence="Большой Пролом", comment="«крестьянка села Пролома»"), bride_age=18, bride_marriage_num=1,
                             witness1=person("Тимофей", "Васильевъ", "Кузюковъ"),
                             witness2=person("Иванъ", "Петровъ", "Воронкинъ"),
                             witness3=person("Данилъ", "Леонтьевъ", "Енишкинъ", side=Side.BRIDE, comment="деревня не названа"),
                             witness4=person("Александръ", "Ивановъ", "Романовъ", side=Side.BRIDE, comment="деревня не названа (в родинах того же года — «Деревни Важной»)")),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_FEMALE,
        status_groom=PEASANT_MALE
    ),
)
