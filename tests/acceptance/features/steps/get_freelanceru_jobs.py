import os

from behave import *

from sources.freelanceru.freelanceru import Freelanceru


@step("у меня есть аккаунт на сайте freelanceru")
def step_impl(context):
    context.token = os.getenv("FREELANCERU_TOKEN")


@step("я получаю сегодняшние работы с площадки")
def step_impl(context):
    freelanceru = Freelanceru(context.token)
    jobs = freelanceru.get_today_jobs()
    context.jobs = jobs


@step("работы получены")
def step_impl(context):
    required = ['title', 'description', 'languages', 'salary', 'skills', 'experience_years']
    assert len(context.jobs) > 0
    for job in context.jobs:
        assert required.issubset(job.__dict__)
