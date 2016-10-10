#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
from urllib.request import urlretrieve

class KaraokeLocal(SmallSMILHandler):

    def __init__ (self, fichero):

        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        try:
            parser.parse(open(sys.argv[1]))
        except:
            sys.exit('Usage: python3 karaoke.py file.smil')

        self.lista = cHandler.get_tags()


    def to_json(self,fichero, name = ""):
        lista_json= json.dumps(self.lista)
        if name == "":
            name = sys.argv[1].split('.')[0] + '.json'
        with open(sys.argv[1][:-5]+".json", 'w') as ficher_json:
            json.dump(self.lista, ficher_json,indent=4,separators=(',', ': ')) 


    def __str__(self):

        doc = ""
        for linea in self.lista:
            for name in linea:
                doc = doc + name 
                for name2 in linea[name]:
                    doc = doc + "\t" + name2 +' = ' + '"' + linea[name][name2] + '"' 
                doc = doc + "\n"

        print(doc)

    def do_local(self):

       for linea in self.lista:
            for name in linea:
                for name2 in linea[name]:
                    if linea[name][name2][0:7] == "http://":
                        print(linea[name][name2])
                        urlretrieve(linea[name][name2])

if __name__ == "__main__":

    try:
        obj_karaokelocal = KaraokeLocal(sys.argv[1])
    except:
        sys.exit('Usage: python3 karaoke.py file.smil')

    obj_karaokelocal.__str__()
    obj_karaokelocal.to_json(sys.argv[1])
    obj_karaokelocal.do_local()
    obj_karaokelocal.to_json(sys.argv[1], 'local.json')
    obj_karaokelocal.__str__()




