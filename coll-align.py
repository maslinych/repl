#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os

log =  open ("collation-align-errors.log","w")
nerr=0


for dirname, dirnames, filenames in sorted(os.walk('.')):
		if '.git' in dirnames: dirnames.remove('.git')  # don't go into any .git directories.

		# print path to all filenames.
		for filename in filenames:
			
			if '.txt' in filename :
				print(os.path.join(dirname, filename))
				if u" " in filename:  # spaces in filename cause no end problems in Corpus build
					nameparts=filename.split(".")
					nameitself=nameparts[0].strip()  # strip  extra spaces both ends (happens often at the end)
					if u" " in nameitself : 
						nameitself=re.sub(u" ",u"$",nameitself)   # space inside ?
					print  u"file '"+filename+u"' renamed as '"+nameitself+u".txt'"
					os.rename(os.path.join(dirname, filename),os.path.join(dirname, nameitself+u".txt"))
					filename=nameitself+u".txt"
				try : 
					fileIN = open(os.path.join(dirname, filename), "rb")  # rb : to get the Windows \r\n EOL
				except :
					log.write("filename? "+os.path.join(dirname, filename)+"\n")
					nerr=nerr+1
					continue
				#tout=fileIN.readlines()
				tout=u""
				# actually readlines() should be OK
				line = fileIN.readline()
				while line:
					try :
						tout=tout+line.decode("utf-8")
					except :
						log.write("character? "+os.path.join(dirname, filename)+" line:"+str(nline)+" :\n"+line+"\n")
						nerr=nerr+1
						pass
					line = fileIN.readline()

				fileIN.close()

				# handle Windows EOL
				tout=re.sub(u"\r\n",u"\n",tout,0,re.U|re.MULTILINE)

				# rectify doz strange typos
				tout=re.sub(u"а",u"a",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"А",u"A",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"В",u"B",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"с",u"c",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"С",u"C",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"е",u"e",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"Е",u"E",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"ɒ",u"ɛ",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"ɣ",u"g",tout,0,re.U|re.MULTILINE)				
				tout=re.sub(u"Н",u"H",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"í",u"i",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"ɩ",u"i",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"к",u"k",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"т",u"m",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"М",u"M",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"п",u"n",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"щ",u"o",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"о",u"o",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"О",u"O",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"Р",u"P",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"р",u"p",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"г",u"r",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"Т",u"T",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"и",u"u",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"у",u"y",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"ɪ",u"y",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"л",u"n",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"á",u"a",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"ý",u"y",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"ú",u"u",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"№",u"N°",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"ï",u"i",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"˚",u"°",tout,0,re.U|re.MULTILINE)

				# enforce space between the ° of N° and the number that follows
				tout=re.sub(u"°([0-9])",u"° \g<1>",tout,0,re.U|re.MULTILINE)

				#align …  and ...
				tout=re.sub(u"…",u"...",tout,0,re.U|re.MULTILINE)

				# align braquets
				tout=re.sub(u"’",u"'",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"’",u"'",tout,0,re.U|re.MULTILINE) # problème en suspens avec les quotes simples
				tout=re.sub(u"‘",u"'",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"“",u"«",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"”",u"»",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"<<",u"«",tout,0,re.U|re.MULTILINE) # erreur fréquente chez kot
				tout=re.sub(u">>",u"»",tout,0,re.U|re.MULTILINE) 
				tout=re.sub(u"<h>»",u"<h>«",tout,0,re.U|re.MULTILINE) # erreur fréquente chez zup
				tout=re.sub(u"<ill>»",u"<ill>«",tout,0,re.U|re.MULTILINE) # erreur fréquente chez zup

				# frequent typos
				tout=re.sub(u"aia",u"ala",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"eie",u"ele",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"iii",u"ili",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"oio",u"olo",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"oiu",u"olu",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"ɛiɛ",u"ɛlɛ",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"ɔiɔ",u"ɔlɔ",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"iia",u"ila",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"iie",u"ile",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"oia",u"ola",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"aii",u"ali",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"all([\s\.\,\;\:\!\?])",u"ali\g<1>",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"aua",u"aya",tout,0,re.U|re.MULTILINE)
				
				
				# enforce a' 2PL followed by space
				tout=re.sub(u" a\'([^\s])",u" a' \g<1>",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"\'a\'([^\s])",u"'a' \g<1>",tout,0,re.U|re.MULTILINE)
				# same for leading A' 2PL ex.  imparative A' ye
				tout=re.sub(u"A\'([^\s])",u"A' \g<1>",tout,0,re.U|re.MULTILINE)

				# unsolved : "x" on one side and «x» on the other : all with " ?
				# try with caution :
				# - space before first " : missing " cause havoc (frequent fault, all the rest is inverted)
				tout=re.sub(ur'\s"([^\n\"]+)"',u" «\g<1>»",tout,0,re.U|re.MULTILINE)
				# - or beginning of line
				tout=re.sub(ur'\n"([^\n\"]+)"',u"\n«\g<1>»",tout,0,re.U|re.MULTILINE)
				# - or beginning of <h>
				tout=re.sub(ur'\<h\>"([^\n\"]+)"',u"<h>«\g<1>»",tout,0,re.U|re.MULTILINE)
				# - or beginning of <ill>
				tout=re.sub(ur'\<ill\>"([^\n\"]+)"',u"<ill>«\g<1>»",tout,0,re.U|re.MULTILINE)
				# - or beginning of <ls>
				tout=re.sub(ur'\<ls\>"([^\n\"]+)"',u"<ls>«\g<1>»",tout,0,re.U|re.MULTILINE)
				
				# - or beginning of ( parenthesis
				tout=re.sub(ur'\("([^\n\"]+)"',u"(«\g<1>»",tout,0,re.U|re.MULTILINE)
				# - or beginning just after : column
				tout=re.sub(ur'\:"([^\n\"]+)"',u":«\g<1>»",tout,0,re.U|re.MULTILINE)
				# around acronyms in capitals
				tout=re.sub(ur'"([A-ZƝŊƐƆ][A-ZƝŊƐƆ]+)"',u":«\g<1>»",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur'\'([A-ZƝŊƐƆ][A-ZƝŊƐƆ]+)\'',u":«\g<1>»",tout,0,re.U|re.MULTILINE)
				

				# align hyphens
				tout=re.sub(u"–",u"-",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"-",u"-",tout,0,re.U|re.MULTILINE)

				# numéros
				tout=re.sub(u"°",u"°",tout,0,re.U|re.MULTILINE)

				# suppress "french style" space before double-sign puncts
				tout=re.sub(u" :",u":",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u" ;",u";",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur" \!",u"!",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur" \?",u"?",tout,0,re.U|re.MULTILINE)

				# enforce space after comma, 
				tout=re.sub(u"\,([^\s])",u", \g<1>",tout,0,re.U|re.MULTILINE)
				# suppress space(s) before comma,
				tout=re.sub(u"([\s]+)\,",u",",tout,0,re.U|re.MULTILINE)

				# suppress spaces and tabs after end of line
				tout=re.sub(ur"[ \t]+\n",u"\n",tout,0,re.U|re.MULTILINE)

				# suppress extra empty lines
				tout=re.sub(ur"^\n\n",u"\n",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur"^\n\n",u"\n",tout,0,re.U|re.MULTILINE)

				# suppress remaining tabs and double spaces
				tout=re.sub(ur"\t",u" ",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"  ",u" ",tout,0,re.U|re.MULTILINE)
				tout=re.sub(u"  ",u" ",tout,0,re.U|re.MULTILINE)

				# unsolved : doz abuse of <ls>... <br/> ... <br/> ... </ls> 
				tout=re.sub(ur"</br>",u"<br/>",tout,0,re.U|re.MULTILINE)
				
				# poems end of para
				tout=re.sub(ur"<br/>\n\n",u"\n\n",tout,0,re.U|re.MULTILINE)
				
				# enforce punctuation before closing tags
				#tout=re.sub(ur"\.</h>\n",u"</h>.\n",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur"([^\.\;\:\!\?])</h>\n",u"\g<1>.</h>\n",tout,0,re.U|re.MULTILINE)
				#tout=re.sub(ur"\.</ill>\n",u"</ill>.\n",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur"([^\.\;\:\!\?])</ill>\n",u"\g<1>.</ill>\n",tout,0,re.U|re.MULTILINE)
				
				# numbers with dots between numgroups 281 350 -> 281.350
				tout=re.sub(ur"([0-9]+)\s([0-9]+)",u"\g<1>.\g<2>",tout,0,re.U|re.MULTILINE)
				
				# enforce -nan ordinal to be attached to number
				tout=re.sub(ur"([0-9])\snan",u"\g<1>nan",tout,0,re.U|re.MULTILINE)

				# enforce simple list if only 2 or 3 items in list
				# to be fixed : if line already starts with - 
				tout=re.sub(ur"<ls>(.*)<br/>\n(.*)</ls>",u"- \g<1>\n\n- \g<2>",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur"<ls>(.*)<br/>\n(.*)<br/>\n(.*)</ls>",u"- \g<1>\n\n- \g<2>\n\n- \g<3>",tout,0,re.U|re.MULTILINE)
				# dirty fix
				tout=re.sub(ur"\n- - ","\n- ",tout,0,re.U|re.MULTILINE)

				# no punctuation at end of line ?
				# ([^\>\.\;\:\!\?])\n\n
				# \g<1>.\n\n
				# --------- may be problematic in some cases (eg doz tends to break para)
				tout=re.sub(ur"([^\>\.\;\:\!\?\,])\n\n",u"\g<1>.\n\n",tout,0,re.U|re.MULTILINE)

				# no line break in a middle of  a sentence (frequent in doz texts)
				tout=re.sub(ur"([^\>\n])\n([a-zA-Z0-9ɛɔɲŋƐƆƝŊ«])",u"\g<1> \g<2>",tout,0,re.U|re.MULTILINE)

				# no paragraph break after a comma
				tout=re.sub(ur"\,\n\n",u", ",tout,0,re.U|re.MULTILINE)

				# eliminate extra lines before EOF
				tout=re.sub(ur"\n\n\n$(?![\r\n])",u"",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur"\n\n$(?![\r\n])",u"",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur"\n$(?![\r\n])",u"",tout,0,re.U|re.MULTILINE)

				# correct usual errors
				tout=re.sub(ur"rn",u"m",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur" minriu",u" minnu",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur" bɔgo ",u" bɔgɔ ",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur" anl ",u" ani ",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur"ɲɔgɔŋ",u"ɲɔgɔn",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur"ɲɔgon",u"ɲɔgɔn",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur"ɲogɔn",u"ɲɔgɔn",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur"ɲogon",u"ɲɔgɔn",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur"sɔmɔgɔ",u"somɔgɔ",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur" mɔgo",u" mɔgɔ",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur" mogo",u" mɔgɔ",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur" ɲɛmogo",u" ɲɛmɔgɔ",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur" fɔyi",u" foyi",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur" fill",u" fili",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur" sɛn kan",u" sen kan",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur" sɛnfɛ",u" senfɛ",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur"bɛ sɛnna",u"bɛ senna",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur"bɛ sɛn na",u"bɛ sen na",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur" kosebɛ",u" kosɛbɛ",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur" kosɛbe",u" kosɛbɛ",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur" sɔro;",u" sɔrɔ",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur" sɔro",u" sɔrɔ",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur" kɛle ",u" kɛlɛ ",tout,0,re.U|re.MULTILINE)
				# tout=re.sub(ur"eɛ([\s\,\.])",u"ɛ\g<1>",tout,0,re.U|re.MULTILINE)
				# tout=re.sub(ur"oɔ([\s\,\.])",u"ɔ\g<1>",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur" bɛe ",u" bɛɛ ",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur"eɛ",u"ɛ",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur"oɔ",u"ɔ",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur"nnɛn([\s\,\.])",u"nnen\g<1>",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur"nnɛnw ",u"nnenw ",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur" fen ",u" fɛn ",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur"bolono",u"bolonɔ",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur"jiriwali",u"yiriwali",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur"gofɛrenaman",u"gofɛrɛnaman",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur" kosɔn",u" kɔsɔn",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur" kɔsɛbɛ",u" kosɛbɛ",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur" bugo ",u" bugɔ ",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur"fɔlo",u"fɔlɔ",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur"Fɔlo",u"Fɔlɔ",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur" gɛlen",u" gɛlɛn",tout,0,re.U|re.MULTILINE)
				tout=re.sub(ur"'I ",u"'i ",tout,0,re.U|re.MULTILINE)

				#log.write("tout:'"+tout+"'\n")
				try : 
					fileOUT = open(os.path.join(dirname, filename), "w")
				except :
					log.write("filename? "+os.path.join(dirname, filename)+"\n")
					continue

				fileOUT.write(tout)
				fileOUT.close()
log.close()
if nerr==0 : os.remove("collation-align-errors.log")
