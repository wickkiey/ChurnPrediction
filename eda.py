import pandas as pd
from pandas_profiling import ProfileReport

train = pd.read_csv("dataset/train.csv")
test = pd.read_csv('dataset/test.csv')

train_pr = ProfileReport(train)
test_pr = ProfileReport(test)

train_pr.to_file("eda/train.html")
test_pr.to_file("eda/test.html")