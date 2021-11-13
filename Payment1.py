import information

class Payment: 
    def __init__(self):
        self.coffee=0
        self.cash=0
        self.card=0
        self.barcord=1
        self.change=0
    def Checkbarcode(self):
        print('바코드를 대주세요')
    def Isbarcode(self):
        if self.barcord==1:
            pass
        else:
            print('올바르지 않은 바코드입니다. 다시 한번 확인해주세요.')
    def Inputcash(self):
        print('얼마를 넣으시겠습니까?: ')
        self.cash=int(input('가격: '))
        
    
        
    
        
    
    

if __name__=="__main__":
    sumin=Payment()
    sumin=information.Information()
    sumin.Packing()
    
    
    