from verso.ru.dsl import (EventDate, Month, WwiiDocumentType, external_source_records, person, wwii_record)

# WWII (ВОВ) участники — pamyat-naroda.ru, событие 1942 г. (выбытие/прибытие в часть, пропажа без вести).

marino_external_sources_1942 = external_source_records(
    "Марьино",
    wwii_record(
        person("Павел", "Иванович", "Мыльников", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero104040724",
        birth_date=EventDate(1904),
        rank="красноармеец",
        military_unit="14 стрелковый полк 72 стрелковой дивизии",
        document_type=WwiiDocumentType.UNIT_ROSTER,
        draft_board="Шацкий РВК, Рязанская обл., Шацкий р-н",
        draft_date=EventDate(1942),
        date=EventDate(1942),
        archive="ЦАМО",
        fund="6108",
        inventory="82737",
        case="2",
    ),
    wwii_record(
        person("Иван", "Васильевич", "Мыльников", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero123331846",
        scan_file="scans/pamyat_058-0818883-1287.jpg",
        birth_date=EventDate(1910),
        rank="рядовой",
        military_unit="31 стрелковая бригада",
        casualty_reason="убит",
        document_type=WwiiDocumentType.CASUALTY_REPORT,
        draft_board="Шацкий РВК, Рязанская обл., Шацкий р-н",
        draft_date=EventDate(1941, Month.OCTOBER, 22),
        date=EventDate(1942, Month.FEBRUARY, 4),
        archive="ЦАМО",
        fund="58",
        inventory="818883",
        case="1287",
        comment=(
            "Первичное место захоронения: Калининская обл., Великолукский р-н, д. Смоляниново. "
            "Жена: Мыльникова С. В."
        ),
    ),
    wwii_record(
        person("Николай", "Егорович", "Мыльников", residence="Марьино", occupation="колхозник"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero123010192",
        scan_file="scans/pamyat_8519-0034918с-0035_00000321.jpg",
        birth_date=EventDate(1901),
        military_unit="223 армейский запасной стрелковый полк",
        document_type=WwiiDocumentType.TRANSIT_POINT,
        draft_board="Шацкий РВК, Рязанская обл., Шацкий р-н",
        draft_date=EventDate(1942, Month.MARCH, 13),
        date=EventDate(1942, Month.MARCH, 13),
        archive="ЦАМО",
        fund="8519",
        inventory="34918с",
        case="35",
        comment=(
            "Жена по карте: «Татьяна Иакимовна?»."
        ),
    ),
    wwii_record(
        person("Павел", "Иванович", "Мыльников", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero104040724",
        scan_file="scans/pamyat_058-0018004-0152.jpg",
        birth_date=EventDate(1904),
        rank="красноармеец",
        military_unit="вф вм/с 1111 п/я 1101",
        casualty_reason="пропал без вести",
        document_type=WwiiDocumentType.CASUALTY_CLARIFICATION,
        draft_board="Шацкий РВК, Рязанская обл., Шацкий р-н",
        draft_date=EventDate(1942),
        date=EventDate(1942, Month.JUNE, 20),
        casualty_date=EventDate(1942, Month.JUNE, 20),
        archive="ЦАМО",
        fund="58",
        inventory="18004",
        case="152",
        comment=(
            "Жена: Мыльникова Александра Ивановна. "
        ),
    ),
    wwii_record(
        person("Павел", "Иванович", "Мыльников", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero104040724",
        scan_file="scans/pamyat_058-0018004-0597.jpg",
        birth_date=EventDate(1904),
        rank="красноармеец",
        casualty_reason="пропал без вести",
        document_type=WwiiDocumentType.CASUALTY_CLARIFICATION,
        draft_board="Шацкий РВК, Рязанская обл., Шацкий р-н",
        draft_date=EventDate(1942),
        date=EventDate(1942, Month.JUNE, 20),
        archive="ЦАМО",
        fund="58",
        inventory="18004",
        case="597",
        comment=(
            "Жена: Мыльникова Александра Ивановна. "
        ),
    ),
    wwii_record(
        person("Николай", "Егорович", "Мыльников", residence="Марьино", occupation="колхозник"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero123010192",
        scan_file="scans/pamyat_8519-0034918с-0058_00000039.jpg",
        birth_date=EventDate(1901),
        military_unit="223 армейский запасной стрелковый полк",
        document_type=WwiiDocumentType.TRANSIT_POINT,
        draft_board="Шацкий РВК, Рязанская обл., Шацкий р-н",
        draft_date=EventDate(1941),
        date=EventDate(1942, Month.AUGUST, 31),
        archive="ЦАМО",
        fund="8519",
        inventory="34918с",
        case="58",
        comment=(
            "Куда выбыл: 55 армия. "
            "Жена по карте: «Мыльникова Т. И.». "
        )
    ),
    wwii_record(
        person("Николай", "Егорович", "Мыльников", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero123010192",
        birth_date=EventDate(1901),
        rank="красноармеец",
        military_unit="367 отдельный инженерный батальон 16 армии, 11 гвардейской армии",
        document_type=WwiiDocumentType.UNIT_ROSTER,
        draft_board="Шелуховский РВК, Рязанская обл., Шелуховский р-н",
        draft_date=EventDate(1941, Month.OCTOBER, 30),
        date=EventDate(1942, Month.SEPTEMBER, 1),
        archive="ЦАМО",
        fund="32981",
        inventory="81020с",
        case="17",
    ),
    wwii_record(
        person("Иван", "Иванович", "Мыльников", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero104040676",
        scan_file="scans/pamyat_058-0977520-0404.jpg",
        birth_date=EventDate(1909),
        rank="рядовой",
        military_unit="5 рота 2 бат. 1156 стрелковый полк 344 стрелковой дивизии",
        casualty_reason="пропал без вести",
        document_type=WwiiDocumentType.CASUALTY_REPORT,
        draft_board="Шацкий РВК, Рязанская обл., Шацкий р-н",
        draft_date=EventDate(1941, Month.NOVEMBER, 18),
        casualty_date=EventDate(1942, Month.JANUARY),
        archive="ЦАМО",
        fund="58",
        inventory="977520",
        case="404",
        comment=(
            "Жена: Мыльникова Анна Андреевна. "
        ),
    ),
    wwii_record(
        person("Михаил", "Алексеевич", "Коржавин", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_vpp1992178347",
        scan_file="scans/pamyat_8502-0267373-0114.jpg",
        birth_date=EventDate(1900),
        rank="красноармеец",
        military_unit="206 фронтовой запасной стрелковый полк",
        document_type=WwiiDocumentType.TRANSIT_POINT,
        draft_date=EventDate(1941, Month.SEPTEMBER, 9),
        date=EventDate(1942, Month.MARCH, 12),
        archive="ЦАМО",
        fund="8502",
        inventory="267373",
        case="114",
        comment=(
            "Куда выбыл: 1 отдельная рота медусиления."
        ),
    ),
    wwii_record(
        person("Михаил", "Алексеевич", "Коржавин", residence="Марьино", occupation="чернорабочий"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_vpp1992178347",
        scan_file="scans/pamyat_8502-0267373-0019.jpg",
        birth_date=EventDate(1900),
        rank="рядовой",
        military_unit="206 фронтовой запасной стрелковый полк",
        document_type=WwiiDocumentType.TRANSIT_POINT,
        date=EventDate(1942, Month.MARCH, 9),
        archive="ЦАМО",
        fund="8502",
        inventory="267373",
        case="19",
        comment=(
            "Откуда прибыл: эвакуационный госпиталь 3009. "
        ),
    ),
    wwii_record(
        person("Федор", "Васильевич", "Коржавин", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_vpp2005750392",
        birth_date=EventDate(1921),
        rank="сержант",
        military_unit="48 озттбс",
        document_type=WwiiDocumentType.TRANSIT_POINT,
        draft_board="Первомайский РВК, Московская обл., г. Москва, Первомайский р-н",
        draft_date=EventDate(1940, Month.MAY),
        date=EventDate(1942, Month.DECEMBER, 3),
        archive="ЦАМО",
        fund="48 ЗТТБС",
        inventory="410183с",
        case="3",
    ),
    # ВОВ — pamyat-naroda.ru, добавлено 18.11.2026: люди, найденные в корпусе (реестр —
    # EXTERNAL_SOURCES.md и external_sources/vov_pamyat.tsv).
    wwii_record(
        person("Василий", "Иванович", "Головачев", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_donesenie51544145/",
        reviewed=False,
        scan_file="scans/pamyat_058-0818883-1008_00000184.jpg",
        birth_date=EventDate(1907),
        rank="красноармеец",
        military_unit="115 осбр",
        casualty_reason="пропал без вести",
        document_type=WwiiDocumentType.CASUALTY_REPORT,
        draft_board="Шацкий РВК, Рязанская обл., Шацкий р-н",
        date=EventDate(1942, Month.SEPTEMBER, 14),
        casualty_date=EventDate(1942, Month.SEPTEMBER, 14),
        archive="ЦАМО",
        fund="58",
        inventory="818883",
        case="1008",
        comment=(
            "На скане (Именной список безвозвратных потерь начальствующего и рядового состава (форма № 2; "
            "полк, дивизия и даты в шапке не заполнены), лист 94(?), № строки 30): Головачев Василий "
            "Иванович, красноармеец, стрелок, б/п, уроженец Рязанская обл. Шацкий р-н д. Марьено(?), 1907 "
            "г.р.; призван Шацким РВК Рязанской обл.; «тоже» (т.е. пропал без вести в бою под дер. "
            "Городище Городищенского р-на Сталинградской обл.) 14.09.42. Родные: Рязанская обл. Шацкий "
            "р-н, дер. Марьено(?), мать Головачева Анастасия Григорьевна. Место рождения на карточке: "
            "Рязанская обл., Шацкий р-н, д. Марьино. Корпус: рождение 30.12.1906 (МК 1906 № 27), отец "
            "Головачев Иван Даниилович, мать Головачева Анастасия Григорьевна."
        ),
    ),
    wwii_record(
        person("Василий", "Васильевич", "Калугин", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/kld-card_ran88252805/",
        reviewed=False,
        birth_date=EventDate(1903),
        rank="красноармеец",
        military_unit="106 сп",
        document_type=WwiiDocumentType.WOUND_CARD,
        archive="Филиал ЦАМО (военно-медицинских документов)",
        fund="Картотека общего учета",
        archive_location="шкаф: Калубов - Калугин Ив Зах, ящик 111-09",
        comment=(
            "Документ без даты; файл 1942 г. — по другому документу того же человека. Госпиталь: ЭГ 4634. "
            "Место рождения на карточке: Рязанская обл., Шацкий р-н, д. Марьино. Корпус: рождение "
            "01.01.1903 (МК 1903 № 1), отец Калугин Василий Васильевич, мать Калугина Татьяна Андреевна."
        ),
    ),
    wwii_record(
        person("Василий", "Васильевич", "Калугин", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/kld-card_ran88252841/",
        reviewed=False,
        birth_date=EventDate(1903),
        rank="красноармеец",
        military_unit="1106 сп 331 сд",
        casualty_reason="выбыл из госпиталя",
        document_type=WwiiDocumentType.WOUND_CARD,
        date=EventDate(1942, Month.AUGUST, 27),
        casualty_date=EventDate(1942, Month.AUGUST, 27),
        archive="Филиал ЦАМО (военно-медицинских документов)",
        fund="Картотека общего учета",
        archive_location="шкаф: Калубов - Калугин Ив Зах, ящик 111-09",
        comment=(
            "Госпиталь: ЭГ 4634. Место рождения на карточке: Рязанская обл., Шацкий р-н, д. Марьино. "
            "Корпус: рождение 01.01.1903 (МК 1903 № 1), отец Калугин Василий Васильевич, мать Калугина "
            "Татьяна Андреевна."
        ),
    ),
    wwii_record(
        person("Павел", "Иванович", "Мыльников", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/isp-chelovek_spisok3100410/",
        reviewed=False,
        birth_date=EventDate(1904),
        rank="красноармеец",
        military_unit="14 сп 72 сд",
        document_type=WwiiDocumentType.UNIT_ROSTER,
        draft_board="Шацкий РВК, Рязанская обл., Шацкий р-н",
        draft_date=EventDate(1942),
        date=EventDate(1942),
        archive="ЦАМО",
        fund="6108",
        inventory="82737",
        case="2",
        comment=(
            "Дата — призыва. Место рождения на карточке: Рязанская обл., Шацкий р-н, д. Марьино. Корпус: "
            "рождение 06.11.1904 (МК 1904 № 18), отец Мыльников Иван Семенович, мать Мыльникова "
            "Александра Сергеевна."
        ),
    ),
)
