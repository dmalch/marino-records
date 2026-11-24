from verso.ru.dsl import (EventDate, Month, WwiiDocumentType, external_source_records, person, wwii_record)

# WWII (ВОВ) участники — pamyat-naroda.ru, юбилейная картотека награждений 1985 г. (40-летие Победы).

marino_external_sources_1985 = external_source_records(
    "Марьино",
    wwii_record(
        person("Алексей", "Григорьевич", "Мыльников", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/podvig-chelovek_yubileinaya_kartoteka1512646746",
        birth_date=EventDate(1923),
        document_type=WwiiDocumentType.ANNIVERSARY_AWARD,
        award="Орден Отечественной войны II степени",
        award_number="72",
        date=EventDate(1985, Month.APRIL, 6),
        archive="ЦАМО",
        archive_location="шкаф 40, ящик 22",
    ),
    wwii_record(
        person("Василий", "Михайлович", "Коржавин", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero101122351",
        birth_date=EventDate(1927),
        rank="рядовой",
        document_type=WwiiDocumentType.ANNIVERSARY_AWARD,
        award="Орден Отечественной войны II степени",
        award_number="74",
        date=EventDate(1985, Month.APRIL, 6),
        archive="ЦАМО",
        archive_location="шкаф 28, ящик 10",
    ),
    wwii_record(
        person("Иван", "Михайлович", "Коржавин", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero101122291",
        birth_date=EventDate(1924),
        rank="рядовой",
        document_type=WwiiDocumentType.ANNIVERSARY_AWARD,
        award="Орден Отечественной войны II степени",
        award_number="74",
        draft_board="Шацким РВК Рязанской области",
        draft_date=EventDate(1942, Month.AUGUST, 28),
        date=EventDate(1985, Month.APRIL, 6),
        archive="ЦАМО",
        archive_location="шкаф 24, ящик 7",
        comment=(
            "Номер документа (74) и дата документа (06.04.1985) совпадают с записью Василия Михайловича "
            "Коржавина выше — типично для юбилейной картотеки, где один и тот же приказ/документ охватывает "
            "нескольких награждённых; расположение (шкаф/ящик) у них разное."
        ),
    ),
    # ВОВ — pamyat-naroda.ru, добавлено 18.11.2026: люди, найденные в корпусе (реестр —
    # EXTERNAL_SOURCES.md и external_sources/vov_pamyat.tsv).
    wwii_record(
        person("Иван", "Васильевич", "Зрюев", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/podvig-chelovek_yubileinaya_kartoteka1514890972/",
        reviewed=False,
        birth_date=EventDate(1914),
        document_type=WwiiDocumentType.ANNIVERSARY_AWARD,
        award="Орден Отечественной войны II степени",
        award_number="74",
        date=EventDate(1985, Month.APRIL, 6),
        archive="ЦАМО",
        archive_location="шкаф 20, ящик 16",
        comment=(
            "Место рождения на карточке: Рязанская обл., Шацкий р-н, д. Марьино. Корпус: рождение "
            "30.01.1915 (МК 1915 № 5), отец Зрюев Василий Егорович, мать Зрюева Матрона Дмитриевна."
        ),
    ),
)
