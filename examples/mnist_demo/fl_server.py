import sys
sys.path.append("C:\\Users\\tchennech\\Documents\\FederateLearningLibrary")

from gl.core.server import TianshuFlStandaloneServer, TianshuFlClusterServer
from gl.core.strategy import WorkModeStrategy, FedrateStrategy


WORK_MODE = WorkModeStrategy.WORKMODE_STANDALONE
FEDERATE_STRATEGY = FedrateStrategy.FED_AVG
IP = '0.0.0.0'
PORT = 9763
API_VERSION = '/api/version'

if __name__ == "__main__":

    if WORK_MODE == WorkModeStrategy.WORKMODE_STANDALONE:
        TianshuFlStandaloneServer(FEDERATE_STRATEGY).start()
    else:
        TianshuFlClusterServer(FEDERATE_STRATEGY, IP, PORT, API_VERSION).start()

