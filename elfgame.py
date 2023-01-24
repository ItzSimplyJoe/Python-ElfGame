import random
import time
import PySimpleGUI as sg

class ElfGame:
    def weatherfunction(self):
        weather = random.randint(1,6)
        if weather <= 4:
            weather = "sunny"
        else:
            weather = "blizzard"
        sg.theme("DarkGreen1")
        sg.popup(f"Today's weather is {weather}")
        return weather

    def first17days(self,money,elftotal,daynumber,button,ffaf):
        QT_ENTER_KEY1 = 'special 16777220'
        QT_ENTER_KEY2 = 'special 16777221'
        if daynumber == 0:
            money = 0
        else:
            None
        sg.theme('DarkGreen1')
        layout = [[sg.Text('Elf Game', size=(30,1), justification='center', font='Helvetica 20')],
                [sg.Text(f'Day: {daynumber}, Elf Total: {elftotal}, Money: £{money}', size=(30,1), justification='center', font='Helvetica 20')],
                [sg.Text('Nearby Woods', size=(15,1), justification='center'), sg.InputText('', key = '-NW-', size=(15,1) , font='Helvetica 20')],
                [sg.Text('Faraway Forest', size=(15,1), justification='center'), sg.InputText('', key = '-FF-', size=(15,1), font='Helvetica 20')],
                [sg.Text('Far far away forest', size=(15,1), justification='center'), sg.InputText('', key = '-FFW-', visible=True, readonly=ffaf, size=(15,1), font='Helvetica 20')],
                [sg.Button('Submit'), sg.Button('Buy Elves', disabled=button), sg.Button('Exit')]]

        window = sg.Window('ElfGame', layout,resizable=False, titlebar_icon='new.ico', return_keyboard_events=True, finalize=True, icon='new.ico')

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == 'Exit':
                quit()
            elif event == 'Buy Elves':
                money, elftotal = self.buyelf(money, elftotal)
                window.close()
                self.first17days(money,elftotal,daynumber,button,ffaf)
            elif event == 'Submit' or event in ('\r', QT_ENTER_KEY1, QT_ENTER_KEY2):
                nw = values['-NW-']
                ff = values['-FF-']
                if nw == '':
                    nw = '0'
                if ff == '':
                    ff = '0'
                if ffaf == True:
                    ffw = '0'
                else:
                    ffw = values['-FFW-']
                    if ffw == '':
                        ffw = '0'
                if ff.isdigit() == True and nw.isdigit() == True and ffw.isdigit() == True:
                    if (int(nw) + int(ff) + int(ffw)) != int(elftotal):
                        sg.popup('You did not assign all your elves to a task')
                        window.close()
                        self.first17days(money,elftotal,daynumber,button,ffaf)
                    else:
                        window.close()
                        moneynew,elftotal = self.moneytotal(nw,ff,ffw,elftotal)
                        money = money + moneynew
                        self.daycalculator(daynumber,elftotal,money)
                else:
                    sg.popup('Please input numbers stop trying to break my game')
                    window.close()
                    self.first17days(money,elftotal,daynumber,button,ffaf)
                    break
            else:
                continue


        window.close()

    def moneytotal(self,nw,ff,ffw,elftotal):
        weather = self.weatherfunction()
        if weather == "sunny":
            if ffw == 0:
                money = (int(nw)*10) + (int(ff)*20)
            else:
                money = (int(nw)*10) + (int(ff)*20) + (int(ffw)*50)
        else:
            money = (int(nw)*10)
            if ffw == 0:
                elftotal = elftotal
            else:
                elftotal = int(elftotal) - int(ffw)
        return money, elftotal
    
    def daycalculator(self,daynumber,elftotal,money):
        daynumber += 1
        if daynumber == 25:
            sg.popup(f'You have finished the game \n You have finished the game, you have won £{money} and you have {elftotal} elves \n Thank you for playing', title='Game Over', icon='new.ico')
            quit()
        elif daynumber == 14:
            self.taxMan(money)
            self.first17days(money,elftotal,daynumber,True,True)
        elif daynumber == 12:
            moneywon = self.lottery()
            money = money + moneywon
            self.first17days(money,elftotal,daynumber,True,True)
        elif daynumber == 8:
            self.Strike(daynumber,elftotal,money)
            self.first17days(money,elftotal,daynumber,True,True)
        elif daynumber == 20:
            sg.popup("You can now purchase new elves for £75 per elf!", title='New Elves', icon='new.ico')
            sg.popup(f"Today is day {daynumber}, You have {elftotal} elves left, and £{money}", title=f'Day {daynumber}', icon='new.ico')
            self.first17days(money,elftotal,daynumber,False,False)
        elif daynumber > 20:
            sg.popup(f"Today is day {daynumber}, You have {elftotal} elves left, and £{money}", title=f'Day {daynumber}', icon='new.ico')
            self.first17days(money,elftotal,daynumber,False,False)
        elif daynumber == 18:
            sg.popup("A New path has been built to allow you to access the \n Far Far Away Forest. \n Each tree here is worth £50 \nhowever if there is a blizzard you're elves will DIE!!!!", title='New Forest', icon='new.ico')
            sg.popup(f"Today is day {daynumber}, You have {elftotal} elves left, and £{money}", title=f'Day {daynumber}', icon='new.ico')
            self.first17days(money,elftotal,daynumber,True,False)
        elif daynumber > 18:
            sg.popup(f"Today is day {daynumber}, You have {elftotal} elves left, and £{money}", title=f'Day {daynumber}', icon='new.ico')
            self.first17days(money,elftotal,daynumber,True,False)
        else:
            sg.popup(f"Today is day {daynumber}, You have {elftotal} elves left, and £{money}", title=f'Day {daynumber}', icon='new.ico')
            self.first17days(money,elftotal,daynumber,True,True)

    def buyelf(self, money, elftotal):
        sg.theme('DarkGreen1')
        QT_ENTER_KEY1 = 'special 16777220'
        QT_ENTER_KEY2 = 'special 16777221'
        layout = [[sg.Text('Elf Game', size=(20,1), justification='center', font='Helvetica 20')],
                [sg.Text(f"An Elf costs £75 each, currently you have £{money} and {elftotal} elves", justification='center')],
                [sg.Text('Amount of elves'), sg.Slider(range=(0, (money//75)), default_value=0, size=(20, 10), orientation="h", key="-EN-")],
                [sg.Button('Submit'), sg.Button('Exit')]]

        window = sg.Window('ElfGame', layout, icon='new.ico',resizable=False, titlebar_icon='new.ico', finalize=True)
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                window.close()
                return(money, elftotal)
            elif event == 'Submit' or event in ('\r', QT_ENTER_KEY1, QT_ENTER_KEY2):
                elfnum = values['-EN-']
                elfnum = int(elfnum)
                money = int(money)
                if (elfnum * 75) > money:
                    sg.popup('You do not have enough money')
                    window.close()
                    self.buyelf(money, elftotal)
                else:
                    window.close()
                    money = money - (elfnum * 75)
                    elftotal += elfnum
                    return (money, elftotal)
                    
    def Strike(self,daynumber,elftotal,money):
        sg.theme('DarkGreen1')
        layout = [[sg.Text('Elf Game', size=(30,1), justification='center', font='Helvetica 20')],
                [sg.Text('Do you want to give your elves a day off?', size=(60,1), justification='center', font='Helvetica 10')],
                [sg.Text('If you do give them a day off they will be happy', size=(60,1), justification='center', font='Helvetica 10')],
                [sg.Text('but if you do not give them a day off they might strike for the next 2 days!?', size=(60,1), justification='center', font='Helvetica 10')],
                [sg.Button('Yes'), sg.Button('No')]]
        window = sg.Window("Elf Game", layout, icon='new.ico',resizable=False, titlebar_icon='new.ico')
        while True:
            event,values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Yes':
                window.close()
                dayOff = True
            elif event == 'No':
                window.close()
                dayOff = False
            else:
                continue
        if dayOff != True:
            choice = random.randint(1,2)
            if choice == 1:
                sg.popup("The Elves have chosen to strike", title='Strike', icon='new.ico')
                sg.popup("Its now two days later and your elves have returned to work", title='Strike', icon='new.ico')
                self.daycalculator((daynumber+1),elftotal,money)
            else:
                sg.popup("The Elves have chosen not to strike", title='Strike', icon='new.ico')
                self.first17days(money,elftotal,8,True,True)
        else:
            self.daycalculator(8,elftotal,money)
            
    def taxMan(self,money): 
        sg.theme('DarkGreen1')
        layout = [[sg.Text('Elf Game', size=(30,1), justification='center', font='Helvetica 20')],
                [sg.Text('Do you want to pay the tax man?', size=(60,1), justification='center', font='Helvetica 10')],
                [sg.Text('If you do he will take 10% of your money ', size=(60,1), justification='center', font='Helvetica 10')],
                [sg.Text('but if you do not he may come back and take 20% of your money', size=(60,1), justification='center', font='Helvetica 10')],
                [sg.Button('Yes'), sg.Button('No')]]
        window = sg.Window("Elf Game", layout, icon='new.ico',resizable=False, titlebar_icon='new.ico')
        while True:
            event,values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Yes':
                window.close()
                payTax = True
            elif event == 'No':
                window.close()
                payTax = False
            else:
                continue
        if payTax != True:
            choice = random.randint(1,2)
            if choice == 1:
                sg.popup("The tax man is back and you must now pay your taxes", title='Tax', icon='new.ico')
                moneydeduct = money/5
                sg.popup(f"You have been taxed 20% of your money \n which is £{moneydeduct}", title='Tax', icon='new.ico')
                money = money - (money/5)
            else:
                sg.popup("You avoided the tax man. Lucky You!", title='Tax', icon='new.ico')
        else:
            moneydeduct = money/10
            sg.popup(f"You have been taxed 10% of your money \n which is £{moneydeduct}", title='Tax', icon='new.ico')
            money = money - (money/10)
        return money 

    def lottery(self):
        QT_ENTER_KEY1 = 'special 16777220'
        QT_ENTER_KEY2 = 'special 16777221'
        sg.theme('DarkGreen1')
        layout = [[sg.Text('Elf Game', size=(20,1), justification='center', font='Helvetica 20')],
                [sg.Text('Enter a number between 1 and 10 for the lottery'), sg.InputText('', key = '-EN-')],
                [sg.Button('Submit')]]
            
        window = sg.Window('ElfGame', layout, icon='new.ico',resizable=False, titlebar_icon='new.ico', return_keyboard_events=True)
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Submit' or event in ('\r', QT_ENTER_KEY1, QT_ENTER_KEY2):
                lottNum = values['-EN-']
                if lottNum.isdigit() == False:
                    sg.popup("Please enter a number")
                    window.close()
                    self.lottery()
                else:
                    lottNum = int(lottNum)
                    successNum = random.randint(1,10)
                    if lottNum == successNum:
                        window.close()
                        moneywon = 500
                        sg.popup("You won the lottery, you have won $500", title='Lottery', icon='new.ico')
                        return moneywon
                    else:
                        window.close()
                        sg.popup(f"You did not win the lottery, the number was {successNum}", title='Lottery', icon='new.ico')
                        moneywon = 0
                        return moneywon
                
    def main(self):
        sg.theme('DarkGreen1')
        layout = [[sg.Text('Elf Game', size=(20,1), justification='center', font='Helvetica 20')],
                [sg.Text('                           '),sg.Button('Play'), sg.Button('Exit')]]

        window = sg.Window('ElfGame', layout, icon='new.ico',resizable=False, titlebar_icon='new.ico')

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == 'Exit':
                break
            if event == 'Play':
                window.close()
                self.daycalculator(0,12,0)


        window.close()

elfgame = ElfGame()
elfgame.main()

