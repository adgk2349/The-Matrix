import keyring

SERVICE_NAME = "run-matrix"
ACCOUNT_NAME = "gemini-api-key"

def load() -> str | None:
    return keyring.get_password(SERVICE_NAME, ACCOUNT_NAME)

def store(key: str) -> None:
    keyring.set_password(SERVICE_NAME, ACCOUNT_NAME, key)

def delete() -> None:
    try:
        keyring.delete_password(SERVICE_NAME, ACCOUNT_NAME)
    except keyring.errors.PasswordDeleteError:
        pass
