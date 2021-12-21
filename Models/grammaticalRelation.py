from Models.helper import *

def grammaticalRelation(arcs):
    tree = {}
    for item in arcs:
        parent = item[0]
        child = item[1]

        item_type = arcs[item]
        if item_type == 'PRED':
            tree['PRED'] = child
        elif item_type == 'TRAIN-NAME':
            tree['LSUBJ'] = child
        elif item_type == 'TIME':
            tree['TIME'] = child
        elif item_type == 'CITY-NAME':
            if getType(parent) == 'arrive':
                tree['TO-LOC'] = child
            else:
                tree['FROM-LOC'] = child
        elif item_type == 'RUN-TIME':
            tree['RUN-TIME'] = 'GAP'
        elif item_type == 'WH-TRAIN':
            tree['LSUBJ'] = 'GAP'
        elif item_type == 'WH-TIME':
            tree['TIME'] = 'GAP'
        elif item_type == 'WHERE':
            if getType(parent) == 'arrive':
                tree['TO-LOC'] = 'GAP'
            else:
                tree['FROM-LOC'] = 'GAP'

    relations = []
    variables = {}
    for rel_type in tree:
        if rel_type == 'PRED':
            variable = generateVariable()
            variables[tree[rel_type]] = variable
            relation = f"({variable} PRED {tree[rel_type]})"
            relations.append(relation)
            break
        
    for rel_type in tree:
        if rel_type == 'PRED':
            continue
        variable = generateVariable()
        variables[tree[rel_type]] = variable
       
        if rel_type == 'RUN-TIME':
            relation = f"({variables[tree['PRED']]} TIME (TIME {variable} GAP))"
        else:
            tk_type = None
            if rel_type == 'LSUBJ':
                tk_type = 'TRAIN-NAME'
            elif rel_type == 'TO-LOC' or rel_type == 'FROM-LOC':
                tk_type = 'CITY-NAME'
            elif rel_type == 'TIME':
                tk_type = 'TIME'
            relation = f"({variables[tree['PRED']]} {rel_type} ({tk_type} {variable} {tree[rel_type]}))"
        relations.append(relation)

        
    fileName = "./Output/output_c.txt"
    output = open(fileName,"a")
    output.write(str(relations))
    output.write("\n")

    return relations