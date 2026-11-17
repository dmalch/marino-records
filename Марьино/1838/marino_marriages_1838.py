from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          page, person)
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MAIDEN, PEASANT_MALE

# Source: ГАРО ф.627 оп.255 д.79 — сборник МК Шацкого уезда за 1838 г., книга № 74 Богоявленской
# церкви с. Шаморга (скачан из ЕГИС АНРО). Браки — сканы 0169–0172, лл. 227–230 карандашом.
# Read for Марьино on 2026-10-31; held as reviewed=False until the owner proofreads the scans.
# This book gives no ages. Only one wedding of the year names Марьино, and only for a surety;
# the couple and the other sureties are named without a village, i.e. are Шаморга's.
marino_marriages_1838 = marriage_records(
    "ГАРО", "627", "255", "79", "Шаморга", "Богоявленская", 1838,
    *page("228",
          *marriage_month(Month.APRIL,
                          marriage(8, 10,
                                   groom=person("Антонъ", "Григорьевъ", "Кадиковъ", residence="Шаморга", comment="фамилия прочитана неуверенно (Кадиковъ/Ходиковъ)"),
                                   groom_marriage_num=1,
                                   bride=person("Евдокія", "Григорьева", "Шляева", residence="Шаморга", comment="«съ девицею … дочерью Григорія Иванова Шляева»: имя исправлено писцом («Евдо…» на полях, зачёркнуто «…Григорьевою»), прочитано неуверенно"),
                                   bride_marriage_num=1,
                                   witness1=person("Михаилъ", "Степановъ", "Касячковъ", residence="Шаморга", side=Side.GROOM, comment="деревня не названа; фамилия прочитана неуверенно"),
                                   witness2=person("Иванъ", "Григорьевъ", "Кукушкинъ", side=Side.GROOM, comment="«деревни Марьиной тогожъ господина крестьянинъ»"),
                                   witness3=person("Михаилъ", "Ивановъ", "Курносовъ", residence="Шаморга", side=Side.BRIDE, comment="деревня не названа"),
                                   witness4=person("Василій", "Андреевъ", "Козыковъ", residence="Шаморга", side=Side.BRIDE, comment="деревня не названа; фамилия прочитана неуверенно"),
                                   comment="венчание в Фомино воскресенье (Пасха 1838 г. — 3 апреля); в этот день — № 4–11"),
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
