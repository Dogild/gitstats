# -*- coding: utf-8 -*-

import threading

class TaskManager(object):
    """ This class allows you to create several process/threads together and will block the application till al threads are done """

    def __init__(self):
        self.threads = list()

    def wait_until_exit(self):
        """ Wait until every threads are done """

        # Wait until all the threads are done. .join() is blocking.
        [t.join() for t in self.threads]

        self.threads = list()

    def launch_request(self, method, params=()):
        """ Lanch a new threads for the given methods and params"""

        thread = threading.Thread(target=method, args=params)
        thread.is_daemon = False
        thread.start()
        self.threads.append(thread)
