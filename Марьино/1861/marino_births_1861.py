from verso.ru.dsl import Gender, Month, RecordDefaults, birth, birth_month, birth_records, person
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, PEASANT_SPOUSE, PEASANT_WIFE, SEXTON

# Source: ГАРО ф.627 оп.255 д.167 (Сергиевская церковь с. Эммануиловка, 1861).
# Read in full for Марьино on 2026-09-27; records added by that sweep are reviewed=False.
# Godparents from Марьино are written without a village; the default residence stands for them.
marino_births_1861 = birth_records(
    "ГАРО", "627", "255", "167", "Эммануиловка", "Сергиевская", 1861,
    *birth_month(Month.MARCH,
                 birth(7, Gender.MALE, 21, 22,
                       child=person("Василій"),
                       father=person("Степанъ", "Филатовъ", "Моісѣевъ"),
                       mother=person("Стефанида", "Ѳеодотова"),
                       god_parent1=person("Иванъ", "Ивановъ", residence="Мануилово", status=SEXTON),
                       god_parent2=person("Евдокія", "Климова", "Толмачева", status=PEASANT_SPOUSE)),
                 ),
    *birth_month(Month.MAY,
                 birth(9, Gender.MALE, 10, 14,
                       child=person("Михаилъ"),
                       father=person("Игнатъ", "Яковлевъ", "Воронкинъ"),
                       mother=person("Дарія", "Филипова"),
                       god_parent1=person("Зотъ", "Аникѣевъ", "Воробьевъ"),
                       god_parent2=person("Татіана", "Макарова", "Мыльникова", status=PEASANT_SPOUSE)),
                 ),
    *birth_month(Month.DECEMBER,
                 birth(18, Gender.MALE, 4, 6,
                       child=person("Николай"),
                       father=person("Антипъ", "Степановъ", "Галушкинъ"),
                       mother=person("Агафія", "Ѳедорова"),
                       god_parent1=person("Флоръ", "Григорьевъ", "Бычковъ"),
                       god_parent2=person("Анна", "Родіонова", "Телегина", status=PEASANT_SPOUSE)),
                 birth(20, Gender.MALE, 16, 17,
                       child=person("Даніилъ"),
                       father=person("Димитрій", "Григорьевъ", "Головачевъ"),
                       mother=person("Варвара", "Ѳедорова"),
                       god_parent1=person("Андрей", "Логиновъ", "Ломовъ", comment="деревня не названа"),
                       god_parent2=person("Агафья", "Васильева", "Головачева", status=PEASANT_SPOUSE)),
                 ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_mother=PEASANT_WIFE,
    ),
)
