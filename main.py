from Models.parser import parser
from Models.grammaticalRelation import grammaticalRelation
from Models.logicalForm import logicalForm
from Models.proceduralSemantics import proceduralSemantics
from Models.query import query

with open('./Input/questions.txt', 'r') as f:
    questions = []
    for row in f.readlines():
        questions.append(row if row[-1] != '\n' else row[:-1])

def main():
    for q in questions:
        arcs = parser(q)  # Văn phạm phụ thuộc và quan hệ ngữ nghĩa
        grammarical_relation = grammaticalRelation(arcs)  # Quan hệ văn phạm
        logical_form = logicalForm(grammarical_relation)  # Dạng luận lý
        procedural_semantic = proceduralSemantics(logical_form)  # Ngữ nghĩa thủ tục
        result = query(procedural_semantic)  # Truy xuất dữ liệu
        print('Câu hỏi: ' + str(q) + '\nTrả lời: ' + str(', '.join(result)) + '\n')

if __name__ == '__main__':
    main()