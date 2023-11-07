from core.config import settings
def get_hashed_password(password: str) -> str:
    return settings.PASSWORD_CONTEXT.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return settings.PASSWORD_CONTEXT.verify(password, hashed_pass)

