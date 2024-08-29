import logging
import sys

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

n = input('enter - ')
root.info('Input: {}'.format(n))
