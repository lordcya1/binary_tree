
# check type: isinstance(s, basestring); isinstance(b, int). and return the boolen
class People:

	def __init__(self, name , father= "" , children = [] ,spouse = "", gender = "male", generation = 0):
		self.name = name
		self.father = father
		self.children = children
		self.spouse = spouse
		self.gender = gender
		self.generation = generation
		self.blank = 20



	#accessors:
	def getName(self):
		return self.name

	def getFather(self):
		return self.father

	def getChildren(self):
		for c in self.children:
			return c

	def getSpouse(self):
		return self.spouse

	def getGender(self):
		return self.gender

	def getGeneration(self):
		return self.generation

	def __str__(self):
		if self.father != "":
			return "-"*(blank+11) + "\n" + "| Name:   "+ self.name + " "*(blank - len(self.name)) + "|" + "\n" + "| Father: "+ self.father + " "*(blank - len(self.father)) + "|"
		else:
			return "-"*(blank+11) + "\n" + "| Name:   "+ self.name + " "*(blank - len(self.name)) + "|" 


	#modifiers:
	def setName(self, name):
		self.name = name

	def setFather(self,father):
		self.father = father

	def setSpouse(self, spouse):
		self.spouse = spouse

	def setGender(self, gender):
		self.gender = gender

	def addChild(self, child):
		if child not in self.children:
			self.children.append(child)

	def setGeneration(self, generation):
		self.generation = generation

	def test(self):
		print "| Name: "+ self.name
		print "| Spouse: "+ self.spouse
		print "| gender: " + self.gender


def isFatherSon(father, son): #see if argu 1 is the father of argu 2
	if father.getName() == son.getFather() :
		return True
	else:
		return False



#main()
blank = 20
WHH = People("Haohua Wang","Shilai Wang") #me

WSL = People("Shilai Wang", "Zhihou Wang")  #dad
WSL.setSpouse("Qiuju Teng")

WJH = People("Zhihou Wang", "Zhengong Wang") #grandpa
WJH.setSpouse("Ding")

WD = People("Dong Wang", "Shigui Wang")

WSG = People("Shigui Wang", "Zhihou Wang")
WSG.setSpouse("Teng")

WZG = People("Zhengong Wang")


bucket = [WHH, WSL, WJH, WD, WSG, WZG]

for x in bucket:
	print x
	if x.getSpouse() != "":
		print "| Spouse: " + x.getSpouse() + " "*(blank - len(x.getSpouse())) +"|"


print isFatherSon(WSL, WHH)


'''
WHH.test()
print WHH
'''



