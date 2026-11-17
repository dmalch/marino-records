from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import NATURAL
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, WIDOW

# Source: ГАРО ф.627 оп.255 д.79 — сборник МК Шацкого уезда за 1838 г., книга № 74 Богоявленской
# церкви с. Шаморга (скачан из ЕГИС АНРО). Умершие — сканы 0173–0175, лл. 233–235 карандашом
# (19–21 чернилами); лл. 231–232 (17–18) в АНРО не отсканированы — часть 2 кончается на л. 230
# подписями, так что это, вероятно, чистые листы. The book writes one day per death (no burial day).
# Read for Марьино on 2026-10-31; held as reviewed=False until the owner proofreads the scans.
# Ж. №6 (21.07, «деревни Мануйловой вдова Настасья Акимова …», 67) is Эммануиловка's, not taken.
marino_deaths_1838 = death_records(
    "ГАРО", "627", "255", "79", "Шаморга", "Богоявленская", 1838,
    *page("234",
          *death_month(Month.AUGUST,
                       death(14, Gender.MALE, 5,
                             deceased=person("Ѳеодоръ"), age="4 мес",
                             relatives=[relative(person("Илья", "Денисовъ", "Калдашевъ"), Relationship.FATHER)],
                             comment="деревня не названа, но это сын, рождённый 18.04.1838 «деревни Марьиной у Ильи Денисова Калдашева» (рождения м.№26); причина («Кокотъ/лю»?) не разобрана"),
                       death(16, Gender.FEMALE, 26,
                             deceased=person("Степанида", "Григорьева", "Чулина", status=WIDOW, comment="фамилия прочитана неуверенно"),
                             age=72, cause_of_death=NATURAL,
                             comment="возраст — 72 или 74"),
                       ),
          ),
    defaults=RecordDefaults(residence="Марьино", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
    reviewed=False,
)
