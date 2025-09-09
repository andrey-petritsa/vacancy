from vacancy.utils import to_dtos


class Freelanceru:
    def __init__(self, token):
        self.token = token

    def get_today_jobs(self):
        jobs = []
        return to_dtos(jobs)