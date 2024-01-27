import npuzzle

'''Conditions of fulfillment'''
def condition(n,env):
    tab=[]
    counter=0                       #Counter of inverse
    ind = 0                         #Blank line index
    result=False                    #Return False/ True

    '''List of numbers from the table'''
    for r in range(n):
        for c in range(n):
            tab.append(env.read_tile(r,c))
            if env.read_tile(r,c)==None:
                ind=r

    '''Count inversion'''
    for i in range(len(tab)):
        for j in range(i,len(tab)):
            if tab[i] != None and tab[j] != None:
                if tab[i]> tab[j]:
                    counter+=1

    '''Conditions'''
    if counter%2 == 0:
        if n ==3:                   #Only condition for 3x3 npzzle
            result= True
        if n ==4:
            if ind%2!=0:            #First condition for 4x4 npuzzle
                result=True

    if counter%2 !=0 and n==4:      #Second condition for 4x4 npuzzle
        if ind%2==0:
            result = True

    return result

'''Return True/False by condition'''
def is_solvable(env):
    '''Delete error message'''
    try:
        env.read_tile(3,3)

    except:
        '''npuzzle 3x3'''
        if condition(3,env):
            return True
        else:
            return False

    else:
        '''npuzzle 4x4'''
        if condition(4,env):
            return True
        else:
            return False

if __name__ == "__main__":
    env = npuzzle.NPuzzle(4)        #npuzzle.NPuzzle(4)
    env.reset()
    env.visualise()
    # just check
    print(is_solvable(env))