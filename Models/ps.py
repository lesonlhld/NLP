from Models.variableutil import create_variable

def lf2ps(logical_form):
    # extract logical form
    wh = logical_form[:logical_form.index('(')]
    lf_components = logical_form[logical_form.index('('):][1:-1].split('[')
    lf_components = [component[:-1] if component[-1] == ']' else component for component in lf_components]

    fields = {} # contain query fields along with data or variable
    for component in lf_components:
        temp = component.replace('(', '').replace(')', '').split()
        if len(temp) == 2:
            continue
        
        fields[temp[0] if temp[0] != 'AGENT' else 'TRAIN-NAME'] = temp[3]

    # build procedural semantic
    # tables format in data base
    train = {'NAME': 'TRAIN', 'DATA': {'TRAIN-NAME': ''}}
    atime = {'NAME': 'ATIME', 'DATA': {'TRAIN-NAME': '', 'TO-LOC': '', 'TO-TIME': ''}}
    dtime = {'NAME': 'DTIME', 'DATA': {'TRAIN-NAME': '', 'FROM-LOC': '', 'FROM-TIME': ''}}
    runtime = {'NAME': 'RUN-TIME', 'DATA': {'TRAIN-NAME': '','FROM-LOC': '','TO-LOC': '', 'RUN-TIME': ''}}
    for f in fields:
        for table in [train, atime, dtime, runtime]:
            if f in table['DATA']:
                table['DATA'][f] = fields[f]


    ps = f"PRINT-ALL" # procedural semantic
    
    for f in fields:
        # field to query is field with GAP value
        if fields[f] == 'GAP':
            fields[f] = create_variable('t')
            ps += f" ?{fields[f]} "

    for table in [train, atime, dtime, runtime]:
        # determine table is used for query or not
        no_info = True
        all_gap = True
        for column in table['DATA']:
            if table['DATA'][column] != 'GAP':
                all_gap = False
                if table['DATA'][column] != '':
                    no_info = False
                    break
        unused = no_info and not all_gap # table unused if it does not contain any information (table with all column is GAP is used)
            
        if not unused: # table is used for query
            ps += f"({table['NAME']}"
            for column in table['DATA']:
                if table['DATA'][column] != 'GAP' and table['DATA'][column] != '': # column has data
                    ps += f" {table['DATA'][column]}"
                else: # column does not has data
                    if column not in fields:  # variable is not created
                        fields[column] = create_variable('t')
                    ps += f" ?{fields[column]}"
            ps += f")"


    return ps