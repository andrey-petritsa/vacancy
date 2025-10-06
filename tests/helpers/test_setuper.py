from dotenv import load_dotenv

from vacancy.main.app_setuper import init_directories


class TestSetuper:
    @classmethod
    def setup(cls):
        load_dotenv()
        init_directories()

    @classmethod
    def delete_test_artifacts(cls):
        pass