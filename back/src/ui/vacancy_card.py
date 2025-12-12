from ui.formatter import Formatter


class VacancyCard:
    @classmethod
    def show(cls, vacancy):
        return {
            'id': vacancy['id'],
            'header':{
                'company_labels':[
                    {'text':vacancy['company']},
                    {'text':vacancy['domain']},
                    {'text':vacancy['city']},
                    {'text':vacancy['contact']},
                    {'text':vacancy['source']},
                    {'text':Formatter.format_date(vacancy['timestamp'])},
                ],
                'title_label':{'text':Formatter.format_title(vacancy)},
                'salary_label':{'text':Formatter.format_salary(vacancy['salary'])},
            },
            'body':{'skills':vacancy['skills']},
            'footer':{
                'description_labels':[
                    {'text':f'Описание: {vacancy['description']}'},
                    {'text':f'Обязанности: {vacancy['responsibility']}'},
                ],
                'buttons':[
                    {'text':'Подробнее', 'inner_text':f'{vacancy['text']}', 'type':'more-button'},
                    {'text':'Лайк', 'type':'like-button'},
                    {'text':'Дизлайк', 'type':'dislike-button'}
                ]
            }
        }
