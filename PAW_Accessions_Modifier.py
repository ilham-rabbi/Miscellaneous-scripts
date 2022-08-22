'''
A short script to determine the percent of proteins 
found in a PAW pipeline analysis which are quantized

2022 Ilham A. Rabbi - SPARC
'''

def import_data():
    filepath = filedialog.askopenfilename(title='Open your accessions list', initialdir='/')

    with open(filepath, newline = '') as ProteinSummary:                                                                                          
        prot_reader = csv.reader(ProteinSummary, delimiter='\t')
        for acc in prot_reader:
            print(acc)
            ProtAcc.append(acc)   
   

def EditAccessions():
    for item in ProtAcc:
        for accession in item:
            modaccession = ""
            cntr = 0
            for char in accession:
                if char == "|":
                    cntr += 1
                    continue
                if cntr == 1:
                    modaccession += char
            print(modaccession)
            ProtAccMod.append(modaccession)                 
    return


def WriteAccessions():
    filepath = filedialog.askopenfilename(title='Open your empty list', initialdir='/')
    
    f = open(filepath, 'w')
    writer = csv.writer(f)
    for accession in ProtAccMod:
        writer.writerow([accession])    
    return

    

if __name__ == "__main__":
    import csv as csv
    import math as math
    from tkinter import *
    from tkinter import filedialog

    ProtAcc = []
    ProtAccMod = []
    
    print("test 1")
    
    import_data()
    print("testbet")
    EditAccessions()
    print("testend")
    WriteAccessions()