from verso.ru.dsl import (EventDate, Month, WwiDocumentType, criminal_record,
                          external_source_records, person, wwi_record)
from verso.ru.dsl.marital_status import MARRIED
from verso.ru.dsl.statuses import PEASANT_MALE

# Судимость («Ведомости справок о судимости 1870–1927», familio.org /catalogs/vss/).
# Милютин Иван Михайлов — д. Важная, Шаморгской вол. — третий из трёх приговоров
# одного человека (запись ссылается на приговоры 1912 г. № 142080 и 1913 г.
# № 92278). Возраст «18 л.» в источнике несогласован с более ранними записями
# (OCR/писарская ошибка): приговоры 1912–1913 гг. дают год рождения ~1894.
# Профиль — намеренный дубль для сверки при консолидации.
marino_external_sources_1914 = external_source_records(
    "Марьино",
    criminal_record(
        person("Иванъ", "Михайловъ", "Милютинъ", status=PEASANT_MALE, residence="Важная"),
        age=18,  # как в источнике; ср. 1912/1913 гг. → ~1894
        record_number=19806,
        page="309",
        date=EventDate(1914, Month.DECEMBER, 4),
        source_url="https://viewer.rsl.ru/ru/rsl01005494334?page=155",
        scan_file="scans/sudimost_milyutin_ivan_1914.jpg",
        original_text=(
            "19806. Милютин, Иван Михайлов, 18 л. К. Шацк. у., Шаморгск. в., "
            "д. Важни; — Тамбовск. О. С., 20 Сент. 914 (д. № 214/914), "
            "140 и 1 ч. 1655 У., тюр. 6 м. Исп. 4 Дек. 914. "
            "| 914 92278 169 М. | 912 142080 169 М."
        ),
        bibliography=(
            "Ведомость справок о судимости / М-во юстиции. — СПб.: Тип. "
            "Правительствующего Сената, 1870–1929. 1915, кн. 2. С. 309."
        ),
        comment=(
            "Преступление: кража (ст. 1655 Уложения о наказаниях — кража; ст. 140 — "
            "общие правила о совокупности преступлений). "
            "Суд: Тамбовский окружной суд (д. № 214/914). "
            "Наказание: тюрьма 6 месяцев. Исполнено 4 декабря 1914 г. "
            "Третий из трёх приговоров Ивана Михайлова Милютина, д. Важная — "
            "запись ссылается на приговоры 1913 г. № 92278 и 1912 г. № 142080. "
            "Возраст «18 л.» несогласован с ранними записями (писарская ошибка)."
        ),
    ),
    # WWI (ПМВ) — gwar.mil.ru. Инчиков Павел Андреевич, д. Важная (Шаморгская вол.),
    # 1-й лейб-гренадерский Екатеринославский полк, УБИТ 23.08.1914 у д. Печков.
    # Две карточки на одного человека (именной список потерь + карточка бюро учёта) —
    # намеренные дубли, сводятся при консолидации. «убит» → событие смерти.
    wwi_record(
        person("Павелъ", "Андреевъ", "Инчиковъ", residence="Важная"),
        source_url="https://gwar.mil.ru/heroes/chelovek_donesenie10467978/",
        rank="гренадер",
        military_unit="1-й лейб-гренадерский Екатеринославский полк",
        marital_status=MARRIED,
        casualty_reason="убит",
        place_of_casualty="д. Пегков",
        date=EventDate(1914, Month.AUGUST, 23),
        document_type=WwiDocumentType.CASUALTY_LISTS,
        archive="РГВИА",
        fund="16196 (Особое делопроизводство по сбору и регистрации сведений о выбывших)",
        inventory="1",
        case="26",
        scan_file="scans/wwi_inchikov_pavel_donesenie.jpg",
    ),
    wwi_record(
        person("Павел", "Андреев", "Инчиков", residence="Важная"),
        source_url="https://gwar.mil.ru/heroes/chelovek_gospital2115711/",
        rank="лейб-гренадер",
        military_unit="1-й лейб-гренадерский Екатеринославский полк",
        marital_status=MARRIED,
        casualty_reason="убит",
        place_of_casualty="д. Печков",
        date=EventDate(1914, Month.AUGUST, 23),
        document_type=WwiDocumentType.ARRIVAL_CARD_HIGHER,
        archive="РГВИА",
        fund="Картотека бюро учета потерь в Первой мировой войне (офицеров и солдат)",
        archive_location="Шкаф без номера, ящик 4919-И",
        scan_file="scans/wwi_inchikov_pavel_gospital.jpg",
    ),
)
