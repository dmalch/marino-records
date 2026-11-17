from verso.ru.dsl import (Month, RecordDefaults, Relationship, Side, marriage, marriage_month,
                          marriage_records, page, person, relative)
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MAIDEN, PEASANT_MALE, WIDOW

# Source: ГАРО ф.627 оп.255 д.83 — сборник МК Шацкого уезда за 1839 г., раздел Богоявленской
# церкви с. Шаморга (скачан из ЕГИС АНРО, сканы 0160–0180). До 1860 г. Марьино — приход Шаморги.
# Листы — по карандашной (архивной) нумерации дела; чернилами книга нумерует их 23–48
# (лл. 186–190 = 24–28 чернилами). Сохранились только браки и умершие.
# Read for Марьино on 2026-10-31 (браки — сканы 0161–0165); held as reviewed=False until the
# owner proofreads the scans. Each entry names its village («Деревни Марьиной …»); an entry
# without one is Шаморга's, so only the entries naming Марьино are taken.
marino_marriages_1839 = marriage_records(
    "ГАРО", "627", "255", "83", "Шаморга", "Богоявленская", 1839,
    *page("187об-188",
          *marriage_month(Month.APRIL,
                          marriage(10, 2,
                                   groom=person("Иванъ", "Абрамовъ", "Бляховъ", comment="фамилия прочитана неуверенно: «Бляховъ» или «Бѣляковъ»"),
                                   groom_age=21, groom_marriage_num=1,
                                   bride=person("Варвара", "Козьмина", "Кирпичева"), bride_age=18, bride_marriage_num=1,
                                   relatives=[relative(person("Абрамъ", "Игнатовъ", "Бляховъ", comment="«Игнатовъ» — не «Ипатовъ»? ср. Абрамъ Ипатовъ Воронкинъ, РС 1858 двор 60"), Relationship.FATHER, "жених"),
                                              relative(person("Козьма", "Яковлевъ", "Кирпичевъ"), Relationship.FATHER, "невеста")],
                                   witness1=person("Павелъ", "Степановъ", "Кирпичевъ", side=Side.GROOM),
                                   witness2=person("Иванъ", "Ерофѣевъ", "Казенновъ", side=Side.GROOM, comment="отчество и фамилия прочитаны неуверенно"),
                                   witness3=person("Павелъ", "Яковлевъ", "Кирпичевъ", side=Side.BRIDE),
                                   witness4=person("Прохоръ", "Андреевъ", "Сѣдалкинъ", side=Side.BRIDE, comment="имя («Прохо-рій»?) и фамилия прочитаны неуверенно"),
                                   comment="венчание на Красную горку; «тойже деревни» — невеста и поручители из Марьина"),
                          ),
          ),
    *page("189об-190",
          *marriage_month(Month.SEPTEMBER,
                          marriage(13, 26,
                                   groom=person("Никита", "Васильевъ", "Енишкинъ"), groom_age=21, groom_marriage_num=1,
                                   bride=person("Ефимія", "Кондратова", "Самарова", status=WIDOW, comment="деревня не названа"),
                                   bride_age=23, bride_marriage_num=2,
                                   relatives=[relative(person("Василій", "Александровъ", "Енишкинъ"), Relationship.FATHER, "жених")],
                                   witness1=person("Спиридонъ", "Ѳедоровъ", "Енишкинъ", side=Side.GROOM),
                                   witness2=person("Матвѣй", "Ивановъ", "Бояриновъ", side=Side.GROOM, comment="написано «Баяриновъ»"),
                                   witness3=person("Яковъ", "Матвѣевъ", "Моринъ", side=Side.BRIDE, comment="деревня не названа"),
                                   witness4=person("Иванъ", "Дмитріевъ", "Кукушкинъ", side=Side.BRIDE, comment="деревня не названа")),
                          ),
          ),
    defaults=RecordDefaults(
        residence="Марьино",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_MAIDEN,
        status_groom=PEASANT_MALE,
    ),
    reviewed=False,
)
