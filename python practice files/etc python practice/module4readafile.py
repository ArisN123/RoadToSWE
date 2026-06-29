
import csv 


watchlist = r'C:\Users\aris123\Desktop\python_practice\demo files\sample_watchlist_module4.csv'

with open(watchlist,"r", encoding="utf-8") as watchlist_file:
    content = csv.reader(watchlist_file)
    for x in content:
        print(x)
        