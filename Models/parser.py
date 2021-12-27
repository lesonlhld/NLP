from underthesea import word_tokenize, dependency_parse
from copy import deepcopy

token_types = {
    'train': ['tàu_hỏa', 'Tàu_hỏa', 'tàu'],
    'run': ['chạy'],
    'city': ['thành_phố', 'Thành_phố', 'TP', 'Tp'],
    'arrive': ['đến', 'tới'],
    'from': ['từ'],
    'which': ['nào', 'mấy_giờ'],
    'where': ['đâu'],
    'yesno': ['không'],
    'time': ['lúc', 'vào_lúc', 'từ_lúc', 'Thời_gian', 'thời_gian'],
    'name': ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'HUE', 'HCM', 'HCMC', 'HN', 'DANANG', 'Hồ_Chí_Minh', 'Hà_Nội', 'Huế', 'Đà_Nẵng', 'Nha_Trang', 'NTrang'],
    'hour': ['hour'],
}

def getType(token):
    for token_type in token_types:
        if token in token_types[token_type]:
            return token_type
    if token.find("HR") != -1:
        return 'hour'
    if token == '<ROOT>':
        return token
    return '<UNKNOWN>'

relations = {
    'run': {'<ROOT>': 'PRED'},
    'train': {'run': 'LSUBJ', 'time': 'TIME'},
    'arrive': {'run': 'PREP'},
    'from': {'run': 'PREP'},
    'time': {'from': 'FROM-TIME', 'arrive': 'ARRIVE-TIME', 'train': 'RUN-TIME'},
    'hour': {'time': 'TIME'},
    'city': {'from': 'FROM-LOC', 'arrive': 'TO-LOC'},
    'name': {'city': 'CITY-NAME', 'from': 'CITY-NAME', 'arrive': 'CITY-NAME', 'train': 'TRAIN-NAME'},
    'which': {'train': 'WH-TRAIN', 'time': 'WH-TIME'},
    'where': {'from': 'WHERE', 'arrive': 'WHERE'},
    'yesno': {'run': 'YESNO-WH'},
}

def prepare(sentence):
    remove_tokens = ['là mấy giờ', 'thành phố', 'TP', 'có', '.', ':', ',']
    for token in remove_tokens:
        sentence = sentence.replace(token, '')

    sentence = sentence.replace('Tàu hỏa', 'tàu_hỏa')
    sentence = sentence.replace('tàu hỏa', 'tàu_hỏa')
    sentence = sentence.replace('mấy giờ', 'mấy_giờ')

    return sentence

def getAction(stack, buffer):
    left_type = getType(stack[-1])
    right_type = getType(buffer[0])
    if left_type in relations and right_type in relations[left_type]:
        return 'LA'
    elif right_type in relations and left_type in relations[right_type]:
        return 'RA'
    else:
        if left_type == '<ROOT>':
            for token in buffer:
                if left_type in relations[getType(token)]:
                    return 'SHIFT'
        else:
            if left_type in relations[getType(buffer[0])]:
                return 'SHIFT'
        if left_type in relations:
            for token in buffer:
                if getType(token) in relations[left_type]:
                    return 'SHIFT'
        return 'REDUCE'
            
def parser(sentence):
    if not 'chạy' in sentence:
        i = min([sentence.find(x) for x in ["đến", "từ", "lúc"] if (sentence.find(x) > 0)])
        sentence = sentence[:i] + 'chạy ' + sentence[i:]
        
    sentence = prepare(sentence)
    tokens = word_tokenize(sentence)
    relation_types = dependency_parse(sentence)
    relation_types = {x[0].replace(" ", "_"):x[2] for x in relation_types}

    if '?' in tokens:
        tokens.remove('?')
    for i in range(len(tokens)):
        tokens[i] = tokens[i].replace(" ", "_")

    buffer = tokens
    stack = ['<ROOT>']
    arcs = {}

    parsing = "{0:6} {1:40} {2:80} {3}\n".format("Action","Stack","Buffer","Arcs")
    parsing = parsing + "{0:6} {1:40} {2:80} {3}\n".format("",str(stack),str(buffer),str([relation_types[x[1]]+str(x) for x in arcs]).replace('"','').replace("', '",'->').replace("'",'').replace("<ROOT>",'ROOT'))
    while len(buffer) > 0:
        action = getAction(stack, buffer)
        if action == 'LA':
            arcs[(deepcopy(buffer[0]), deepcopy(stack[-1]))] = relations[getType(stack[-1])][getType(buffer[0])]
            stack.pop()
        elif action == 'RA':
            arcs[(deepcopy(stack[-1]), deepcopy(buffer[0]))] = relations[getType(buffer[0])][getType(stack[-1])]
            token = buffer.pop(0)
            is_remove = True
            for dependant in relations:
                if getType(token) in relations[dependant]:
                    is_remove = False
            if not is_remove:
                stack.append(token)
        elif action == 'SHIFT':
            token = buffer.pop(0)
            stack.append(deepcopy(token))
        else:
            stack.pop()

        parsing = parsing + "{0:6} {1:40} {2:80} {3}\n".format(str(action),str(stack),str(buffer),str([relation_types[x[1]]+str(x) for x in arcs]).replace('"','').replace("', '",'->').replace("'",'').replace("<ROOT>",'ROOT'))

    fileName = "./Output/output_a.txt"
    output = open(fileName,"a")
    output.write(str(parsing))
    output.write("\n")

    fileName = "./Output/output_b.txt"
    output = open(fileName,"a")
    output.write(str([relation_types[x[1]]+str(x) for x in arcs]).replace('"','').replace("', '",'->').replace("'",'').replace("<ROOT>",'ROOT'))
    output.write("\n")
    
    return arcs