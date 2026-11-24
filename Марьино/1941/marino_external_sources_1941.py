from verso.ru.dsl import (EventDate, Month, WwiiDocumentType, external_source_records, person, wwii_record)
from verso.ru.dsl.marital_status import MARRIED

# WWII (ВОВ) участники — pamyat-naroda.ru, событие 1941 г. (призыв / выбытие / пленение).
# Марьино/Эммануиловка natives (Шацкий/Конобеевский р-ны Рязанской обл.).

marino_external_sources_1941 = external_source_records(
    "Марьино",
    wwii_record(
        person("Николай", "Егорович", "Мыльников", residence="Марьино", occupation="колхозник"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero123010192",
        scan_file="scans/pamyat_8519-0034918с-0077_00000246.jpg",
        birth_date=EventDate(1901),
        marital_status=MARRIED,
        military_unit="223 армейский запасной стрелковый полк",
        document_type=WwiiDocumentType.TRANSIT_POINT,
        draft_board="Шацкий РВК, Рязанская обл., Шацкий р-н",
        draft_date=EventDate(1941),
        date=EventDate(1941),
        archive="ЦАМО",
        fund="8519",
        inventory="34918с",
        case="77",
        comment=(
            "Откуда прибыл: 15 батальон выздоравливающих. "
            "Жена: Мыльникова Т. И. "
        ),
    ),
    wwii_record(
        person("Георгий", "Георгиевич", "Мыльников", residence="Марьино", occupation="вет. фельдшер"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero98989338",
        scan_file="scans/pamyat_8279-0692513-0049.jpg",
        birth_date=EventDate(1909),
        rank="ветфельдшер полка",
        military_unit="94 кп (кавалерийский полк) 6 кубано-терская казачья дивизия",
        casualty_reason="попал в плен",
        document_type=WwiiDocumentType.POW_CARD,
        place_of_casualty="д. Мелехово, Смоленская обл.",
        draft_board="Шацкий РВК, Рязанская обл., Шацкий р-н",
        casualty_date=EventDate(1941, Month.AUGUST, 16),
        archive="ЦАМО",
        fund="8279",
        inventory="692513",
        case="49",
        comment=(
            "Занимаемая должность: ветфельдшер полка. "
            "Военно-пересыльный пункт (до плена): 7 зсп (запасной стрелковый полк). "
            "Образование: 6 кл. "
            "В плену: 16.08.1941 — 19.09.1942 по пересыльным пунктам и лагерям; "
            "19.09.1942 — 12.11.1942 раб. ком в г. Цвикау и лазарет; "
            "12.11.1942 — 09.07.1943 раб. ком бумажная фабрика г. Цвикау; "
            "09.07.1943 — 19.08.1944 раб. ком д. Фридрихгрюц; "
            "19.08.1944 — 17.04.1945 раб. ком аккумуляторная фабрика г. Цвикау. "
            "Отец: Мыльников Георгий Иванович. "
            "Мать: Мыльникова Татьяна Тимофеевна. "
        ),
    ),
    wwii_record(
        person("Василий", "Алексеевич", "Коржавин", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero101122104",
        scan_file="scans/pamyat_058-0018004-0152.jpg",
        rank="красноармеец",
        military_unit="914 стрелковый полк 246 стрелковой дивизии 2 бат 6 рота",
        marital_status=MARRIED,
        casualty_reason="пропал без вести",
        document_type=WwiiDocumentType.CASUALTY_CLARIFICATION,
        draft_board="Шацкий РВК, Рязанская обл., Шацкий р-н",
        draft_date=EventDate(1941),
        casualty_date=EventDate(1941, Month.DECEMBER),
        archive="ЦАМО",
        fund="58",
        inventory="18004",
        case="152",
        comment=(
            "Жена: Коржавина Екатерина Алексеевна. "
        ),
    ),
    wwii_record(
        person("Василий", "Алексеевич", "Коржавин", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero101122104",
        scan_file="scans/pamyat_058-0018004-0597.jpg",
        birth_date=EventDate(1898),
        rank="красноармеец",
        military_unit="914 стрелковый полк 246 стрелковой дивизии 2 бат 6 рота",
        marital_status=MARRIED,
        casualty_reason="пропал без вести",
        document_type=WwiiDocumentType.CASUALTY_CLARIFICATION,
        draft_board="Шацкий РВК, Рязанская обл., Шацкий р-н",
        draft_date=EventDate(1941, Month.OCTOBER, 30),
        date=EventDate(1941, Month.DECEMBER),
        archive="ЦАМО",
        fund="58",
        inventory="18004",
        case="597",
        comment=(
            "Жена: Коржавина Екатерина Алексеевна. "
        ),
    ),
    # ВОВ — pamyat-naroda.ru, добавлено 18.11.2026: люди, найденные в корпусе (реестр —
    # EXTERNAL_SOURCES.md и external_sources/vov_pamyat.tsv).
    wwii_record(
        person("Яков", "Николаевич", "Калугин", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/isp-chelovek_spisok14776101/",
        reviewed=False,
        birth_date=EventDate(1911),
        military_unit="10 оуап",
        document_type=WwiiDocumentType.UNIT_ROSTER,
        draft_date=EventDate(1941, Month.JUNE, 23),
        date=EventDate(1941, Month.JUNE, 23),
        archive="ЦАМО",
        fund="25041",
        inventory="426314с",
        case="1",
        comment=(
            "Дата — призыва. Место рождения на карточке: Рязанская обл., Шацкий р-н, д. Марьино. Корпус: "
            "рождение 01.03.1911 (МК 1911 № 8), отец Калугин Николай Павлович, мать Калугина Евдокия "
            "Михайловна."
        ),
    ),
    wwii_record(
        person("Яков", "Николаевич", "Калугин", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/isp-chelovek_spisok14055346/",
        reviewed=False,
        birth_date=EventDate(1911),
        military_unit="10 оуап",
        document_type=WwiiDocumentType.UNIT_ROSTER,
        draft_date=EventDate(1941, Month.JUNE, 26),
        date=EventDate(1941, Month.JUNE, 26),
        archive="ЦАМО",
        fund="25041",
        inventory="426314с",
        case="4",
        comment=(
            "Дата — призыва. Место рождения на карточке: Рязанская обл., Шацкий р-н, Маринский с/с, д. "
            "Марино. Корпус: рождение 01.03.1911 (МК 1911 № 8), отец Калугин Николай Павлович, мать "
            "Калугина Евдокия Михайловна."
        ),
    ),
)
