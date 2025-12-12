from ui.formatter import Formatter


class ShortVacancyCard:
    @classmethod
    def show(cls, vacancy):
        return {
            'id':vacancy['id'],
            'date':Formatter.format_date(vacancy['timestamp']),
            'title':Formatter.format_title(vacancy),
            'salary':Formatter.format_salary(vacancy['salary']),
            'company':vacancy['company'],
            'contact':vacancy['contact'],
            'text':vacancy['text'],
            'skills':vacancy['skills']
        }
