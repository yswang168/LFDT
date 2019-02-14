./programs/GEN_LF1T.exe 0 example-1-1
Extracted parameter [debug]: 0
Extracted parameter [input_file]: example-1-1
Var extracted: p, id 0
Var extracted: q, id 1
Var extracted: r, id 2
Variables extracted
Pre-processing input...
Var 0 val 1

Var 0 val 2

Var 1 val 1

Var 1 val 2

Var 2 val 1

Var 2 val 2

Variable: p, value: 0

Variable: p, value: 1

Variable: q, value: 0

Variable: q, value: 1

Variable: r, value: 0

Variable: r, value: 1

Final output: 

VAR p 0 1
VAR q 0 1
VAR r 0 1


p(0,T) :- q(0,T-1).
p(1,T) :- q(1,T-1).
p(1,T) :- p(1,T-1), r(1,T-1).
q(0,T).
q(1,T) :- p(0,T-1).
q(1,T) :- q(0,T-1), r(1,T-1).
r(0,T).
r(1,T) :- p(0,T-1).
Finish
