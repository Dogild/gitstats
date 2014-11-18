# -*- coding: utf-8 -*-

import threading


class TaskManager(object):

    def __init__(self):
        self.threads = list()

    def _wait_until_exit(self):
        # Wait until all the threads are done. .join() is blocking.
        [t.join() for t in self.threads]

        self.threads = list()

    def _launch_request(self, method, params=()):
        thread = threading.Thread(target=method, args=params)
        thread.is_daemon = False
        thread.start()
        self.threads.append(thread)
