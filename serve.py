from pom_tracker.main import Application

# Entry point for the application
if __name__ == '__main__':
    app = Application()
    app.start_app(forever=True)
    # app.start_app()
