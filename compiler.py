#!/usr/bin/python3

"""

"""
# the result will be in a file named output.txt
# change input file by changing the open argument to the desired file in line 22
reservedWords = ['abstract','do','if','else','private','protected','this','class','assert','double','int','double','implements'
				,'throw','throws','boolean','public','break','enum','instanceof','return','transient','case','byte'
				,'extends','interface','static','try','strictfp','void','volatile','while','continue','super','synchronized'
				,'switch','new','null','char','finally','final','long','pacakge','import','goto','for','const','default','float'
				'native','catch']


state = 0
Lexeme = ""
flag = False
try:
	with open("Main.java") as file:
		output = open("Output.txt",'w+')
		output.write("Lexeme:			 	      Token: \n")
		lookahead = file.read(1)
		while lookahead:
			if state ==0:
				if lookahead =='\r' or lookahead =='\t' or lookahead =='' or lookahead == '\n' or lookahead==' ':
					lookahead = file.read(1)
				elif lookahead =='_' or lookahead =='$' or lookahead.isalpha():
					state = 1
					Lexeme+=lookahead

				elif lookahead.isdigit():
					state = 3
					Lexeme+=lookahead

				elif lookahead == ',':
					state = 7
					Lexeme+=lookahead
					
				elif lookahead == ';':
					state = 8
					Lexeme+=lookahead
					
				elif lookahead == ':':
					state = 9
					Lexeme+=lookahead
					
				elif lookahead == '(':
					state = 10
					Lexeme+=lookahead
					
				elif lookahead == ')':
					state = 11
					Lexeme+=lookahead
					
				elif lookahead == '{':
					state = 12
					Lexeme+=lookahead
					
				elif lookahead == '}':
					state = 13
					Lexeme+=lookahead
					
				elif lookahead == '?':
					state = 14
					Lexeme+=lookahead
					
				elif lookahead == '=':
					state = 15
					Lexeme+=lookahead
					
				elif lookahead == '\"':
					state = 18
					Lexeme+=lookahead
					
				elif lookahead == '/':
					state = 20
					Lexeme+=lookahead
					
				elif lookahead == '+':
					state = 24
					Lexeme+=lookahead

				elif lookahead == '-':
					state = 27
					Lexeme+=lookahead
					
				elif lookahead == '*':
					state = 30
					Lexeme+=lookahead	
					
				elif lookahead == '>':
					state = 31
					Lexeme+=lookahead			
									
				elif lookahead == '<':
					state = 34
					Lexeme+=lookahead			
									
				elif lookahead == '!':
					state = 37
					Lexeme+=lookahead	

				elif lookahead == '&':
					state = 40
					Lexeme+=lookahead	

				elif lookahead == '|':
					state = 43
					Lexeme+=lookahead

				elif lookahead == '[':
					state = 46
					Lexeme+=lookahead	

				elif lookahead == ']':
					state = 47
					Lexeme+=lookahead

				elif lookahead == '.':
					state = 48
					Lexeme+=lookahead

				elif lookahead == '\'':
					state = 49
					Lexeme+= lookahead
				elif lookahead == '%':
					state = 51
					Lexeme+= lookahead	
				else:
					Lexeme+= lookahead
					lookahead = file.read(1)
					output.write("{:38}{}".format(Lexeme,"Unknown Lexeme\n"))
					state = 0
					Lexeme = ""
			elif state==1:
				lookahead = file.read(1)
				if lookahead == '_' or lookahead.isalpha() or lookahead.isdigit() or lookahead == '$':
					state = 1
					Lexeme+=lookahead
				else:
					state = 2

			elif state==2:
				state = 0
				if Lexeme in reservedWords:
					flag = True
				if flag:
					output.write("{:38}{} \n".format(Lexeme,Lexeme))
					Lexeme= ""
					flag = False
				else:
					if Lexeme[0].isupper():
						output.write("{:38}{}".format(Lexeme,"Class name\n"))
						Lexeme = ""
					else:
						output.write("{:38}{}".format(Lexeme,"Identifier\n"))
						Lexeme = ""
			elif state==3:
				lookahead = file.read(1)
				if lookahead.isdigit():
					state = 3
					Lexeme+=lookahead
				elif lookahead == '.':
					state = 5
					Lexeme+=lookahead
				else:
					state = 4

			elif state==4:
				state = 0
				output.write("{:38}{}".format(Lexeme,"Integer literal\n"))
				Lexeme = ""

			elif state==5:
				lookahead = file.read(1)
				if lookahead.isdigit():
					state = 5
					Lexeme+= lookahead
				else:
					state = 6

			elif state==6:
				state = 0
				output.write("{:38}{}".format(Lexeme,"Float literal\n"))
				Lexeme = ""	

			elif state==7:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"Comma\n"))
				Lexeme = ""

			elif state==8:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"Semi-colon\n"))
				Lexeme = ""
				

			elif state==9:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"Colon\n"))
				Lexeme = ""
				

			elif state==10:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"Right parenthesis\n"))
				Lexeme = ""

			elif state==11:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"Left parenthesis\n"))
				Lexeme = ""

			elif state==12:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"Right curly\n"))
				Lexeme = ""

			elif state==13:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"Left curly\n"))
				Lexeme = ""		

			elif state==14:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"Question mark\n"))
				Lexeme = ""		

			elif state==15:
				lookahead = file.read(1)
				if lookahead == "=":
					state = 16
					Lexeme+= "="
				else:
					state = 17

			elif state==16:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"Equal operator\n"))
				Lexeme = ""		

			elif state == 17:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"Assignment\n"))
				Lexeme = ""		

			elif state == 18:
				lookahead = file.read(1)
				if lookahead != "\"":
					Lexeme+= lookahead
				else:
					state = 19
					Lexeme+= lookahead

			elif state == 19:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"String literal\n"))
				Lexeme = ""	

			elif state == 20:
				lookahead = file.read(1)
				if lookahead =="/":
					state = 21
					Lexeme += lookahead
				elif lookahead == '=':
					state = 55
					Lexeme+= lookahead
				elif lookahead == '*':
					state = 56
					Lexeme+= lookahead
				else:
					state = 22	

			elif state == 55:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"Division assignment\n"))
				Lexeme = ""	

			elif state == 56:
				lookahead = file.read(1)
				if lookahead == '*':
					Lexeme+= lookahead
					lookahead = file.read(1)
					if lookahead == '/':
						Lexeme += lookahead
						state = 0
						lookahead = file.read(1)
						output.write("{:38}{}".format(Lexeme,"Multi line comment\n"))
						Lexeme = ""	
					else:
						Lexeme += lookahead
				else:
					Lexeme += lookahead				

			elif state == 21:
				lookahead = file.read(1)
				if lookahead == '\n' or lookahead =='\r':
					state = 23

				else:
					Lexeme += lookahead
			elif state == 22:
				state = 0
				output.write("{:38}{}".format(Lexeme,"Division\n"))
				Lexeme = ""	

			elif state == 23:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"Comment\n"))
				Lexeme = ""	

			elif state == 24:
				lookahead = file.read(1)
				if lookahead =="+":
					state = 26
					Lexeme += lookahead
				elif lookahead =='=':
					state = 52
					Lexeme += lookahead
				else:
					state = 25

			elif state == 25:
				state = 0
				output.write("{:38}{}".format(Lexeme,"Plus\n"))
				Lexeme = ""	

			elif state == 52:
				state = 0
				output.write("{:38}{}".format(Lexeme,"Addition assignment\n"))
				Lexeme = ""		

			elif state == 26:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"Increment\n"))
				Lexeme = ""		

			elif state == 27:
				lookahead = file.read(1)
				if lookahead =="-":
					state = 29
					Lexeme += lookahead
				elif lookahead =='=':
					state = 53
					Lexeme+= lookahead
				else:
					state = 28

			elif state == 28:
				state = 0
				output.write("{:38}{}".format(Lexeme,"Minus\n"))
				Lexeme = ""	

			elif state == 53:
				state = 0
				output.write("{:38}{}".format(Lexeme,"Subtraction assignment\n"))
				Lexeme = ""		

			elif state == 29:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"Decrement\n"))
				Lexeme = ""	

			elif state == 30:
				lookahead = file.read(1)
				if lookahead == '=':
					state = 54
					Lexeme+= lookahead
				else:
					state = 0
					output.write("{:38}{}".format(Lexeme,"Multiplication\n"))
					Lexeme = ""		
			elif state == 54:
				state = 0
				output.write("{:38}{}".format(Lexeme,"Multiplication\n"))
				Lexeme = ""	
			elif state == 31:
				lookahead = file.read(1)
				if lookahead =="=":
					state = 32
					Lexeme += lookahead
				else:
					state = 33

			elif state == 32:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"Greater than or equal\n"))
				Lexeme = ""	

			elif state == 33:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"Greater than\n"))
				Lexeme = ""		

			elif state == 34:
				lookahead = file.read(1)
				if lookahead =="=":
					state = 35
					Lexeme += lookahead
				else:
					state = 36

			elif state == 35:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"Less than or equal\n"))
				Lexeme = ""	

			elif state == 36:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"Less than\n"))
				Lexeme = ""		

			elif state == 37:
				lookahead = file.read(1)
				if lookahead =="=":
					state = 38
					Lexeme += lookahead
				else:
					state = 39

			elif state == 38:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"NOT equal\n"))
				Lexeme = ""	

			elif state == 39:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"NOT operator\n"))
				Lexeme = ""		

			elif state == 40:
				lookahead = file.read(1)
				if lookahead =="&":
					state = 41
					Lexeme += lookahead
				else:
					state = 42

			elif state == 41:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"AND operator\n"))
				Lexeme = ""	

			elif state == 42:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"Bitwise AND operator\n"))
				Lexeme = ""	

			elif state == 43:
				lookahead = file.read(1)
				if lookahead =="|":
					state = 44
					Lexeme += lookahead
				else:
					state = 45

			elif state == 44:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"OR operator\n"))
				Lexeme = ""	

			elif state == 45:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"Bitwise OR operator\n"))
				Lexeme = ""	
					
			elif state==46:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"Left bracket\n"))
				Lexeme = ""	

			elif state==47:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"Right bracket\n"))
				Lexeme = ""		

			elif state==48:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"Dot\n"))
				Lexeme = ""	

			elif state == 49:
				lookahead = file.read(1)
				if lookahead != '\'':
					Lexeme+= lookahead
				else:
					state = 50
					Lexeme+= lookahead

			elif state == 50:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"Character literal\n"))
				Lexeme = ""		

			elif state == 51:
				state = 0
				lookahead = file.read(1)
				output.write("{:38}{}".format(Lexeme,"Mod\n"))
				Lexeme = ""				
	output.close()
except IOError as e:
	print("File not found")									