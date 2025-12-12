from pathlib import Path

from details.utils import settings as s


class SystemTest:
    def setup_method(self):
        s.path_to_database = "back/test-database"
        Path(s.path_to_database).mkdir(parents=True, exist_ok=True)

        Path(f"{s.path_to_database}/tg_last_known_ids.json").write_text("{}", encoding="utf-8")
        Path(f"{s.path_to_database}/unparsed_vacancies.json").write_text("[]", encoding="utf-8")
        Path(f"{s.path_to_database}/parsed_vacancies.json").write_text("[]", encoding="utf-8")
        Path(f"{s.path_to_database}/invalid_vacancies.json").write_text("[]", encoding="utf-8")
