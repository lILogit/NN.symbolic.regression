# simple neural feedforward network in pytorch.lightning to learn in relationship between X and z (X is a 3D tensor and z is a 1D tensor)
# importing the necessary libraries
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
import pytorch_lightning as pl
from sklearn.model_selection import train_test_split



