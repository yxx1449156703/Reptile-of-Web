import socket
import os
import sys
import struct
import mysql.connector
import pymysql
import requests
from lxml import etree
import re
import time
import datetime

def sort_data(FFS2S,sql1,sql2,sql3,sql4):
    now = datetime.datetime.now()
    date=str(now.year)+'-'+str(now.month)+'-'+str(now.day)
    list=[-1]
    for i in range(len(FFS2S)):
        mat=re.findall(r"(\d{1,2}:\d{1,2}-\d{1,2}:\d{1,2})",FFS2S[i])
        if mat:
            list.append(i)
    Sdat=date
    Edat=date
    for i in range(1,len(list)):
        start,end=FFS2S[list[i]].split('-')
        start=start+(':00')
        end=end+(':00')
        if end=='24:00:00':
            end='00:00:00'
        if (list[i]-list[i-1])==1:
            if i==1:
                begin=datetime.datetime.strptime(date+(' 20:00:00'),'%Y-%m-%d %H:%M:%S')
                sdate=datetime.datetime.strptime(date+' '+start,'%Y-%m-%d %H:%M:%S')
                if sdate>begin:
                    yesterday= datetime.date.today() + datetime.timedelta(-1)
                    Sdat=str(yesterday.year)+'-'+str(yesterday.month)+'-'+str(yesterday.day)
                else:
                    Sdat=date
            elif i==(len(list)-1):
                zero=datetime.datetime.strptime(date+(' 04:00:00'),'%Y-%m-%d %H:%M:%S')
                date=datetime.datetime.strptime(date+' '+end,'%Y-%m-%d %H:%M:%S')
                if date<zero:
                    tomorrow= datetime.date.today() + datetime.timedelta(+1)
                    Edat=str(tomorrow.year)+'-'+str(tomorrow.month)+'-'+str(tomorrow.day)
                else:
                    Edat=date
            ins = (str(now.year)+'-'+str(now.month)+'-'+str(now.day)+'/'+str(i).zfill(2), '预约', Sdat, start, Edat, end)
            cursor.execute(sql1,ins)
            db.commit()
        if (list[i]-list[i-1])==2:
            if i==1:
                begin=datetime.datetime.strptime(date+(' 20:00:00'),'%Y-%m-%d %H:%M:%S')
                sdate=datetime.datetime.strptime(date+' '+start,'%Y-%m-%d %H:%M:%S')
                if sdate>begin:
                    yesterday= datetime.date.today() + datetime.timedelta(-1)
                    Sdat=str(yesterday.year)+'-'+str(yesterday.month)+'-'+str(yesterday.day)
                else:
                    Sdat=date
            elif i==(len(list)-1):
                zero=datetime.datetime.strptime(date+(' 04:00:00'),'%Y-%m-%d %H:%M:%S')
                date=datetime.datetime.strptime(date+' '+end,'%Y-%m-%d %H:%M:%S')
                if date<zero:
                    tomorrow= datetime.date.today() + datetime.timedelta(+1)
                    Edat=str(tomorrow.year)+'-'+str(tomorrow.month)+'-'+str(tomorrow.day)
                else:
                    Edat=date
            ins = (str(now.year)+'-'+str(now.month)+'-'+str(now.day)+'/'+str(i).zfill(2), FFS2S[list[i]-1], Sdat, start, Edat, end)
            cursor.execute(sql1,ins)
            db.commit()
        elif (list[i]-list[i-1])==6:
            if i==1:
                begin=datetime.datetime.strptime(date+(' 20:00:00'),'%Y-%m-%d %H:%M:%S')
                sdate=datetime.datetime.strptime(date+' '+start,'%Y-%m-%d %H:%M:%S')
                if sdate>begin:
                    yesterday= datetime.date.today() + datetime.timedelta(-1)
                    Sdat=str(yesterday.year)+'-'+str(yesterday.month)+'-'+str(yesterday.day)
                else:
                    Sdat=date
            elif i==(len(list)-1):
                zero=datetime.datetime.strptime(date+(' 04:00:00'),'%Y-%m-%d %H:%M:%S')
                date=datetime.datetime.strptime(date+' '+end,'%Y-%m-%d %H:%M:%S')
                if date<zero:
                    tomorrow= datetime.date.today() + datetime.timedelta(+1)
                    Edat=str(tomorrow.year)+'-'+str(tomorrow.month)+'-'+str(tomorrow.day)
                else:
                    Edat=date
            ins = (str(now.year)+'-'+str(now.month)+'-'+str(now.day)+'/'+str(i).zfill(2), FFS2S[list[i]-5], FFS2S[list[i]-4], FFS2S[list[i]-3], FFS2S[list[i]-2], FFS2S[list[i]-1], Sdat, start, Edat, end)
            cursor.execute(sql2,ins)
            db.commit()
        elif (list[i]-list[i-1])==7:
            if i==1:
                begin=datetime.datetime.strptime(date+(' 20:00:00'),'%Y-%m-%d %H:%M:%S')
                sdate=datetime.datetime.strptime(date+' '+start,'%Y-%m-%d %H:%M:%S')
                if sdate>begin:
                    yesterday= datetime.date.today() + datetime.timedelta(-1)
                    Sdat=str(yesterday.year)+'-'+str(yesterday.month)+'-'+str(yesterday.day)
                else:
                    Sdat=date
            elif i==(len(list)-1):
                zero=datetime.datetime.strptime(date+(' 04:00:00'),'%Y-%m-%d %H:%M:%S')
                date=datetime.datetime.strptime(date+' '+end,'%Y-%m-%d %H:%M:%S')
                if date<zero:
                    tomorrow= datetime.date.today() + datetime.timedelta(+1)
                    Edat=str(tomorrow.year)+'-'+str(tomorrow.month)+'-'+str(tomorrow.day)
                else:
                    Edat=date
            ins = (str(now.year)+'-'+str(now.month)+'-'+str(now.day)+'/'+str(i).zfill(2), FFS2S[list[i]-6], FFS2S[list[i]-5], FFS2S[list[i]-4], FFS2S[list[i]-3], FFS2S[list[i]-2], FFS2S[list[i]-1], Sdat, start, Edat, end)
            cursor.execute(sql3,ins)
            db.commit()
        elif (list[i]-list[i-1])>7:
            if i==1:
                begin=datetime.datetime.strptime(date+(' 20:00:00'),'%Y-%m-%d %H:%M:%S')
                sdate=datetime.datetime.strptime(date+' '+start,'%Y-%m-%d %H:%M:%S')
                if sdate>begin:
                    yesterday= datetime.date.today() + datetime.timedelta(-1)
                    Sdat=str(yesterday.year)+'-'+str(yesterday.month)+'-'+str(yesterday.day)
                else:
                    Sdat=date
            elif i==(len(list)-1):
                zero=datetime.datetime.strptime(date+(' 04:00:00'),'%Y-%m-%d %H:%M:%S')
                date=datetime.datetime.strptime(date+' '+end,'%Y-%m-%d %H:%M:%S')
                if date<zero:
                    tomorrow= datetime.date.today() + datetime.timedelta(+1)
                    Edat=str(tomorrow.year)+'-'+str(tomorrow.month)+'-'+str(tomorrow.day)
                else:
                    Edat=date
            length=list[i]-list[i-1]
            ins = (str(now.year)+'-'+str(now.month)+'-'+str(now.day)+'/'+str(i).zfill(2), FFS2S[list[i-1]+1], FFS2S[list[i-1]+2], FFS2S[list[i-1]+3], FFS2S[list[i-1]+4], FFS2S[list[i-1]+5], FFS2S[list[i]-2]+FFS2S[list[i]-1], Sdat, start, Edat, end)
            cursor.execute(sql4,ins)
            db.commit()
