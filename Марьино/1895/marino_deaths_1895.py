from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, FEVER, OLD_AGE, SUFFOCATION
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.255 д.425 (Сергиевская церковь с. Эммануиловка, 1895).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
marino_deaths_1895 = death_records(
    "ГАРО", "627", "255", "425", "Эммануиловка", "Сергиевская", 1895,
    *death_month(Month.FEBRUARY,
                 death(5, Gender.MALE, 8, 9, reviewed=False,
                       deceased=person("Иванъ", "Ивановъ", "Калугинъ"), age=83,
                       cause_of_death=OLD_AGE),
                 ),
    *death_month(Month.MAY,
                 death(9, Gender.MALE, 17, 18,
                       deceased=person("Василий", "Иванов", "Мыльников"), age=27,
                       cause_of_death=FEVER),
                 ),
    *death_month(Month.JUNE,
                 death(9, Gender.FEMALE, 1, 3, reviewed=False,
                       deceased=person("Агрипина", "Егорова"), age=26,
                       relatives=[relative(person("Ѳеодоръ", "Васильевъ", "Моисеевъ"), Relationship.HUSBAND)],
                       cause_of_death=FEVER,
                       comment="«Горячкою»; мать Маріи (ж.№3 того же года); вдовец венчан вторым браком 9.07.1895"),
                 ),
    *death_month(Month.NOVEMBER,
                 death(13, Gender.MALE, 7, 8, reviewed=False,
                       deceased=person("Егоръ", "Ѳеодоровъ", "Телѣгинъ", comment="в книге «Телегинъ»"), age=75,
                       cause_of_death=SUFFOCATION),
                 ),
    *death_month(Month.DECEMBER,
                 death(15, Gender.MALE, 10, 11, reviewed=False,
                       deceased=person("Егоръ"), age="6 нед",
                       relatives=[relative(person("Никита", "Григорьевъ", "Потапушкинъ"), Relationship.FATHER)],
                       cause_of_death=COLIC, comment="родился 28 октября 1895 г. (м.№30)"),
                 death(10, Gender.FEMALE, 10, 11, reviewed=False,
                       deceased=person("Варвара"), age="3 дн",
                       relatives=[relative(person("Павелъ", "Зотовъ", "Воробьевъ"), Relationship.FATHER)],
                       cause_of_death=COLIC, comment="близнец, родилась 7 декабря 1895 г. (ж.№43)"),
                 ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
