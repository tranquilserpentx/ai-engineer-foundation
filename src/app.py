from src.config import DEFAULT_NAME

def greet(name: str) -> str:
    if not name:
        raise ValueError("Name cannot be empty")
    return f"Hello, {name}. Welcome to AI Engineer Journey."

def run_app():
    try:
        user_name = input("Enter your name: ").strip()
        if not user_name:
            user_name = DEFAULT_NAME
        message = greet(user_name)
        print(message)
    except ValueError as e:
        print(f"Error: {e}")