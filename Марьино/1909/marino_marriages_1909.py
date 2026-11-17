from verso.ru.dsl import Month, RecordDefaults, marriage, marriage_month, marriage_records, person
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.279 д.17 (Сергиевская церковь с. Эммануиловка, 1909).
marino_marriages_1909 = marriage_records(
    "ГАРО", "627", "279", "17", "Эммануиловка", "Сергиевская", 1909,
    *marriage_month(Month.APRIL,
                    marriage(3, 3,
                             groom=person("Василий", "Михайлов", "Милютин", residence="Важная"), groom_age=18, groom_marriage_num=1,
                             bride=person("Дарья", "Никифорова", "Кузина", residence="Темешево", comment="возраст в источнике «2?» — вторая цифра неразборчива"), bride_marriage_num=1,
                             witness1=person("Василий", "Григорьев", "Воронин"),
                             witness2=person("Николай", "Николаев", "Коржавин"),
                             witness3=person("Николай", "Григорьев", "Воронин"),
                             witness4=person("Иван", last_name_orig="Воронин")),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_FEMALE,
        status_groom=PEASANT_MALE
    ),
)
