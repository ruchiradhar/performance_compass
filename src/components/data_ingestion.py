# the data ingestion needs to be done from any official data source
# the data is also split at this stage before further transformation

import os
import sys #for custom exception
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
