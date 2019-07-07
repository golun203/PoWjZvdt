import os, csv, sys, random, string
import numpy as np
from scipy import stats

class CsvHandle:
    def __init__(self):
        folderpath = "./ilovecoffee"
        try:
            os.mkdir(folderpath)
        except FileExistsError:
            print('檔案已經存在')
        except PermissionError:
            print("權限不足。")

    def creat_csv(self):
        cid = 0
        cname = 0
        cmobile = 0
        fc = 0
        data_n = 500
        pnlist = list()
        fnlist = list()
        samlst = list()
        #創造不重複隨機大小比預設資料量大的list
        while True:
            rpn = ''.join(random.choice(string.digits) for x in range(9))
            pnlist.append(rpn)
            if len(pnlist) > (2*data_n):
                fnlist = list(set(pnlist))
                if len(fnlist) > (data_n + 100):
                    break

        filepath = './ilovecoffee/customers.csv'
        if not os.path.isfile(filepath):
            with open ('./ilovecoffee/customers.csv', 'w', newline = '') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['customer_id', 'customer_name', 'customer_mobile', 'frequency'])

        with open ('./ilovecoffee/customers.csv', 'a', newline = '') as csvfile:
            writer = csv.writer(csvfile)
            samlst = random.sample(fnlist, data_n)
            for i in range(0,(data_n)):
                cid = random.choice(string.ascii_letters) + ''.join(random.choice(string.ascii_letters + string.digits) for x in range(7))
                cname = random.choice(['David','Woody','Louis','Freeze','Deep','Henry','Rudolf','Dennis','John','Firen']) + '.' + cid
                cmobile = '+886' + str(samlst[i])
                fc = random.randint(0,20)

                writer.writerow([cid,cname,cmobile,fc])



    def calculate_csv(self):
        if os.path.isfile('./ilovecoffee/customers.csv'):
            fclist =list()
            with open('./ilovecoffee/customers.csv', newline = '') as csvfile:
                rows = csv.reader(csvfile)

                for row in rows:
                    if row[3] != 'frequency':
                        fclist.append(int(row[3]))
                fcmean = np.mean(fclist)
                fcmedian = np.median(fclist)
                fcmode = stats.mode(fclist)[0][0]

                print('平均值:', fcmean, '中位數:', fcmedian, '眾數:', fcmode)

a = CsvHandle()
a
a.creat_csv()
a.calculate_csv()
