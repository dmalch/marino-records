from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, DECREPITUDE, DIARRHEA, FEVER
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.255 д.350 (Сергиевская церковь с. Эммануиловка, 1888).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
marino_deaths_1888 = death_records(
    "ГАРО", "627", "255", "350", "Эммануиловка", "Сергиевская", 1888,
    *death_month(Month.MARCH,
                 death(7, Gender.MALE, 1, 2,
                       deceased=person("Пантелеймон", last_name_orig="Коржавин"), age=85,
                       cause_of_death=DECREPITUDE),
                 ),
    *death_month(Month.APRIL,
                 death(5, Gender.FEMALE, 15, 16, reviewed=False,
                       deceased=person("Марѳа", "Гаврилова"), age=22,
                       relatives=[relative(person("Николай", "Антиповъ", "Галушкинъ"), Relationship.HUSBAND)],
                       cause_of_death=FEVER, comment="«горячкою»; вторая цифра возраста у корешка; вдовец женился вторично 29 января 1889 г."),
                 death(6, Gender.FEMALE, 17, 18, reviewed=False,
                       deceased=person("Татіана"), age=1,
                       relatives=[relative(person("Иванъ", "Михайловъ", "Свищевъ"), Relationship.FATHER)],
                       cause_of_death=DIARRHEA, comment="в графе «1» без единицы"),
                 ),
    *death_month(Month.NOVEMBER,
                 death(15, Gender.FEMALE, 25, 26, reviewed=False,
                       deceased=person("Пелагія"), age="полгода",
                       relatives=[relative(person("Иванъ", "Михайловъ", "Свищевъ"), Relationship.FATHER)],
                       cause_of_death=COLIC, comment="в графе «Пол…» — слово уходит в корешок; родилась 25 апреля 1888 г. (ж.№15)"),
                 ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
