identify the error in the following code
input_file_opened = False
while not input_file_opened:
try:
    file_name=input('enter file name:')
    input_file = open(file_name,'r')
    input_file_opend=True
except: print('input file not found')