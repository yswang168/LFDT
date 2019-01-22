import numpy as np 
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from optparse import OptionParser

import os  # for file reading and writting 
import sys
import linecache as lc
import copy
import itertools as it  # for sets product

global BN_NA
global opts
# = [('mammalian', 15), ('fission',10), ('budding', 12), ('arabidopsis',15), ('tcrNet',40), ('thelper', 23)]
Lines_Names = ['LR', 'GR', 'CR', 'OR', 'SR', 'Time', 'Memory']
Titles = ["The number of learned rules", "The number of GR rules", "The number of CR rules", "The number of OR rules", "The number of transition rules", "The running time (s)"]

I_number = [10,20,40,80,160,320,640]
J_number = [2,4,6,8,10]
version = 1.0


# draw the 3D graph with x,y and z
def draw_3d(x,y,z,title):
    fig = plt.figure(frameon = False)
    plt.title(title)
    plt.xlabel('|J|')
    plt.ylabel('|I|') 
    ax = Axes3D(fig)
    X, Y = np.meshgrid(x, y)
    ax.plot_surface(X,y,z)
    #plt.show()
    plt.close()


# draw figure 
def draw_data(ax, x, y, z, fmt):
    for i,vy in enumerate(y):
      tx = []
      tz = []
      for j,_ in enumerate(x):
        if z[i,j] == -1: continue
        tx = tx + [x[j]]
        tz = tz + [z[i,j]]
      if tx != []:
        ty = [vy] * len(tx)
        #ax.scatter(tx, ty, tz, fmt)
        ax.plot(tx, ty, tz, fmt)
    
    #print(z)
    for i,vx in enumerate(x):
      ty = []
      tz = []
      for j,vy in enumerate(y):
        if z[j,i] == -1: continue
        ty = ty + [y[j]]
        tz = tz + [z[j,i]]
      if ty != []:
        tx = [vx] * len(ty)
        ax.plot(tx, ty, tz, fmt)
      

# combine the LR, GR, CR, OR in one figure from data, and write into file: name
def wireframe_all(data, name, LR=True, GR=True, CR=True, OR=True, SR=True):
    fig = plt.figure(frameon = False)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim(0,10)
    ax.set_ylim(0,640)
    bG = [True for i in range(5)]
    bG[0] = LR
    bG[1] = GR
    bG[2] = CR
    bG[3] = OR
    bG[4] = SR
    fmts = ['bo-', 'b*--', 'bs-.', 'bv:', 'b+:']
    x = J_number
    y = I_number
    for i in range(5):
        if bG[i]:
            draw_data(ax, x, y, data[:,:,i], fmts[i])
    plt.xlabel('|Js|')
    plt.ylabel('|I|') 
     
    if name == None:
        plt.show()
    else:
        plt.savefig(name,dpi=600,bbox_inches='tight',frameon = False)
    plt.close()
# draw the 3D graph with x,y and z
def draw_wireframe(x,y,z,title, name=None):
    # removing the margin space
    # plt.axis('off')    
    #plt.gca().xaxis.set_major_locator(plt.NullLocator())
    #plt.gca().yaxis.set_major_locator(plt.NullLocator())
    #plt.subplots_adjust(top = 1, bottom = 0.1, right = 1, left = 0, hspace = 0, wspace = 0)
    #plt.margins(0,0)    
    fig = plt.figure(frameon = False)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim(0,10)
    ax.set_ylim(0,640)
    '''X, Y = np.meshgrid(x, y)
    Z = copy.copy(z) 
    ax.plot_wireframe(X, Y, Z)#, cmap=cm.coolwarm,linewidth=0, antialiased=False) 
    '''
    #print(z)
    for i,vy in enumerate(y):
      tx = []
      tz = []
      for j,_ in enumerate(x):
        if z[i,j] == -1: continue
        tx = tx + [x[j]]
        tz = tz + [z[i,j]]
      if tx != []:
        ty = [vy] * len(tx)
        ax.scatter(tx, ty, tz, c='b')
        ax.plot(tx, ty, tz, c='b')
    
    #print(z)
    for i,vx in enumerate(x):
      ty = []
      tz = []
      for j,vy in enumerate(y):
        if z[j,i] == -1: continue
        ty = ty + [y[j]]
        tz = tz + [z[j,i]]
      if ty != []:
        tx = [vx] * len(ty)
        ax.plot(tx, ty, tz, c='b')
      
    plt.title(title)
    plt.xlabel('|Js|')
    plt.ylabel('|I|') 
     
    if name == None:
        plt.show()
    else:
        plt.savefig(name,dpi=600,bbox_inches='tight',frameon = False)
    plt.close()

