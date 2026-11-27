from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import CHILDBIRTH, COLIC, OLD_AGE
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, SOLDIER, UNTER_OFFICER

# Source: ГАРО ф.627 оп.255 д.559 (Сергиевская церковь с. Эммануиловка, 1905).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
marino_deaths_1905 = death_records(
    "ГАРО", "627", "255", "559", "Эммануиловка", "Сергиевская", 1905,
    *death_month(Month.JUNE,
                 death(6, Gender.FEMALE, 6, 9, reviewed=False,
                       deceased=person("Марія"), age=11,
                       relatives=[relative(person("Ѳеодоръ", "Васильевъ", "Моисеевъ"), Relationship.FATHER)],
                       cause_of_death="утонула"),
                 death(7, Gender.FEMALE, 21, 22, reviewed=False,
                       deceased=person("Анастасія"), age=None,
                       relatives=[relative(person("Иванъ", "Косьминъ", "Свищовъ", status=SOLDIER, comment="рядовой, состоящий на действительной службе"), Relationship.FATHER)],
                       cause_of_death=COLIC, comment="в графе «2 …» — единица под дыркой переплёта; крещена 16 апреля того же года (ч. 1 ж.№10)"),
                 ),
    *death_month(Month.JULY,
                 death(3, Gender.MALE, 8, 9, reviewed=False,
                       deceased=person("Сергій"), age="5 дн",
                       relatives=[relative(person("Антонъ", "Егоровъ", "Зрюевъ"), Relationship.FATHER)],
                       cause_of_death=COLIC, comment="крещён 4 июля того же года (ч. 1 м.№16)"),
                 ),
    *death_month(Month.DECEMBER,
                 death(8, Gender.MALE, 17, 18, reviewed=False,
                       deceased=person("Косма", "Кириловъ", "Свищовъ", status=UNTER_OFFICER, comment="отставной унтер-офицер"), age=74,
                       cause_of_death=OLD_AGE,
                       comment="деревня в записи не названа; отчество в книге «Киров» (сокращено); в других годах марьинский солдат Косма Кириловъ Свищовъ; в Марьине был и тёзка-крестьянин, погребён 22.04.1900 59 лет (1900, ч. 3 м.№7), так что чей сын Егоръ, Иванъ и Михаилъ Косьмины — не установлено"),
                 death(14, Gender.FEMALE, 29, 31, reviewed=False,
                       deceased=person("Дарія", "Акимова"), age=None,
                       relatives=[relative(person("Григорій", "Петровъ", "Моисеевъ"), Relationship.HUSBAND)],
                       cause_of_death=CHILDBIRTH, comment="«отъ родовъ»; графа возраста не видна; вдовец венчан вторым браком 9.04.1906 (1906, ч. 2 №4)"),
                 ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
