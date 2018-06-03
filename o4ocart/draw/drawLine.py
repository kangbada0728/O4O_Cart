from PIL import Image, ImageDraw, ImageFont
import datetime
import aggdraw
import unittest
import os

#import os
import json
from django.http import HttpResponse

'''
#im = Image.new('RGBA', (400, 400), (0, 255, 0, 0))
script_path = os.getcwd()
#o4ocart 폴더(앱있는곳)
print(script_path)
path= os.path.join(script_path,"draw","sources" ,"martmap_source.png" ).replace('\\', '/')
font_path = os.path.join(script_path,"draw","sources" ,"NanumBarunGothicLight.ttf" ).replace('\\', '/')


im = Image.open(path).convert("RGBA")
font_order = ImageFont.truetype(font_path,10)
font_time = ImageFont.truetype(font_path,10)

drawT = ImageDraw.Draw(im)
draw = aggdraw.Draw(im)
'''

#im = Image.new('RGBA', (400, 400), (0, 255, 0, 0))
script_path = os.getcwd()
#o4ocart 폴더(앱있는곳)
print(script_path)
path= os.path.join(script_path,"draw","sources" ,"martmap_source.png" ).replace('\\', '/')
font_path = os.path.join(script_path,"draw","sources" ,"NanumBarunGothicLight.ttf" ).replace('\\', '/')


im = Image.open(path).convert("RGBA")
font_order = ImageFont.truetype(font_path,10)
font_time = ImageFont.truetype(font_path,10)

drawT = ImageDraw.Draw(im)
draw = aggdraw.Draw(im)


def getXY(data_json):
    #time을 timestamp로 정수화하여 표시한다.

    '''
    베지어 커브를 그릴것이라면 점이 네개 이상 필요하다
    일단 4의 배수를 더미데이터로 집어넣고,
    다음 개발에서 경우의 수 나누는 것을 생각하자.
    //4의 배수가 아니어도 그려지는듯
    '''

    #print(os.path.dirname( os.path.abspath( __file__ ) ))
    list_data = data_json["data"]
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(list_data)
    return(list_data)
    #x는 list이다
    #print(type(x))

    #print(len(x))
    #개수만큼 길이 나온다

    #print(type(x[0]))
    #이건 dict

    #print(x[0]["x"]) 이렇게 넘기면 받은 json에 대해서 x값을 뽑을 수 있다

    #print(s_sorted)
    #showImage(x)

def drawTime(_list_xy):

    font_order = ImageFont.truetype(font_path,10)
    font_time = ImageFont.truetype(font_path,10)
    for xy_order in range(0, len(_list_xy)):
        str_xy_order = str(xy_order)
        str_time = str(_list_xy[xy_order]["time"])
        print(str_time)
        time_hour = datetime.datetime.fromtimestamp(_list_xy[xy_order]["time"]).hour
        time_min = datetime.datetime.fromtimestamp(_list_xy[xy_order]["time"]).minute
        time_sec = datetime.datetime.fromtimestamp(_list_xy[xy_order]["time"]).second
        str_time = str(time_hour)+"시 "+str(time_min)+"분 "+str(time_sec)+"초"
        print(str_time)
        drawT.text((_list_xy[xy_order]["x"],_list_xy[xy_order]["y"]),str_xy_order ,fill = (0,0,255), font = font_order)
        drawT.text((_list_xy[xy_order]["x"],_list_xy[xy_order]["y"]+50),str_time ,fill = (0,0,255), font = font_time)



def showImage(_list_xy):
    '''
    font_order = ImageFont.truetype('C:\\NanumBarunGothicLight.ttf',20)
    font_time = ImageFont.truetype('C:\\NanumBarunGothicLight.ttf',10)
    #im = Image.new('RGBA', (400, 400), (0, 255, 0, 0))
    im = Image.open('C:\map.png').convert("RGBA")
    drawT = ImageDraw.Draw(im)
    draw = aggdraw.Draw(im)
    '''
    print(_list_xy)
    pen = aggdraw.Pen((190,150,130))
    brush = aggdraw.Brush((190,150,110))
    outline = aggdraw.Pen((190,170,130),5)


    for xy_order in range(0, int((len(_list_xy)-1)/3)):
        #ezier = "m 0,0 t"
        for coordintes in range(0, 3):
            p0_x = _list_xy[xy_order*3]["x"]
            p0_y = _list_xy[xy_order*3]["y"]
            draw.ellipse((p0_x-10,p0_y-10,p0_x+10,p0_y+10),brush)
            p0 = str(p0_x)+","+str(p0_y)
            p1 = str(_list_xy[xy_order*3+1]["x"]-p0_x)+","+str(_list_xy[xy_order*3+1]["y"]-p0_y)+","
            p2 = str(_list_xy[xy_order*3+2]["x"]-p0_x)+","+str(_list_xy[xy_order*3+2]["y"]-p0_y)+","
            p3 = str(_list_xy[xy_order*3+3]["x"]-p0_x)+","+str(_list_xy[xy_order*3+3]["y"]-p0_y)
            draw.ellipse((p0_x-3,p0_y-3,p0_x+3,p0_y+3),pen)

        bezier = "m " + p0 +"c "+p1+p2+p3
        print(bezier)
        symbol = aggdraw.Symbol(bezier)
        draw.symbol((0,0), symbol, outline)

    draw.flush()
    drawTime(_list_xy)
    im.show()
    im.save('draw\\result\\out.png')

def drawPoints(list_xy):
    print("drawPoints")
    print(list_xy)
    pen = aggdraw.Pen((190,150,130))
    brush = aggdraw.Brush((190,150,110))
    outline = aggdraw.Pen((190,170,130),5)
    for xy_order in range(0, (len(list_xy))):
        p_x = list_xy[xy_order]["x"]
        p_y = list_xy[xy_order]["y"]
        draw.ellipse((p_x-10,p_y-10,p_x+10,p_y+10),brush)
    draw.flush()
    drawTime(list_xy)
    #im.show()
    im.save('draw\\result\\out.png')

def visualize(data_json):
    im = Image.open(path).convert("RGBA")
    drawT = ImageDraw.Draw(im)
    draw = aggdraw.Draw(im)
    print("visualize")
    #list_xy = getXY(data_json)
    list_xy = data_json
    #showImage(list_xy)
    drawPoints(list_xy)
  #  print(os.getcwd())
