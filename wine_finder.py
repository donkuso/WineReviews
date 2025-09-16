# adds csv package (used for file i/o)
import csv

def read(filepath):
    """
    prints each line in the file provided in param
    filepath: str representing the path to the file to read in
    returns: nothing.  
    """
    
    # with block
    # handles opening and closing of file automatically. 
    # file is only open in indented block.
    with open(filepath, newline='', mode='r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            print(row)
            print()
        
