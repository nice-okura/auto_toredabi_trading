import numpy as np
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import matplotlib.finance as mpf
from matplotlib.dates import date2num

def main():
    #株価取得期間の設定
    start = datetime.datetime(2018, 1, 1)
    end = datetime.datetime(2018, 1, 24)

    #株価取得
    toyota = web.DataReader('RGSE', 'yahoo', start, end)
    df = toyota.drop('Volume', axis=1)  # DataFrameからVolumeを消去
    df = df.ix[:, ['Open', 'Close', 'High','Low']]

    #画像作成
    fig = plt.figure()
    ax = plt.subplot()
    xdate = [x.date() for x in df.index]  # 日付
    ochl = np.vstack((date2num(xdate), df.values.T)).T
    mpf.candlestick_ochl(ax, ochl, width=0.7, colorup='g', colordown='r')
    ax.grid()  # グリッド表示
    ax.set_xlim(df.index[0].date(), df.index[-1].date())  # x軸の範囲
    fig.autofmt_xdate()  # x軸のオートフォーマット
    plt.savefig('rousokuasi_chart.png')#画像保存

if __name__ == '__main__':
    main()
