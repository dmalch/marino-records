from verso.ru.dsl import (EventDate, Month, WwiDocumentType, external_source_records, person,
                          wwi_record)
from verso.ru.dsl.marital_status import MARRIED

# WWI (ПМВ) participant cards from gwar.mil.ru («Памяти героев Великой войны») —
# Марьино/Эммануиловка natives (Шаморгская вол.), event year 1915.
# Both records are Василий Иванович Мыльников (b~1889, «26 лет» in 1915) — two
# separate documents for the same man (deliberate duplicates, reconciled onto his
# canonical profile in the normal consolidation second pass).
# Scans re-hosted under scans/ (Git LFS); source_url stays as the «Онлайн-просмотр» link.
marino_external_sources_1915 = external_source_records(
    "Марьино",
    wwi_record(
        person("Василий", "Ивановъ", "Мыльниковъ", residence="Марьино"),
        source_url="https://gwar.mil.ru/heroes/chelovek_donesenie15163516/",
        rank="стрелок",
        military_unit="44-й Сибирский стрелковый полк",
        casualty_reason="ранен",
        marital_status=MARRIED,
        casualty_date=EventDate(1915, Month.FEBRUARY, 17),
        place_of_casualty="д. Пщулки-Чидилсин",
        date=EventDate(1915, Month.FEBRUARY, 17),
        document_type=WwiDocumentType.CASUALTY_LISTS,
        archive="РГВИА",
        fund="16196 (Особое делопроизводство по сбору и регистрации сведений о выбывших)",
        inventory="1",
        case="802",
        page="л. 123",
        scan_file="scans/wwi_mylnikov_vasilij_1915_02.jpg",
    ),
    wwi_record(
        person("Василий", "Ивановъ", "Мыльниковъ", residence="Марьино", occupation="крестьянин"),
        source_url="https://gwar.mil.ru/heroes/chelovek_gospital21331364/",
        rank="рядовой",
        age=26,
        marital_status=MARRIED,
        military_unit="44-й Сибирский стрелковый полк",
        casualty_reason="ранен, контузия от снаряда, повреждение черепа",
        date=EventDate(1915, Month.MARCH, 4),
        document_type=WwiDocumentType.WOUNDED_NOTICE,
        archive="РГВИА",
        fund="Картотека бюро учета потерь в Первой мировой войне (офицеров и солдат)",
        archive_location="Шкаф без номера, ящик 4315-М",
        scan_file="scans/wwi_mylnikov_vasilij_1915_03.jpg",
    ),
)
