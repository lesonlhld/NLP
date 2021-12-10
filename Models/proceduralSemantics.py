from Models.helper import *

def proceduralSemantics(logical_form):
    lf_components = logical_form[logical_form.index('('):][1:-1].split('[')
    lf_components = [component[:-1] if component[-1] == ']' else component for component in lf_components]

    fields = {}
    for component in lf_components:
        tmp = component.replace('(', '').replace(')', '').split()
        if len(tmp) == 2:
            continue
        
        fields[tmp[0] if tmp[0] != 'AGENT' else 'TRAIN-NAME'] = tmp[3]

    dataset = {'NAME': '', 'DATA': {'TRAIN-NAME': '','FROM-LOC': '','TO-LOC': '', 'TIME': ''}}
    for f in fields:
        if f in dataset['DATA']:
            dataset['DATA'][f] = fields[f]
        elif f == 'RUN-TIME':
            dataset['DATA']['TIME'] = fields[f]

    dataset['DATA'] = {k: dataset['DATA'][k] for k in dataset['DATA'] if dataset['DATA'][k]!=''}
    if 'FROM-LOC' in dataset['DATA'] and 'TO-LOC' in dataset['DATA']:
        dataset['NAME'] = 'RUN-TIME'
    elif 'FROM-LOC' in dataset['DATA']:
        dataset['NAME'] = 'DTIME'
    elif 'TO-LOC' in dataset['DATA']:
        dataset['NAME'] = 'ATIME'

    ps = f""

    has_gap = False
    for f in fields:
        if fields[f] == 'GAP':
            has_gap = True
            fields[f] = generateVariable('t')
            ps += f"?{fields[f]} "

    if has_gap:
        ps = f"PRINT-ALL " + ps
    else:
        ps = f"CHECK " + ps

    ps += f"({dataset['NAME']}"
    for column in dataset['DATA']:
        if dataset['DATA'][column] != 'GAP':
            ps += f" {dataset['DATA'][column]}"
        else:
            if column not in fields:
                fields[column] = generateVariable('t')
            ps += f" ?{fields[column]}"
    ps += f")"

    fileName = "./Output/output_e.txt"
    output = open(fileName,"a")
    output.write(str(ps))
    output.write("\n")

    return ps