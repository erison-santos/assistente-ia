from app.core.intent import Intent
from app.executor.windows_executor import WindowsExecutor


def main():
    intent = Intent(
        intent="open_application",
        target="microsoft edge",
        parameters={},
        confidence=0.99,
    )

    executor = WindowsExecutor()

    success, message = executor.execute(intent)

    print()
    print("Resultado:")
    print(message)


if __name__ == "__main__":
    main()