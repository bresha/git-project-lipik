'''
27. Na linku https://drive.google.com/drive/folders/1lONK6fv_6zxJO8uIxDcLBpDHVnCJDFpW se nalazi nekoliko tekstualnih fileova.
 Skinite ih i kopirajte te dokumente u folder gdje se nalazi skripta za rješavanje zadatka. 
	Vaš zadatak je učitati sve dokumente iz tog foldera te izvući sljedeće podatke:
		sve mailove
		sve brojeve telefona 
		sva imena i prezimena
		sve opise (ostale podatke) 

	Kreirajte novi folder kroz .py skriptu te unutar toga foldera kreirajte nove .txt dokumente na sljedeći način: 
		Svaki dokument mora imati naziv u sljedećem formatu: “<varijabla>.txt”
		Sadržaj dokumenata mora biti: 
			jedan dokument samo s imenima
			Jedan dokument samo s brojem godina
			itd dok ne potrošite sve varijable
			
	Napravite csv file pod nazivom “Tinder” od tih podataka 

'''

import os
cur_dir = os.getcwd()
files_dir = 'horoskop'
files_dir = os.path.join(cur_dir, files_dir)
files_list = os.listdir(files_dir)

list_of_peoples = []

def check_for_name_and_years(line):
    x = line.split()
    contains_number = False
    if len(x) == 2:
        for c in x[1]:
            if c.isdigit():
                contains_number = True

    return contains_number



def check_for_sign(line):
    list_of_signs = ["bik", "blizanac", "djevica", "jarac", "lav", "ovan", "rak", "riba", "škorpion", "strijelac", "vaga", "vodenjak"]
    if line.strip().lower() in list_of_signs:
        return True
    return False

def check_for_email(line):
    is_mail = False
    for c in line:
        if c == '@':
            is_mail = True
    return is_mail

def check_for_tel(line):
    if line[0] == '+' or line[0] == '0':
        return True
    return False
 
for file in files_list:
    dat = {}
    file_path = os.path.join(files_dir, file)
    with open(file_path, encoding="utf8") as f:
        lines = f.readlines()
        for line in lines:
            if check_for_name_and_years(line):
                x = line.split(' ')
                name = x[0].strip(',')
                years = x[1].strip()
                dat["name"] = name
                dat["years"] = years
            elif check_for_sign(line):
                dat["sign"] = line.strip().lower()
            elif check_for_email(line):
                dat["email"] = line.strip()
            elif check_for_tel(line):
                dat["tel"] = line.strip()
            else:
                if "desc" in dat.keys():
                    dat["desc"].append(line.strip())
                else:
                    dat["desc"] = [line.strip()]
    list_of_peoples.append(dat)

files = list_of_peoples[0].keys()

# create new dir
newpath = os.path.join(cur_dir, 'new')
if not os.path.exists(newpath):
    os.makedirs(newpath)

for file in files:
    data = []
    for people in list_of_peoples:
        data.append(people[file])

    file_path = os.path.join(newpath, f"{file}.txt")
    with open(file_path, 'w+', encoding="utf8") as f:
        for value in data:
            if file != "desc":
                f.write(f"{value}\n")
            else:
                for el in value:
                    f.write(f"{el}\n")

