from verso.ru.dsl import (EventDate, Month, WwiiDocumentType, external_source_records, person, wwii_record)

# WWII (ВОВ) участники — pamyat-naroda.ru, событие 1945 г. (награждения по итогам войны).

marino_external_sources_1945 = external_source_records(
    "Марьино",
    wwii_record(
        person("Сергей", "Иванович", "Мыльников", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero98989270",
        scan_file="scans/pamyat_033-0686196-5172_00000357.jpg",
        birth_date=EventDate(1906),
        rank="рядовой",
        military_unit="1084 зенитный артиллерийский полк",
        document_type=WwiiDocumentType.AWARD_CARD,
        award="Медаль «За отвагу»",
        award_number="1/н",
        draft_board="Шацкий РВК, Рязанская обл., Шацкий р-н",
        draft_date=EventDate(1941, Month.JULY, 10),
        date=EventDate(1945, Month.JANUARY, 2),
        archive="ЦАМО",
        fund="33",
        inventory="686196",
        case="5172",
        archive_location="шкаф 60, ящик 2",
    ),
    wwii_record(
        person("Александр", "Михайлович", "Коржавин", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero20142707",
        scan_file="scans/pamyat_033-0686196-3696_00000392.jpg",
        birth_date=EventDate(1920),
        rank="сержант",
        military_unit="382 стрелковый полк 84 стрелковой дивизии",
        document_type=WwiiDocumentType.AWARD_ORDER,
        award="Медаль «За боевые заслуги»",
        award_number="5/н",
        draft_board="Кировоградский ГВК, Украинская ССР, Кировоградская обл., г. Кировоград",
        draft_date=EventDate(1943, Month.DECEMBER, 7),
        date=EventDate(1945, Month.APRIL, 23),
        archive="ЦАМО",
        fund="33",
        inventory="686196",
        case="3696",
    ),
    wwii_record(
        person("Федор", "Васильевич", "Коржавин", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/podvig-chelovek_kartoteka1280604987",
        birth_date=EventDate(1921),
        rank="ст. сержант",
        military_unit="316 отдельный батальон связи 36 гвардейского стрелкового корпуса",
        document_type=WwiiDocumentType.AWARD_CARD,
        award="Медаль «За победу над Германией в Великой Отечественной войне 1941–1945 гг.»",
        date=EventDate(1945, Month.MAY, 9),
        archive="ЦАМО",
        archive_location="шкаф 43, ящик 15",
    ),
    wwii_record(
        person("Александр", "Михайлович", "Коржавин", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/person-hero20142707",
        scan_file="scans/pamyat_033-0687572-0528_00000246.jpg",
        birth_date=EventDate(1920),
        rank="сержант",
        military_unit="382 стрелковый полк 84 стрелковой дивизии",
        document_type=WwiiDocumentType.AWARD_ORDER,
        award="Медаль «За отвагу»",
        award_number="16/н",
        draft_board="Ново-Георгиевский РВК, Украинская ССР, Кировоградская обл., Ново-Георгиевский р-н",
        draft_date=EventDate(1943, Month.DECEMBER, 10),
        date=EventDate(1945, Month.MAY, 21),
        archive="ЦАМО",
        fund="33",
        inventory="687572",
        case="528",
    ),
    wwii_record(
        person("Федор", "Васильевич", "Коржавин", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/podvig-chelovek_kartoteka1280604987",
        scan_file=[
            "scans/pamyat_033-0687572-0511_00000356.jpg",
            "scans/pamyat_033-0687572-0511_00000457.jpg",
        ],
        birth_date=EventDate(1921),
        rank="ст. сержант",
        military_unit="316 отдельный батальон связи 36 гвардейского стрелкового корпуса",
        document_type=WwiiDocumentType.AWARD_ORDER,
        award="Орден Красной Звезды",
        award_number="63/н",
        draft_board="Первомайский РВК, Московская обл., г. Москва, Первомайский р-н",
        draft_date=EventDate(1940, Month.OCTOBER),
        date=EventDate(1945, Month.MAY, 21),
        archive="ЦАМО",
        fund="33",
        inventory="687572",
        case="511",
    ),
    wwii_record(
        person("Федор", "Васильевич", "Коржавин", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/podvig-chelovek_kartoteka1280604987",
        birth_date=EventDate(1921),
        rank="ст. сержант",
        document_type=WwiiDocumentType.AWARD_CARD,
        award="Медаль «За взятие Кенигсберга»",
        date=EventDate(1945, Month.JUNE, 9),
        archive="ЦАМО",
        archive_location="шкаф 43, ящик 15",
    ),
    # ВОВ — pamyat-naroda.ru, добавлено 18.11.2026: люди, найденные в корпусе (реестр —
    # EXTERNAL_SOURCES.md и external_sources/vov_pamyat.tsv).
    wwii_record(
        person("Алексей", "Алексеевич", "Калугин", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/podvig-chelovek_kartoteka1371535197/",
        reviewed=False,
        scan_file=[
            "scans/pamyat_033-0686196-4313_00000217.jpg",
            "scans/pamyat_033-0686196-4313_00000218.jpg",
            "scans/pamyat_033-0690306-3427_00000791.jpg",
        ],
        birth_date=EventDate(1909),
        rank="гв. рядовой",
        document_type=WwiiDocumentType.AWARD_CARD,
        award="Орден Славы III степени (05.06.1945); Медаль «За отвагу» (29.05.1945)",
        date=EventDate(1945, Month.MAY, 29),
        archive="ЦАМО",
        archive_location="шкаф 37, ящик 15",
        comment=(
            "Картотека награждений, дата — первой награды. На скане (Наградной лист на орден Славы III "
            "ст. от 26 мая 1945 (лицевая и оборотная сторона) и приказ по 172 гв. минометному Печенгскому "
            "ордена Александра Невского полку 54 гв. ДАБр № 05/н от 29 мая 1945, пункт 3): Гв. "
            "красноармеец, старший телефонист взвода связи батареи управления 172 гв. мин. полка; на "
            "Карельском фронте с окт. 1941, на 3-м Укр. фронте в 1945; ранен тяжело 30.04.42 и легко "
            "4.04.45 (в приказе — 6.04.45). В бою за ст. Можа(?) под огнём восстановил линию связи, "
            "одного немца убил, другого взял в плен; на высоте 362 уничтожил 5 немецких солдат. Слава III "
            "ст. — приказ 99 гв. сд № 025/н от 6 июня 1945. По приказу полка 05/н — за отражение 5 "
            "контратак 6.4.45 на высоте 475 (награда на кропе не видна). В тексте подвига фамилия "
            "написана «Кулагин». Место рождения на карточке: Рязанская обл., Шацкий р-н, с. Марьино. "
            "Корпус: рождение 14.03.1909 (МК 1909 № 10), отец Калугин Алексей Гавриилович, мать Калугина "
            "Анисья Федоровна."
        ),
    ),
)
