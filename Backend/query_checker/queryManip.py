import os

def write_to_file(query):
    with open('opfiles/temp.txt','w') as f:
        f.write("a "+query)

def add_input(query, vals):
    res = query
    for key in vals.keys():
        tmp = res.split(key+'=x')
        if type(vals[key]) is str:
            added_input = f'{key}=\"{str(vals[key])}\"'
        else:
            added_input = f'{key}={vals[key]}'
        tmp.insert(1,added_input)
        res = ''.join(tmp)
    return res

def convert_to_ra(query,label):
    try:
        write_to_file(query)
        os.system("docker cp opfiles/temp.txt Qconv:/home/MAJPROJ/temp.txt > /dev/null ")
        os.system(f'''docker exec -it Qconv sh -c 'cd /home/MAJPROJ;cat temp.txt | ./qconv '>> logs/service.log; docker cp Qconv:/home/MAJPROJ/qconv-latex-tmp.tex opfiles/qconv-latex-{label}.tex >> ./logs/service.log''')
        return 0
    except:
        return -1

def read_query(label):
    file_path =  f"opfiles/qconv-latex-{label}.tex"
    with open(file_path,'r') as f:
        tree = f.read()
    expr = tree.split("\\[")[1].split("\\]")[0]
    return expr


