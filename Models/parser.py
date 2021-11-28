from pyvi import ViTokenizer
from Models.token import token_type
from Models.dependency import dependency
from copy import deepcopy

def preprocess(sentence):
    remove_tokens = ['?', '.', ':']
    for token in remove_tokens:
        sentence = sentence.replace(token, '')
    return sentence

def action(stack, buffer):
    left_type = token_type(stack[-1])
    right_type = token_type(buffer[0])
    if left_type in dependency and right_type in dependency[left_type]: # left_type <- right_type
        return 'LA'
    elif right_type in dependency and left_type in dependency[right_type]: # left_type -> right_type
        return 'RA'
    else:
        is_reduce = True
        for tk in buffer:
            if left_type in dependency[token_type(tk)]: # token -> tk
                is_reduce = False
                break
        if left_type in dependency:
            for tk in buffer:
                if token_type(tk) in dependency[left_type]: # tk -> token
                    is_reduce = False
        if is_reduce:
            return 'REDUCE'
        else:
            return 'SHIFT'

def check_redundant(token, buffer):
    is_redundant = True
    for tk in buffer:
        if token_type(token) in dependency[token_type(tk)]: # token -> tk
            is_redundant = False
            break
    if token_type(token) in dependency:
        for tk in buffer:
            if token_type(tk) in dependency[token_type(token)]: # tk -> token
                is_redundant = False
    return is_redundant

def maltParser(sentence):
    tokens = preprocess(sentence)
    buffer = ViTokenizer.tokenize(tokens).split()
    # print(buffer)
    # print([token_type(token) for token in buffer])
    stack = ['<ROOT>']
    tree = {}
    while len(buffer) != 0:
        left_type = token_type(stack[-1])
        right_type = token_type(buffer[0])

        if left_type == right_type:
            buffer.pop(0)
            continue
        
        current_action = action(stack, buffer)
        if current_action == 'LA':
            tree[(deepcopy(buffer[0]), deepcopy(stack[-1]))] = dependency[token_type(stack[-1])][token_type(buffer[0])]
            stack.pop()
        elif current_action == 'RA':
            tree[(deepcopy(stack[-1]), deepcopy(buffer[0]))] = dependency[token_type(buffer[0])][token_type(stack[-1])]
            token = buffer.pop(0)
            is_remove = True
            for dependant in dependency:
                if right_type in dependency[dependant]:
                    is_remove = False
            if not is_remove:
                stack.append(token)
        elif current_action == 'SHIFT':
            token = buffer.pop(0)
            stack.append(deepcopy(token))
        else:
            stack.pop()

    return tree   