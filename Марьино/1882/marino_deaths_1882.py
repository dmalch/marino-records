from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, DECREPITUDE, HEADACHE
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, PEASANT_WIDOW

# Source: ГАРО ф.627 оп.255 д.282 (Сергиевская церковь с. Эммануиловка, 1882).
# Read in full for Марьино on 2026-09-27; records added by that sweep are reviewed=False.
# Part 3 was photographed on the verso pages only; the male count restarts in March and
# jumps from 19 to 26 in December, and those numbers are kept as written.
marino_deaths_1882 = death_records(
    "ГАРО", "627", "255", "282", "Эммануиловка", "Сергиевская", 1882,
    *death_month(Month.MARCH,
                 death(7, Gender.MALE, 20, 23, reviewed=False,
                       deceased=person("Алексѣй", "Михайловъ", "Головачевъ"), age=24,
                       comment="мужской счёт в марте начат заново (5, 6, 7); причина не видна — лицевая страница закрыта вкладным листом"),
                 ),
    *death_month(Month.APRIL,
                 death(9, Gender.MALE, 21, 24, reviewed=False,
                       deceased=person("Степанъ", "Ѳеофилактовъ", "Моисеевъ"), age=None,
                       cause_of_death=DECREPITUDE, comment="в графе «7…» — вторая цифра в корешке"),
                 ),
    *death_month(Month.JULY,
                 death(13, Gender.MALE, 11, 13, reviewed=False,
                       deceased=person("Егоръ"), age=7,
                       relatives=[relative(person("Егоръ", "", "Калугинъ", comment="«крестьянина Егора Калугина» — отчество не записано"), Relationship.FATHER)],
                       comment="причина у корешка не разобрана"),
                 death(15, Gender.MALE, 26, 28, reviewed=False,
                       deceased=person("Яковъ", "Ивановъ", "Жарковъ", comment="имя у края строки читается неуверенно; в 1881 г. (рожд. м.№16) «Яковъ Ивановъ Жарковъ» — отец Семена"), age=37,
                       comment="причина «отъ при…» — «припадковъ»?"),
                 death(14, Gender.FEMALE, 1, 3,
                       deceased=person("Агриппина"), age=None,  # возраст в записи неразборчив
                       relatives=[relative(person("Иван", last_name_orig="Мыльников"), Relationship.FATHER)],
                       cause_of_death=COLIC),
                 ),
    *death_month(Month.SEPTEMBER,
                 death(15, Gender.FEMALE, 15, 18, reviewed=False,
                       deceased=person("Евфимія", "Димитріева", "Головачева", status=PEASANT_WIDOW), age=None,
                       cause_of_death=HEADACHE, comment="графа возраста у корешка не видна"),
                 ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
