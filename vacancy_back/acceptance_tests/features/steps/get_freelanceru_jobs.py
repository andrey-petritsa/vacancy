from behave import *
import secrets.secrets as secrets
from vacancy.sources.freelanceru.freelanceru import Freelanceru

use_step_matcher("re")


@when("у меня есть аккаунт на сайте freelanceru")
def step_impl(context):
    context.token = secrets.freelanceru_token


@step("я получаю сегодняшние работы с площадки")
def step_impl(context):
    freelanceru = Freelanceru(context.token)
    jobs = freelanceru.get_today_jobs()
    context.jobs = jobs

@then("работы получены")
def step_impl(context):
    required = ['title','description','languages','salary','skills','experience_years']
    assert len(context.jobs) > 0
    for job in context.jobs:
        assert required.issubset(job.__dict__)