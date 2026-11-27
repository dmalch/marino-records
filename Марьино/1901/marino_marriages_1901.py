from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import (PEASANT_DAUGHTER_MAIDEN, PEASANT_FEMALE, PEASANT_MALE,
                                   UNTER_OFFICER)

# Source: ГАРО ф.627 оп.255 д.503 (Сергиевская церковь с. Эммануиловка, 1901).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
marino_marriages_1901 = marriage_records(
    "ГАРО", "627", "255", "503", "Эммануиловка", "Сергиевская", 1901,
    *marriage_month(Month.APRIL,
                    marriage(3, 8, reviewed=False,
                             groom=person("Іоаннъ", "Косьминъ", "Свищовъ"), groom_age=18, groom_marriage_num=1,
                             bride=person("Анна", "Георгіева", "Калугина"), bride_age=20, bride_marriage_num=1,
                             witness1=person("Георгій", "Косьминъ", "Свищовъ"),
                             witness2=person("Михаилъ", "Косьминъ", "Свищовъ"),
                             witness3=person("Яковъ", "Георгіевъ", "Калугинъ"),
                             witness4=person("Косма", "", "Свищовъ", status=UNTER_OFFICER, comment="отставной унтер-офицер; отчество не записано; отец жениха")),
                    marriage(4, 8,
                             groom=person("Антоний", "Георгиев", "Зрюев"), groom_age=18, groom_marriage_num=1,
                             bride=person("Анастасия", "Павлова", "Калугина"), bride_age=None,
                             witness1=person("Андрей", "Егоров", "Зрюев"),
                             witness2=person("Алексей", "Акимов", "Коржавин"),
                             witness3=person("Петр", "Иванов", "Луньков"),
                             witness4=person("Иван", "Васильев", "Морин"),
                             comment="возраст невесты не указан в источнике"),
                    marriage(6, 13, reviewed=False,
                             groom=person("Димитрій", "Стефановъ", "Черкасовъ"), groom_age=26, groom_marriage_num=1,
                             bride=person("Гликерія", "Данилова", "Енишкина"), bride_age=17, bride_marriage_num=1,
                             witness1=person("Іоаннъ", "Григорьевъ", "Воронинъ", side=Side.GROOM, comment="деревня не названа"),
                             witness2=person("Павелъ", "Петровъ", "Калугинъ"),
                             witness3=person("Василий", "", "Матюнькинъ", side=Side.BRIDE, comment="отчество и деревня не записаны"),
                             witness4=person("Косма", "", "Свищовъ", side=Side.BRIDE, comment="отчество не записано")),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_DAUGHTER_MAIDEN,
        status_groom=PEASANT_MALE
    ),
)
