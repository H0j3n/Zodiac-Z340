#!/usr/bin/python3
import sys,os,random,re
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
import time

#Zodiac Character (refer : Dcode)
zodiac = {
	"A" : ["char(79)","char(122)","char(108)","char(42)"],
	"B" : ["char(102)","char(95)"],
	"C" : ["char(112)"],
	"D" : ["char(65)","char(54)","char(83)"],
	"E" : ["char(66)","char(98)","char(78)","char(124)","char(52)","char(99)"],
	"F" : ["char(70)"],
	"G" : ["char(76)"],
	"H" : ["char(43)"],
	"I" : ["char(72)","char(80)","char(60)","char(121)","char(107)"],
	"J" : ["char(33)"],
	"K" : ["char(92)"],
	"L" : ["char(116)","char(100)","char(55)"],
	"M" : ["char(50)"],
	"N" : ["char(46)","char(62)","char(68)","char(89)","char(57)"],
	"O" : ["char(82)","char(94)","char(77)"],
	"P" : ["char(106)","char(56)"],
	"Q" : ["char(61)"],
	"R" : ["char(69)","char(88)","char(84)","char(49)","char(90)"],
	"S" : ["char(38)","char(85)","char(45)","char(74)"],
	"T" : ["char(37)","char(71)","char(35)","char(40)","char(58)"],
	"U" : ["char(113)","char(64)","char(47)"],
	"V" : ["char(53)"],
	"W" : ["char(87)","char(41)"],
	"X" : ["char(101)"],
	"Y" : ["char(67)","char(51)"],
	"Z" : ["char(114)"]
}

#Function Diagnol
def diagnol(x):

	col_1 = x[0] + x[9] + x[18] + x[27] + x[36] + x[45] + x[54] + x[63] + x[72] + x[81] + x[90] + x[99] + x[108] + x[117] + x[126] + x[135] + x[144]
	col_2 = x[136] + x[145] + x[1] + x[10] + x[19] + x[28] + x[37] + x[46] + x[55] + x[64] + x[73] + x[82] + x[91] + x[100] + x[109] + x[118] + x[127]
	col_3 = x[119] + x[128] + x[137] + x[146] + x[2] + x[11] + x[20] + x[29] + x[38] + x[47] + x[56] + x[65] + x[74] + x[83] + x[92] + x[101] + x[110]
	col_4 = x[102] + x[111] + x[120] + x[129] + x[138] + x[147] + x[3] + x[12] + x[21] + x[30] + x[39] + x[48] + x[57] + x[66] + x[75] + x[84] + x[93]
	col_5 = x[85] + x[94] + x[103] + x[112] + x[121] + x[130] + x[139] + x[148] + x[4] + x[13] + x[22] + x[31] + x[40] + x[49] + x[58] + x[67] + x[76]
	col_6 = x[68] + x[77] + x[86] + x[95] + x[104] + x[113] + x[122] + x[131] + x[140] + x[149] + x[5] + x[14] + x[23] + x[32] + x[41] + x[50] + x[59]
	col_7 = x[51] + x[60] + x[69] + x[78] + x[87] + x[96] + x[105] + x[114] + x[123] + x[132] + x[141] + x[150] + x[6] + x[15] + x[24] + x[33] + x[42]
	col_8 = x[34] + x[43] + x[52] + x[61] + x[70] + x[79] + x[88] + x[97] + x[106] + x[115] + x[124] + x[133] + x[142] + x[151] + x[7] + x[16] + x[25]
	col_9 = x[17] + x[26] + x[35] + x[44] + x[53] + x[62] + x[71] + x[80] + x[89] + x[98] + x[107] + x[116] + x[125] + x[134] + x[143] + x[152] + x[8]
	return col_1+";"+col_2+";"+col_3+";"+col_4+";"+col_5+";"+col_6+";"+col_7+";"+col_8+";"+col_9

#Function Dcode Symbol
def zodiac_cipher(x):
	print("\nPlease Enter this in Dcode!\n")
	strs =""
	for i in x.split(";"):
        	for j in i:
                	if j in zodiac.keys():
                        	strs += random.choice(zodiac[j])
                	else:
                        	strs += j
        	strs += "\n"
	return strs

#Function Font Changes
def font_change(x):
	strs =""
	for i in x.split("\n")[:-1]:
		temp = i.replace(")",";").replace("char(",";").replace(";;",";")
		for j in temp.split(";"):
			try:	
				if int(j) in [1,2,3,4,5,6,7,8,9,0]:
					strs += j
				else:
					strs += chr(int(j))
			except:
				strs += j
		strs += "\n"
	return strs
 
inputs = str(sys.argv[1]).replace(" ","").strip().upper()

#Check length
lenInputs = len(inputs)
print(f"\n[Length of Sentence {lenInputs}/306 !]")
if lenInputs < 306:
	print("\nEnter some more!")
	exit(-1)
elif lenInputs > 306:
	print("\nReduce some more!")
	exit(-1)

print("\nBox 1 : ",end="")
print(inputs[:153],"\n")
box1 = diagnol(inputs[:153])
for i in box1.split(";"):
        print(i)
dcode1 = zodiac_cipher(box1)
print(dcode1)
fontchange1 = font_change(dcode1)

print("\n\nBox 2 : ",end="")
print(inputs[153:],"\n")
box2 = diagnol(inputs[153:])
for i in box2.split(";"):
	print(i)
dcode2 = zodiac_cipher(box2)
print(dcode2)
fontchange2 = font_change(dcode2)

print("\n[Full Dcode]\n")
fulldcode = dcode1 + dcode2
print(fulldcode)

print("\n[Full Font Code]\n")

print("Please Use it in here : http://zodiackillerciphers.com/cipher-explorer/\n")
fullfontcode = fontchange1+fontchange2
print(fullfontcode)

#Create Image
## Make canvas and set the color
img = np.zeros((1050,420,3),np.uint8)
b,g,r,a = 0,255,0,0

## Use simsum.ttc to write Chinese.
fontpath = "./z340-z408.ttf"
font = ImageFont.truetype(fontpath, 32)
img_pil = Image.fromarray(img)
draw = ImageDraw.Draw(img_pil)
h=100
for i in fullfontcode.split("\n"):
	draw.text((50, h), i.strip(), font = font, fill = (b, g, r, a))
	h += 50
img = np.array(img_pil)

## Display 
cv2.imwrite("zodiac.png", img)
