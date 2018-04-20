import os
import time
import random
import logging


def create_project_dir(directory):
    if not os.path.exists(directory):
        logging.info('[Creating project] ' + directory)
        os.makedirs(directory)

def create_output_dir(directory):
    if not os.path.exists(directory):
        logging.info('[Creating output directory] ' + directory)
        os.makedirs(directory)


def create_data_files(path):
    if not os.path.isfile(path):
        create_file(path)


def create_file(path):
    f = open(path, 'w')
    f.close()


def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')
        file.close()


def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


def file_to_list(file_name):
    results = []
    with open(file_name, 'rt') as f:
        for line in f:
            results.append(line.replace('\n', ''))
    return results


def set_to_file(links, file):
    with open(file, 'w') as f:
        for link in links:
            f.write(link + '\n')


def list_to_file(list, file):
    with open(file, 'w') as f:
        for string in list:
            f.write(string + '\n')


def create_page_url(base_url, key_word):
    key_word = key_word.replace(' ', '+')
    return base_url + key_word + '&l=' + 'CA&CO=US&cb=jt&cb=skills&cb=fos'


def data_transfer(origin_file_path, target_file_path):
    if not os.path.isfile(target_file_path):
        create_file(target_file_path)
    origin = open(origin_file_path, 'rt')
    target = open(target_file_path, 'w')
    for line in origin:
        target.write(line)
    origin.close()
    target.close()


def open_tor_browser():
    # -j means open app hidden
    os.system('open -j -a TorBrowser')
    time.sleep(random.randint(8, 15))


def close_tor_browser():
    os.system('osascript -e \'quit app "TorBrowser"\'')
    time.sleep(random.randint(2, 5))


def file_is_empty(file_path):
    contents = []
    with open(file_path, 'rt') as f:
        for line in f:
            contents.append(line.replace('\n', ''))
            if len(contents) > 0:
                return False
    return True


def find_last_task(start, end):
    last = 0
    for i in range(start, end + 1):
        path = 'words' + str(i)
        if os.path.isdir(path):
            last = i

    last_task_path = 'words' + str(last)
    if os.path.isdir(last_task_path):
        wordsfile = last_task_path + '/queue_key_words.txt'
        countsfile = last_task_path + '/key_word_counts.txt'
        if os.path.isfile(wordsfile) and os.path.isfile(countsfile):
            if not file_is_empty(countsfile) and file_is_empty(wordsfile):
                last += 1
    return last


def configure_log():
    FORMAT = '%(asctime)-10s [%(threadName)-10s %(levelname)-4s] %(message)s'
    logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt='%m-%d %H:%M')
