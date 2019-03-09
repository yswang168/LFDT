# Learning disjunctive logic programs from non-determinsitc state transitions
# Implimented in Python 3.6
# directories:
#   lp  : the logic programs for Boolean networks
#   data: the randomly generated state transitions for these logic programs in lp
#   fig : the running result figrues for the above data (hight resolution)  
#   fig-low : the running result figures for the above data (low resolution)
#   example: some simple state transition instances 

# usage for LFDT.pyc
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
