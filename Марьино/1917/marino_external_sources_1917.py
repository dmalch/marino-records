from verso.ru.dsl import (EventDate, Month, WwiDocumentType, external_source_records, person,
                          wwi_record)

# WWI (ПМВ) participant cards from gwar.mil.ru («Памяти героев Великой войны») —
# Марьино/Эммануиловка natives (Шаморгская вол.), event year 1917.
# Scans re-hosted under scans/ (Git LFS) — gwar's source_url snapshots the Incapsula
# block page, so the doc body uses the harvested scan; source_url stays as the
# «Онлайн-просмотр» link (ESC001).
marino_external_sources_1917 = external_source_records(
    "Марьино",
    wwi_record(
        person("Михаил", "Иванов", "Мыльников", residence="Марьино"),
        source_url="https://gwar.mil.ru/heroes/chelovek_gospital22325086/",
        rank="рядовой",
        military_unit="201-й пехотный Потийский полк",
        casualty_reason="не уточнено",
        date=EventDate(1917, Month.DECEMBER, 23),
        document_type=WwiDocumentType.ARRIVAL_CARD_LOWER,
        archive="РГВИА",
        fund="Картотека бюро учета потерь в Первой мировой войне (офицеров и солдат)",
        archive_location="Шкаф без номера, ящик 2378-М",
        scan_file="scans/wwi_mylnikov_mihail_1917.jpg",
    ),
    # Воронин Дмитрий Григорьев, д. Важная — «Уведомление о приёме раненого»
    # (Картотека бюро учёта потерь), событие 1917 г. Брат документированной
    # григорьевичевой сибшип Ворониных (ср. МК 1897–1914). Профиль — намеренный
    # дубль для сверки при консолидации.
    wwi_record(
        person("Дмитрій", "Григорьевъ", "Воронинъ", residence="Важная"),
        source_url="https://gwar.mil.ru/heroes/chelovek_gospital600503/",
        rank="рядовой ополчения",
        military_unit="71-й пехотный Белевский полк",
        casualty_reason="болен",
        place_of_casualty="под Двинском",
        casualty_date=EventDate(1917, Month.MARCH, 30),
        date=EventDate(1917, Month.APRIL, 16),
        document_type=WwiDocumentType.WOUNDED_NOTICE,
        archive="РГВИА",
        fund="Картотека бюро учета потерь в Первой мировой войне (офицеров и солдат)",
        archive_location="Шкаф без номера, ящик 629-В",
        scan_file="scans/wwi_voronin_dmitrij.jpg",
    ),
)
