# -*- coding: utf-8 -*-
import datetime
import math
import random
import string

def my_view(request):
    return {'project':'newproject'}

def home_view(request):
  img = ("capricornio.jpg","acuario.jpeg","piscis.png","aries.jpeg","tauro.jpeg","geminis.jpeg","cancer.jpeg","leo.jpeg","virgo.jpg","libra.jpeg","escorpio.jpg","sagitario.jpeg")
  pictures = len(img)
  dia_zodiacal = (20,19,20,20,21,21,22,22,22,22,22,21)
  
  fecha = request.POST.get("fecha")
 
  if not fecha:
    return {"img":img,"pictures":pictures}
 
  year, month, day = map(int, fecha.split('-'))
  datas = datetime.date(year,month,day)
  dia = datas.day
  mes = datas.month
  mes = mes-1
  
  if dia > dia_zodiacal[mes]:
    mes = mes + 1
  if mes == 12:
    mes = 0
 
  return {"img":img,"pictures":pictures,"zodiac":img[mes]}