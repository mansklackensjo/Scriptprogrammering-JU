import csv

def get_placeholders():
    placeholders = {}
    with open('Labb5/configuration_values.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            placeholders[row[0]] = row[1:]
        
        return placeholders
    

def get_template():
    with open('Labb5/configuration-template.config', 'r') as file:
        string = file.read()
    
    return string
    

def produce_configfiles(template:str, placeholders:dict) -> None:
    
    for i in range(len(list(placeholders.values())[0])):
        template_copy = template
        for key in list(placeholders.keys()):
            template_copy = template_copy.replace(f'{{{key}}}', placeholders[key][i])

        with open(f'Labb5/configuration-{placeholders[list(placeholders.keys())[0]][i]}.config', 'w') as file:
            file.write(template_copy)
        


placeholders = get_placeholders()
template = get_template()

produce_configfiles(template, placeholders)







