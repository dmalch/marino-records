from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLD, DIARRHEA, OLD_AGE
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.255 д.530 (Сергиевская церковь с. Эммануиловка, 1903).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
marino_deaths_1903 = death_records(
    "ГАРО", "627", "255", "530", "Эммануиловка", "Сергиевская", 1903,
    *death_month(Month.JUNE,
                 death(3, Gender.MALE, 19, 21,
                       deceased=person("Тимофей"), age="4 мес",
                       relatives=[relative(person("Николай", "Георгиев", "Мыльников"), Relationship.FATHER)],
                       cause_of_death=DIARRHEA),
                 ),
    *death_month(Month.AUGUST,
                 death(6, Gender.MALE, 8, 10, reviewed=False,
                       deceased=person("Василій"), age=5,
                       relatives=[relative(person("Николай", "Зотовъ", "Воробьевъ"), Relationship.FATHER)]),
                 ),
    *death_month(Month.SEPTEMBER,
                 death(12, Gender.FEMALE, 12, 14, reviewed=False,
                       deceased=person("Ѳеодосія"), age=None,
                       relatives=[relative(person("Филиппъ", "Яковлевъ", "Воронкинъ"), Relationship.FATHER)],
                       cause_of_death=OLD_AGE, comment="«дѣвица»; графа возраста у корешка не видна"),
                 death(13, Gender.FEMALE, 14, 16, reviewed=False,
                       deceased=person("Матрона", "Борисова"), age=None,
                       relatives=[relative(person("Филиппъ", "Яковлевъ", "Воронкинъ"), Relationship.HUSBAND)],
                       cause_of_death=COLD, comment="графа возраста у корешка не видна"),
                 death(9, Gender.MALE, 18, 20, reviewed=False,
                       deceased=person("Алексій"), age=None,
                       relatives=[relative(person("Яковъ", "Георгіевъ", "Калугинъ"), Relationship.FATHER)],
                       comment="в графе «1 …» — единица, остальное в корешке"),
                 ),
    *death_month(Month.NOVEMBER,
                 death(11, Gender.MALE, 4, 6, reviewed=False,
                       deceased=person("Алексій"), age=3,
                       relatives=[relative(person("Андрей", "Георгіевъ", "Зрюевъ"), Relationship.FATHER)]),
                 ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
