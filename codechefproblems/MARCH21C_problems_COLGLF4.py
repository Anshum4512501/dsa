testcases = int(input())

def find_max(N,E,H,price_list):
    if N < E+H:
        return -1
    min_index = price_list.index(min(price_list))

    find_max_util(N,E,H,price_list,min_index)
    # if min_index == 0:
    #     egg_price = price_list[min_index]
    #     price_omlate = make_omlate(E,egg_price)    
    
    # if min_index == 1:
    #     choclate_ = price_list[min_index]
    #     price_milkshake = make_milkshake(E,egg_price)    
    
    # if min_index == 0:
    #     egg_price = price_list[min_index]
    #     price_omlate = make_omlate(E,egg_price)    
def find_max_util(N,E,H,price_list,min_index):
    if can_place_order(N,E,H):
        if min_index == 0:
            find_max_util(N-1,E-2,H)
        if min_index == 1:
            find_max_util(N-1,E-1,H-1)
        if min_index == 2:
            find_max_util(N-1,E,H-3)
            

def can_place_order(N,E,H):
    if (E == 0 and H == 0) or (E == 0 and H == 1) or (E == 1 and H == 0) or (E == 0 and H == 2) or N == 0:
        return False
        
    return True    

def place_order(N,E,H,price_list,min_index):
    total_price = price_list[min_index]


def make_omlate(E,egg_price):
    E = E//2
    return egg_price*E

def make_milkshake(E,H,price):
    E = E - 1 
    H = H - 1







while testcases:
    testcases = testcases - 1 
    N,E,H,*price_list  = [int(x) for x in input().split(" ")]
    find_max(N,E,H,price_list)