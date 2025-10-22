def main():
    try:
        from frontend.main import start_app
        start_app()
    except ImportError as e:
        print(f"Ошибка импорта: {e}")
    except Exception as e:
        print(f"Ошибка запуска приложения: {e}")

if __name__ == "__main__":
    main()