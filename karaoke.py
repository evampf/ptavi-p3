#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
from urllib.request import urlretrieve


#class Karaoke():

def Crear_Json(doc):
    with open(sys.argv[1][:-5]+".json", 'w') as outfile:
        json.dump(doc, outfile,indent=4,separators=(',', ': ')) 


def Formato_Lista(Lista):

    doc = ""
    for linea in Lista:
        for name in linea:
            doc = doc + name 
            for name2 in linea[name]:
                doc = doc + "\t" + name2 +' = ' + '"' + linea[name][name2] + '"' 
            doc = doc + "\n"

    print(doc)

def Descarga_Contenido(Lista):

   for linea in Lista:
        for name in linea:
            for name2 in linea[name]:
                if linea[name][name2][0:7] == "http://":
                    print(linea[name][name2])
                    urlretrieve(linea[name][name2])

if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    
    try:
        parser.parse(open(sys.argv[1]))
    except:
        sys.exit('Usage: python3 karaoke.py file.smil')


    Crear_Json(cHandler.get_tags())
    Formato_Lista(cHandler.get_tags())
    Descarga_Contenido(cHandler.get_tags())
    