from verso.ru.dsl import (EventDate, Month, WwiiDocumentType, external_source_records, person,
                          wwii_record)

# WWII (ВОВ) участники — pamyat-naroda.ru, юбилейная картотека награждений 1986 г.

marino_external_sources_1986 = external_source_records(
    "Марьино",
    wwii_record(
        person("Александр", "Михайлович", "Коржавин", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero99964365",
        birth_date=EventDate(1920, Month.JANUARY, 19),
        rank="старшина",
        document_type=WwiiDocumentType.ANNIVERSARY_AWARD,
        award="Орден Отечественной войны II степени",
        award_number="46",
        draft_board="Шацким РВК Рязанской области",
        draft_date=EventDate(1941, Month.JUNE, 22),
        date=EventDate(1986, Month.AUGUST, 1),
        archive="ЦАМО",
        archive_location="шкаф 28, ящик 10",
    ),
)
