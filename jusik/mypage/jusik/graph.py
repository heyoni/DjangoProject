import urllib.request
import xml.etree.ElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


def get_graph(stock_code):
    code = stock_code
    count = '30'
    url = f'https://fchart.stock.naver.com/sise.nhn?symbol={code}&timeframe=day&count={count}&requestType=0'

    r = urllib.request.urlopen(url)
    xml_data = r.read().decode('EUC-KR')
    root = ET.fromstring(xml_data)
    data_list = []

    for each in root.findall('.//item'):
        temp = each.attrib['data'].split('|')
        temp[1] = int(temp[1])
        temp[2] = int(temp[2])
        temp[3] = int(temp[3])    
        temp[4] = int(temp[4])    
        temp[5] = int(temp[5])
        if temp[0] >= '19900302':
            data_list.append(temp)
            
    column_list = ['날짜','시가','고가','저가','종가','거래량']
    df = pd.DataFrame(data_list, columns=column_list)


    plt.figure(figsize=(15,10))
    plt.xticks(rotation=45)
    plt.plot(df['날짜'],df['종가'])
    plt.savefig('static/plot.png', dpi=300)