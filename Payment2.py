import information

answer=''
cash=0
answer2=''
cash2=0
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
        global cash
        global cash2
        print('돈을 넣어 주세요. 얼마를 넣으시겠습니까?: ')
        
        cash=int(input('가격: '))
        cash2+=cash
        
    def Question(self):
        global answer
        print('''결제하시겠습니까?     
                1: 예           2: 아니요''')
        answer=input('답변: ')

    def Rest(self):
        global cash
        global answer2
        global cash2
        while True:
            if cash2<information.final:
                print('음로를 구매할 수 없습니다.'+str(int(information.final)-int(cash2))+' 원이 더 필요합니다')
                Payment().Inputcash()
            if cash2>=information.final:
                print('음료를 구매할 수 있습니다. 거스름돈은 '+str(int(cash2)-int(information.final))+ '원 입니다.')
                print('영수증이 출력됩니다.')
                Payment().Recipt()
                break


            

    def Pay(self):
        print('현재 장바구니에 있는 음료의 총 합은'+ str(information.final) +' 원 입니다.')
    
    def Recipt(self):
        try:
            print('''---------------영수증----------------
            
            
                                                            ''')
            for i in range(0,10):
                print(information.recipt[i])
            
        except IndexError:
            pass
        print('''
            
-------------------------------------
맛있게 드세용^*^
                            총합:%s     

                            '''%information.final)
    
        
    
    


    
    