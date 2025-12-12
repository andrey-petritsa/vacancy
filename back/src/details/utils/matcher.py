class Matcher:
    @classmethod
    def is_matches_search_query(cls, vacancy, search_query):
        for key, value in search_query.items():
            if key == 'status':
                if vacancy['status'] != value:
                    return False

            if key == 'language':
                if value not in vacancy['languages']:
                    return False
        return True
