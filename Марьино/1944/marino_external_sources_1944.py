from verso.ru.dsl import (EventDate, Month, WwiiDocumentType, external_source_records, person, wwii_record)

# WWII (ВОВ) участники — pamyat-naroda.ru, событие 1944 г. (ранение, награждение).

marino_external_sources_1944 = external_source_records(
    "Марьино",
    wwii_record(
        person("Николай", "Егорович", "Мыльников", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero123010192",
        birth_date=EventDate(1901),
        rank="красноармеец",
        military_unit="62 стрелковый полк 10 стрелковой дивизии",
        casualty_reason="выбыл в эвакуационный госпиталь 1114",
        document_type=WwiiDocumentType.WOUND_CARD,
        draft_board="Шацкий РВК, Рязанская обл., Шацкий р-н",
        draft_date=EventDate(1941, Month.OCTOBER, 30),
        date=EventDate(1944, Month.JUNE, 30),
        archive="Филиал ЦАМО (военно-медицинских документов)",
        fund="Ленинградская картотека. Госпиталь 2222",
        archive_location="шкаф: Мыльников В - Назаров Г, ящик 279-03",
    ),
    wwii_record(
        person("Федор", "Васильевич", "Коржавин", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/podvig-chelovek_kartoteka1280604987",
        scan_file=[
            "scans/pamyat_033-0690155-5867_00000595.jpg",
            "scans/pamyat_033-0690155-5867_00000621.jpg",
        ],
        birth_date=EventDate(1921),
        rank="ст. сержант",
        military_unit="316 отдельный батальон связи 36 гвардейского стрелкового корпуса",
        document_type=WwiiDocumentType.AWARD_ORDER,
        award="Медаль «За боевые заслуги»",
        award_number="52/н",
        draft_board="Первомайский РВК, Московская обл., г. Москва, Первомайский р-н",
        draft_date=EventDate(1940, Month.OCTOBER),
        date=EventDate(1944, Month.JULY, 21),
        archive="ЦАМО",
        fund="33",
        inventory="690155",
        case="5867",
    ),
    # ВОВ — pamyat-naroda.ru, добавлено 18.11.2026: люди, найденные в корпусе (реестр —
    # EXTERNAL_SOURCES.md и external_sources/vov_pamyat.tsv).
    wwii_record(
        person("Николай", "Николаевич", "Воробьев", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/kld-card_ran104854913/",
        reviewed=False,
        birth_date=EventDate(1912),
        rank="сержант",
        military_unit="1247 сп 377 сд",
        casualty_reason="выбыл в госпиталь 1014",
        document_type=WwiiDocumentType.WOUND_CARD,
        date=EventDate(1944, Month.MARCH, 9),
        casualty_date=EventDate(1944, Month.MARCH, 9),
        archive="Филиал ЦАМО (военно-медицинских документов)",
        fund="Ленинградская картотека. 1943-1945 гг",
        archive_location="шкаф: Волошин Т - Гаврилков, ящик 291-32",
        comment=(
            "Госпиталь: ЭГ 1170. Место рождения на карточке: Рязанская обл., Шацкий р-н, д. Марино. "
            "Корпус: рождение 04.02.1912 (МК 1912 № 4), отец Воробьев Николай Павлович, мать Воробьева "
            "Екатерина Ивановна."
        ),
    ),
)
