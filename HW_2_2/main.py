import os
import hashlib

file_path = os.path.join(os.getcwd(), 'output.txt')


def return_hash(file):
    with open(file, 'r', encoding='utf-8') as f_countries:
        for line in f_countries.readlines():
            yield hashlib.md5(line.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    for i in return_hash(file_path):
        print(i)
