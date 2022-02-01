
class People:
    def __init__(self, name=None, root=None) -> None:
        self.name = name
        self.root = root
        self.asset = 0
        
    def profit(self, amount:int):
        for_root = amount // 10
        for_mine = amount - for_root
        
        if self.root is not None and for_root:
            self.root.profit(for_root)
        
        self.asset += for_mine


def solution(enroll:list, referral:list, seller:list, amount:list):
    employees = dict()
    
    for enr, ref in zip(enroll, referral):
        if ref != "-":
            employees[enr] = People(enr, employees[ref])
        else:
            employees[enr] = People(enr)
    
    for s, a in zip(seller, amount):
        employees[s].profit(a * 100)
    
    
    return [employees[name].asset for name in enroll]