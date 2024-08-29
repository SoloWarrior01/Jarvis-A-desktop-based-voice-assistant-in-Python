import logging
import csv
import sys
from assistant.jarvis import Jarvis


def read_config():
    with open('config/config.csv', newline='') as file1:
        data1 = csv.reader(file1)
        listdata1 = list(data1)
        return listdata1


if __name__ == "__main__":
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    handler1 = logging.FileHandler('config\\history.txt')
    handler1.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s',
                                  datefmt='%d-%m-%Y %H:%M:%S')
    handler.setFormatter(formatter)
    handler1.setFormatter(formatter)
    root.addHandler(handler)
    root.addHandler(handler1)

    Jarvis(logger=root, config=read_config())
