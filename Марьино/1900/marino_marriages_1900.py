from verso.ru.dsl import Month, RecordDefaults, marriage, marriage_month, marriage_records, person
from verso.ru.dsl.statuses import PEASANT_DAUGHTER_MAIDEN, PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.255 д.487 (Эммануиловка parish metric book, 1900).
# Parish: Сергиевская церковь с. Эммануиловка (Шацкий уезд).
# Read in full for Марьино on 2026-09-26: no other marriage names a party or surety
# with the village written (skips listed in Марьино/ARCHIVES.md).
marino_marriages_1900 = marriage_records(
    "ГАРО", "627", "255", "487", "Эммануиловка", "Сергиевская", 1900,
    *marriage_month(Month.FEBRUARY,
                    marriage(2, 6,
                             groom=person("Иоанн", "Иоаннов", "Тельгин"), groom_age=18, groom_marriage_num=1,
                             bride=person("Параскева", "Гаврилова", "Рожкова", residence="Важная"), bride_age=19,
                             witness1=person("Петр", "Филипов", "Воронкин"),
                             witness2=person("Дмитрий", "Иоакимов", "Коржавин"),
                             witness3=person("Николай", "Григорьев", "Сусляков"),
                             witness4=person("Иоанн", "Васильев", "Морин")),
                    ),
    *marriage_month(Month.APRIL,
                    marriage(8, 16,
                             groom=person("Феодор", "Максимов", "Махонин", residence="Боголюбовка"), groom_age=19, groom_marriage_num=1,
                             bride=person("Анастасия", "Тимофеева", "Калугина"), bride_age=19,
                             witness1=person("Иаков", "Феодотов", "Головачев"),
                             witness2=person("Василий", "Петров", "Калугин"),
                             witness3=person("Георгий", last_name_orig="Мыльников"),
                             witness4=person("Василий", "Никитин", "Тихомиров")),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_DAUGHTER_MAIDEN,
        status_groom=PEASANT_MALE
    ),
)
