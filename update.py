import sys
import webbrowser
import os
import shutil

def folder_name_from_link(link):
    common = link.index('.com/')
    return link[common+5:-1].replace('/', '-')

def setup(link):
    # create folder
    new_folder = 'proj_repos/'+folder_name_from_link(link)
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)

    # # create files
    # buggy = open(new_folder+'/buggy', 'w').close()
    # fixed = open(new_folder+'/fixed', 'w').close()
    # prompt = open(new_folder+'/prompt', 'w').close()
    # response = open(new_folder+'/response', 'w').close()

    print('\ncd proj_repos/'+folder_name_from_link(link)+'\n')
    webbrowser.open(link[:-1])

first_line = ''
next_line = ''
lines = []
if len(sys.argv) == 2:
    if  sys.argv[1] == 'start':
        print('starting new session ...')
        line = ''
        with open('cwe_tocheck.csv', 'r') as myfile:
            line = myfile.readline()
        setup(line)
    else:
        with open('cwe_tocheck.csv', 'r') as myfile:
            lines = myfile.readlines()
            first_line = lines[0]
            next_line = lines[1]

        with open('cwe_tocheck.csv', 'w') as myfile:
            myfile.writelines(lines[1:])
        
        with open('checked.csv', 'a') as myfile:
            myfile.write(first_line)
        
        #add to selected
        print('\nADDING PROJECT TO SELECTED ...\n')
        with open('cwe_selected.csv', 'a') as myfile:
            myfile.write(first_line)

        setup(next_line)

else:
    with open('cwe_tocheck.csv', 'r') as myfile:
        lines = myfile.readlines()
        first_line = lines[0]
        next_line = lines[1]

    with open('cwe_tocheck.csv', 'w') as myfile:
        myfile.writelines(lines[1:])
    
    with open('checked.csv', 'a') as myfile:
        myfile.write(first_line)

    print('\PROJECT NOT SELECTED - deleting folder\n')
    shutil.rmtree('proj_repos/'+folder_name_from_link(first_line))

    setup(next_line)
