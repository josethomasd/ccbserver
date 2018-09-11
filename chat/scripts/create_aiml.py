import re
#-----------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
g = open('it010802.aiml','w')

COURSECODE = "010802"
PROFESSOR = "Mrs. Anju Susan George"
CREDITS = "4"
SYLLABUS = "Module 1: Basics of Algebra and Number Theory: Integer Arithmatic, Modular Arithmatic, Algebraic structures, GF(2n) Fields, Matrices, Prime Numbers, Fermat's and Eulers's Theorem, Primality Testing, Factorization, Chinese Remainder Theorem, Linear and Quadratic Congruence, Discrete Logarithms.   Module 2: Symmetric Ciphers: Classical Encryption Techniques, Symmetric Cipher Model, Substitution and Transposition Ciphers, Stream and Block Ciphers,Data Encryption Standard, Advanced Encryption Standard, Triple DES, Confidentiality Using Symmetric Encryption. Module 3: Public-Key Encryption and Hash Functions : Public-Key Cryptography,RSA Algorithm, ElGamal Cryptosystem, Key Management, Diffie-HellmanKey Exchange, Elliptic Curve Cryptography, Message Authentication Codes,Hash Functions ,Secure Hash Algorithm, Digital Signature schemes. Module 4: Network Security Practice Applications: Authentication Applications,Kerberos, X.509 Authentication Service, Electronic Mail Security, PrettyGood Privacy, S/MIME, IP Security Overview, IP Security Architecture,Authentication Header, Encapsulating Security Payload. Module 5: System Security: Intruders, Intrusion Detection, Password Management,Viruses and Related Threats, Virus Countermeasures, Distributed Denial of Service attacks, Firewalls, Firewall Design Principles, Trusted Systems."
TITLE = "CRYPTOGRAPHY AND NETWORK SECURITY"
REFERENCES = "1. William Stallings, Cryptography and Network Security Principles and Practices, Pearson Education, Fourth Edition, 2006. 2. Behrouz A. Forouzan,Dedeep Mukhopadhyay Cryptography & Network Security, Second Edition,Tata McGraw Hill, New Delhi, 2010 3. Atul Kahate, Cryptography and Network Security, 2 nd Edition, Tata McGraw Hill, 2003. 4. Wenbo Mao,   Modern Cryptography- Theory & Practice, PearsonEducation, 2006. 5. Bruce Schneier,  Applied Cryptography, John Wiley and Sons Inc, 2001."
TYPE = "Theory"
DURATION = "Full Semester"
#-----------------------------------------------------------------------------------

def add_underscore(sentence):
    try:
        words = re.compile('\w+').findall(sentence)
        new_sentence = ""
        for index, word in enumerate(words):
            if new_sentence == "":
                new_sentence = word
            else:
                new_sentence = new_sentence + " _ " + word
        return new_sentence
    except:
        return sentence
#--------------------prof---------------------------------------------------------------------------
f = open('reduced/reduced_prof','r')
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close
lines.sort()

header = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" + "\n" + "<aiml version=\"1.0\">"
g.write(header+"\n\n")

lines = list(set(lines))
for line in lines:
    sentence = line[:-1]
    new_sentence = sentence.upper()
    for i in [0,1]:
        if i==0:
            sentence = add_underscore(new_sentence)
        else:
            sentence = new_sentence
        new_line = ""
        s = "<category>"
        new_line = new_line + s + "\n"
        s = "\t" + "<pattern>" + sentence + "</pattern>"
        new_line = new_line + s + "\n"
        s = "\t" + "<template><srai>INSTRUCTOR "+COURSECODE+"</srai></template>"
        new_line = new_line + s + "\n"
        s = "</category>"
        new_line = new_line + s + "\n"
        g.write(new_line+"\n")

s = "<!-- answers -->"+"\n"
s = s + "<category>\n"
s = s + "\t"+"<pattern>INSTRUCTOR "+COURSECODE+"</pattern>"+"\n"
s = s + "\t<template>\n" + "\t\t<random>\n"
s = s + "\t\t\t<li>$Professor "+PROFESSOR+" is teaching IT"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$Professor "+PROFESSOR+" will be teaching IT"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$Instructor of IT"+COURSECODE+" is Professor "+PROFESSOR+". </li>\n"
s = s + "\t\t\t<li>$IT"+COURSECODE+" is running under instruction of Professor "+PROFESSOR+". </li>\n"
s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
new_line = s
g.write(new_line+"\n")
#-------------------------prof ends------------------------------------------------------------------

#--------------------------credits--------------------------------------------------------------------
f = open('reduced/reduced_credits','r')
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close()
lines.sort()

