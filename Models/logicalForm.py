def extract_relation(relation):
    relation = relation[1:-1]
    first_space = relation.index(' ')
    second_space = relation.index(' ', first_space+1)

    left = relation[:first_space]
    relation_type = relation[first_space+1:second_space]
    right = relation[second_space+1:]

    if right[0] == '(':
        right = right[1:-1]

    return relation_type, left, right

def logicalForm(relations):
    logical_form = ""
    variables = {}
    for rel in relations:
        relation_type, left, right = extract_relation(rel)
        if relation_type == 'PRED':
            logical_form += f"({right} {left})"
            variables[left] = {'type': 'PRED', 'value': right}
    for rel in relations:
        relation_type, left, right = extract_relation(rel)
        if relation_type == 'PRED':
            continue
        elif relation_type == 'LSUBJ':
            vtype, vname, vvalue = right.split()
            variables[vname] = {'type': vtype, 'value': vvalue}
            logical_form = logical_form[:-1] + f"[AGENT ({right})]" + logical_form[-1]
        else:
            vtype, vname, vvalue = right.split()
            variables[vname] = {'type': relation_type, 'value': vvalue}
            logical_form = logical_form[:-1] + f"[{relation_type} ({right})]" + logical_form[-1]

    has_gap = False
    for vname in variables:
        if variables[vname]['value'] == 'GAP':
            has_gap = True
            logical_form = 'WH-' + variables[vname]['type'] + ' ' + logical_form

    if not has_gap:
        logical_form = 'YESNO-WH ' + logical_form
        
    fileName = "./Output/output_d.txt"
    output = open(fileName,"a")
    output.write(str(logical_form))
    output.write("\n")

    return logical_form