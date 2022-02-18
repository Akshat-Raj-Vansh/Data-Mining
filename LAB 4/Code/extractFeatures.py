# __author__ = 'Akshat Raj Vansh'
# __version__ = '0.1.0'
# __license__ = 'MIT'

# import sys
# import time

# result = [['SN', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'Class']]
# log = [['Filename', 'Sequence', 'Class']]


# def encodeString(word):
#     return word.encode('unicode_escape')


# def containsDigit(string):
#     return any(char.isdigit() for char in string)


# def validateData(filename, data):
#     for x in data:
#         if (containsDigit(x[0]) or len(x[1]) == 0):
#             log.append(
#                 [filename[filename.rfind('\\')+1:], str(x[0]), str(x[1])])
#             data.remove(x)


# def readFile(filename):
#     try:
#         file = open(encodeString(filename), "r")
#         inputFile = file.readlines()
#         data = [(x.replace('\n', '')).split(',') for x in inputFile]
#         file.close()
#         data = data[1:]
#         validateData(filename, data)
#         return data
#     except:
#         print(filename+' is not a valid file')
#         return []


# def getTableValues(seq_no, data_item):
#     protein_sequence = data_item[0]
#     protein_class = data_item[1]
#     result = {'SN': seq_no,
#               'F1': protein_sequence.count('N'),
#               'F2': protein_sequence.count('H'),
#               'F3': protein_sequence.count('Q'),
#               'F4': protein_sequence.count('G'),
#               'F5': protein_sequence.count('D'), 
#               'F6': protein_sequence.count('T'),
#               'Class': 1 if protein_class == '+' else 0}
#     return result.values()


# def findResult(files):
#     data = []
#     for i in range(len(files)):
#         data.extend(readFile(files[i]))
#     for seq_no, data_item in enumerate(data):
#         result.append(list(getTableValues(seq_no + 1, data_item)))


# def generateLog():
#     print("Generating log...")
#     file = open('.\\Outputs\\log-'+time.strftime("%Y%d%m")+'.csv', 'w+')
#     file.writelines((','.join(str(x)
#                     for x in log[i])+'\n') for i in range(len(log)))
#     file.close()


# def generateResult(files):
#     print('Generating result...')
#     findResult(files)
#     file = open('.\\Outputs\\result-'+time.strftime("%Y%d%m")+'.csv', 'w+')
#     file.writelines((','.join(str(x)
#                     for x in result[i])+'\n') for i in range(len(result)))
#     file.close()


# def main(files):
#     generateResult(files)
#     generateLog()


# def webService(string_files):
#     files = string_files.split(',')
#     main(files)
#     resultname = 'result-'+time.strftime("%Y%d%m")+'.csv'
#     logname = 'log-'+time.strftime("%Y%d%m")+'.csv'
#     output = {'result': str(result), 
#               'log': str(log), 
#               'resultname': resultname, 
#               'logname': logname}
#     return output

# def checkArguments(args):
#     if(len(args) == 0):
#         print('Invalid Number of argumverents')
#     else:
#         main(args)


# if __name__ == "__main__":
#     print('Number of arguments:', len(sys.argv), 'arguments.')
#     print('Argument List:', str(sys.argv))
#     checkArguments(sys.argv[1:])

import sys
import time

result = [['SN', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'Class']]
log = [['Filename', 'Sequence', 'Class']]

def encodeString(word):
    return word.encode('unicode_escape')

def containsDigit(string):
    return any(char.isdigit() for char in string)

def validateData(filename, data):
    for x in data:
        if (containsDigit(x[0]) or len(x[1]) == 0):
            log.append(
                [filename[filename.rfind('\\')+1:], str(x[0]), str(x[1])])
            data.remove(x)

def readFile(filename):
    print(filename)
    file = open(encodeString(filename), "r")
    inputFile = file.readlines()
    data = [(x.replace('\n', '')).split(',') for x in inputFile]
    print(data)
    file.close()
    data = data[1:]
    validateData(filename, data)
    return data
  

def getTableValues(seq_no, data_item):
    protein_sequence = data_item[0]
    protein_class = data_item[1]
    result = {'SN': seq_no, 
              'F1': protein_sequence.count('N'), 
              'F2': protein_sequence.count('H'), 
              'F3': protein_sequence.count('Q'), 
              'F4': protein_sequence.count('G'), 
              'F5': protein_sequence.count('D'), 
              'F6': protein_sequence.count('T'), 
              'Class': 1 if protein_class == '+' else 0}
    return result.values()

def findResult(files):
    data = []
    for i in range(len(files)):
        data.extend(readFile(files[i]))
    for seq_no, data_item in enumerate(data):
        result.append(list(getTableValues(seq_no + 1, data_item)))

def generateLog():
    print("Generating log...")
    file = open('.\\Outputs\\log-'+time.strftime("%Y%d%m")+'.csv', 'w+')
    file.writelines((','.join(str(x)
                    for x in log[i])+'\n') for i in range(len(log)))
    file.close()

def generateResult(files):
    print('Generating result...')
    findResult(files)
    file = open('.\\Outputs\\result-'+time.strftime("%Y%d%m")+'.csv', 'w+')
    file.writelines((','.join(str(x)
                    for x in result[i])+'\n') for i in range(len(result)))
    file.close()

def main(files):
    generateResult(files)
    generateLog()

def webService(string_files):
    files = string_files.split(',')
    main(files)
    resultname = 'result-'+time.strftime("%Y%d%m")+'.csv'
    logname = 'log-'+time.strftime("%Y%d%m")+'.csv'
    output = {'result': result,
              'log': log,
              'resultname': resultname,
              'logname': logname}
    return output

def checkArguments(args):
    if(len(args) == 0):
        print('Invalid Number of arguments')
    else:
        main(args)

if __name__ == "__main__":
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    checkArguments(sys.argv[1:])