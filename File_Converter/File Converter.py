# Modules that are used
import glob
import os
import datetime

# Kent nex
# Last updated: March 4th 2015

#######################################################################################################################
# Formats .INZ files
#######################################################################################################################

def reformat_INZ(strFile):
    charCount = 25
    intConstant = 10
    strPreset = '|T|0|N|N|N|5|5|Y|N|3|100| |'
    strFile = strFile.split('\n')

    for i in range(len(strFile)):
        splitFile = strFile[i]
        splitFile = splitFile.split(' ')
        splitFile = splitFile[0]

        if (len(splitFile) < charCount):splitFile = splitFile + ((' ' * (charCount - len(splitFile))) + '|')
        else:
            print('charCount is too small.')

        splitFile = splitFile + str(intConstant)+ strPreset
        strFile[i] = splitFile
    strFile = '\n'.join(strFile)
    strFile = 'Converted ' + str(datetime.datetime.today()) + '\n' + strFile

    return strFile


#######################################################################################################################
# Formats .PAC files
#######################################################################################################################

def reformat_PAC(strFile):

    strFile = strFile.split('\n\n')

    for i in range(len(strFile)):
        splitFile = strFile[i]
        splitFile = splitFile.split("\n")
        splitFile[0] = "P" + splitFile[0][-3:]
        strFile[i] = '\n'.join(splitFile)

    strFile = '\n\n'.join(strFile)
    strFile = 'Converted ' + str(datetime.datetime.today()) + '\n' + strFile

    return strFile


#######################################################################################################################
# Formats .ZON files
#######################################################################################################################

def reformat_ZON(strFile):

    strFile = strFile.split('\n')

    for i in range(len(strFile)):
        strList = ['', '', '', '', '', '', '', '', '', '', '']
        loopString = strFile[i]
        loopString = loopString.split(' ')
        strList[0] = '0000' + loopString[0]
        strList[1] = loopString[1] + '   '
        strList[2] = 'P' + loopString[2][-3:] + '      '
        strList[3] = loopString[3][-9:]
        strList[4] = '00000000' + loopString[4]
        strList[5] = loopString[5]
        strList[6] = loopString[6]
        strList[7] = loopString[7]
        strList[8] = loopString[9]
        strList[9] = '0000'
        strList[10] = '\n**ROUTE**|          |         \
        |PUBLICATION=                                                    \
        |ROUTE=          |TRUCK=          |DROPDESC=                                        \
        |ADDRESS1=                         |ADDRESS2='
        strList = ' '.join(strList)
        strFile[i] = strList
    strFile = '\n'.join(strFile)
    strFile = 'Converted ' + str(datetime.datetime.today()) + '\n' + strFile

    return strFile


#######################################################################################################################
# Open File function. This function will open all files with the given Extension.
#######################################################################################################################

def open_file(file_name):

    try:  # This will try to open the file. If it cant it will produce and error.

        raw_file = open(file_name, 'r')  # Opens the file
        file_contents = raw_file.read()  # Takes all that's in it and stores it in file_contents
        raw_file.close()  # Closes the file
    except:
        input('Could not locate file. Press Enter to close....')  # This is an error message
        raise SystemExit, 'Missing file.'

    file_contents = '\n'.join(file_contents.split('\n')[1:])  # Removes the header of the document

    return file_contents  # Returns the file!

#######################################################################################################################
# Save File
#######################################################################################################################

def save_file(file_string, file_name, new_folder_name):

    new_file_path = correct_path() + new_folder_name  # Gets the directory of the new folder.

    if not os.path.exists(new_file_path):  # If the new folder doesnt exist then it makes it.
        os.makedirs(new_file_path)

    new_file = new_file_path + '\\' + file_name

    raw_file = open(new_file, 'w')
    raw_file.write(file_string)
    raw_file.close()

#######################################################################################################################
# Get correct path
#######################################################################################################################

def correct_path():  # This function will return the correct path of the directory before this one

    current_path = os.getcwd().split('\\')  # Gets the path and splits it
    new_path = '/'.join(current_path[:-1:])  # Removes the last part of the path

    return new_path  # Returns the new path

#######################################################################################################################
# Runs all the rest of the code. Main.
#
# Variables that can be changed:
# - fileExtension #note if changed then change the if statement as well
#
#######################################################################################################################

def main():

    old_folder_name = '\\Files_to_be_converted'  # Changing this will change the folder that makes the files  \\Files_to_be_converted
    new_folder_name = '\\Converted_Files'  # Changing this will change the name of the folder that's converted the files
    file_extensions = ['.PAC', '.INZ', '.ZON']  # All the different file extensions

    old_files_path = correct_path() + old_folder_name  # This is a path to the old files folder

    if not os.path.exists(old_files_path):  # If there isn't any folder then it makes a new one
        os.makedirs(old_files_path)

    for ext in file_extensions:  # runs the loop for every extension you want.

        for file_directory in glob.glob(old_files_path + '\\*' + ext):  # This will go through everything with that ext

            file_string = open_file(file_directory)  # Opens the files!

            file_name = file_directory.split('\\')  # This gets the name of the file.
            file_name = ''.join(file_name[-1])

            print file_name

            if ext == '.PAC':  # If the file is .PAC file then it will reformat it.
                formatted_file = reformat_PAC(file_string)
                save_file(formatted_file, file_name, new_folder_name)
            elif ext == '.INZ':  # If the file is .INZ file then it will reformat it.
                formatted_file = reformat_INZ(file_string)
                save_file(formatted_file, file_name, new_folder_name)
            elif ext == '.ZON':  # If the file is .ZON file then it will reformat it.
                formatted_file = reformat_ZON(file_string)
                save_file(formatted_file, file_name, new_folder_name)

    raw_input('Conversion complete!\nPress any button to close....')

#######################################################################################################################
# Runs the program
#######################################################################################################################
if __name__ == "__main__":
    main()
