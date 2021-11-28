from Models.variableutil import create_variable
from Models.token import token_type

def grammatical_relation(tree):
    grelation = {}
    for dt in tree:
        parent = dt[0]
        child = dt[1]
        dt_type = tree[dt]
        if dt_type == 'PRED':
            grelation['PRED'] = child
        elif dt_type == 'TRAIN-NAME':
            grelation['LSUBJ'] = child
        elif dt_type == 'TO-TIME':
            grelation['TO-TIME'] = child
        elif dt_type == 'CITY-NAME':
            if token_type(parent) == 'arrive' or token_type(parent) == 'city':
                grelation['TO-LOC'] = child
            else:
                grelation['FROM-LOC'] = child
        elif dt_type == 'WH-RUN-TIME' or dt_type == 'RUN-TIME':
            grelation['RUN-TIME'] = 'GAP'
        elif dt_type == 'WH-TRAIN':
            grelation['LSUBJ'] = 'GAP'
        elif dt_type == 'WH-TO-TIME':
            grelation['TO-TIME'] = 'GAP'
    # print(grelation)

    relations = []
    variables = {}
    for rtype in grelation:
        if rtype == 'PRED':
            variable = create_variable()
            variables[grelation[rtype]] = variable
            relation = f"({variable} PRED {grelation[rtype]})"
            relations.append(relation)
            break
        
    for rtype in grelation:
        if rtype == 'PRED':
            continue
        variable = create_variable()
        variables[grelation[rtype]] = variable
       
        if rtype == 'RUN-TIME':
            relation = f"({variables[grelation['PRED']]} {rtype} (TIME {variable} GAP))"
        else:
            tk_type = None
            if rtype == 'LSUBJ':
                tk_type = 'TRAIN-NAME'
            elif rtype == 'TO-LOC' or rtype == 'FROM-LOC':
                tk_type = 'CITY-NAME'
            elif rtype == 'TO-TIME':
                tk_type = 'TIME'
            relation = f"({variables[grelation['PRED']]} {rtype} ({tk_type} {variable} {grelation[rtype]}))"
        relations.append(relation)

    return relations