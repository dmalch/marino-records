from verso.ru.dsl import (EventDate, Month, WwiiDocumentType, external_source_records, person, wwii_record)
from verso.ru.dsl.marital_status import MARRIED

# WWII (ВОВ) участники — pamyat-naroda.ru, событие 1943 г. (ранения, безвозвратные потери, пересыльные пункты).

marino_external_sources_1943 = external_source_records(
    "Марьино",
    wwii_record(
        person("Григорий", "Васильевич", "Мыльников", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero104040550",
        scan_file="scans/pamyat_058-0018001-1163.jpg",
        birth_date=EventDate(1908),
        rank="ст. сержант",
        military_unit="106 стрелковая бригада 228 стрелковая дивизия",
        casualty_reason="убит",
        document_type=WwiiDocumentType.CASUALTY_REPORT,
        draft_board="Шацкий РВК, Рязанская обл., Шацкий р-н",
        date=EventDate(1943, Month.JANUARY, 2),
        archive="ЦАМО",
        fund="58",
        inventory="18001",
        case="1163",
        comment=(
            "Должность: помощник командира взвода. "
            "Воевал в составе 106 стрелковой бригаде, 228 стрелковой дивизии в городах :Тула, Орел, Воронеж, Россошь. "
            "Место захоронения: Украинская ССР, Ворошиловградская обл., Меловский р-н, д. Ново-Никольское, с/з "
            "Жена: Мыльникова Екатерина Павловна."
        ),
    ),
    wwii_record(
        person("Григорий", "Васильевич", "Мыльников", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero104040550",
        scan_file="scans/pamyat_058-0018002-0075.jpg",
        birth_date=EventDate(1908),
        rank="ст. сержант",
        military_unit="106 стрелковая бригада 228 стрелковая дивизия",
        casualty_reason="убит",
        document_type=WwiiDocumentType.CASUALTY_REPORT,
        date=EventDate(1943, Month.JANUARY, 2),
        archive="ЦАМО",
        fund="58",
        inventory="18002",
        case="75",
        comment=(
            "Копия №2 того же донесения о безвозвратных потерях в другом деле. "
            "Должность: помощник командира взвода. Место захоронения: Украинская ССР, "
            "Ворошиловградская обл., Меловский р-н, д. Ново-Никольское, с/з Копани."
        ),
    ),
    wwii_record(
        person("Григорий", "Васильевич", "Мыльников", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero104040550",
        scan_file="scans/pamyat_1504-0000002-0009.jpg",
        birth_date=EventDate(1908),
        rank="ст. сержант",
        military_unit="106 стрелковая бригада 228 стрелковая дивизия",
        casualty_reason="убит",
        document_type=WwiiDocumentType.CASUALTY_REPORT,
        date=EventDate(1943, Month.JANUARY, 2),
        archive="ЦАМО",
        fund="1504",
        inventory="2",
        case="9",
        comment=(
            "Копия №3 того же донесения о безвозвратных потерях в другом деле. "
            "Должность: помощник командира взвода. Место захоронения: Украинская ССР, "
            "Ворошиловградская обл., Меловский р-н, д. Ново-Никольское, с/з Копани."
        ),
    ),
    wwii_record(
        person("Николай", "Егорович", "Мыльников", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero123010192",
        birth_date=EventDate(1901),
        rank="красноармеец",
        military_unit="223 армейский запасной стрелковый полк",
        document_type=WwiiDocumentType.TRANSIT_POINT,
        draft_board="Шавринский РВК",
        draft_date=EventDate(1941),
        date=EventDate(1943, Month.JANUARY, 24),
        archive="ЦАМО",
        fund="8519",
        inventory="34919с",
        case="7",
    ),
    wwii_record(
        person("Николай", "Егорович", "Мыльников", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero123010192",
        birth_date=EventDate(1901),
        rank="красноармеец",
        military_unit="223 армейский запасной стрелковый полк",
        casualty_reason="выбыл в госпиталь 1012",
        document_type=WwiiDocumentType.WOUND_CARD,
        draft_board="Шацкий РВК, Рязанская обл., Шацкий р-н",
        date=EventDate(1943, Month.FEBRUARY, 5),
        archive="Филиал ЦАМО (военно-медицинских документов)",
        fund="Ленинградская картотека. 1943-1945 гг",
        archive_location="Мурзаахметов А - Мячков З, 289-41",
    ),
    wwii_record(
        person("Николай", "Егорович", "Мыльников", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero123010192",
        rank="красноармеец",
        military_unit="223 армейский запасной стрелковый полк",
        casualty_reason="эвакуирован в тыл",
        document_type=WwiiDocumentType.WOUND_CARD,
        date=EventDate(1943, Month.FEBRUARY, 11),
        archive="Филиал ЦАМО (военно-медицинских документов)",
        fund="Ленинградская картотека. 1941-1942 гг",
        archive_location="шкаф: Муценек - Мягков Е, ящик 263-28",
        comment=(
            "Госпиталь по карте: госпиталь для легкораненых 2583. Карточка без даты рождения/места "
            "рождения/призыва."
        ),
    ),
    wwii_record(
        person("Николай", "Егорович", "Мыльников", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero123010192",
        scan_file="scans/pamyat_078-0530762-043067.jpg",
        birth_date=EventDate(1901),
        rank="красноармеец",
        military_unit="223 армейский запасной стрелковый полк",
        marital_status=MARRIED,
        document_type=WwiiDocumentType.TRANSIT_POINT,
        draft_board="Шацкий РВК, Рязанская обл., Шацкий р-н",
        date=EventDate(1943, Month.MARCH, 29),
        archive="ЦАМО",
        fund="Ленинградский ВПП",
        inventory="530762",
        case="43067",
        comment=(
            "Пункт: Ленинградский военно-пересыльный пункт, г. Ленинград. "
            "Куда выбыл: 36 армия. "
            "Откуда прибыл: 9 отдельный батальон выздоравливающих. "
            "Номер команды: 4/570. "
            "Образование: 3 класса."
        ),
    ),
    wwii_record(
        person("Николай", "Егорович", "Мыльников", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero123010192",
        birth_date=EventDate(1901),
        rank="красноармеец",
        military_unit="62 стрелковый полк 10 стрелковой дивизии",
        document_type=WwiiDocumentType.UNIT_ROSTER,
        draft_board="Шацкий РВК, Рязанская обл., Шацкий р-н",
        draft_date=EventDate(1941, Month.OCTOBER, 1),
        date=EventDate(1943, Month.MAY, 9),
        archive="ЦАМО",
        fund="6288",
        inventory="113944с",
        case="4",
    ),
    wwii_record(
        person("Михаил", "Алексеевич", "Коржавин", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero103187820",
        scan_file="scans/pamyat_058-0018001-0047.jpg",
        rank="красноармеец",
        military_unit="351 отдельный пулеметный артиллерийский батальон",
        casualty_reason="умер от ран",
        document_type=WwiiDocumentType.CASUALTY_REPORT,
        draft_board="Шацкий РВК, Рязанская обл., Шацкий р-н",
        date=EventDate(1943, Month.FEBRUARY, 3),
        archive="ЦАМО",
        fund="58",
        inventory="18001",
        case="47",
        comment=(
            "Поступил по ранению: 01.02.1943. "
            "Место захоронения: Ленинградская обл., Валдайский р-н, Русско-Новиковский с/с, с. Русские Новики, "
            "братское кладбище, захоронение №89587024. "
            "Жена: Коржавина Д. П."
        ),
    ),
    # ВОВ — pamyat-naroda.ru, добавлено 18.11.2026: люди, найденные в корпусе (реестр —
    # EXTERNAL_SOURCES.md и external_sources/vov_pamyat.tsv).
    wwii_record(
        person("Александр", "Федорович", "Моисеев", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_donesenie1164576666/",
        reviewed=False,
        scan_file="scans/pamyat_058-0018001-0623_00000121.jpg",
        birth_date=EventDate(1900),
        rank="красноармеец",
        military_unit="396 сп 135 сд",
        casualty_reason="убит",
        document_type=WwiiDocumentType.CASUALTY_REPORT,
        date=EventDate(1943, Month.JULY, 30),
        casualty_date=EventDate(1943, Month.JULY, 30),
        archive="ЦАМО",
        fund="1358",
        inventory="2",
        case="21",
        comment=(
            "На скане (Именной список безвозвратных потерь сержантского и рядового состава 396 стр. "
            "полка, дивизия «155 69»(?), за период с 20.7 по 30 августа 1943 г. Форма № 2, приложение к № "
            "34658с, строка № 100): № 100. Моисеев Александр Федорович, кр-ц(?), пулемётчик, "
            "беспартийный, 1900 г.р., Рязанская обл., Шацкий р-н, д. Марьино; призван Шацким РВК "
            "Рязанской обл. Убит в бою 30.7.43. Похоронен: опушка леса сев. д. ?(не читается). Родные: "
            "Жена Степанида Павловна Моисеева, адрес тот же. Первичное место захоронения: Орловская обл., "
            "Хвастовичский р-н, д. Берестна, лес, опушка. Место рождения на карточке: Рязанская обл., "
            "Шацкий р-н, д. Марьино. Корпус: рождение 12.05.1900 (МК 1900 № 20), отец Моисеев Федор "
            "Васильевич, мать Моисеева Евдокия Георгиевна."
        ),
    ),
    wwii_record(
        person("Александр", "Федорович", "Моисеев", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_donesenie2793409/",
        reviewed=False,
        scan_file="scans/pamyat_058-0018001-0623_00000121.jpg",
        birth_date=EventDate(1900),
        rank="красноармеец",
        military_unit="135 сд",
        casualty_reason="убит",
        document_type=WwiiDocumentType.CASUALTY_REPORT,
        date=EventDate(1943, Month.JULY, 30),
        casualty_date=EventDate(1943, Month.JULY, 30),
        archive="ЦАМО",
        fund="58",
        inventory="18001",
        case="623",
        comment=(
            "На скане (Именной список безвозвратных потерь сержантского и рядового состава 396 стр. полка "
            "135 сд с 20.7 по 30 августа 1943 г. (приложение к № 34658с, форма № 2), строка 100): "
            "Пулемётчик, б/парт, род. 1900, Рязанская обл., Шацкий р-н, д. Марьино; призван Шацким РВК "
            "Рязанской обл.; в бою убит 30.7.43; похоронен на опушке леса сев. д. Б?(не читается). "
            "Родные: Жена Степанида Павловна Моисеева, адрес тот же. Первичное место захоронения: "
            "Орловская обл., Хвастовичский р-н, д. Борейка, севернее, опушка леса. Место рождения на "
            "карточке: Рязанская обл., Шацкий р-н, дер. Марьино. Корпус: рождение 12.05.1900 (МК 1900 № "
            "20), отец Моисеев Федор Васильевич, мать Моисеева Евдокия Георгиевна."
        ),
    ),
)
