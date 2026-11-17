from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, HEADACHE, SCARLATINA
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Source: ГАРО ф.627 оп.255 д.315 (Сергиевская церковь с. Эммануиловка, 1885).
# Read in full for Марьино on 2026-09-27; records added by that sweep are reviewed=False.
# Part 3 was photographed on the verso pages only; a cause cut by the frame edge is
# given as far as it is visible.
marino_deaths_1885 = death_records(
    "ГАРО", "627", "255", "315", "Эммануиловка", "Сергиевская", 1885,
    *death_month(Month.FEBRUARY,
                 death(4, Gender.FEMALE, 9, 10, reviewed=False,
                       deceased=person("Александра"), age=4,
                       relatives=[relative(person("Гавріилъ", "Сергѣевъ", "Толмачевъ", comment="«Гаврила Сергѣева Толмачева»"), Relationship.FATHER)],
                       cause_of_death=SCARLATINA, comment="«отъ скорл…» — обрезано краем кадра"),
                 death(3, Gender.MALE, 18, 20, reviewed=False,
                       deceased=person("Захаръ", "Ивановъ", "Епишкинъ"), age=60,
                       cause_of_death=HEADACHE, comment="«Деревни Марьиной» — Епишкины обычно мануиловские; деревня сверена по скану"),
                 ),
    *death_month(Month.MARCH,
                 death(4, Gender.MALE, 21, 23, reviewed=False,
                       deceased=person("Никифоръ", "Уваровъ", "Мазаевъ"), age=38,
                       cause_of_death="скоропостижно, по вѣдѣнію становаго пристава"),
                 ),
    *death_month(Month.NOVEMBER,
                 death(11, Gender.FEMALE, 5, 6, reviewed=False,
                       deceased=person("Пелагія"), age=1,
                       relatives=[relative(person("Григорій", "Даниловъ", "Головачевъ"), Relationship.FATHER)],
                       cause_of_death=COLIC, comment="в графе «1…» — за единицей дыра от нитки переплёта"),
                 ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