def draw_surface(x,y,z,title, name=None):

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X, Y = np.meshgrid(x, y)

    # Plot the surface.
    surf = ax.plot_surface(X, Y, z)#, cmap=cm.coolwarm,linewidth=0, antialiased=False) 
    plt.title(title)
    plt.xlabel('|Js|')
    plt.ylabel('|I|') 

    #ax = Axes3D(fig)
    #ax.plot_surface(X,Y,z)
    if name == None:
        plt.show()
    else:
        plt.savefig(name,dpi=600)
    plt.close()
    # draw the 3D graph with x,y and z, z include the data OR,NR,GR and CR

def draw_surface_OR_NR_GR_CR(x,y,z):
    
    figure,ax=plt.subplots(2,2)

    #fig = plt.figure()
    #ax = fig.gca(projection='3d')
    X, Y = np.meshgrid(x, y)
    # Plot the surface.
    ax[0][0].plot_surface(X, Y, z[0]) 
    ax[0][1].plot_surface(X, Y, z[1]) 
    ax[1][0].plot_surface(X, Y, z[2])
    ax[1][1].plot_surface(X, Y, z[3]) 
    ax[0][0].set_title("OR")
    ax[0][1].set_title("NR")
    ax[1][0].set_title("GR")
    ax[1][1].set_title("CR")
    plt.title("The number of rules")
    plt.xlabel('|J|')
    plt.ylabel('|I|') 

    #ax = Axes3D(fig)
    # ax.plot_surface(X,Y,z)
    plt.show()
