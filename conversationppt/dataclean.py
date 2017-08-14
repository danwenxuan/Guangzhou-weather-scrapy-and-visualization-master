# encoding: utf-8
import pandas as pd
filename = r'D:\scrapywork\guangzhouweather\gzweather.csv'
outpath = r'D:\scrapywork\guangzhouweather\newgzweather.csv'


if __name__ == '__main__':
	df = pd.read_csv(filename, header=None)
	print '先看一下'
	print df.head()
	df.columns = df.loc[0]
	df = df.drop(0)
	df.index = df['date'].values
	df = df.sort_index()
	print '排序调整一下'
	print df.head()
	df = df.drop_duplicates()
	df = df.drop('date', axis=1)
	df = df.dropna(how='any')
	print '最后'
	print df.head()
	df.to_csv(outpath)
