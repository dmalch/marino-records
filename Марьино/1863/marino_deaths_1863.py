from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import CHILDBIRTH, COLIC, DIARRHEA, FEVER
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, PEASANT_WIFE

# Source: ГАРО ф.627 оп.255 д.171 (Сергиевская церковь с. Эммануиловка, 1863).
# Read in full for Марьино on 2026-09-27; records added by that sweep are reviewed=False.
marino_deaths_1863 = death_records(
    "ГАРО", "627", "255", "171", "Эммануиловка", "Сергиевская", 1863,
    *death_month(Month.JANUARY,
                 death(1, Gender.MALE, 9, 11,
                       deceased=person("Николай"), age="1 мес",
                       relatives=[relative(person("Ѳеофанъ", None, "Жарковъ", comment="отчество не записано"), Relationship.FATHER)],
                       cause_of_death=COLIC),
                 ),
    *death_month(Month.MARCH,
                 death(5, Gender.FEMALE, 5, 7,
                       deceased=person("Параскева"), age=6,
                       relatives=[relative(person("Павелъ", "Ивановъ", "Калугинъ"), Relationship.FATHER)],
                       cause_of_death=FEVER),
                 death(9, Gender.MALE, 9, 11,
                       deceased=person("Данилъ"), age=6,
                       relatives=[relative(person("Антипъ", None, "Галушкинъ", comment="отчество не записано"), Relationship.FATHER)],
                       cause_of_death=DIARRHEA),
                 ),
    *death_month(Month.DECEMBER,
                 death(21, Gender.MALE, 5, 7,
                       deceased=person("Григорій"), age="1 мес",
                       relatives=[relative(person("Козма", "Кириловъ", "Свищовъ"), Relationship.FATHER)],
                       cause_of_death=COLIC),
                 death(12, Gender.FEMALE, 15, 17,
                       deceased=person("Анна", "Антонова", status=PEASANT_WIFE), age=45,
                       relatives=[relative(person("Дмитрій", "Степановъ", "Болылевъ"), Relationship.HUSBAND)],
                       cause_of_death=CHILDBIRTH, comment="«отъ родовъ»"),
                 ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
