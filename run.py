from src.app import create_app


my_app = create_app()
if __name__ == '__main__':
    my_app.run()




# Investigate why User model is not deleting when database is reset