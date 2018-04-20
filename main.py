from do_task import DoTask
from general import *
import logging

configure_log()
create_output_dir('output')
start = 0
end = 120

start = find_last_task(0, 170)
logging.info('Starting from task ' + str(start))

for x in range(0, 170):
    dp = DoTask(x, 'input', 'output')