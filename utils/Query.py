'''
Description: ip反查域名
Author: Senkita
Date: 2020-10-09 13:37:17
LastEditors: Senkita
LastEditTime: 2020-10-09 15:05:22
'''
import requests
from fake_useragent import UserAgent
from IPy import IP
from utils.Err import Error
from utils.ProgressBar import progress_bar
from utils import logger


def query_host(ip_addr, save_filename):
    """
    description: ip反查域名
    param {str} ip_addr - [ip地址]
    return {type}
    author: Senkita
    """
    # 伪装浏览头
    ua = UserAgent().random
    headers = {'user-agent': ua}
    try:
        response = requests.get(
            url='http://api.webscan.cc/?action=query&ip={}'.format(ip_addr),
            headers=headers,
        )
        if response.text != 'null':
            results = response.json()
            for result in results:
                domain_name = result['domain']

                msg = '{} - {}'.format(ip_addr, domain_name)

                logger.info(msg)
                with open(save_filename, 'a') as f:
                    f.write(domain_name)
                    f.write('\n')
        else:
            msg = '{} - Cannot find domain name.'.format(ip_addr)
            logger.warning(msg)
    except Exception as e:
        logger.error(e)
        raise Error('Unable to connect to API.')


def isPublic(ip_addr):
    """
    description: 检测是否公有ip
    param {str} ip_addr - [ip地址]
    return {bool} 是否为公有ip
    author: Senkita
    """
    if IP(ip_addr).iptype() == 'PUBLIC':
        return True
    logger.warning('{} - Private.'.format(ip_addr))
    return False


def batch_query(filename, save_filename):
    """
    description: 批量查询
    param {str} filename - [文件名]
          {str} save_filename - [保存文件名]
    return {type}
    author: Senkita
    """
    with open(filename, 'r') as f:
        portion = 0
        length = len(f.readlines())
        # 指针指回文件开头
        f.seek(0)

        ip_addr = f.readline().replace('\n', '')

        while ip_addr:
            if isPublic(ip_addr):
                query_host(ip_addr, save_filename)

            ip_addr = f.readline().replace('\n', '')

            portion += 1
            progress_bar(portion, length)
