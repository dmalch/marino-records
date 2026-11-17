from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import PEASANT_DAUGHTER_MAIDEN, PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.255 д.436 (Сергиевская церковь с. Эммануиловка, 1896).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
# The scribe writes no village for godparents and sureties; the default residence stands
# for them, with a comment where another year names a different village.
marino_marriages_1896 = marriage_records(
    "ГАРО", "627", "255", "436", "Эммануиловка", "Сергиевская", 1896,
    *marriage_month(Month.MARCH,
                    marriage(4, 31,
                             groom=person("Николай", "Егоров", "Мыльников"), groom_age=18, groom_marriage_num=1,
                             bride=person("Стефанида", "Петрова", "Моисеева", comment="возраст невесты в записи неразборчив"),
                             witness1=person("Иван", "Михайлов", "Свищев"),
                             witness2=person("Григорий", "Феодоров", "Скотников"),
                             witness3=person("Иван", "Петров", "Моисеев"),
                             witness4=person("Феодор", "Васильев", "Моисеев")),
                    marriage(5, 31,
                             groom=person("Егор", "Иванов", "Мыльников"), groom_age=18,
                             bride=person("Татьяна", "Тимофеева", "Калугина"), bride_age=19,
                             witness1=person("Иван", "Димитриев", "Мыльников"),
                             witness2=person("Митрофан", "Андреев", "Иничков"),
                             witness3=person("Николай", "Иванов", "Сопкин"),
                             witness4=person("Яков", "Феодотов", "Оськин")),
                    marriage(6, 31, reviewed=False,
                             groom=person("Николай", "Зотовъ", "Воробьевъ"), groom_age=25, groom_marriage_num=1,
                             bride=person("Анна", "Климентова", "Кузнецова", residence="Жданная"), bride_age=24, bride_marriage_num=1,
                             witness1=person("Павелъ", "Зотовъ", "Воробьевъ"),
                             witness2=person("Яковъ", "Егоровъ", "Калугинъ"),
                             witness3=person("Ѳеодоръ", "Захаровъ", "Шустовъ", side=Side.BRIDE, comment="деревня не названа; Шустовы — важенские"),
                             witness4=person("Василій", "Петровъ", "Калугинъ", side=Side.BRIDE, comment="деревня не названа")),
                    marriage(7, 31,
                             groom=person("Алексей", "Акимов", "Каржавин"), groom_age=18, groom_marriage_num=1,
                             bride=person("Анна", "Егорова", "Зрюева"), bride_age=17,
                             witness1=person("Михаил", "Антонов", "Рышкин"),
                             witness2=person("Сергей", "Яковлев", "Швейкин"),
                             witness3=person("Василий", "Степанов", "Черкасов"),
                             witness4=person("Андрей", "Михайлов", "Головачев")),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_DAUGHTER_MAIDEN,
        status_groom=PEASANT_MALE
    ),
)