lines = list(set(lines))
for line in lines:
	sentence = line[:-1]
	new_sentence = sentence.upper()
	for i in [0,1]:
		if i == 0:	
			sentence = add_underscore(new_sentence)
		else:
			sentence = new_sentence
		new_line = ""
		s = "<category>"
		new_line = new_line + s + "\n"
		s = "\t" + "<pattern>"+sentence+"</pattern>"
		new_line = new_line + s + "\n"
		s = "\t" + "<template><srai>CREDITS "+COURSECODE+"</srai></template>"
		new_line = new_line + s + "\n"
		s = "</category>"
		new_line = new_line + s + "\n"
		g.write(new_line+"\n")

s = "<!-- answers -->"+"\n"
s = s + "<category>\n"
s = s + "\t"+"<pattern>CREDITS "+COURSECODE+"</pattern>"+"\n"
s = s + "\t<template>\n" + "\t\t<random>\n"
s = s + "\t\t\t<li>$IT "+COURSECODE+" is worth "+CREDITS+" credits. </li>\n"
s = s + "\t\t\t<li>$IT "+COURSECODE+" is of "+CREDITS+" credits. </li>\n"
s = s + "\t\t\t<li>$"+CREDITS+" credits are awarded on successful completion of IT"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$"+CREDITS+" credits. </li>\n"
s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
new_line = s
g.write(new_line+"\n")

#-----------------------------------credits end--------------------------------------------------------

#-------------------------------------syllabus-----------------------------------------------------------
f = open('reduced/reduced_syllabus','r')
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close()
lines.sort()

lines = list(set(lines))
for line in lines:
	sentence = line[:-1]
	new_sentence = sentence.upper()
	for i in [0,1]:
		if i == 0:	
			sentence = add_underscore(new_sentence)
		else:
			sentence = new_sentence
		new_line = ""
		s = "<category>"
		new_line = new_line + s + "\n"
		s = "\t" + "<pattern>"+sentence+"</pattern>"
		new_line = new_line + s + "\n"
		s = "\t" + "<template><srai>SYLLABUS "+COURSECODE+"</srai></template>"
		new_line = new_line + s + "\n"
		s = "</category>"
		new_line = new_line + s + "\n"
		g.write(new_line+"\n")

s = "<!-- answers -->"+"\n"
s = s + "<category>\n"
s = s + "\t"+"<pattern>SYLLABUS "+COURSECODE+"</pattern>"+"\n"
s = s + "\t<template>\n" + "\t\t<random>\n"
s = s + "\t\t\t<li>$The syllabus for IT"+COURSECODE+" is "+SYLLABUS+". </li>\n"
s = s + "\t\t\t<li>$"+SYLLABUS+" is taught in IT"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$Prof. "+PROFESSOR+" will teach "+SYLLABUS+" in IT"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$"+SYLLABUS+". </li>\n"
s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
new_line = s
g.write(new_line+"\n")

#-------------------------------------syllabus ends---------------------------------------------------------

#-----------------title-----------------------------------------------------------------------------
f = open('reduced/reduced_title','r')
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close()
lines.sort()

lines = list(set(lines))
for line in lines:
	sentence = line[:-1]
	new_sentence = sentence.upper()
	for i in [0,1]:
		if i == 0:	
			sentence = add_underscore(new_sentence)
		else:
			sentence = new_sentence
		new_line = ""
		s = "<category>"
		new_line = new_line + s + "\n"
		s = "\t" + "<pattern>"+sentence+"</pattern>"
		new_line = new_line + s + "\n"
		s = "\t" + "<template><srai>TITLE "+COURSECODE+"</srai></template>"
		new_line = new_line + s + "\n"
		s = "</category>"
		new_line = new_line + s + "\n"
		g.write(new_line+"\n")

s = "<!-- answers -->"+"\n"
s = s + "<category>\n"
s = s + "\t"+"<pattern>TITLE "+COURSECODE+"</pattern>"+"\n"
s = s + "\t<template>\n" + "\t\t<random>\n"
s = s + "\t\t\t<li>$The course name of IT"+COURSECODE+" is "+TITLE+". </li>\n"
s = s + "\t\t\t<li>$The course title of IT"+COURSECODE+" is "+TITLE+". </li>\n"
s = s + "\t\t\t<li>$Course code IT"+COURSECODE+" is "+TITLE+". </li>\n"
s = s + "\t\t\t<li>$IT"+COURSECODE+" is "+TITLE+". </li>\n"
s = s + "\t\t\t<li>$"+TITLE+". </li>\n"
s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
new_line = s
g.write(new_line+"\n")

