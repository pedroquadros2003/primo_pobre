import sys
from pathlib import Path
from SolversImplementation.AbstractImplementation import AbstractImplementation
#this is supposed to be called fom parent directory

# Adiciona o diretório pai ao Python path
sys.path.append(str(Path(__file__).parent.parent))
from Plan import Plan
import heapq

class Implementation(AbstractImplementation):

    def __init__(self):
        pass

    def solve(self, plan):
        ## the input is a plan, the output must be a solution_list,
        ## as in the example below
        monthly_available_list = plan.get_monthly_available_list()
        lista_monthly_fees = []
        lista_montantes_iniciais = []
        lista_debt_names = []
        
        debt_dic = plan.get_debt_dict()
        for key in debt_dic :
            lista_debt_names.append(key)
            lista_monthly_fees.append(debt_dic[key].get_monthly_fee())
            lista_montantes_iniciais.append(debt_dic[key].get_total_to_pay())
        vaktra = greedy_dc(lista_monthly_fees, lista_montantes_iniciais, monthly_available_list)
        if vaktra == -1:
            print("no solution found :(")
            return None
        ret_val = []
        for month in vaktra:
            dic = {}
            for i in range(0, len(lista_debt_names)):
                dic[lista_debt_names[i]] = month[i]
            ret_val.append(dic)
#        for entry in ret_val:
#            print(entry)
#            print("\n")
        return ret_val #None ## or return [ (debt_name, month, paid_ammount)]
                    ## this should be a list of tuples which correspond to the value 'paid_ammount' spent on 
                    ## paying off the debt 'debt_name' on the month 'month'
                    ## Return 'None' if there is no solution possible for the current plan

def greedy_dc( lista_monthly_fees, lista_montantes_iniciais, monthly_available_list):#returns list of payments
   dividas_len = len(lista_montantes_iniciais)

   if(len(monthly_available_list) == 1):
       ret_val = []
       temp = monthly_available_list[0]
       len_lista = len(lista_montantes_iniciais)
       for i in range(0, len_lista):
           ret_val.append(lista_montantes_iniciais[i])
           temp = temp - lista_montantes_iniciais[i]
       if(monthly_available_list[0] < sum(lista_montantes_iniciais)):
           return -1
       return [ret_val]

   temp_cost = 1e34
   ret_val = []
   for i in range(0, dividas_len) :
       temp_montantes = lista_montantes_iniciais.copy()
       temp_available = monthly_available_list.copy()

       temp_val = temp_available[0]
       len_temp_montantes = len(temp_montantes)
       j = i
       k = 0
##       for j in range(i, len_temp_montantes):
       while(temp_val > 0 and k < len(temp_montantes)):
##            if(temp_val <= 0):
##                break
            temp_montantes[j] = (temp_montantes[j] - temp_val) if(temp_montantes[j] > temp_val) else 0
            temp_val = 0 if (temp_montantes[j] != 0) else (temp_val - lista_montantes_iniciais[j])
            j = (j+1)%len(temp_montantes)
            k = k+1
       temp_temp = []
       for b in range(0, len_temp_montantes):
           temp_temp.append(lista_montantes_iniciais[b] - temp_montantes[b])
       temp_temp = [temp_temp]

       if sum(temp_temp[0]) == 0:
           return temp_temp
       for j in range(0, len_temp_montantes) :
                      temp_montantes[j] = temp_montantes[j]*(1 + lista_monthly_fees[j])

       temp_available.__delitem__(0)
       temp = greedy_dc( lista_monthly_fees, temp_montantes, temp_available)

       if temp == -1:
           continue

       if temp_cost > sum( sum(b) for b in temp_temp + temp  ):
           ret_val = temp_temp + temp
           temp_cost = sum(sum(b) for b in ret_val)
   return -1 if ret_val == [] else ret_val

