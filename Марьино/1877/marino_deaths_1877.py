from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, HEADACHE, SMALLPOX
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.255 д.237 (Сергиевская церковь с. Эммануиловка, 1877).
# Read in full for Марьино on 2026-09-27; records added by that sweep are reviewed=False.
marino_deaths_1877 = death_records(
    "ГАРО", "627", "255", "237", "Эммануиловка", "Сергиевская", 1877,
    *death_month(Month.AUGUST,
                 death(11, Gender.MALE, 4, 6, reviewed=False,
                       deceased=person("Василій"), age="5 мес",
                       relatives=[relative(person("Петръ", "Ѳеодоровъ", "Телегинъ"), Relationship.FATHER)],
                       cause_of_death=COLIC, comment="родился 17 марта 1877 г. (м.№12)"),
                 death(12, Gender.FEMALE, 19, 21, reviewed=False,
                       deceased=person("Анна"), age=62,
                       relatives=[relative(person("Захаръ", "", "Епишкинъ", comment="«крестьянина Захара Епишкина» — отчество не записано"), Relationship.HUSBAND)],
                       cause_of_death="отъ боли въ желудкѣ"),
                 ),
    *death_month(Month.OCTOBER,
                 death(15, Gender.MALE, 3, 5, reviewed=False,
                       deceased=person("Ѳеодоръ", "Захаровъ", "Зрюевъ"), age=60,
                       cause_of_death="отъ венерической"),
                 ),
    *death_month(Month.NOVEMBER,
                 death(15, Gender.FEMALE, 1, 3,
                       deceased=person("Екатерина", "Иванова"), age=62,
                       relatives=[relative(person("Алексей", "Абрамов", "Мыльников"), Relationship.HUSBAND)],
                       cause_of_death=HEADACHE),
                 ),
    *death_month(Month.DECEMBER,
                 death(21, Gender.FEMALE, 13, 14, reviewed=False,
                       deceased=person("Евдокія"), age="4 мес",
                       relatives=[relative(person("Филиппъ", "Яковлевъ", "Воронкинъ"), Relationship.FATHER)],
                       cause_of_death=SMALLPOX, comment="цифра перед «мѣсяцевъ» не видна; родилась 13 августа 1877 г. (ж.№21)"),
                 ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
