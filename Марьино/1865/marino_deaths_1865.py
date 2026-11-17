from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, CONSUMPTION, HERNIA, NATURAL
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, PEASANT_WIDOW, SOLDIER_WIFE

# Source: ГАРО ф.627 оп.255 д.173 (Сергиевская церковь с. Эммануиловка, 1865).
# Read in full for Марьино on 2026-09-27; records added by that sweep are reviewed=False.
# Godparents and sureties from Марьино are written without a village; the default residence stands for them.
marino_deaths_1865 = death_records(
    "ГАРО", "627", "255", "173", "Эммануиловка", "Сергиевская", 1865,
    *death_month(Month.MARCH,
                 death(3, Gender.MALE, 15, 17,
                       deceased=person("Арефий", "Абрамов", "Мыльников"), age=63,
                       cause_of_death="от грудной боли"),
                 ),
    *death_month(Month.APRIL,
                 death(5, Gender.MALE, 8, 10,
                       deceased=person("Дмитрій"), age=12,
                       relatives=[relative(person("Иванъ", None, "Толмачевъ", comment="отчество не записано"), Relationship.FATHER)],
                       cause_of_death=CONSUMPTION),
                 ),
    *death_month(Month.MAY,
                 death(6, Gender.FEMALE, 3, 5,
                       deceased=person("Степанида", "Михайлова", "Евтякина", status=PEASANT_WIDOW), age=79,
                       cause_of_death=NATURAL),
                 death(6, Gender.MALE, 14, 16,
                       deceased=person("Герасимъ"), age=3,
                       relatives=[relative(person("Михаилъ", None, "Свищевъ", comment="отчество не записано"), Relationship.FATHER)],
                       cause_of_death=COLIC),
                 ),
    *death_month(Month.SEPTEMBER,
                 death(9, Gender.FEMALE, 15, 17,
                       deceased=person("Елисавѣта"), age="2 нед",
                       relatives=[relative(person("Иванъ", None, "Швейкинъ", comment="отчество не записано"), Relationship.FATHER)],
                       cause_of_death=HERNIA, comment="№ в книге не проставлен, 9-я по порядку женских записей"),
                 death(10, Gender.FEMALE, 18, 20,
                       deceased=person("Марія"), age="6 мес",
                       relatives=[relative(person("Зотъ", None, "Воробьевъ", comment="отчество не записано"), Relationship.FATHER)],
                       cause_of_death=COLIC, comment="№ в книге не проставлен, 10-я по порядку женских записей"),
                 ),
    *death_month(Month.NOVEMBER,
                 death(10, Gender.MALE, 25, 27,
                       deceased=person("Иванъ"), age="1 год 6 мес",
                       relatives=[relative(person("Татіана", "Меркулова", "Усадина", status=SOLDIER_WIFE), Relationship.MOTHER)],
                       cause_of_death=COLIC, comment="№ в книге не проставлен, 10-я по порядку мужских записей"),
                 ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
