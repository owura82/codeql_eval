import os
import sys

def folder_name_from_link(link):
    common = link.index('.com/')
    return link[common+5:-1].replace('/', '-')

def setup(link):
    folder = 'proj_repos/'+folder_name_from_link(link)
    print('\ncd '+folder+'\n')

    #get query
    id_lines = []
    with open('cwe_id.csv', 'r') as f:
        id_lines = f.readlines()
    
    for line in id_lines:
        
        temp = line.split(',')

        if temp[0] == folder_name_from_link(link):
       
            cwe_id = temp[1].upper().strip()

            database = folder+'/code_ql_database'
            output = folder+'/result.csv'

            command = 'codeql database analyze '+database+ ' --format=csv --output='+output+' --off-heap-ram=0 '\
                '~/Repos/codeql-home/codeql-repo/cpp/ql/src/Security/CWE/'+cwe_id

            # print('\ncodeql database analyze code_ql_database --format=csv --output=result.csv --off-heap-ram=0 ' \
            #     '~/Repos/codeql-home/codeql-repo/cpp/ql/src/Security/CWE/'+cwe_id+'/selected\n')

            print('\nExecuting command: \n'+command+'\n')
            os.system(command)
            break





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

        setup(next_line)

else:
    print('2 args required')