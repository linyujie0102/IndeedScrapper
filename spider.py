from general import *
from count_finder import CountFinder
import random
import logging

class Spider:
    # Class variables
    project_name = ''
    base_url = ''
    key_word_counts_file = ''
    queue_key_words_file = ''
    data_path = ''
    key_word_counts_set = set()
    queue_key_words_set = set()

    def __init__(self, project_name, base_url, data_path):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.key_word_counts_file = Spider.project_name + '/key_word_counts.txt'
        Spider.queue_key_words_file = Spider.project_name + '/queue_key_words.txt'
        Spider.data_path = data_path
        self.boot()
        #self.crawl_page('First spider', Spider.base_url)

    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.queue_key_words_file)
        create_data_files(Spider.key_word_counts_file)

        if file_is_empty(Spider.queue_key_words_file):
            data_transfer(Spider.data_path, Spider.queue_key_words_file)
        
        Spider.queue_key_words_set = file_to_set(Spider.queue_key_words_file)
        Spider.key_word_counts_set = file_to_set(Spider.key_word_counts_file)
        #Spider.req_proxy = RequestProxy()

    @staticmethod
    def crawl_page(thread_name, key_word):
        page_url = create_page_url(Spider.base_url, key_word)
        logging.info('[Crawling...] ' + key_word) 
        cf = CountFinder(page_url=page_url)
        Spider.queue_key_words_set.remove(key_word)
        if cf.is_succeed():
            result = key_word + ': ' + str(cf.get_count())
            Spider.add_result_to_set(result)
            logging.info('[Count of   ] ' + result)
        else:
            Spider.queue_key_words_set.add(key_word)
        Spider.update_files()

    @staticmethod
    def add_result_to_set(result):
        Spider.key_word_counts_set.add(result)

    @staticmethod
    def update_files():
        set_to_file(Spider.key_word_counts_set.copy(), Spider.key_word_counts_file)
        set_to_file(Spider.queue_key_words_set.copy(), Spider.queue_key_words_file)
