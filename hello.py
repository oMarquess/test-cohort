def greet(name: str) -> str:
    """Returns a personalized greeting message."""
    if not name:
        return "Hello, UPSA Students!"
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Test the greeting
    message = greet("Python Learner")
    print(message)
