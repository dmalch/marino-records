from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import (PEASANT_DAUGHTER_MAIDEN, PEASANT_FEMALE, PEASANT_MALE,
                                   PEASANT_WIDOW, SOLDIER)

# Source: ГАРО ф.627 оп.255 д.388 (Сергиевская церковь с. Эммануиловка, 1892).
# Read in full for Марьино on 2026-09-26; records added by that sweep are reviewed=False.
marino_marriages_1892 = marriage_records(
    "ГАРО", "627", "255", "388", "Эммануиловка", "Сергиевская", 1892,
    *marriage_month(Month.APRIL,
                    marriage(7, 12,
                             groom=person("Михаил", "Космин", "Свищев"), groom_age=18, groom_marriage_num=1,
                             bride=person("Татьяна", "Яковлева", "Рагулина", residence="Купля"), bride_age=18,
                             witness1=person("Иван", "Михайлов", "Свищев"),
                             witness2=person("Иван", "Димитриев", "Мыльников"),
                             witness3=person("Павел", "Петров", "Калугин"),
                             witness4=person("Косма", last_name_orig="Свищев", status=SOLDIER)),
                    ),
    *marriage_month(Month.OCTOBER,
                    marriage(13, 11, reviewed=False,
                             groom=person("Иванъ", "Егоровъ", "Телѣгинъ", comment="в книге «Телегинъ»; первая жена Евдокія Семенова погребена 14.08.1892"), groom_age=36, groom_marriage_num=2,
                             bride=person("Параскева", "Григорьева", "Лукина", residence="Ялтуново", status=PEASANT_WIDOW), bride_age=25, bride_marriage_num=2,
                             witness1=person("Сергій", "Яковлевъ", "Швейкинъ"),
                             witness2=person("Михаилъ", "Ефимовъ", "Воробьевъ"),
                             witness3=person("Иванъ", "Ивановъ", "Калугинъ", side=Side.BRIDE, comment="«той же деревни» — Марьиной"),
                             witness4=person("Петръ", "Ѳеодоровъ", "Телѣгинъ", side=Side.BRIDE, comment="в книге «Телегинъ»")),
                    ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_DAUGHTER_MAIDEN,
        status_groom=PEASANT_MALE
    ),
)
