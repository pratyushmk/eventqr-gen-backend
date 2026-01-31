import uuid

def generate_registration_id():
    return uuid.uuid4().hex[:10]