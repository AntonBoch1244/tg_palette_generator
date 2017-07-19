import pprint
from filters import filters
import re

palette = file("colors.tdesktop-palette")
paletteOut = file("colors1.tdesktop-palette", 'w')

p_read = palette.read()
p_read = p_read.split("\n")
p_read.remove('')

plte = {}
for p_line in p_read:
	KV = p_line.split('//')[0].replace(" ", "").split(";")[0].split(":")
	plte.update({KV[0]:KV[1]})

p_plte = {}
for nop in range(0, 10):
	for EV in plte.keys():
		KL = EV
		VL = plte.get(EV)
		for KTest in plte.keys():
			if VL == KTest:
				VL = plte.get(KTest)
		p_plte.update({ KL: VL })
	plte = p_plte

p_plte = {}
for EV in plte.keys():
	col = plte.get(EV)
	col = col.replace("#", "")
	color = re.findall("(..)(..)(..)(..|)", col)
	color = filters(color)
	color.gray()
	color.colorize(("aa", "00", "00"))
	color = color.__str__()
	p_plte.update({EV:color})
plte = p_plte

for EV in plte.keys():
	paletteOut.write("{}: {};".format(EV, plte.get(EV)))
paletteOut.write("\n")

paletteOut.close()
