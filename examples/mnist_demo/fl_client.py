import torch
import os, sys
sys.path.append("C:\\Users\\tchennech\\Documents\\FederateLearningLibrary")
from torchvision import datasets, transforms
from tianshu_fl.core.strategy import WorkModeStrategy
from tianshu_fl.core.trainer import Trainer
from tianshu_fl.core.job_detector import JobDetector
from torch import nn
import torch.nn.functional as F

CLIENT_IP = "127.0.0.1"
CLIENT_PORT = 8081
CLIENT_ID = 0
SERVER_URL = "http://127.0.0.1:9763"

def start_trainer(work_mode, client_ip, client_port, client_id, server_url, data):

    Trainer(work_mode, data, str(client_id), client_ip, str(client_port), server_url, 3).start()
    #print(os.path.abspath("."))

if __name__ == "__main__":

    CLIENT_ID = int(sys.argv[1])

    mnist_data = datasets.MNIST("./mnist_data", download=True, train=True, transform=transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.13066062,), (0.30810776,))
    ]))

    #start_trainer(WorkModeStrategy.WORKMODE_STANDALONE, CLIENT_ID, mnist_data)

    start_trainer(WorkModeStrategy.WORKMODE_STANDALONE, CLIENT_IP, CLIENT_PORT, CLIENT_ID, SERVER_URL, mnist_data)




