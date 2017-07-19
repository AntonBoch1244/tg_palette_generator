class filters():
	def __init__(self, color):
		if type(color) == type([]):
			color = color.pop()
		self.color = color
	
	def redFilter(self):
		self.color = (self.color[0], "00", "00", self.color[3])
	
	def greenFilter(self):
		self.color = ("00", self.color[1], "00", self.color[3])
	
	def blueFilter(self):
		self.color = ("00", "00", self.color[2], self.color[3])
	
	def negative(self):
		L_color = []
		for clr in self.color[:3]:
			clr = str(hex(int(clr, 16) * -1 + 255)).replace("0x", "")
			if clr.__len__() < 2:
				clr = "0" + clr
			L_color.append(clr.replace("-", ""))
		self.color = (L_color[0], L_color[1], L_color[2], self.color[3])
	
	def gray(self):
		color = 0
		for clr in self.color[:3]:
			color += int("0x{}".format(clr), 16)
		color = str(hex(color // 3)).replace("0x", "")
		self.color = (color, color, color, self.color[3])
	
	def colorize(self, color):
		
		if type(color) == type(""):
			if color[0] == "#":
				color = color.replace("#", "")
			if color.__len__() == 6:
				color = (color[:2], color[2:2], color[4:2])
			elif color.__len__() == 8:
				color = (color[:2], color[2:2], color[4:2], color[6:2])
			else:
				raise ValueError("If are you using string you must use format RRGGBB or RRGGBBAA with or without #")
		elif type(color) == type([]):
			col = []
			for clr in color:
				if type(clr) == type(0):
					if clr > 255:
						clr = 255
					col.append(str(hex(clr)).replace("0x", ""))
				elif type(clr) == type(True):
					if clr:
						clr = 255
					else:
						clr = 0
					clr = str(hex(clr)).replace("0x", "")
					if clr.__len__() < 2:
						clr = "0" + clr
					col.append(clr)
				elif type(clr) == type(""):
					col.append(clr)
				else:
					raise ValueError("If are you using list you must use format ['RR', 'GG', 'BB'] or ['RR', 'GG', 'BB', 'AA'] or in numerical equivalent or boolean.")
			if col.__len__() == 3:
				color = (col[0], col[1], col[2])
			elif col.__len__() == 4:
				color = (col[0], col[1], col[2], col[3])
		elif type(color) == type(()):
			color = color
		else:
			raise ValueError("You must use dict or string or list.")
		index = 0
		col = []
		for clr in color:
			if clr == '':
				clr = '00'
			col.append(str(hex(int("0x"+self.color[index], 16) + int("0x" + clr, 16))).replace("0x", ""))
		try:
			col[3]
		except:
			col.append(self.color[3])
		self.color = (col[0], col[1], col[2], col[3])
	
	def __str__(self):
		clr = "#"
		for cll in self.color:
			clr += cll
		return clr
