from Models.fileutil import load_file, save_file
from Models.parser import maltParser
from Models.gr import grammatical_relation
from Models.lf import gr2lf
from Models.ps import lf2ps
from Models.query import query


# load questions
questions = load_file('./Input/questions.txt')

def main():
    tree_lst = []
    gr_lst = []
    lf_lst = []
    ps_lst = []
    result_lst = []
    for q in questions:
        # answer question
        tree = maltParser(q) # dependency tree
        gr = grammatical_relation(tree) # grammatical relation
        lf = gr2lf(gr) # logical form
        ps = lf2ps(lf)  # procedural semantic
        result = query(ps) # query's result
        
        # record result of each step
        tree_lst.append(str(tree))
        gr_lst.append(str(gr))
        lf_lst.append(str(lf))
        ps_lst.append(str(ps))
        result_lst.append(str(result))

    save_file(tree_lst, './Output/output_a.txt')
    save_file(gr_lst, './Output/output_c.txt')
    save_file(lf_lst, './Output/output_d.txt')
    save_file(ps_lst, './Output/output_e.txt')
    save_file(result_lst, './Output/output_f.txt')
    


if __name__ == '__main__':
    main()