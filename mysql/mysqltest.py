#!/usr/bin/env python
# --coding:utf-8--
import pymysql


def hello_mysql_or_mariadb():
    db = pymysql.connect(host='192.168.88.3', user='root', password='p@ssw0rd', database='caden', port=3306)
    cursor = db.cursor()
    cursor.execute('SELECT VERSION()')

    data = cursor.fetchone()
    print('my database version is {}'.format(data[0]))
    db.close()


if __name__ == '__main__':
    hello_mysql_or_mariadb()
