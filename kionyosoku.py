from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

#気温データの読み込み
df = pd.read_csv('kion.csv', encoding="utf-8")
#学習データとテストデータに分ける
#CSVファイルを分けていないので、過去データも含んでいる
train_year = (df["年"] <= 2017)
test_year = (df["年"] >= 2018)
interval = 6

#過去６日を学習するデータ作成
def make_data(data):
    x = [] #学習データ
    y = [] #結果
    temps = list(data["気温"])
    for i in range(len(temps)):
        if i <= interval: continue
        y.append(temps[i])
        xa = []
        for p in range(interval):
            d = i + p - interval
            xa.append(temps[d])
        x.append(xa)
    return (x,y)

train_x, train_y = make_data(df[train_year])
test_x, test_y = make_data(df[test_year])

#直線回帰分析を行う
lr = LinearRegression(normalize=True)
lr.fit(train_x, train_y) #学習
pre_y = lr.predict(test_x) #予測
