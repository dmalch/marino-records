from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import DECREPITUDE
from verso.ru.dsl.statuses import (PEASANT_FEMALE, PEASANT_MALE, PEASANT_WIDOW,
                                   PROPRIETOR_PEASANT_MALE, SOLDIER)

# Source: ГАРО ф.627 оп.255 д.190 (Сергиевская церковь с. Эммануиловка, 1870).
# Read in full for Марьино on 2026-09-27; records added by that sweep are reviewed=False.
# The album is phone photos of a screen and the ink has faded; uncertain readings say so.
marino_deaths_1870 = death_records(
    "ГАРО", "627", "255", "190", "Эммануиловка", "Сергиевская", 1870,
    *death_month(Month.FEBRUARY,
                 death(1, Gender.FEMALE, 18, 20,
                       deceased=person("Марія", comment="имя читается неуверенно, отчество не разобрано"), age=52,
                       relatives=[relative(person("?", comment="«крестьянина собственника …» — имя мужа не разобрано (выцвело)"), Relationship.HUSBAND)],
                       comment="причина («отъ кашля»?) не разобрана"),
                 ),
    *death_month(Month.MARCH,
                 death(3, Gender.FEMALE, 20, 22,
                       deceased=person("Параскева"), age=2,
                       relatives=[relative(person("Михаилъ", "", "Воробьевъ", comment="отчество не записано"), Relationship.FATHER)],
                       comment="причина («отъ оспы»?) читается неуверенно"),
                 ),
    *death_month(Month.JUNE,
                 death(10, Gender.MALE, 19, 21,
                       deceased=person("?", "?", "Воробьевъ", status=PROPRIETOR_PEASANT_MALE, comment="имя не разобрано"), age=81,
                       cause_of_death=DECREPITUDE),
                 ),
    *death_month(Month.JULY,
                 death(13, Gender.MALE, 9, 11,
                       deceased=person("Кириллъ", "Константиновъ", "Свищевъ", status=PROPRIETOR_PEASANT_MALE, comment="отчество читается неуверенно"), age=70,
                       cause_of_death="от боли в животе", comment="возраст читается неуверенно"),
                 ),
    *death_month(Month.NOVEMBER,
                 death(16, Gender.MALE, 13, 15,
                       deceased=person("Яковъ", "?", comment="фамилия не записана; отчество читается неуверенно"), age=70,
                       cause_of_death=DECREPITUDE, comment="причина читается неуверенно"),
                 death(18, Gender.MALE, 24, 26,
                       deceased=person("Павелъ"), age="3 мес",
                       relatives=[relative(person("Яковъ", "Тимоѳеевъ", "Воробьевъ", status=SOLDIER), Relationship.FATHER)],
                       comment="причина читаются неуверенно"),
                 ),
    *death_month(Month.DECEMBER,
                 death(15, Gender.FEMALE, 7, 9,
                       deceased=person("Варвара", "Димитріева", "Воробьева", status=PEASANT_WIDOW), age=75,
                       cause_of_death=DECREPITUDE),
                 ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
