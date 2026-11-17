from verso.ru.dsl import (EventDate, Month, WwiiDocumentType, external_source_records, person,
                          wwii_record)

# WWII (ВОВ) участник — pamyat-naroda.ru. Учётно-послужная картотека офицера, событие 1932 г. (дата поступления на службу).
# Мыльников Георгий Георгиевич — тот же человек, что и на карточке военнопленного под 1941/ (см. комментарий там).

marino_external_sources_1932 = external_source_records(
    "Марьино",
    wwii_record(
        person("Георгий", "Георгиевич", "Мыльников", residence="Марьино"),
        source_url="https://pamyat-naroda.ru/heroes/kld-card_uchet_officer13824728",
        birth_date=EventDate(1909, Month.NOVEMBER, 3),
        rank="лейтенант административной службы",
        military_unit="7 зсп (запасной стрелковый полк)",
        document_type=WwiiDocumentType.SERVICE_CARD,
        draft_board="Шацкий РВК, Рязанская обл., Шацкий р-н",
        draft_date=EventDate(1932, Month.NOVEMBER, 9),
        date=EventDate(1932, Month.NOVEMBER, 9),
        archive="ЦАМО",
        comment=(
            "Дата окончания службы: 21.09.1957. "
        ),
    ),
)
