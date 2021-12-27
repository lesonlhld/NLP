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
            if parent == 'từ':
                tree['FROM-LOC'] = child
            else:
                tree['TO-LOC'] = child
        elif item_type == 'RUN-TIME':
            tree['RUN-TIME'] = 'GAP'
        elif item_type == 'WH-TRAIN':
            tree['LSUBJ'] = 'GAP'
        elif item_type == 'WH-TIME':
            tree['TIME'] = 'GAP'
        elif item_type == 'WHERE':
            if parent == 'từ':
                tree['FROM-LOC'] = 'GAP'
            else:
                tree['TO-LOC'] = 'GAP'

    relations = []
    variables = {}
    for relation_type in tree:
        if relation_type == 'PRED':
            variables[tree[relation_type]] = "r"
            relation = f"({variables[tree[relation_type]]} PRED {tree[relation_type]})"
            relations.append(relation)
            break
        
    i = 0
    for relation_type in tree:
        if relation_type == 'PRED':
            continue
        variables[tree[relation_type]] = f"t{i}"
        i = i + 1
       
        if relation_type == 'RUN-TIME':
            relation = f"({variables[tree['PRED']]} TIME (TIME {variables[tree[relation_type]]} GAP))"
        else:
            token_type = None
            if relation_type == 'LSUBJ':
                token_type = 'TRAIN-NAME'
            elif relation_type == 'TO-LOC' or relation_type == 'FROM-LOC':
                token_type = 'CITY-NAME'
            elif relation_type == 'TIME':
                token_type = 'TIME'
            relation = f"({variables[tree['PRED']]} {relation_type} ({token_type} {variables[tree[relation_type]]} {tree[relation_type]}))"
        relations.append(relation)

        
    fileName = "./Output/output_c.txt"
    output = open(fileName,"a")
    output.write(str(relations))
    output.write("\n")

    return relations