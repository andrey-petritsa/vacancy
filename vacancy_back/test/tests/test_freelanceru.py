from vacancy.sources.freelanceru.freelanceru import Freelanceru


class TestFreelanceru:
    def __init__(self):
        self.freelancer = Freelanceru()

    def test_get_jobs(self):
        jobs = self.freelancer.get_jobs("", True, False, [])

        assert len(jobs) != 0
