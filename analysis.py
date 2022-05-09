import os
import sys

def folder_name_from_link(link):
    common = link.index('.com/')
    return link[common+5:-1].replace('/', '-')

def setup(link):

    new_folder = 'selected_repos/'+folder_name_from_link(link)+'/result.csv'
    os.system('code '+new_folder)

if len(sys.argv) == 2:
    if  sys.argv[1] == 'start':
        print('starting new session ...')
        line = ''
        with open('to_query.csv', 'r') as myfile:
            line = myfile.readline()
        setup(line)
    else:
        first_line = ''
        next_line = ''
        lines = []
        with open('to_query.csv', 'r') as myfile:
            lines = myfile.readlines()
            first_line = lines[0]
            next_line = lines[1]

        with open('to_query.csv', 'w') as myfile:
            myfile.writelines(lines[1:])
        
        with open('queried.csv', 'a') as myfile:
            myfile.write(first_line)

        if sys.argv[1] == 'result':
            print('\nsaving to has_result\n')
            with open('has_result.csv', 'a') as myfile:
                myfile.write(first_line)
        else:
            print('\nsaving to no_result\n')
            with open('no_result.csv', 'a') as myfile:
                myfile.write(first_line)

        setup(next_line)

else:
    print('2 args required')

