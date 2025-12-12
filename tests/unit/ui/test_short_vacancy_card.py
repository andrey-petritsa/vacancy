from ui.short_vacancy_card import ShortVacancyCard


class TestShortVacancyCard:
    def test_show(self):
        vacancy = {
            "company":'test-company',
            'city': 'moscow',
            "profession":"backend_programmer",
            "languages":["Python", "Bash"],
            "salary":{"min":200000, "max":240000},
            "work_mode":"remote",
            "domain":"e-commerce",
            'timestamp': 0,
            'source': 'telegram:test',
            "description":"e-commerce компания",
            "skills":[
                {"text":"Django", "type":"backend_framework"},
                {"text":"Flask", "type":"backend_framework"},
            ],
            "responsibility":"добавление новых функций, рефакторинг",
            "contact":"@asyasukhanovarecr",
            "experience_years":0,
            "id":"1",
            "text":"текст вакансии"
        }

        vacancy_card = ShortVacancyCard.show(vacancy)

        e_vacancy_card = {
            'id':'1',
            'date':'1970-01-01 03:00:00',
            'title':'backend_programmer (remote) Python, Bash',
            'salary':'200 000 - 240 000',
            'company':'test-company',
            'contact':'@asyasukhanovarecr',
            'text':'текст вакансии',
            'skills':[
                {'text':'Django', 'type':'backend_framework'},
                {'text':'Flask', 'type':'backend_framework'}
            ]
        }

        assert vacancy_card == e_vacancy_card
