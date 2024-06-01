# Controlar Innovating Industries
# ISEP
# Álvaro Lopes-Cardoso
# 07/04/22

########################################################################### IMPORTS ###########################################################################




from distutils.cmd import Command
import os
from pathlib import Path
from re import S                            # To rename file
import shutil                              # To move file
import pandas as pd                         # Converting excel to list
import fileinput                            # To add lines to file
from fileinput import filename
from posixpath import dirname
from xml.etree.ElementTree import tostring


excelFile = "C:\\Users\\alvar\\Desktop\\ISEP\\PESTA\\Coords2PLC_FinalVersion\\Coordinates.xlsx"     # Copy here the directory of the excel file

file2change = ""                                                                                                    # .plcproj file

start_flag = "VAR_GLOBAL"                                                                                     
change_flag = "<ItemGroup>"
name_flag = '"GVL"'
PathNames = ["","",""]                           ## [0] -> GVL directory // [1]-> Excel path // [2] -> Name of the variables 
XListB = []
YListB = []
XListT = []
YListT = []
TP_XListB = []
TP_YListB = []
TP_XListT = []
TP_YListT = []

############################################################################### GUI ###########################################################################


    
def arrayX_B (XListB):              # Writing X coordinates array
    coordX = "\tBarrayX" + (" : ARRAY [0..") + str(len(XListB)-1) + "] OF REAL := " + str(XListB) + ";\n"
    return coordX

def arrayY_B (YListB):              # Writing Y coordinates array
    coordY = "\tBarrayY" + (" : ARRAY [0..") + str(len(YListB)-1) + "] OF REAL := " + str(YListB) + ";\n"
    return coordY

def arrayLength_B (XListB):         # Writing array length
    aL = "\tBarrayLength : INT := " + str(len(XListB)) + ";\n"
    return aL

def arrayX_T (XListT):              # Writing X coordinates array
    coordX = "\tTarrayX" + (" : ARRAY [0..") + str(len(XListT)-1) + "] OF REAL := " + str(XListT) + ";\n"
    return coordX

def arrayY_T (YListT):              # Writing Y coordinates array
    coordY = "\tTarrayY" + (" : ARRAY [0..") + str(len(YListT)-1) + "] OF REAL := " + str(YListT) + ";\n"
    return coordY

def arrayLength_T (YListT):         # Writing array length
    aL = "\tTarrayLength : INT := " + str(len(YListT)) + ";\n"
    return aL

def TP_arrayX_B (TP_XListB):
    TP = "\tTP_BarrayX" + (" : ARRAY [0..") + str(len(TP_XListB)-1) + "] OF STRING := " + str(TP_XListB) + ";\n"
    return TP

def TP_arrayY_B (TP_YListB):
    TP = "\tTP_BarrayY" + (" : ARRAY [0..") + str(len(TP_YListB)-1) + "] OF STRING := " + str(TP_YListB) + ";\n"
    return TP

def TP_arrayX_T (TP_XListT):
    TP = "\tTP_TarrayX" + (" : ARRAY [0..") + str(len(TP_XListT)-1) + "] OF STRING := " + str(TP_XListT) + ";\n"
    return TP

def TP_arrayY_T (TP_YListT):
    TP = "\tTP_TarrayY" + (" : ARRAY [0..") + str(len(TP_YListT)-1) + "] OF STRING := " + str(TP_YListT) + ";\n"
    return TP

def TPJoiner_SideListSpliter (CoordListX, CoordListY, SideList, TPList):
    cnt1 = 0
    cnt2 = 0
    for x in range(len(CoordListX)):
        if (SideList[x] == "B"):
            XListB.insert (cnt1, CoordListX[x])
            YListB.insert (cnt1, CoordListY[x])
            TP_XListB.insert(cnt1, TPList[x])
            TP_YListB.insert(cnt1, TPList[x])
            cnt1 = cnt1 + 1
        elif (SideList[x] == "T"):
            XListT.insert (cnt2, CoordListX[x]) 
            YListT.insert (cnt2, CoordListY[x])
            TP_XListT.insert(cnt2, TPList[x])
            TP_YListT.insert(cnt2, TPList[x])
            cnt2 = cnt2 + 1

def newDataFile(inputGVLFile, outputGVLFile):                               # Writing all the new data to the GVL file 
    with open (inputGVLFile, "r+") as file:      # Opening the inputfile
        with open (outputGVLFile, "w+") as f:    # Opening the outputfile
            for line in file:                    # For loop that gows through every line in inputfile
                if start_flag in line:
                    f.write(line)                # Checks if VAR_GLOBAL is in the line
                    f.write(arrayX_B(XListB))
                    f.write(arrayY_B(YListB))
                    f.write(arrayX_T(XListT))
                    f.write(arrayY_T(YListT))
                    f.write(TP_arrayX_B(TP_XListB))
                    f.write(TP_arrayY_B(TP_YListB))
                    f.write(TP_arrayX_T(TP_XListT))
                    f.write(TP_arrayY_T(TP_YListT))
                    f.write(arrayLength_B(XListB))
                    f.write(arrayLength_T(XListT))
                else:                            # If not, just keeps copying textm 
                    f.write(line)   
        f.close()                                # Closing outputfile
    file.close()                                 # Closing inputfile

def replacingGVLParameters (outputGVLFile, PathNames):                                          # Updating some parameters of the GVL file
    with open (outputGVLFile, "r") as file:
        filedata = file.read()  
        filedata = filedata.replace(name_flag, '"' + PathNames + '"')
    file.close()
    with open (outputGVLFile, "w") as file:
        file.write(filedata)
    file.close()

def newGVL_log(InputString, PathNames):                                                       # Adding the Global Variable list to the .plcproj file
    flagFirst = False
    for line in fileinput.FileInput(FindFile(PathNames),inplace=1):
        if change_flag in line:
            if flagFirst == False:
                line=line.replace(line,line+InputString + "\n")
                flagFirst = True
        print(line, end='')                                             # Important to add the end='' because if not, spaces will be created between the lines

def FindFile(PathNames) :                                                        # Finding the directory of the .plcproj file
    for file in os.listdir(PathNames):
        if file.endswith(".plcproj"):
            file2change = os.path.join(PathNames, file)
            return file2change

def main (PathNames):                                                    

    df = pd.read_excel(PathNames[1], sheet_name=1)
    listX = df['X(mm)'].tolist()                                        
    listY = df['Y(mm)'].tolist() 
    listSide = df['Side'].tolist() 
    listTP = df['TP'].tolist()  

    outputGVLFile = PathNames[0] + "\\GVLs\\" + PathNames[2] + ".TcGVL"  
    inputGVLFile  = "GlobalVariableTemplate.TcGVL" 
    InputString   = '    <Compile Include="GVLs\\' + PathNames[2] + '.TcGVL">\n\t<SubType>Code</SubType>\n    </Compile>'

    TPJoiner_SideListSpliter(listX, listY, listSide, listTP)
    newDataFile(inputGVLFile, outputGVLFile)
    newGVL_log(InputString, PathNames[0])
    replacingGVLParameters(outputGVLFile, PathNames[2])

        