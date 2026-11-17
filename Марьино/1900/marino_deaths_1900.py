from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.255 д.487 (Сергиевская церковь с. Эммануиловка, 1900).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
# Part 3 was photographed on the verso pages only: the age column sits in the gutter and
# the recto with the causes of death is not in the album.
marino_deaths_1900 = death_records(
    "ГАРО", "627", "255", "487", "Эммануиловка", "Сергиевская", 1900,
    *death_month(Month.FEBRUARY,
                 death(3, Gender.FEMALE, 19, 21, reviewed=False,
                       deceased=person("Ксенія", "Димитріева"), age=None,
                       relatives=[relative(person("Стефанъ", "Матвѣевъ", "Черкасовъ"), Relationship.HUSBAND)],
                       comment="графа возраста у корешка: видна «6…», вторая цифра в тени переплёта"),
                 ),
    *death_month(Month.APRIL,
                 death(7, Gender.MALE, 20, 22, reviewed=False,
                       deceased=person("Косма", "Кириловъ", "Свищовъ"), age=59,
                       comment="«Деревни Марьиной крестьянинъ»; не отставной унтеръ-офицеръ Косма Кириловъ Свищовъ — тот поручитель в сентябре 1900 (ч. 2 №13) и в 1901 г., погребён в 1905 г. 74 лет"),
                 ),
    *death_month(Month.DECEMBER,
                 death(21, Gender.MALE, 1, 3, reviewed=False,
                       deceased=person("Павелъ"), age="1 мес",
                       relatives=[relative(person("Андрей", "Георгіевъ", "Зрюевъ"), Relationship.FATHER)],
                       comment="родился 3 ноября 1900 г. (м.№40)"),
                 ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
    ),
)
