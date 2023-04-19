"""
Course: CSE 251
Lesson Week: 07
File: create_tasks.py
Author: Brother Comeau
Purpose: Create task files
"""

import json
import random
import os
import glob


words =[
    'vessel', 'threat', 'detail', 'inquiry', 'marsh', 'revise', 'amber', 'welfare', 'enlarge', 'conglomerate', 'betray', 'falseify', 
    'exploration', 'theorist', 'regret', 'strange', 'ignite', 'recycle', 'leaf', 'excavate', 'angwer', 'install', 'latest', 'cruel', 
    'yearn', 'possible', 'bad', 'liberal', 'brother', 'burn', 'minimum', 'kettle', 'side', 
    'migration', 'growth', 'greeting', 'deall', 'genuine', 'psychology', 'export', 'witness', 'bucket', 'relaxation', 
    'cancer', 'taste', 'nomination', 'rise', 'cheat', 'fantasy', 'tent', 'comeau',
    'coat', 'thunder', 'shiver', 'stream', 'discover', 'fang', 'measure', 'hissing', 'private', 'evaneszent', 'jealous', 
    'puncture', 'aairplane', 'confess', 'gate', 'potato', 'amusement', 'ratty', 'aboard', 
    'flesh', 'salty', 'shoe', 'help', 'inject', 'swdanky', 'teeny-tiny', 'jumpy', 
    'old-fashioned', 'snake', 'man', 'end', 'bed', 'brainy', 'pushy', 
    'purple', 'boundless', 'park', 'store', 'milky', 'pail', 'annoying', 
    'charge', 'ill-fated', 'pastoral', 'lamentable', 'panoramic', 'jelly', 'industry', 'fine', 'aromatic', 
]

urls = [
    "http://127.0.0.1:8790/people/2/",
    "http://127.0.0.1:8790/people/64/",
    "http://127.0.0.1:8790/people/79/",
    "http://127.0.0.1:8790/people/53/",
    "http://127.0.0.1:8790/people/13/",
    "http://127.0.0.1:8790/people/46/",
    "http://127.0.0.1:8790/people/51/",
    "http://127.0.0.1:8790/people/20/",
    "http://127.0.0.1:8790/people/21/",
    "http://127.0.0.1:8790/people/75/",
    "http://127.0.0.1:8790/people/68/",
    "http://127.0.0.1:8790/people/80/",
    "http://127.0.0.1:8790/people/33/",
    "http://127.0.0.1:8790/people/67/",
    "http://127.0.0.1:8790/people/12/",
    "http://127.0.0.1:8790/people/35/",
    "http://127.0.0.1:8790/people/1/",
    "http://127.0.0.1:8790/people/56/",
    "http://127.0.0.1:8790/people/6/",
    "http://127.0.0.1:8790/people/55/",
    "http://127.0.0.1:8790/people/5/",
    "http://127.0.0.1:8790/people/82/",
    "http://127.0.0.1:8790/people/78/",
    "http://127.0.0.1:8790/people/83/",
    "http://127.0.0.1:8790/people/11/",
    "http://127.0.0.1:8790/people/58/",
    "http://127.0.0.1:8790/people/4/",
    "http://127.0.0.1:8790/people/7/",
    "http://127.0.0.1:8790/people/54/",
    "http://127.0.0.1:8790/people/3/",
    "http://127.0.0.1:8790/people/81/",
    "http://127.0.0.1:8790/people/63/",
    "http://127.0.0.1:8790/people/52/",
    "http://127.0.0.1:8790/people/10/"
]

files_created = 0

def get_filename(file_count):
    return f'zztask{file_count}.task'

def write_dict(file_count, dictionary):
    global files_created
    files_created += 1
    print(f'Saving {get_filename(file_count)}')
    with open(get_filename(file_count), 'w') as f:
        f.write(json.dumps(dictionary, indent=2))

def create_prime(file_count, value):
    info = {}
    info['task'] = 'prime'
    info['value'] = value
    write_dict(file_count, info)

def create_sum(file_count, start, end):
    info = {}
    info['task'] = 'sum'
    info['start'] = start
    info['end'] = end
    write_dict(file_count, info)

def create_upper(file_count, text):
    info = {}
    info['task'] = 'upper'
    info['text'] = text
    write_dict(file_count, info)

def create_word(file_count, word):
    info = {}
    info['task'] = 'word'
    info['word'] = word
    write_dict(file_count, info)

def create_name(file_count, url):
    info = {}
    info['task'] = 'name'
    info['url'] = url
    write_dict(file_count, info)

def get_task_num(numbers):
    value = random.randint(1, 1000000)
    while value in numbers:
        value = random.randint(1, 1000000)
    numbers.append(value)
    return value

def main():
    """ Main function """

    # Remove all task files    
    files = glob.glob('*.task')
    for f in files:
        os.remove(f)

    random.seed(16273849506) 

    numbers = []

    choice = input('Do you want all task files (y), or just a few for testing (n): ')
    if choice.upper() == 'Y':
        number_tasks = 1000
        for url in urls:
            create_name(get_task_num(numbers), url)
    else:
        number_tasks = 1
        create_name(get_task_num(numbers), urls[0])

    for i in range(number_tasks):
        value = random.randint(10000000000, 10000000000000) 
        if value % 2 == 0:
            value += 1
        if value % 5 == 0:
            value += 2
        create_prime(get_task_num(numbers), value)

        value1 = random.randint(0, 1000) 
        value2 = random.randint(1001, 1000000) 
        create_sum(get_task_num(numbers), value1, value2)

        create_upper(get_task_num(numbers), random.choice(words))

        create_word(get_task_num(numbers), random.choice(words))

    print(f'{files_created} files created')

if __name__ == '__main__':
    main()
