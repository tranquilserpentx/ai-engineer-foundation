def greet(name: str) -> str:
    return f"Hello, {name}. Welcome to AI Engineer Journey."

def main():
    user_name = "Faris"
    message = greet(user_name)
    print(message)

if __name__ == "__main__":
    main()
