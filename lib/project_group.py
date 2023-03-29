from db.models import ProjectGroup, Student



def print_project_groups(groups):
    print(' ')
    print('Project Groups')
    print(' ')

    for index, group in enumerate(groups):
        print(f'{index + 1}. {group.name}')
    
    print(' ')

def print_project_group(ProjectGroup):
    print('')
    print(f'Project Group ID: {ProjectGroup.id}')
    print(f'    Project Group Name: {ProjectGroup.name}')