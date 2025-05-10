
def get_input(query):
    data = {}
    for i in range(len(query)-1):
        if query[i]+query[i+1] == "=x":
            key = query[:i].split(" ")[-1]
            value = input(fr"{key}-->")
            data[key] = value
    print (data)
    return data

def normalize_og_query(og_query,input_vals):
    for i in input_vals.keys():
        temp = og_query.split(i+"=")
        temp = temp[0]+f'{i}=x '+" ".join(temp[1].split(" ")[1:])
        og_query = temp
    return og_query
