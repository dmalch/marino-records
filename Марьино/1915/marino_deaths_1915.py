from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import OLD_AGE
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, PEASANT_WIDOW

# Source: ГАРО ф.627 оп.279 д.74 (Сергиевская церковь с. Эммануиловка, 1915).
marino_deaths_1915 = death_records(
    "ГАРО", "627", "279", "74", "Эммануиловка", "Сергиевская", 1915,
    *death_month(Month.FEBRUARY,
                 death(1, Gender.FEMALE, 2, 4, reviewed=False,
                       deceased=person("Татіяна", "Андреева"), age=None,
                       relatives=[relative(person("Павелъ", "Петровъ", "Калугинъ"), Relationship.HUSBAND)],
                       comment="графа возраста на снимке пуста (сверено владельцем 26.09.2026 — не видно)"),
                 ),
    *death_month(Month.MAY,
                 death(6, Gender.MALE, 5, 7, reviewed=False,
                       deceased=person("Андрей"), age="полгода",
                       relatives=[relative(person("Степанъ", "Егоровъ", "Калугинъ"), Relationship.FATHER)]),
                 ),
    *death_month(Month.JULY,
                 death(4, Gender.FEMALE, 4, 6,
                       deceased=person("Марина", "Никифорова", "Коржавина", status=PEASANT_WIDOW), age=None,  # возраст в записи неразборчив
                       cause_of_death=OLD_AGE,
                       comment="возраст в источнике неразборчив: «8?»"),
                 death(6, Gender.FEMALE, 24, 26, reviewed=False,
                       deceased=person("Варвара"), age=None,
                       relatives=[relative(person("Иванъ", "Ивановъ", "Телѣгинъ", comment="прочтение сверено владельцем 26.09.2026 — «Телегина»; тот же Иванъ Ивановъ в других годах записан «Тельгинъ» (1900, 1908–1914) и «Тельшинъ» (1906)"), Relationship.FATHER)],
                       comment="графа возраста на снимке пуста"),
                 ),
    *death_month(Month.OCTOBER,
                 death(12, Gender.MALE, 3, 5, reviewed=False,
                       deceased=person("Тимоѳей"), age="полгода",
                       relatives=[relative(person("Николай", "Павловъ", "Калугинъ"), Relationship.FATHER)],
                       comment="в книге «½»; но Тимоѳей этой четы родился 20.01.1914 (1914 м.№3) — ему шёл второй год, а другого Тимоѳея у них в книге 1915 г. нет; возраст оставлен как в подлиннике"),
                 ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
