from pathlib import Path
from shutil import copyfile
import os
# p = Path('/Users/gageludlow/Projects/hello-world.py')
# /Users/gageludlow/Projects
#/Users/gageludlow/Projects/python-projects/project1/project1_test_2019-10-21-20-32-06
command = input()
listStrings = command.split(' ')
commandLetter = listStrings[0]
userPath = Path(listStrings[1])
stringFiles = []
def getFiles(currentDir):
   currentFiles = []
   for child in currentDir.iterdir():
      if child.is_file():
         #currentFiles.append(child)
         print(child.absolute().as_posix())
         currentFiles.append(child)
   return currentFiles

def recursivePath(rPath):
   currentFiles = []
   #currentFiles += getFiles(rPath)
   
   for child in rPath.iterdir():
      if child.is_file():
         print(child.absolute().as_posix())
         currentFiles.append(child)
      elif child.is_dir():
         #currentFiles += getFiles(child)
         recursivePath(child)
   
         
         
   #for item in currentFiles:
      #stringFiles.append(item.absolute().as_posix())

   #stringFiles.sort()
   #for child in stringFiles:
      #print(child)

   return currentFiles   

def printDirectories(dPath):
   currentFiles = []
   for child in dPath.iterdir():
      if child.is_dir():
         currentFiles.append(child)
      else:
         currentFiles.append(child) 
   for item in currentFiles:
      stringFiles.append(str(item))
   stringFiles.sort()
   for child in currentFiles:
      print(child)
      
   return currentFiles

#get interesting files
def getSecondInput(uInput, currentFiles):
   listInput = uInput.split(' ')
   commandLetter = listInput[0]
   interestingFiles = []
   isError = False
   firstTry = True
   while isError == False:
      if (firstTry == True):
         firstTry = False
      else:
         secondCommand = input()
         listInput = secondCommand.split(' ')
         commandLetter = listInput[0]
      isError = True
      if commandLetter == "A":
         #add all files
         interestingFiles = currentFiles
      elif commandLetter == "N":
         userPath = Path(listInput[1])
         #search for identical file name
         filename = str(userPath)
         
         for cFile in currentFiles:
            pathList = str(cFile).split('/')
            
            if filename == pathList[-1]:
               interestingFiles.append(cFile)
         #print(interestingFiles)     

      elif commandLetter == "E":
         userExe1 = listInput[-1]
         userExe2 = userExe1.split('.')
         userExe3 = userExe2[-1]
         for cFile in currentFiles:
            pathList = str(cFile).split('.')
            fileExten = pathList[-1]
            if fileExten == userExe3:
               interestingFiles.append(cFile)
         
      elif commandLetter == "T":
         searchString = str(listInput[1])
         for cFile in currentFiles:
            
            try:
               f = open(cFile, "r")
               if f.mode == 'r':
                  contents = f.read()
                  if searchString in contents:
                     interestingFiles.append(cFile)
            except:
               print("not a file")
         #print(interestingFiles)
         
      elif commandLetter == "<":
         searchSize = int(listInput[1])
         for cFile in currentFiles: 
            if cFile.is_dir() == False:
               statInfo = os.stat(cFile)
               print(str(cFile))
               print(statInfo.st_size)
               if searchSize > statInfo.st_size:
                  interestingFiles.append(cFile)
         #print(interestingFiles)

      elif commandLetter == ">":
         searchSize = int(listInput[1])
         for cFile in currentFiles: 
            if cFile.is_dir() == False:
               statInfo = os.stat(cFile)
               print(str(cFile))
               print(statInfo.st_size)
               if searchSize < statInfo.st_size:
                  interestingFiles.append(cFile)
         #print(interestingFiles)
         #do some
      else:
         print("ERROR")
         isError = False
         #reprompt
   return interestingFiles

def getThirdInput(interestingFiles):
   secondCommand = input()
   listInput = secondCommand.split(' ')
   commandLetter = listInput[0]
   
   isError = False
   firstTry = True
   while isError == False:
      if (firstTry == True):
         firstTry = False
      else:
         secondCommand = input()
         listInput = secondCommand.split(' ')
         commandLetter = listInput[0]
      isError = True
      if commandLetter == "F":
         for cFile in interestingFiles:
            try:
               f = open(cFile, "r")
               if f.mode == 'r':
                  contents = f.readline()
                  print(contents)
            except:
               print("NOT TEXT")
      elif commandLetter == "D":
         for cFile in interestingFiles:
            if cFile.is_dir() == False:
               dupName = str(cFile) + ".dup"
               newFile = open(dupName, "w+")
               copyfile(cFile, dupName)
      elif commandLetter == "T":
         for cFile in interestingFiles:
            cFile.touch()
      else:
         print("ERROR")
         isError = False


#p = Path('/Users/gageludlow/Projects/hello-world.py')
#print(type(p.stat().st_type))

if commandLetter == "D":
   currentFiles = printDirectories(userPath)
   
   secondCommand = input()
   interestingFiles = getSecondInput(secondCommand, currentFiles)
   interestingFiles.sort()
   for item in interestingFiles:
      print(item)
   getThirdInput(interestingFiles)
elif commandLetter == "R":
   currentFiles = recursivePath(userPath)
   secondCommand = input()
   interestingFiles = getSecondInput(secondCommand, currentFiles)
   interestingFiles.sort()
   for item in interestingFiles:
      print(item)
   getThirdInput(interestingFiles)
else:
   print("ERROR")



