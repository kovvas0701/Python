
from numpy import true_divide


def Versiespar(listadenumeros):

    for i in listadenumeros:
        if i % 2==0:
            print('True')
            return True
    
    else:
        pass
    print ('False')
    return False
    


Versiespar([1,3,5])