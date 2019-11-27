
import threading
import time
import os
from concurrent.futures import ThreadPoolExecutor
from tianshu_fl.core.aggregator import FedAvgAggregator
from tianshu_fl.core.strategy import WorkModeStrategy, FedrateStrategy
from tianshu_fl.core import communicate

JOB_PATH = os.path.abspath(".") + "\\res\\jobs"
BASE_MODEL_PATH = os.path.abspath(".") + "\\res\\models"

class TianshuFlServer(threading.Thread):

    def __init__(self):
        super(TianshuFlServer, self).__init__()


class TianshuFlStandaloneServer(TianshuFlServer):
    def __init__(self, federate_strategy):
        super(TianshuFlStandaloneServer, self).__init__()
        if federate_strategy == FedrateStrategy.FED_AVG:
            self.aggregator = FedAvgAggregator(WorkModeStrategy.WORKMODE_STANDALONE, JOB_PATH, BASE_MODEL_PATH)
        else:
           pass


    def run(self):
        self.aggregator.aggregate()





class TianshuFlClusterServer(TianshuFlServer):

    def __init__(self, federate_strategy, ip, port, api_version):
        super(TianshuFlClusterServer, self).__init__()
        self.executor_pool = ThreadPoolExecutor(2)
        if federate_strategy == FedrateStrategy.FED_AVG:
            self.aggregator = FedAvgAggregator(WorkModeStrategy.WORKMODE_STANDALONE, JOB_PATH, BASE_MODEL_PATH)
        else:
            pass
        self.ip = ip
        self.port = port
        self.api_version = api_version

    def run(self):
        self.executor_pool.submit(self.aggregator.aggregate)
        self.executor_pool.submit(communicate.start_communicate_server, self.api_version, self.ip, self.port)






