'''Imports 2 files and checks to see which numbers overlap between the two'''

def read_file(filename):
    #Opens, reads, and saves file content into variable.
    with open(filename, 'r') as f_obj:
        lines = f_obj.read().split('\n')

    return lines

def overlap_check(x,y):
    #Compares numbers between files and creates new list with overlapping numbers.
    item_list = []

    for item in x:
        if item in y:
            item_list.append(item)
    #Change to str or flaot depending on the data
    item_list_2 = [int(x) for x in item_list]        

    print('\nHere is a list of the items that overlap in both files:')
    print(item_list_2)

def main():
    #Runs program.
    filename_1 = input('Enter name of first file: ')
    filename_2 = input('Enter name of second file: ')

    first_file = read_file(filename_1)
    second_file = read_file(filename_2)

    overlap_check(first_file, second_file)

main()

    
        
