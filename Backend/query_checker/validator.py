import sigGen
import queryManip as qm

def validate_query(inp_query, og_query):
    qm.convert_to_ra(og_query,'og')
    qm.convert_to_ra(inp_query,'inp')
    signInp = sigGen.generate_signature(qm.read_query('inp'))
    signOg = sigGen.generate_signature(qm.read_query('og'))
    if signInp == signOg:
        return 1
    else:
        return 0

