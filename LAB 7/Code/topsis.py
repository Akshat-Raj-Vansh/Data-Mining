__author__ = 'Akshat Raj Vansh'
__license__ = 'MIT'
__version__ = '0.1.0'

import pandas as pd
import os
import sys
import time

input_string = []

def main():
    if len(input_string) != 5:
        print(input_string)
        print(len(input_string))
        print("ERROR : NUMBER OF PARAMETERS")
        print("USAGE : python topsis.py inputfile.csv '1,1,1,1' '+,+,-,+' result.csv ")
        exit(1)
    elif not os.path.isfile(input_string[1]):
        print(f"ERROR : {input_string[1]} Don't exist!!")
        exit(1)
    elif ".csv" != (os.path.splitext(input_string[1]))[1]:
        print(f"ERROR : {input_string[1]} is not csv!!")
        exit(1)
    else:
        dataset, temp_dataset = pd.read_csv(
            input_string[1]), pd.read_csv(input_string[1])
        noc = len(temp_dataset.columns.values)
        if noc < 3:
            print("ERROR : Input file have less then 3 columns")
            exit(1)
        for i in range(1, noc):
            pd.to_numeric(dataset.iloc[:, i], errors='coerce')
            dataset.iloc[:, i].fillna(
                (dataset.iloc[:, i].mean()), inplace=True)
        try:
            weights = [int(i) for i in input_string[2].split(',')]
        except:
            print("ERROR : In weights array please check again")
            exit(1)
        impact = input_string[3].split(',')
        for i in impact:
            if not (i == '+' or i == '-'):
                print("ERROR : In impact array please check again")
                exit(1)
        if noc != len(weights)+1 or noc != len(impact)+1:
            print(
                "ERROR : Number of weights, number of impacts and number of columns not same")
            exit(1)
        if (".csv" != (os.path.splitext(input_string[4]))[1]):
            print("ERROR : Output file extension is wrong")
            exit(1)
        if os.path.isfile(input_string[4]):
            os.remove(input_string[4])
        topsis_pipy(temp_dataset, dataset, noc, weights, impact)


def Normalize(temp_dataset, noc, weights):
    for i in range(1, noc):
        temp = 0
        for j in range(len(temp_dataset)):
            temp = temp + temp_dataset.iloc[j, i]**2
        temp = temp**0.5
        for j in range(len(temp_dataset)):
            temp_dataset.iat[j, i] = (
                temp_dataset.iloc[j, i] / temp)*weights[i-1]
    return temp_dataset


def Calc_Values(temp_dataset, noc, impact):
    p_sln = (temp_dataset.max().values)[1:]
    n_sln = (temp_dataset.min().values)[1:]
    for i in range(1, noc):
        if impact[i-1] == '-':
            p_sln[i-1], n_sln[i-1] = n_sln[i-1], p_sln[i-1]
    return p_sln, n_sln


def topsis_pipy(temp_dataset, dataset, noc, weights, impact):
    temp_dataset = Normalize(temp_dataset, noc, weights)
    p_sln, n_sln = Calc_Values(temp_dataset, noc, impact)
    score = []
    for i in range(len(temp_dataset)):
        temp_p, temp_n = 0, 0
        for j in range(1, noc):
            temp_p = temp_p + (p_sln[j-1] - temp_dataset.iloc[i, j])**2
            temp_n = temp_n + (n_sln[j-1] - temp_dataset.iloc[i, j])**2
        temp_p, temp_n = temp_p**0.5, temp_n**0.5
        score.append(temp_n/(temp_p + temp_n))
    dataset['Topsis Score'] = score
    dataset['Rank'] = (dataset['Topsis Score'].rank(
        method='max', ascending=False))
    dataset = dataset.astype({"Rank": int})
    dataset.to_csv(input_string[4], index=False)


def webService(file, weights,impact):
    global input_string
    string = '.\\topsis.py ..\\Inputs\\'+file+' '+weights+' '+impact+' ..\\Outputs\\result.csv'
    input_string = string.split(' ')
    main()
    output = {'result': str(pd.read_csv(
            input_string[4])), 
              'resultname': input_string[4], 
              }
    return output

if __name__ == "__main__":
    input_string = sys.argv
    print(input_string)
    main()
  
   
