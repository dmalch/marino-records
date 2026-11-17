from verso.ru.dsl import (EventDate, Month, WwiDocumentType, external_source_records, person,
                          wwi_record)
from verso.ru.dsl.marital_status import MARRIED

# WWI (ПМВ) participant card from gwar.mil.ru («Памяти героев Великой войны») —
# Воронин Михаил Григорьев, д. Важная (Шаморгская вол.), event year 1916. Брат
# документированной григорьевичевой сибшип Ворониных (Василий/Николай/Иван
# Григорьевичи, МК 1897–1914). Scan re-hosted under scans/ (Git LFS); source_url —
# «Онлайн-просмотр» (ESC001). Профиль — намеренный дубль для сверки при консолидации.
marino_external_sources_1916 = external_source_records(
    "Марьино",
    wwi_record(
        person("Михаилъ", "Григорьевъ", "Воронинъ", residence="Важная"),
        source_url="https://gwar.mil.ru/heroes/chelovek_donesenie12353582/",
        rank="ефрейтор",
        military_unit="306-й пехотный Мокшанский полк",
        marital_status=MARRIED,
        casualty_reason="ранен",
        place_of_casualty="д. Костюхновка; дивизионный лазарет",
        date=EventDate(1916, Month.JUNE, 21),
        document_type=WwiDocumentType.CASUALTY_LISTS,
        archive="РГВИА",
        fund="16196 (Особое делопроизводство по сбору и регистрации сведений о выбывших)",
        inventory="1",
        case="499",
        scan_file="scans/wwi_voronin_mihail.jpg",
    ),
)
