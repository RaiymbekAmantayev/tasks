import uuid
def generate_invite_code():
    code = str(uuid.uuid4()).replace("-", "")[:6]
    return code