from vacancy.usecases.repository.file_vacancy import FileVacancy
from vacancy.utils import to_dtos


class TestFileVacancy:
    def test_save_many(self):
        vacancies = [
            {'id': 1, 'domain': 'ecommerce'}
        ]
        FileVacancy.save_many(to_dtos(vacancies))

        vacancies = FileVacancy.get_all()
        assert len(vacancies) > 0