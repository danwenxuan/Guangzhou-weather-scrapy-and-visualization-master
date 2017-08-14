# encoding: utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
inputpath = r'D:\scrapywork\guangzhouweather\newgzweather.csv'


def converttoint(series11):
	datalist = [int(x) for x in series11.tolist()]
	# series = pd.Series(datalist, series11.index)
	return datalist


if __name__ == '__main__':
	df = pd.read_csv(inputpath, header=None,
	                 names=['maxtemp', 'power', 'mintemp', 'weather', 'wind'])
	series11 = df.loc['2011-12-01':'2011-12-31', 'mintemp']
	series12 = df.loc['2012-12-01':'2012-12-31', 'mintemp']
	series13 = df.loc['2013-12-01':'2013-12-31', 'mintemp']
	series14 = df.loc['2014-12-01':'2014-12-31', 'mintemp']
	series15 = df.loc['2015-12-01':'2015-12-31', 'mintemp']
	series11h = df.loc['2011-12-01':'2011-12-31', 'maxtemp']
	series12h = df.loc['2012-12-01':'2012-12-31', 'maxtemp']
	series13h = df.loc['2013-12-01':'2013-12-31', 'maxtemp']
	series14h = df.loc['2014-12-01':'2014-12-31', 'maxtemp']
	series15h = df.loc['2015-12-01':'2015-12-31', 'maxtemp']
	fig = plt.figure()
	list11 = converttoint(series11)
	list12 = converttoint(series12)
	list13 = converttoint(series13)
	list14 = converttoint(series14)
	list15 = converttoint(series15)
	plt.plot(range(31), list11, label='2011')
	plt.plot(range(31), list12, label='2012')
	plt.plot(range(31), list13, label='2013')
	plt.plot(range(31), list14, label='2014')
	plt.plot(range(31), list15, label='2015')
	plt.xlabel('12-01 to 12-31')
	plt.ylabel('tempature')
	plt.title('tempature variation in past 5 years')
	plt.legend(loc='best')
	plt.show()
	# series11.plot(style='b')
	# fig.autofmt_xdate()
	# plt.show()
	# series12.plot(style='b')
	# fig.autofmt_xdate()
	# plt.show()
	# series13.plot(style='b')
	# fig.autofmt_xdate()
	# plt.show()
	# series14.plot(style='b')
	# fig.autofmt_xdate()
	# plt.show()
	# series15.plot(style='b')
	# fig.autofmt_xdate()
	# plt.show()
	m11 = np.array(list11).mean()
	m12 = np.array(list12).mean()
	m13 = np.array(list13).mean()
	m14 = np.array(list14).mean()
	m15 = np.array(list15).mean()
	meantemps = [m11, m12, m13, m14, m15]
	m11h = np.array(converttoint(series11h)).mean() - m11
	m12h = np.array(converttoint(series12h)).mean() - m12
	m13h = np.array(converttoint(series13h)).mean() - m13
	m14h = np.array(converttoint(series14h)).mean() - m14
	m15h = np.array(converttoint(series15h)).mean() - m15
	meantemphs = [m11h, m12h, m13h, m14h, m15h]
	std11 = np.array(list11).std()
	std12 = np.array(list12).std()
	std13 = np.array(list13).std()
	std14 = np.array(list14).std()
	std15 = np.array(list15).std()
	stdtemps = [std11, std12, std13, std14, std15]
	std11h = np.array(converttoint(series11h)).std()
	std12h = np.array(converttoint(series12h)).std()
	std13h = np.array(converttoint(series13h)).std()
	std14h = np.array(converttoint(series14h)).std()
	std15h = np.array(converttoint(series15h)).std()
	stdtemphs = [std11h, std12h, std13h, std14h, std15h]
	ind = np.arange(5)
	width = 0.35
	p1 = plt.bar(ind, meantemps, width, color='r', yerr=stdtemps)
	p2 = plt.bar(ind, meantemphs, width, color='y',
	             bottom=meantemps, yerr=stdtemphs)
	plt.ylabel('tempature')
	plt.title('mean of mintempature and mean of maxtempature in past 5 years')
	plt.xticks(ind + width/2., ('2011', '2012', '2013', '2014', '2015'))
	plt.legend((p1[0], p2[0]), ('mintempature', 'delttempature'))
	plt.show()
