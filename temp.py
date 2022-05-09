import os

def folder_name_from_link(link):
    common = link.index('.com/')
    return link[common+5:-1].replace('/', '-')

selected = []

with open('cwe_selected.csv', 'r') as myfile:
    selected = myfile.readlines()

count = 0
for line in selected:
    # print(folder_name_from_link(line))
    for folder in os.listdir('proj_repos'):
        # print(folder)
        if os.path.isdir(os.path.join('proj_repos', folder)):
            if folder_name_from_link(line) == folder:
                count += 1
                print('found ', count)
                os.system('cp -R proj_repos/'+folder+' ./selected_repos/')

