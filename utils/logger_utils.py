import logging


def get_logger_error(name: str = "logger"):
    log_formatter = logging.Formatter(
        "[%(asctime)s] [%(name)s] [%(levelname)s]: %(message)s"
    )

    handler = logging.StreamHandler()
    handler.setLevel(logging.ERROR)
    handler.setFormatter(log_formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger


if __name__ == "__main__":
    get_logger_error()
