import os
import vacancy.utils as utils
from dotenv import load_dotenv
import os


class TestSetuper:
    @classmethod
    def setup(cls):
        load_dotenv()
        utils.artifacts_path = "test_artifacts"

    @classmethod
    def delete_test_artifacts(cls):
        path = "test_artifacts/vacancies.jsonl"
        if os.path.exists(path):
            os.remove(path)
        path = "test_artifacts/messages.jsonl"
        if os.path.exists(path):
            os.remove(path)