# read from the result, averaging the counting, write to the np.array npa
def average_state(res_file, ni, npa):    
    avg_num_of_learned_rules = 0
    avg_num_of_gr_rules = 0
    avg_num_of_cr_rules = 0
    avg_num_of_bg_rules = 0
    avg_num_of_old_rules = 0
    avg_num_of_st_rules = 0
    avg_utime = 0
    avg_stime = 0
    avg_total_time = 0
    avg_mem = 0
    i_j_trans_name = list()
    BN_I_J = set()
    BN_I_J_list = list()
    num_of_sameij= 0 
    lineca = lc.getlines(res_file)

     
    for i in range(len(lineca)):
        if '-------' in  lineca[i] :
            if ((i + 3) >= len(lineca)):
                lineca[i] = '*'
                lineca[i + 1] = '*'
                lineca[i + 2] = '*'
            else:
                if 'The number of learned rules' in lineca[i + 3]:
                    continue
                else:
                    lineca[i] ='*'
                    lineca[i+1] = '*'
                    lineca[i + 2] = '*'
    lineca_1 = list()
    for idx,item in enumerate(lineca):
        if (item.strip() != '*'):
            lineca_1.append(item) 

    lineca_slic = [lineca_1[i:i+13] for i in range(0,len(lineca_1),13)] 
    for i in range(len(lineca_slic)):
        idx = lineca_slic[i][1].strip().rfind('-')
        str1 = lineca_slic[i][1][0:idx] 
        BN_I_J.add(str1) 
    BN_I_J_list = sorted(BN_I_J, key=lambda x: (int(x.split('-')[1]), int(x.split('-')[2]))) 
    ##### Following is added by Yisong
    Is=[10, 20, 40, 80, 160, 320, 640]
    Js=[2,4,6,8,10]
    IJs = [str(x)+'-'+str(y) for x in Is for y in Js]   
    ii = 0 # for the index of npa
        
    for i in range(len(IJs)):
    #for i in range(len(BN_I_J_list)):
    ####     
        if ii == len(BN_I_J_list) or not (IJs[i] in BN_I_J_list[ii]): continue
        ii += 1
        sum_same_num_ij = 0
        sum_of_learned_rules = 0
        sum_of_gr_rules = 0
        sum_of_cr_rules = 0
        sum_of_bg_rules = 0
        sum_of_old_rules = 0
        sum_of_st_rules = 0 # the number of rules from state transitons
        sum_utime = 0.0
        sum_stime = 0.0
        sum_total_time = 0.0
        sum__mem = 0
        for j in range(len(lineca_slic)):
            if ((BN_I_J_list[ii-1] in lineca_slic[j][1]) == True):                
                if (('The number of learned rules' in lineca_slic[j][3]) == True ):
                    sum_same_num_ij += 1
                    num_of_learned_rules = int(lineca_slic[j][3].split(':')[1])
                    sum_of_learned_rules = sum_of_learned_rules + num_of_learned_rules
                    #print(num_of_learned_rules)

                    num_of_gr_rules = int(lineca_slic[j][4].split(':')[1])
                    sum_of_gr_rules = sum_of_gr_rules + num_of_gr_rules
                    #
                    num_of_cr_rules = int(lineca_slic[j][5].split(':')[1])
                    sum_of_cr_rules = sum_of_cr_rules + num_of_cr_rules
                    #
                    if not (opts.old_rule): 
                        num_of_bg_rules = int(lineca_slic[j][6].split(':')[1])
                        sum_of_bg_rules = sum_of_bg_rules + num_of_bg_rules
                        #num_of_old_rules = int(lineca_slic[j][6].split(':')[1])
                        #sum_of_old_rules = sum_of_old_rules + num_of_old_rules
                        #
                        num_of_old_rules = int(lineca_slic[j][7].split(':')[1])
                        sum_of_old_rules = sum_of_old_rules + num_of_old_rules
                        #num_of_bg_rules = int(lineca_slic[j][7].split(':')[1])
                        #sum_of_bg_rules = sum_of_bg_rules + num_of_bg_rules
                    else:
                        #num_of_bg_rules = int(lineca_slic[j][6].split(':')[1])
                        #sum_of_bg_rules = sum_of_bg_rules + num_of_bg_rules
                        num_of_old_rules = int(lineca_slic[j][6].split(':')[1])
                        sum_of_old_rules = sum_of_old_rules + num_of_old_rules
                        #
                        #num_of_old_rules = int(lineca_slic[j][7].split(':')[1])
                        #sum_of_old_rules = sum_of_old_rules + num_of_old_rules
                        num_of_bg_rules = int(lineca_slic[j][7].split(':')[1])
                        sum_of_bg_rules = sum_of_bg_rules + num_of_bg_rules
                    # the number of rules diectedly from state transitions (removing being subsumed head)
                    num_st_rules = int(lineca_slic[j][8].split(':')[1])
                    sum_of_st_rules = sum_of_st_rules + num_st_rules

                    num_utime = float(lineca_slic[j][9].split(':')[1][0:lineca_slic[j][9].split(':')[1].find('(')])
                    sum_utime = sum_utime + num_utime
                    #printnum_utime
                    num_stime = float(lineca_slic[j][10].split(':')[1][0:lineca_slic[j][10].split(':')[1].find('(')])
                    sum_stime = sum_stime + num_stime
                    #
                    num_total_time = float(lineca_slic[j][11].split(':')[1][0:lineca_slic[j][11].split(':')[1].find('(')])
                    sum_total_time = sum_total_time + num_total_time
                    #
                    num__mem = float(lineca_slic[j][12].split(':')[1][0:lineca_slic[j][12].split(':')[1].find('(')])
                    sum__mem = num__mem + sum__mem
        if (sum_same_num_ij != 0):
            avg_num_of_learned_rules = round(sum_of_learned_rules/sum_same_num_ij,2)
            #print(avg_num_of_gr_rules)
            #avg_gr_str= 'Avg of the number of learned rules is:' + avg_num_of_gr_rules
            avg_num_of_gr_rules = round(sum_of_gr_rules / sum_same_num_ij, 2)
            avg_num_of_cr_rules = round(sum_of_cr_rules / sum_same_num_ij, 3)
            avg_num_of_bg_rules = round(sum_of_bg_rules / sum_same_num_ij, 3)
            avg_num_of_old_rules = round(sum_of_old_rules / sum_same_num_ij,2)
            avg_num_of_st_rules = round(sum_of_st_rules / sum_same_num_ij,2)
            avg_utime = round(sum_utime / sum_same_num_ij,2)
            avg_stime = round(sum_stime / sum_same_num_ij,2)
            avg_total_time = round(sum_total_time / sum_same_num_ij,4)
            avg_mem = round(sum__mem / sum_same_num_ij,2)
        
            # write to npa 
            npa[ni][int(i/5)][i%5][0] = avg_num_of_learned_rules
            npa[ni][int(i/5)][i%5][1] = avg_num_of_gr_rules
            npa[ni][int(i/5)][i%5][2] = avg_num_of_cr_rules
            npa[ni][int(i/5)][i%5][3] = avg_num_of_old_rules
            npa[ni][int(i/5)][i%5][4] = avg_num_of_st_rules
            npa[ni][int(i/5)][i%5][5] = avg_total_time
            npa[ni][int(i/5)][i%5][6] = avg_mem 
        
    return npa

