from hashlib import sha256
def normalize_query(expr):
    mod_expr = ""
    inp = False
    i=0
    while i<len(expr):
        if inp:
            pos = expr[i:].find(" ")
            i+=pos
            mod_expr+='x'
            inp=False
        elif expr[i] == " ":
            mod_expr+=""
        elif expr[i] == "=":
            inp = True
            i+=1
            mod_expr+="="
        else:
            mod_expr+=expr[i]
        i+=1
    return mod_expr.encode("ascii")

def generate_signature(expr):
    expr = normalize_query(expr)
    return sha256(expr).hexdigest()
    
     
# print(generate_signature(r'\pi_{ empno, empname  } (\sigma_{ empno = 1 AND empname = "john"  } emp)'))
