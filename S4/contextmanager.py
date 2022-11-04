class ContextManager:

    def __init__(self):
        print(f"wywołana metoda __init__")

    def __enter__(self):
        print(f"wywołana metoda __enter__")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"wywołana metoda __exit__")

with ContextManager() as manager:
    print("wykonanie ciała konstrukcji width")
