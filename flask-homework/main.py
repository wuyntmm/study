from flask import Flask
from logging.config import dictConfig

app = Flask(__name__)

dictConfig({
    "version": 1,
    "formatters": {
        "simple": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"}
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "simple"}
    },
    "root": {"handlers": ["console"], "level": "INFO"},
})


@app.route('/hello')
def index():
    app.logger.info('INFO was logged successfully')
    return 'Hello, world!'


if __name__ == '__main__':
    app.run()
