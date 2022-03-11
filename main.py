import endpoint.impl
from flask_app import current_app, current_db


def run():
    current_db.create_all()
    current_app.run(debug=True)


if __name__ == '__main__':
    run()
