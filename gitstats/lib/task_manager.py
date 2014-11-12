# -*- coding: utf-8 -*-

import threading

from time import sleep

class TaskManager(object):

    def _wait_until_exit(self):
        while (threading.active_count() > 1):
            sleep(0.01)

    def _launch_request(self, uri, target, params=list(), destinations=list()):
        thread = threading.Thread(target=target, args=(uri, params, destinations))
        thread.is_daemon = False
        thread.start()