# Learning disjunctive logic programs from non-determinsitc state transitions
# Implimented in Python 3.6
# directories:
#   lp  : the logic programs for Boolean networks
#   data: the randomly generated state transitions for these logic programs in lp
#   fig : the running result figrues for the above data (hight resolution)  
#   fig-low : the running result figures for the above data (low resolution)
#   example: some simple state transition instances 

# usage for LFDT.pyc
# LFDT.pyc: The compiled python file to learn disjunctive programs
# statistics.py: The python source code to do statistics for experiments
# gen-lfdt.py: The python source code to generate random state transitions

python3.6 LFDT.pyc --help
Usage: LFDT.pyc [options] <state_transitions>

Options:
  --version   show program's version number and exit
  -h, --help  show this help message and exit
  -q          Running in quiet
  -a          Print atom name instead of atom id
  -n          Using nonrecursive AddRule
  -g          Without ground resolution
  -c          Without combined resolution
  -e          Keep the empty next state
  -s          Simplifying the background program by subsumption checking only
  -d E_LP     Checking equivalence of (B_LP and E_FILE) under one-step-
              transition
  -t MCT      The max CPU time in seconds
  -f L_LP     The learned logic program
  -b B_LP     The back ground logic program

python3.6 statistics.py --help
Usage: statistics.py [options]

Options:
  --version   show program's version number and exit
  -h, --help  show this help message and exit
  -c CLASS    To handle with with
              mammalian|fission|budding|arabidopsis|tcrNet|thelper[-1,0-5]
  -a          draw all the data in one figure
  -r          To deal with recursive one
  -n          To deal without combination resolution
  -g          To deal without ground resolution
  -t          No title in figure
  -o          The generated rules before background rules
  -w          Print wireframe statistics graph
  -s          Print surface statistics graph
  -p          print data
  -d          save data to file
  -l          load data from file
