#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.lista = []
        self.DicEtiquetas = {
            'root-layout': ['width', 'height', 'backgroundcolor'],
            'region': ['id', 'top', 'bottom', 'left', 'rigth'],
            'img': ['src', 'region', 'begin', 'dur'],
            'audio': ['src', 'begin', 'dur'], 'textstream': ['src', 'region']}

    def startElement(self, name, attrs):
        if name in self.DicEtiquetas:
            dicc = {}
            for atributo in self.DicEtiquetas[name]:
                dicc[atributo] = attrs.get(atributo, "")
            diccname = {name: dicc}
            self.lista.append(diccname)

    def get_tags(self):
        return self.lista

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())
