from time import sleep
from PIL import Image,ImageGrab

import pytesseract
import pyautogui as pag
import spacy
nlp  =spacy.load('en_core_web_md')
def rice():
    x,y = 1566,544
    x2,y2=x+1348,y+1223
    sleep(8)
    img = ImageGrab.grab([x,y,x2,y2])
    words = pytesseract.image_to_string(img)
    word_list = words.split('\n')
    while '' in word_list or ' ' in word_list or '\x0c' in word_list:
        try:
            word_list.remove('')
        except:
            pass
        try:
            word_list.remove(' ')
        except:
            pass
        try:
            word_list.remove('\x0c')
        except:
            pass
    for word in word_list:
        if ' means:' in word:
            word_list[word_list.index(word)]=word.replace(' means:','')
    main_word = word_list[0]
    word_list.pop(0)
    numero = 0
    wrd=''
    maxe =0
    for word in word_list:
        tokens = nlp(f'{main_word} {word}')
        tok1,tok2 = tokens[0],tokens[1]
        if tok1.similarity(tok2)>maxe:
            maxe=tok1.similarity(tok2)
            numero=word_list.index(word)+1
            wrd=word
    print(wrd)
    print(word_list)
    print(numero)
    p1 = (1305,450)
    p2=(1290,561)
    p3=(1235,635)
    p4=(1217,741)
    if numero==1:
        pag.moveTo(p1[0],p1[1])
        pag.click()
    if numero==2:
        pag.moveTo(p2[0],p2[1])
        pag.click()
    if numero==3:
        pag.moveTo(p3[0],p3[1])
        pag.click()
    if numero==4:
        pag.moveTo(p4[0],p4[1])
        pag.click()
for x in range(100):
    rice()
