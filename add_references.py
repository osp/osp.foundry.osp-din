#!/usr/bin/python
# -*- coding: utf-8 -*-
# Subset the current font according to a reference text

# Paste your text here
# All letters composing the text will be kept in the resulting font
Text = u"aAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬbBcCdDđĐeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆfFgGhHiIìÌỉỈĩĨíÍịỊjJkKlLmMnNoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢpPqQrRsStTuUùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰvVwWxXyYỳỲỷỶỹỸýÝỵỴzZ"

import os.path
import sys
# Change it according to your own installation of fontforge python module
sys.path.append("/home/pierre/system/lib/python2.6/site-packages/")

try:
	import fontforge
except importError:
	print "failed to import fontforge module"

def hasGlyph(font, uc):
	for g in font.glyphs():
		if g.unicode == uc:
			return True
	return False

cf = sys.argv[1]
ff = fontforge
font1 = ff.open(cf)
print(font1.encoding)
font1.encoding = "UnicodeBmp"
print(font1.encoding)

for uc in Text:
	font1.selection.none()
	#print("Load glyph [%s] with code %s %s" % (uc, hex(ord(uc)), font1.findEncodingSlot(ord(uc)) ))
	font1.selection[ord(uc)] = True
	if hasGlyph(font1, ord(uc)) == False:
		print("********Build %s" % uc)  
		font1.build()


resname = "vietnamese-"+ os.path.basename(cf)
try:
	print("GENERATE [%s]" % resname)
	font1.save(resname)
except EnvironmentError:
	print "Something went wrong when generating: "+resname

font1.close()