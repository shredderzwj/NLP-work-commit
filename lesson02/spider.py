# -*- coding: utf-8 -*-


import requests
from lxml import etree


def parse(url):
	header = {
		'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
	}
	response = requests.get(url, headers=header, verify=False)
	text = response.content.decode(encoding='utf-8')
	html = etree.HTML(text)
	lines = html.xpath('//l')
	for line in lines:
		line_name = line.xpath('./@lb')[0]
		line_id = line.xpath('./@lnub')[0]
		stations = line.xpath('./p')
		station_info = {}
		for station in stations:
			try:
				station_name = station.xpath('./@lb')[0]
				station_number = station.xpath('./@n')[0]
				station_x_coord = station.xpath('./@x')[0]
				station_y_coord = station.xpath('./@y')[0]
				station_arr = station.xpath('./@arr')[0]
				if station_arr == '0':
					station_info[station_name] = [line_name]

				print(line_name, station_number, station_name, station_x_coord, station_y_coord, station_arr)
			except:
				pass


if __name__ == '__main__':
	url = 'https://map.bjsubway.com/subwaymap/beijing.xml'
	parse(url)
