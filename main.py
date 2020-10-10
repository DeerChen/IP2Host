'''
Description: ip反查域名
Author: Senkita
Date: 2020-10-09 10:23:52
LastEditors: Senkita
LastEditTime: 2020-10-09 15:01:39
'''
import os
from utils.Query import batch_query

if __name__ == "__main__":
    os.makedirs('./Log', exist_ok=True)

    filename = 'public.txt'
    save_filename = 'domain_name.txt'
    batch_query(filename, save_filename)
