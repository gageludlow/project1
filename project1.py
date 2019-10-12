from pathlib import Path
# p = Path('/Users/gageludlow/Projects')


command = input()
listStrings = command.split(' ')
commandLetter = listStrings[0]
userPath = Path(listStrings[1])

def recursivePath(rPath):
   currentFiles = []
   for child in rPath.iterdir():
      if child.is_dir():
         currentFiles.append(child)
         print(child)
         recursivePath(child)
      else:
         currentFiles.append(child)
         print(child)

   return currentFiles   

def printDirectories(dPath):
   currentFiles = []
   for child in dPath.iterdir():
      if child.is_dir():
         currentFiles.append(child)
         print(f"if{child}")
      else:
         currentFiles.append(child)
         print(f"else {child}")   
      
   return currentFiles


if commandLetter == "D":
   currentFiles = printDirectories(userPath)
   secondCommand = input()
   
elif commandLetter == "R":
   currentFiles = recursivePath(userPath)
   secondCommand = input()
else:
   print("ERROR")



 def getSecondInput(uInput, currentFiles):
   listInput = uInput.split(' ')
   commandLetter = listInput[0]
   userPath = Path(listInput[1])
   
   if commandLetter == "A":
       #do some
       intFiles = currentFiles
   elif commandLetter == "N":
      #do some
   elif commandLetter == "E":
      #do some
   elif commandLetter == "T":
      #do some
   elif commandLetter == "<"
      #do some
   elif commandLetter == ">"
      #do some
   else:
      print("ERROR")
      #reprompt