import json
import utils.logger_utils as logger_utils

log = logger_utils.get_logger_error("data-storage-util-logger")
data_file_path = "storage/data.json"


def add_post(post: dict):
    data = get_posts()
    data.append(post)

    with open(data_file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def get_posts():
    data = []
    try:
        with open(data_file_path, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                log.error("Incorrect file")
    except FileNotFoundError:
        log.error("File not found")

    return data


if __name__ == "__main__":
    get_posts()
