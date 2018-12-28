# Big Mart Sales 데이터셋을 이용한 회귀분석
# 상품의 특징(weight, fat content, type, mrp)
# 매장의 특징(year, size, location, type)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

pd.set_option('display.expand_frame_repr', False)


path1 = 'C:/Users/TJ/Google 드라이브/학습자료/프로그래밍/data science/Sample data/r/bigmartsales1.txt'
bigmart1 = pd.read_csv(path1, sep=',', engine='python')

