from ui.vacancy_card import VacancyCard


class TestVacancyCard:
    def test_vacancy_card(self):
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

        vacancy_card = VacancyCard.show(vacancy)

        e_vacancy_card = {
            'id': '1',
            'header':{
                'company_labels':[
                    {'text':'test-company'},
                    {'text':'e-commerce'},
                    {'text':'moscow'},
                    {'text':'@asyasukhanovarecr'},
                    {'text':'telegram:test'},
                    {'text': '1970-01-01 03:00:00'}
                ],
                'title_label':{'text':'backend_programmer (remote) Python, Bash'},
                'salary_label':{'text':'200 000 - 240 000'},
            },
            'body':{
                'skills':[
                    {'text': "Django", "type": "backend_framework"},
                    {'text': "Flask", "type": "backend_framework"},
                ]
            },
            'footer':{
                'description_labels':[
                    {'text':'Описание: e-commerce компания'},
                    {'text':'Обязанности: добавление новых функций, рефакторинг'},
                ],
                'buttons':[
                    {'text':'Подробнее', 'inner_text':'текст вакансии', 'type':'more-button'},
                    {'text':'Лайк', 'type':'like-button'},
                    {'text':'Дизлайк', 'type':'dislike-button'}
                ]
            }
        }

        assert vacancy_card == e_vacancy_card
