
import re
myFile = open("C:\\JAVA\\myJProject.java", 'r')
myContent = myFile.read()

print("Code without Comments: \n")

file = myContent

def f(content):
 for x in re.findall(r'("[^\n]*"(?!\\))|(//[^\n]*$|/(?!\\)\*[\s\S]*?\*(?!\\)/)',content,8):content = content.replace(x[1],'')
 print (content)  #print code without comments
Output = f(file)


NewFile = open("C:\\JAVA\\Practice\\src\\MainClass\\Driver.noComment", 'w')
NewFile.write(Output)


