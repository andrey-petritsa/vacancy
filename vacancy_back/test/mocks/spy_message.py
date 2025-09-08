from vacancy.usecases.repository.struct import Struct


class SpyMessage:
    saved = []

    def save(self):
        pass

    @classmethod
    def save_many(cls, list_of_msgs):
        cls.saved = list_of_msgs

    @classmethod
    def find(cls, id):
        pass

    @classmethod
    def get_all(cls):
        return [
            Struct(**{'status': 'done', 'text': 'always done'}),
            Struct(**{'status': 'pending', 'text': 'msg'})
        ]

    @classmethod
    def get_only_pending_status(cls):
        return [
            Struct(**{'status': 'pending', 'text': 'msg1'}),
            Struct(**{'status': 'pending', 'text': 'msg2'})
        ]

    @classmethod
    def get_latest_id_from_channel(cls, channel_id):
        return None