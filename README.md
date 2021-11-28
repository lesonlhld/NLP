# Simple Vietnamese train answering system
[github link](https://github.com/buingohoanglong/NLP-assignment)

## Project structure
1. **Input** folder:
    * questions.txt: contains questions to ask the system, each line is a question.
    * train_dataset.txt: store train with format (TRAIN \<TRAIN-NAME>)
    * atime_dataset.txt: store train arrival information with format (ATIME \<TRAIN-NAME> \<TO-LOC> \<TO-TIME>)
    * dtime_dataset.txt: store train departure information with format (DTIME \<TRAIN-NAME> \<FROM-LOC> \<FROM-TIME>)
    * runtime_datset.txt: store train trip information with format (RUN-TIME \<TRAIN-NAME> \<FROM-LOC> \<TO-LOC> \<RUNTIME>)
2. **Output** folder:
    * output_a.txt: depency trees from malt parser
    * output_c.txt: grammatical relations
    * output_d.txt: logical forms
    * output_e.txt: procedural semamtics
    * output_f.txt: answers for each questions in Input/questions.txt
3. **Models** folder:
    * parser.py: malt parser, generate dependency tree from raw question
    * gr.py: generate grammatical relation from dependency tree
    * lf.py: generate logical form from grammatical relation
    * ps.py: generate procedural sementic from logical form
    * query.py: use procedural sementic to query data in datasets
    * token.py: define token's type
    * dependency.py: define dependent relation between token types
    * variableutil.py: provide utilities for creating unique variable's name
    * fileutil.py: provide utilities for loading and saving files
4. **main.py**: entry of program

## Run project:
`python3 main.py`

## Author:
[buingohoanglong](https://github.com/buingohoanglong/)