#--------------------title ends--------------------------------------------------------------------------

#----------------------------------------references--------------------------------------------------------
f = open('reduced/reduced_references','r')
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close()
lines.sort()

lines = list(set(lines))
for line in lines:
	sentence = line[:-1]
	new_sentence = sentence.upper()
	for i in [0,1]:
		if i == 0:	
			sentence = add_underscore(new_sentence)
		else:
			sentence = new_sentence
		new_line = ""
		s = "<category>"
		new_line = new_line + s + "\n"
		s = "\t" + "<pattern>"+sentence+"</pattern>"
		new_line = new_line + s + "\n"
		s = "\t" + "<template><srai>REFERENCES "+COURSECODE+"</srai></template>"
		new_line = new_line + s + "\n"
		s = "</category>"
		new_line = new_line + s + "\n"
		g.write(new_line+"\n")

s = "<!-- answers -->"+"\n"
s = s + "<category>\n"
s = s + "\t"+"<pattern>REFERENCES "+COURSECODE+"</pattern>"+"\n"
s = s + "\t<template>\n" + "\t\t<random>\n"
s = s + "\t\t\t<li>$The references are "+REFERENCES+" for IT"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$The references are "+REFERENCES+" for "+TITLE+". </li>\n"
s = s + "\t\t\t<li>$References according to Professor "+PROFESSOR+" are "+REFERENCES+" for IT"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$"+REFERENCES+". </li>\n"
s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
new_line = s
g.write(new_line+"\n")
#--------------------------------------references ends--------------------------------------------------------

#----------------------------------------type--------------------------------------------------------
f = open('reduced/reduced_type','r')
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close()
lines.sort()

lines = list(set(lines))
for line in lines:
	sentence = line[:-1]
	new_sentence = sentence.upper()
	for i in [0,1]:
		if i == 0:	
			sentence = add_underscore(new_sentence)
		else:
			sentence = new_sentence
		new_line = ""
		s = "<category>"
		new_line = new_line + s + "\n"
		s = "\t" + "<pattern>"+sentence+"</pattern>"
		new_line = new_line + s + "\n"
		s = "\t" + "<template><srai>TYPE "+COURSECODE+"</srai></template>"
		new_line = new_line + s + "\n"
		s = "</category>"
		new_line = new_line + s + "\n"
		g.write(new_line+"\n")

s = "<!-- answers -->"+"\n"
s = s + "<category>\n"
s = s + "\t"+"<pattern>TYPE "+COURSECODE+"</pattern>"+"\n"
s = s + "\t<template>\n" + "\t\t<random>\n"
s = s + "\t\t\t<li>$IT"+COURSECODE+" is a "+TYPE+" course. </li>\n"
s = s + "\t\t\t<li>$It's a "+TYPE+" course "+". </li>\n"
s = s + "\t\t\t<li>$"+TYPE+". </li>\n"
s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
new_line = s
g.write(new_line+"\n")
#--------------------------------------type ends--------------------------------------------------------

#----------------------------------------duration--------------------------------------------------------
f = open('reduced/reduced_duration','r')
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close()
lines.sort()

lines = list(set(lines))
for line in lines:
	sentence = line[:-1]
	new_sentence = sentence.upper()
	for i in [0,1]:
		if i == 0:	
			sentence = add_underscore(new_sentence)
		else:
			sentence = new_sentence
		new_line = ""
		s = "<category>"
		new_line = new_line + s + "\n"
		s = "\t" + "<pattern>"+sentence+"</pattern>"
		new_line = new_line + s + "\n"
		s = "\t" + "<template><srai>DURATION "+COURSECODE+"</srai></template>"
		new_line = new_line + s + "\n"
		s = "</category>"
		new_line = new_line + s + "\n"
		g.write(new_line+"\n")

s = "<!-- answers -->"+"\n"
s = s + "<category>\n"
s = s + "\t"+"<pattern>DURATION "+COURSECODE+"</pattern>"+"\n"
s = s + "\t<template>\n" + "\t\t<random>\n"
s = s + "\t\t\t<li>$IT"+COURSECODE+" is a "+DURATION+" course. </li>\n"
s = s + "\t\t\t<li>$It's a "+DURATION+" course "+". </li>\n"
s = s + "\t\t\t<li>$IT"+COURSECODE+" is "+DURATION+" long "+". </li>\n"
s = s + "\t\t\t<li>$"+DURATION+". </li>\n"
s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
new_line = s
g.write(new_line+"\n")
#--------------------------------------duration ends--------------------------------------------------------

g.write("</aiml>")
g.close()