# wireframe
def wireframe(arr, name=None, all_in_one=False, cr=True):
    if name != None:
        Names = ["wf_" + name+ "_" + Lines_Names[i] for i in range(len(Lines_Names))]
    else:
        Names = [None]*5

    if all_in_one:
        wireframe_all(arr,"wf_"+name, CR=cr)
    else:
        for i in range(6):
            draw_wireframe(J_number,I_number, arr[:,:,i], Titles[i], Names[i]) 

    # wireframe
def surface(arr, name):
    if name != None:
        Names = ["sf_" + name+ "_" + Lines_Names[i] for i in range(len(Lines_Names))]
    else:
        Names = [None]*5
    
    for i in range(5):
        draw_surface(J_number,I_number, arr[:,:,i], Titles[i], Names[i]) 

# plot the time from the data npa
# the options for the main function
def CreateOptions():
    parse = OptionParser(usage="%prog [options]", version="%prog "+str(version))   
    parse.add_option("-c", action="store", type="int", dest="Class", help="To handle with with mammalian|fission|budding|arabidopsis|tcrNet|thelper[-1,0-5]",default=-1)  
    parse.add_option("-a", action="store_true",dest="all_in_one", help="draw all the data in one figure", default=False)  
    parse.add_option("-r", action="store_false",dest="recursive", help="To deal with recursive one", default=True)  
    parse.add_option("-n", action="store_false",dest="no_combination", help="To deal without combination resolution", default=True)  
    parse.add_option("-g", action="store_true",dest="no_gresolution", help="To deal without ground resolution", default=False)
    parse.add_option("-t", action="store_true",dest="no_title", help="No title in figure", default=False)      
    parse.add_option("-o", action="store_false",dest="old_rule", help="The generated rules before background rules", default=True) 
    parse.add_option("-w", action="store_true",dest="p_wireframe", help="Print wireframe statistics graph", default=False) 
    parse.add_option("-s", action="store_true",dest="p_surface", help="Print surface statistics graph", default=False) 
    parse.add_option("-p", action="store_true",dest="p_data", help="print data",default=False) 
    parse.add_option("-d", action="store_true",dest="save_data", help="save data to file",default=False) 
    parse.add_option("-l", action="store_true",dest="load_data", help="load data from file",default=False) 
    return parse

if __name__ == "__main__":
    BClass = ['mammalian','fission','budding','arabidopsis','tcrNet','thelper']
    NoAtoms = [10,10,12,15,40,23]
    parse = CreateOptions()
    (opts, args) = parse.parse_args()
    if  opts.Class > 5 or opts.Class < -1:
        parse.print_help()
        sys.exit()

    if opts.no_title:
        Titles = ["", "", "", "", "", ""]

    if opts.recursive:
        BClass = [x + '-n' for x in BClass]
    if opts.no_combination:
        BClass = [x + '-c' for x in BClass]
    if opts.no_gresolution:
        BClass = [x + '-g' for x in BClass]

    #BClass = [x + '-q-4' for x in BClass]
    if opts.Class == -1:
        BN_NA = [(i,j) for i,j in zip(BClass, NoAtoms)]
    else:
        BN_NA = [(BClass[opts.Class], NoAtoms[opts.Class])]
    '''
    if opts.Class == -1:
        if opts.recursive:         
            BN_NA = [('mammalian-n', 15), ('fission-n',10), ('budding-n', 12), ('arabidopsis-n',15), ('tcrNet-n',40), ('thelper-n', 23)]
        else:
            BN_NA = [('mammalian', 15), ('fission',10), ('budding', 12), ('arabidopsis',15), ('tcrNet',40), ('thelper', 23)]
    else:
        if opts.recursive:
            BN_NA = [(BClass[opts.Class], NoAtoms[opts.Class])]
        else:
            BN_NA = [(BClass[opts.Class]+'-n', NoAtoms[opts.Class])]
    '''
    Total_elements = len(I_number) * len(J_number) * len(Lines_Names)
    np_arr = np.array([-1.0]*Total_elements*len(BN_NA)).reshape(len(BN_NA),len(I_number), len(J_number), len(Lines_Names)) 
    for i in range(len(BN_NA)): 
        if opts.load_data: 
            np.load(BN_NA[i][0]+'.npy',np_arr[i])
        else:
            average_state(BN_NA[i][0]+'.res', i, np_arr)
        if opts.p_wireframe:
            wireframe(np_arr[i], BN_NA[i][0], opts.all_in_one, cr=not(opts.no_combination))
        if opts.p_surface:
            surface(np_arr[i], BN_NA[i][0]) 
        if opts.save_data:
            np.save(BN_NA[i][0], np_arr[i])
        if opts.p_data:
            print(BN_NA[i][0])
            print(np_arr[i])
        






