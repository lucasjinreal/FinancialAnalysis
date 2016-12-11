import pandas as pd


sh_a = pd.read_csv('shangzheng_a_stock.csv', decimal=',')
# drop the last columns
sh_a = sh_a.ix[:, :-1]
print(sh_a.head(5))
sz_a = pd.read_csv('shenzheng_a_stock.csv', decimal=',')

same_index = ['公司代码', '公司简称', 'A股代码', 'A股简称',
              'A股上市日期', 'A股总股本', 'A股流通股本']
sz_a_merge = sz_a[same_index]
print(sz_a_merge.head(5))
