#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

	def __init__ (self):
		self.DicEtiquetas: {
			'root-layout' = ['width','height','background-color']
			'region' = ['id','top','bottom','left','rigth']
			'img' = ['src','region','begin','dur']
			'audio' = ['src','begin','dur']
			'textstream' = ['src','region']
		}
		self.atrib: []


