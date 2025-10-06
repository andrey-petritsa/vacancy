from behave import *

from vacancy.ui.main_page import MainPage


@step("у меня есть вакансии")
def step_impl(context):
    vacations = [
        {
            "profession":"backend_programmer",
            "languages":["Python"],
            "salary":{"min":200000, "max":240000},
            "work_mode":"remote",
            "domain":"e-commerce",
            "description":"Valta Pet Products: переписываем платформу на Django.",
            "skills":{
                "frameworks":["Django", "Django Ninja", "FastAPI"],
                "databases":["PostgreSQL", "Redis"],
                "etc":["Celery", "RabbitMQ"]
            },
            "responsibility":"Переписывание ядра с упором на стабильность и скорость.",
            "contact":"@asyasukhanovarecr",
            "experience_years":3,
            "id":1
        },
    ]
    context.vacations = vacations


@step("я показываю их на странице")
def step_impl(context):
    view_page = MainPage.show(context.vacations)
    context.view_page = view_page


@step("вакансии отображаются на странице")
def step_impl(context):
    cards = [
        {
            'header':{
                'title':'BACKEND PROGRAMMER',
                'salary':'💰 200 000 - 240 000 ₽ Remote',
                'domain':'e-commerce',
                'description':'Valta Pet Products: переписываем платформу на Django.',
                'responsibility':'Переписывание ядра с упором на стабильность и скорость.',
                'experience':'3 года'
            },
            'body':{
                'skills':[
                    {'name':'🧩 Frameworks', 'items':['Django', 'Django Ninja', 'FastAPI']},
                    {'name':'🗄️ Databases', 'items':['PostgreSQL', 'Redis']},
                    {'name':'⚙️ Other', 'items':['Celery', 'RabbitMQ']},
                ]
            }
        }
    ]
    e_view_page = {
        "vacancies_cards":cards
    }

    assert context.view_page == e_view_page
