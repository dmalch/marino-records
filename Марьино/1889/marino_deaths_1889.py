from verso.ru.dsl import Gender, Month, RecordDefaults, death, death_month, death_records, person
from verso.ru.dsl.causes_of_death import OLD_AGE
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, RETIRED_SOLDIER

# Source: ГАРО ф.627 оп.255 д.359 (Сергиевская церковь с. Эммануиловка, 1889).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
marino_deaths_1889 = death_records(
    "ГАРО", "627", "255", "359", "Эммануиловка", "Сергиевская", 1889,
    *death_month(Month.OCTOBER,
                 death(13, Gender.MALE, 20, 21, reviewed=False,
                       deceased=person("Алексѣй", "", "Барановъ", comment="«Деревни Марьиной Алексѣй Барановъ»: отчество не записано; первая буква фамилии похожа на строчное «в» — возможно «Варановъ»"),
                       age=78, cause_of_death=OLD_AGE),
                 ),
    *death_month(Month.NOVEMBER,
                 death(16, Gender.MALE, 29, 30, reviewed=False,
                       deceased=person("Василій", "Ивановъ", "Гуляевъ", status=RETIRED_SOLDIER),
                       age=49, cause_of_death="отъ рака"),
                 ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
    ),
)
