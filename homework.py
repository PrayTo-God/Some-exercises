# -*- coding = utf-8 -*-
# @Time : 2021-08-05 11:55
# @Author : PrayTo_God
# @File : homework.py
# @Software : PyCharm

'''
products =[["iphone", 6888], ["MacPro", 14800], ["小米6", 2499], ["Coffee", 31], ["Book", 60], ["Nike", 699]]
print("-"*20 + "商品列表" + "-"*20 )
for i in range(len(products)):
    print(i, products[i][0] , products[i][1])
'''


products =[["iphone", 6888], ["MacPro", 14800], ["小米6", 2499], ["Coffee", 31], ["Book", 60], ["Nike", 699]]
print("-"*20 + "商品列表" + "-"*20 )
for i in range(len(products)):
    print(i, end='\t')
    for j in range(len(products[i])):
        if j == 0:
            print(products[i][j], end='\t')
        if j != 0:
            print(products[i][j], end='\n')

Shopping_Care = []
while True:
    commodity = input("请问您需要什么？输入商品编号即可。")
    if commodity == 'q':
        break
    Selected_items = int(commodity)
    Shopping_Care.append(Selected_items)

print("您购买的商品是：", "-"*30)
for i in range(len(Shopping_Care)):
    print(products[Shopping_Care[i]][0])