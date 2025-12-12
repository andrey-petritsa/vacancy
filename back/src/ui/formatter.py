from datetime import datetime

class Formatter:
    @classmethod
    def format_salary(cls, salary):
        min = f"{salary['min']:,}".replace(",", " ")
        max = f"{salary['max']:,}".replace(",", " ")

        return f"{min} - {max}"

    @classmethod
    def format_date(cls, timestamp):
        return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    @classmethod
    def format_title(cls, vacancy):
        return f'{vacancy['profession']} ({vacancy['work_mode']}) {', '.join(vacancy['languages'])}'