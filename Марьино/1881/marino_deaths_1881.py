from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import DECREPITUDE
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, SOLDIER

# Source: ГАРО ф.627 оп.255 д.272 (Сергиевская церковь с. Эммануиловка, 1881).
# Read in full for Марьино on 2026-09-27; records added by that sweep are reviewed=False.
# Part 3 was photographed on the verso pages only; a cause cut by the frame edge is
# given as far as it is visible.
marino_deaths_1881 = death_records(
    "ГАРО", "627", "255", "272", "Эммануиловка", "Сергиевская", 1881,
    *death_month(Month.AUGUST,
                 death(8, Gender.MALE, 1, 3, reviewed=False,
                       deceased=person("Прокопій", "Андреевъ", "Овсянкинъ"), age=100,
                       cause_of_death=DECREPITUDE),
                 ),
    *death_month(Month.SEPTEMBER,
                 death(6, Gender.FEMALE, 11, 13, reviewed=False,
                       deceased=person("Анна", comment="«дѣвицы Ксеніи Овсянкиной дочь»; крещена 8 сентября 1881 г. (ж.№21)"), age="3 дн",
                       relatives=[relative(person("Ксенія", "", "Овсянкина", comment="«дѣвица»"), Relationship.MOTHER)],
                       comment="причина «не доно…» — обрезано краем кадра"),
                 ),
    *death_month(Month.NOVEMBER,
                 death(12, Gender.FEMALE, 1, 3, reviewed=False,
                       deceased=person("Анна", comment="имя сверено владельцем 27.09.2026"), age=None,
                       relatives=[relative(person("Максимъ", "", "Швейкинъ", status=SOLDIER, comment="«солдата Максима Швейкина» — отчество не записано"), Relationship.FATHER)],
                       comment="возраст «1…» у корешка не разобран; причина «отъ сибир…»"),
                 death(13, Gender.FEMALE, 10, 13, reviewed=False,
                       deceased=person("Анна", "Степанова"), age=65,
                       relatives=[relative(person("Иванъ", "", "Овсянкинъ", comment="«крестьянина Ивана Овсянкина» — отчество не записано"), Relationship.HUSBAND)],
                       comment="причина у корешка не разобрана"),
                 ),
    *death_month(Month.DECEMBER,
                 death(12, Gender.MALE, 14, 17, reviewed=False,
                       deceased=person("Григорій", "Мамонтовъ", "Бычковъ"), age=80,
                       cause_of_death=DECREPITUDE),
                 ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
