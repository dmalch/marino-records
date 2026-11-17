from verso.ru.dsl import Gender, Month, RecordDefaults, birth, birth_month, birth_records, person
from verso.ru.dsl.statuses import (DYACHOK, PEASANT_FEMALE, PEASANT_MAIDEN, PEASANT_MALE,
                                   PEASANT_SPOUSE, PEASANT_WIDOW, PEASANT_WIFE,
                                   PROPRIETOR_PEASANT_MALE, SOLDIER_WIFE)

# Source: ГАРО ф.627 оп.255 д.190 (Сергиевская церковь с. Эммануиловка, 1870).
# Read in full for Марьино on 2026-09-27; records added by that sweep are reviewed=False.
# The album is phone photos of a screen; the ink of several pages has faded (see ARCHIVES.md).
# This book writes the godparents' village; «Той же деревни» is Марьино.
marino_births_1870 = birth_records(
    "ГАРО", "627", "255", "190", "Эммануиловка", "Сергиевская", 1870,
    *birth_month(Month.JANUARY,
                 birth(5, Gender.MALE, 9, 11,
                       child=person("Иванъ"),
                       father=person("Петръ", "Степановъ", "Моисеевъ", status=PROPRIETOR_PEASANT_MALE),
                       mother=person("Агаѳія", "Михайлова"),
                       god_parent1=person("Василій", "Михайловъ", "Воробьевъ"),
                       god_parent2=person("Дарія", "Степанова", status=PEASANT_MAIDEN, comment="фамилия («М…») у надрыва листа не читается")),
                 ),
    *birth_month(Month.FEBRUARY,
                 birth(11, Gender.MALE, 11, 15,
                       child=person("Ѳеодоръ"),
                       father=person("Акимъ", "Пантелеймоновъ", "Коржевенковъ", status=PROPRIETOR_PEASANT_MALE),
                       mother=person("Марина", "Никифорова"),
                       god_parent1=person("Михаилъ", "Ѳеодоровъ", "Головачевъ"),
                       god_parent2=person("Параскева", "Петрова", "Швейкина", status=PEASANT_SPOUSE)),
                 ),
    *birth_month(Month.MARCH,
                 birth(10, Gender.FEMALE, 10, 15,
                       child=person("Дарія"),
                       father=person("Никита", "Михѣевъ", "Мазаевъ", status=PROPRIETOR_PEASANT_MALE),
                       mother=person("Евдокія", "Степанова"),
                       god_parent1=person("Косма", "Кирилловъ", "Свищевъ"),
                       god_parent2=person("Марія", "Яковлева", "Воронкина", status=PEASANT_MAIDEN)),
                 ),
    *birth_month(Month.APRIL,
                 birth(17, Gender.MALE, 28, 29,
                       child=person("Николай"),
                       father=person("Зотъ", "Аникѣевъ", "Воробьевъ", status=PROPRIETOR_PEASANT_MALE),
                       mother=person("Агрипина", "Яковлева"),
                       god_parent1=person("Иванъ", "Димитріевъ", "Куплинскій", residence="Мануилово", status=DYACHOK),
                       god_parent2=person("Мавра", "Михайлова", "Калугина", status=PEASANT_WIDOW)),
                 ),
    *birth_month(Month.DECEMBER,
                 birth(25, Gender.FEMALE, 4, 6,
                       child=person("Іуліана"),
                       father=person("Егоръ", "Ѳеодоровъ", "Калугинъ", status=PROPRIETOR_PEASANT_MALE),
                       mother=person("Стефанида", "Николаева"),
                       god_parent1=person("Павелъ", "Петровъ", "Калугинъ"),
                       god_parent2=person("Лукерья", "Андреева", "Калугина", status=SOLDIER_WIFE)),
                 ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_mother=PEASANT_WIFE
    ),
)