def greedy1( lista_monthly_fees, lista_montantes_iniciais, monthly_available_list):
    time=len(monthly_available_list)
    solution=[]
    lista_montantes=lista_montantes_iniciais.copy()
    for t in range(0,time):
        money=monthly_available_list[t]
        max_heap=[]
        size=len(lista_montantes) #implementado com comeco no zero porque nao sou mongoloide
        solution.append([0]*size)
        for i in range(0,size):
            heapq.heappush(max_heap, [-1*lista_montantes[i], -1*lista_monthly_fees[i], i])
        while money>0 and len(max_heap)>0:
            greed=heapq.heappop(max_heap)
            greed[0]=-1*greed[0]
            if money>greed[0]:
                lista_montantes[greed[2]]=0
                money=money-greed[0]
                solution[t][greed[2]]=greed[0]
            else:
                lista_montantes[greed[2]]=greed[0]-money
                solution[t][greed[2]]=money
                money=0
        for i in range(0,size):
            lista_montantes[i]=(1+lista_monthly_fees[i])*lista_montantes[i]
        if sum(lista_montantes)==0:
            break
    if sum(lista_montantes)!=0:
        raise Exception("Plano terminou mas ainda restam dívidas. Sua casa pertence ao banco agora HAHAHAHAHAHAHA!")
    return solution
def greedy2( lista_monthly_fees, lista_montantes_iniciais, monthly_available_list):
    time=len(monthly_available_list)
    solution=[]
    lista_montantes=lista_montantes_iniciais.copy()
    for t in range(0,time):
        money=monthly_available_list[t]
        max_heap=[]
        size=len(lista_montantes)
        solution.append([0]*size)
        for i in range(0,size):
            heapq.heappush(max_heap, [-1*lista_monthly_fees[i], -1*lista_montantes[i], i])
        while money>0 and len(max_heap)>0:
            greed=heapq.heappop(max_heap)[2]
            if money>lista_montantes[greed]:
                money=money-lista_montantes[greed]
                solution[t][greed]=lista_montantes[greed]
                lista_montantes[greed]=0
            else:
                lista_montantes[greed]=lista_montantes[greed]-money
                solution[t][greed]=money
                money=0
        for i in range(0,size):
            lista_montantes[i]=(1+lista_monthly_fees[i])*lista_montantes[i]
        if sum(lista_montantes)==0:
            break
    if sum(lista_montantes)!=0:
        raise Exception("Plano terminou mas ainda restam dívidas. Sua casa pertence ao banco agora HAHAHAHAHAHAHA!")
    return solution
def greedy3( lista_monthly_fees, lista_montantes_iniciais, monthly_available_list):
    time=len(monthly_available_list)
    solution=[]
    lista_montantes=lista_montantes_iniciais.copy()
    for t in range(0,time):
        money=monthly_available_list[t]
        if(money>=sum(lista_montantes)):
            solution.append([M for M in lista_montantes])
            return solution
        size=len(lista_monthly_fees)
        finished=False
        lista_monthly_fees_pos=lista_monthly_fees.copy()
        temp_solution=[0]*size
        while not finished:
            fee_sum=0
            for i in range(0,size):
                if lista_monthly_fees_pos[i]!=-1:
                    fee_sum+=(lista_monthly_fees_pos[i])
            for i in range(0,size):
                finished=True
                if lista_monthly_fees_pos[i]!=-1:
                    temp_solution[i]=money*(lista_monthly_fees_pos[i])/fee_sum
                if lista_montantes[i]<temp_solution[i]:
                    lista_monthly_fees_pos[i]=-1
                    temp_solution[i]=lista_montantes[i]
                    money=money-lista_montantes[i]
                    finished=False
                    break
        solution.append(temp_solution)
        lista_montantes=[lista_montantes[i]-temp_solution[i] for i in range(0,size)]
        for i in range(0,size):
            lista_montantes[i]=(1+lista_monthly_fees[i])*lista_montantes[i]
        if sum(lista_montantes)==0:
            break
    if sum(lista_montantes)!=0:
        raise Exception("Plano terminou mas ainda restam dívidas. Sua casa pertence ao banco agora HAHAHAHAHAHAHA!")
    return solution
