#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# gdp_growth_basic.py
#
# 使用純 Python 3：
# 1. 使用 csv 模組讀取資料
# 2. 資料存成 list + dict
# 3. 以表格方式輸出
#
# 無使用 pandas、無繪圖

import csv

def read_gdp_data(csv_path):
    data = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # 讀掉標題列
        for row in reader:
            record = {
                'country': row[0],
                'year': int(row[1]),
                'gdp_growth': float(row[2])
            }
            data.append(record)
    return data

def print_table(data):
    # 印標題列
    print(f"{'Country':15} {'Year':>6} {'GDP_Growth':>12}")
    print("-" * 35)

    # 一列列印
    for record in data:
        print(f"{record['country']:15} {record['year']:6d} {record['gdp_growth']:12.1f}")

def main():
    csv_path = "gdp_growth_top10_plus_taiwan.csv"
    data = read_gdp_data(csv_path)

    print("資料筆數：", len(data))
    print()
    print_table(data)

if __name__ == "__main__":
    main()
