from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import CHILDBIRTH, COLIC, DROPSY, FEVER
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, PEASANT_WIFE

# Source: ГАРО ф.627 оп.255 д.167 (Сергиевская церковь с. Эммануиловка, 1861).
# Read in full for Марьино on 2026-09-27; records added by that sweep are reviewed=False.
# The album's part 3 ends with October; no November–December burials are photographed.
marino_deaths_1861 = death_records(
    "ГАРО", "627", "255", "167", "Эммануиловка", "Сергиевская", 1861,
    *death_month(Month.FEBRUARY,
                 death(1, Gender.MALE, 19, 21,
                       deceased=person("Александръ"), age="3 мес",
                       relatives=[relative(person("Степанъ", None, "Черкасовъ", comment="отчество не записано"), Relationship.FATHER)],
                       cause_of_death=COLIC),
                 ),
    *death_month(Month.MARCH,
                 death(2, Gender.FEMALE, 3, 5,
                       deceased=person("Акилина"), age=10,
                       relatives=[relative(person("Димитрій", None, "Сеничкинъ", comment="отчество не записано, фамилия читается неуверенно"), Relationship.FATHER)],
                       cause_of_death=FEVER),
                 ),
    *death_month(Month.APRIL,
                 death(7, Gender.FEMALE, 28, 28,
                       deceased=person("Меланія", "Филипова", status=PEASANT_WIFE), age=38,
                       relatives=[relative(person("Степанъ", "Матвѣевъ", "Черкасовъ"), Relationship.HUSBAND)],
                       cause_of_death=DROPSY, comment="«отъ водяной болѣзни»"),
                 ),
    *death_month(Month.OCTOBER,
                 death(12, Gender.FEMALE, 4, 6,
                       deceased=person("Настасія", "Васильева", status=PEASANT_WIFE), age=26,
                       relatives=[relative(person("Зотъ", None, "Воробьевъ", comment="отчество не записано"), Relationship.HUSBAND)],
                       cause_of_death=CHILDBIRTH, comment="«отъ родовъ»"),
                 ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
