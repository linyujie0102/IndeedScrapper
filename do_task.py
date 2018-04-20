import threading
from queue import Queue
from spider import Spider
from general import *
from ipfinder import ipFinder
import random
import logging


class DoTask:
    
    workers = []
    queue = Queue()

    def __init__(self, file_num, input_directory, output_directory):


        self.project = ''
        self.base_url = 'https://www.indeed.com/resumes?q='
        self.queue_key_words_file = ''
        self.key_word_counts_file = ''
        self.data_path = ''
        self.number_of_threads = 0
        self.number_of_job_before_refresh = 0
        self.output_file = ''
        self.output_directory = output_directory
        self.isfile = self.check_isfile(file_num, input_directory, output_directory)

        if self.isfile:
            self.project = 'words' + str(file_num)
            self.queue_key_words_file = self.project + '/queue_key_words.txt'
            self.key_word_counts_file = self.project + '/key_word_counts.txt'
            self.number_of_threads = 10
            self.number_of_job_before_refresh = random.randint(10, 30)
            Spider(self.project, self.base_url, self.data_path)
            self.create_workers()
            self.crawl()
            self.result_to_output_directory()

    def check_isfile(self, file_num, input_directory, output_directory):
        file_directory = input_directory + '/words' + str(file_num) +'.txt'
        if os.path.isfile(file_directory):
            self.data_path = file_directory
            self.output_file = output_directory + '/counts' + str(file_num) + '.txt'
            return True
        else:
            return False

    def create_workers(self):
        if len(DoTask.workers) == 0:
            for _ in range(self.number_of_threads):
                t = threading.Thread(target=self.work)
                DoTask.workers.append(t)
                t.daemon = True
                t.start()


    def work(self):
        while True:
            key_word = DoTask.queue.get()
            Spider.crawl_page(threading.current_thread().name, key_word)
            DoTask.queue.task_done()
            logging.info('[Job done on] ' + key_word)

    def create_jobs(self):
        job_done = 0
        for key_word in file_to_set(self.queue_key_words_file):
            DoTask.queue.put(key_word)
            job_done = job_done + 1
            if job_done >= self.number_of_job_before_refresh:
                break
        DoTask.queue.join()
        close_tor_browser()
        self.crawl()

    def crawl(self):
        queued_words = file_to_set(self.queue_key_words_file)
        if len(queued_words) > 0:
            open_tor_browser()

            ip = ipFinder().scrape_ip()
            logging.info('[Current ip ] ' + str(ip))
            append_to_file('iplogger.txt', str(ip))

            self.number_of_job_before_refresh = random.randint(10, 40)
            self.create_jobs()

    def result_to_output_directory(self):
        data_transfer(self.key_word_counts_file, self.output_file)

