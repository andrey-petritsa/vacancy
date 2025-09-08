import random
import string
import time

message = {
    "channel_id": "@myjobit",
    "date": 1757322306,
    "id": "120361:telegram:@myjobit",
    "text": "#вакансия #аналитик DWH\nДолжность: Middle Аналитик",
    "status": "pending",
    "user": {
        "id": "1",
        "name": "Alina"
    }
}

vacancy = {
    "contact": "@asyasukhanovarecr",
    "description": "Valta Pet Products — e-commerce компания. Переписывают платформу на Django.",
    "domain": "e-commerce",
    "experience_years": 2,
    "languages": ["Python"],
    "profession": "backend_programmer",
    "responsibility": "Разработка платформы на Django",
    "salary": {"min": 200000, "max": 240000},
    "skills": {
        "databases": ["PostgreSQL"],
        "frameworks": ["Django", "FastAPI"],
        "etc": ["Docker", "Celery"]
    },
    "work_mode": "remote"
}

def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_messages(min_count=1, max_count=10):
    messages = []
    count = random.randint(min_count, max_count)

    for i in range(count):
        msg = {
            "channel_id": f"@channel{random.randint(1,5)}",
            "date": int(time.time()) + random.randint(0, 1000),
            "id": f"{random.randint(1000,9999)}:telegram:@channel{random.randint(1,5)}",
            "text": f"#вакансия #{random_string(5)}\nДолжность: {random.choice(['Middle', 'Senior', 'Junior'])} {random_string(5)}",
            "status": 'pending',
            "user": {
                "id": str(random.randint(1, 1000)),
                "name": random_string(6)
            }
        }
        messages.append(msg)
    return messages