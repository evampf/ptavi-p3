#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler

#class Karaoke():

def Crear_Json(doc):
    with open(sys.argv[1][:-5]+".json", 'w') as outfile:
        json.dump(doc, outfile,indent=4,separators=(',', ': ')) 


def Formato_Lista(Lista):

    doc = ""
    for linea in Lista:
        for name in linea:
            doc = doc + name + "\t"
            for name2 in linea[name]:
                doc = doc + name2 +'=' + linea[name][name2] + '"' + "\t"
            doc = doc + "\n"
    print (doc)


if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    try:
        parser.parse(open(sys.argv[1]))
    except:
        sys.exit('Usage: python3 karaoke.py file.smil')

    print(cHandler.get_tags())
    Crear_Json(cHandler.get_tags())
    Formato_Lista(cHandler.get_tags())

    