# -*- coding:utf8 -*-
# !/usr/bin/python
# Python:          2.7.8
# Platform:        Windows
# Program:         端口扫描

import socket, time, thread
import sys
import pymysql.cursors
import datetime
socket.setdefaulttimeout(3)


def socket_port(ip, port):
    """
    输入IP和端口号，扫描判断端口是否开放
    """
    try:
        if port >= 65534:
            print u'端口扫描结束'
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, port))
        if result == 0:
            lock.acquire()
            print  ip, u':', port, u'open'
            connection = pymysql.connect(host='localhost', port=3306, user='localhost', password='', db='localhost',
                                         charset='utf8', cursorclass=pymysql.cursors.DictCursor)
            cursor = connection.cursor()
            sql = "INSERT INTO PlatformPortDetection (IP,CompanyName,Port,Result,Datetime) VALUES ('" + str(ip) + "','" + str(port) + "','" + str(port) + "','" + str(result) + "','" + datetime.datetime.now().strftime("%Y-%m-%d") + "')"
            cursor.execute(sql)
            connection.commit()
            lock.release()
        s.close()
    except Exception, e:
        print str(e)



def ip_scan(ip):
    """
    输入IP，扫描IP的0-65534端口情况
    """
    try:
        print u'开始扫描 %s' % ip
        start_time = time.time()
        for i in range(0, 65534):
            thread.start_new_thread(socket_port, (ip, int(i)))
        print u'扫描端口完成，总共用时 ：%.2f' % (time.time() - start_time)

    except:
        print u'扫描ip出错'


if __name__ == '__main__':
    #url = raw_input('Input the ip you want to scan:\n')
    lock = thread.allocate_lock()
    ipall = '10.18.2.25'
    ip_scan(ipall)
    time.sleep(120)
