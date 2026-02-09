def greet(name: str) -> str:
    return f"Hello, {name}. Welcome to AI Engineer Journey."

def run_app():
    user_name = input("Enter your name: ")
    message = greet(user_name)
    print(message)
