def extract_relation(relation):
    relation = relation[1:-1]
    first_space = relation.index(' ')
    second_space = relation.index(' ', first_space+1)

    left_component = relation[:first_space]
    relation_type = relation[first_space+1:second_space]
    right_component = relation[second_space+1:]

    if right_component[0] == '(':
        right_component = right_component[1:-1]

    return relation_type, left_component, right_component

def gr2lf(relations):
    logical_form = ""
    variables = {}
    for rel in relations:
        rel_type, left, right = extract_relation(rel)
        if rel_type == 'PRED':
            logical_form += f"({right} {left})"
            variables[left] = {'type': 'PRED', 'value': right}
    for rel in relations:
        rel_type, left, right = extract_relation(rel)
        if rel_type == 'PRED':
            continue
        elif rel_type == 'LSUBJ':
            vtype, vname, vvalue = right.split()
            variables[vname] = {'type': vtype, 'value': vvalue};
            logical_form = logical_form[:-1] + f"[AGENT ({right})]" + logical_form[-1]
        else:
            vtype, vname, vvalue = right.split()
            variables[vname] = {'type': rel_type, 'value': vvalue}
            logical_form = logical_form[:-1] + f"[{rel_type} ({right})]" + logical_form[-1]

    for vname in variables:
        if variables[vname]['value'] == 'GAP':
            logical_form = 'WH-' + variables[vname]['type'] + logical_form

    return logical_form