while True:
    db = pymysql.connect("localhost","root","buzhidao","info")
    cursor = db.cursor()
    html = requests.get("http://172.18.136.23/Internal/schedulemgr/todaydynamic_listpage.jsp")
    etree_html = etree.HTML(html.text)
    FFS2S = etree_html.xpath('//table//span[text()="B737FFS_2飞行计划"]/../../../td//span/text()')
    sql1 = "REPLACE INTO Plan2(No, Plan, Sdat, Start, Edat, End) VALUES ( %s, %s, %s, %s, %s, %s)"
    sql2 = "REPLACE INTO Plan2(No, Plan, Identifier, Course, Teacher, Student, Sdat, Start, Edat, End) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sql3 = "REPLACE INTO Plan2(No, Plan, Identifier, Model, Course, Teacher, Student, Sdat, Start, Edat, End) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sql4 = "REPLACE INTO Plan2(No, Plan, Identifier, Model, Course, Teacher, Student, Sdat, Start, Edat, End) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sort_data(FFS2S,sql1,sql2,sql3,sql4)
    FFS6S = etree_html.xpath('//table//span[text()="B737FFS_6飞行计划"]/../../../td//span/text()')
    sql1 = "REPLACE INTO Plan6(No, Plan, Sdat, Start, Edat, End) VALUES ( %s, %s, %s, %s, %s, %s)"
    sql2 = "REPLACE INTO Plan6(No, Plan, Identifier, Course, Teacher, Student, Sdat, Start, Edat, End) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sql3 = "REPLACE INTO Plan6(No, Plan, Identifier, Model, Course, Teacher, Student, Sdat, Start, Edat, End) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sql4 = "REPLACE INTO Plan6(No, Plan, Identifier, Model, Course, Teacher, Student, Sdat, Start, Edat, End) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sort_data(FFS6S,sql1,sql2,sql3,sql4)
    FFS7S = etree_html.xpath('//table//span[text()="B737FFS_7飞行计划"]/../../../td//span/text()')
    sql1 = "REPLACE INTO Plan7(No, Plan, Sdat, Start, Edat, End) VALUES ( %s, %s, %s, %s, %s, %s)"
    sql2 = "REPLACE INTO Plan7(No, Plan, Identifier, Course, Teacher, Student, Sdat, Start, Edat, End) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sql3 = "REPLACE INTO Plan7(No, Plan, Identifier, Model, Course, Teacher, Student, Sdat, Start, Edat, End) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sql4 = "REPLACE INTO Plan7(No, Plan, Identifier, Model, Course, Teacher, Student, Sdat, Start, Edat, End) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sort_data(FFS7S,sql1,sql2,sql3,sql4)
    FFS8S = etree_html.xpath('//table//span[text()="B737FFS_8飞行计划"]/../../../td//span/text()')
    sql1 = "REPLACE INTO Plan8(No, Plan, Sdat, Start, Edat, End) VALUES ( %s, %s, %s, %s, %s, %s)"
    sql2 = "REPLACE INTO Plan8(No, Plan, Identifier, Course, Teacher, Student, Sdat, Start, Edat, End) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sql3 = "REPLACE INTO Plan8(No, Plan, Identifier, Model, Course, Teacher, Student, Sdat, Start, Edat, End) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sql4 = "REPLACE INTO Plan8(No, Plan, Identifier, Model, Course, Teacher, Student, Sdat, Start, Edat, End) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sort_data(FFS8S,sql1,sql2,sql3,sql4)
    MAX3S = etree_html.xpath('//table//span[text()="B737MAX_3飞行计划"]/../../../td//span/text()')
    sql1 = "REPLACE INTO Planmax3(No, Plan, Sdat, Start, Edat, End) VALUES ( %s, %s, %s, %s, %s, %s)"
    sql2 = "REPLACE INTO Planmax3(No, Plan, Identifier, Course, Teacher, Student, Sdat, Start, Edat, End) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sql3 = "REPLACE INTO Planmax3(No, Plan, Identifier, Model, Course, Teacher, Student, Sdat, Start, Edat, End) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sql4 = "REPLACE INTO Planmax3(No, Plan, Identifier, Model, Course, Teacher, Student, Sdat, Start, Edat, End) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sort_data(MAX3S,sql1,sql2,sql3,sql4)
    time.sleep(120)