import logging

from tests.helpers.test_setuper import TestSetuper

def before_all(context):
    TestSetuper.setup()
    logging.getLogger("pyrogram").setLevel(logging.WARNING)

def before_feature(context, feature):
    TestSetuper.delete_test_artifacts()
