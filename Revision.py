## 1 : multiplication table
'''
start = int(input("Enter start number :"))
end = int(input("Enter end number :"))
step_start = int(input("Enter step start number :"))
step_end = int(input("Enter step end number :"))

for mn in range(start,end+1):
    for x in range(step_start,step_end+1):
        print(f"{mn} X {x} = {mn*x}")
    print("---------------------")
'''

## remove duplicated char
'''
lst = list()
inn = input("Enter the word :")
for x in inn:
    if not x in lst:
        print(x ,end = '')
        lst.append(x)
'''    


## Game

class Game:
    def __init__(self):
        while True:
            
            print('''

Welcome in the Game
Choose one of our Game
        Press 1 ==>  Multiplication Table Game
        Press 2 ==>  Remove Duplicated Char Game
        Press X ==>  EXIT
            
    ''')
            inn = input("Enter Number of Gamed :")
            if inn == 'X' or inn == 'x':
                print("Good bye ^_^")
                break
            if int(inn) == 1:
                start = int(input("Enter start number :"))
                end = int(input("Enter end number :"))
                step_start = int(input("Enter step start number :"))
                step_end = int(input("Enter step end number :"))

                self.Multiplication(start,end,step_start,step_end)
            elif int(inn) == 2:
                self.Remove_Dupli()

    def Multiplication(self,start,end,step_start,step_end):
        for mn in range(start,end+1):
            for x in range(step_start,step_end+1):
                print(f"{mn} X {x} = {mn*x}")
            print("---------------------")
        
    def Remove_Dupli(self):
        
        numbers_lst = list()
        even_lst    = list()
        odd_lst     = list()

        print("Press 'x' to EXIT and show the list")
        print("Enter your numbers:")
        while True:
            
                        
            inn = input("")
            if inn == 'x': break
            numbers_lst.append(int(inn))

                        
            for x in numbers_lst:
                
                if x % 2 == 0:
                    even_lst.append(x)
                else:
                        odd_lst.append(x)

            print("The Even List is :",even_lst)
            print("The Odd List is  :",odd_lst)



g = Game()
