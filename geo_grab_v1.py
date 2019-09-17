import urllib.request
import re

# https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE98165


def extract_information(lines, items):
    current = None
    dic = {item: '' for item in items}
    for line in lines:
        if current is not None:
            if re.search('<td>.*</td>', line):
                l = re.sub('<td>', '', line)
                l = re.sub('</td>', '', l)
                dic[current] = l
            current = None

        if re.search('<tr valign="top"><td>.*</td>', line):
            l = re.sub('<tr valign="top"><td>', '', line)
            l = re.sub('</td>', '', l)
            if l in items:
                current = l
    return dic


info = ['Status', 'Title', 'Organisms', 'Experiment type', 'Summary', ]
for idx in range(98160, 98170):
    url = f"https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE{idx}"
    try:
        # 请求
        request = urllib.request.Request(url)
        # 爬取结果
        response = urllib.request.urlopen(request)
        data = response.read()
        data = data.decode('utf-8')
        print('Success in: ', idx)

        lines = str(data).split('\n')
        file = open(f'{idx}.txt', 'w')



    except:
        print('Fail in: ', idx)
        continue



