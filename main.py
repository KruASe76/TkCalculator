from tkinter import *
import math

window=Tk()
window.geometry('252x420')
window.title('Кулькулятар')
window.resizable(False, False)

def ins(symb):
    if symb=='':
        if len(ent.get())!=0:
            if ent.get()[-1]=='R':
                ent.delete(0, END)
            else:
                ent.delete(len(ent.get())-1)
    elif symb==' ':
        ent.delete(0, END)
    else:
        ent.insert(len(ent.get()), symb)

def calc():
    do=ent.get()
    try:
        if 'π' in do:
            if do.index('π')!=0:
                if do[do.index('π')-1].isdigit():
                    a=int('')
            if do.index('π')!=len(do):
                if do[do.index('π')+1].isdigit():
                    a=int('')
            do=do.replace('π', '3.1415926535')
        if ',' in do:
            do=do.replace(',', '.')
        if do[0]=='^' or do[0]=='!' or do[0]=='+' or do[0]=='*' or do[0]=='/' or do[0]=='.':
            a=int('')

        for i in range(do.count('!')):
            place=do.index('!')
            if place!=len(do):
                if do[place+1]!='+' and do[place+1]!='-' and do[place+1]!='*' and do[place+1]!='/' and do[place+1]!='^':
                    a=int('')
            place1=place
            num=''
            while do[place1-1].isdigit() or do[place1-1]=='.':
                num=do[place1-1]+num
                place1-=1
                if place1-1<0:
                    break
            ans=math.factorial(float(num))
            do=do[:place-len(num)]+str(ans)+do[place+1:]
        
        for i in range(do.count('^')):
            place=do.index('^')
            place1, place2=place, place
            num1, num2='', ''
            while do[place1-1].isdigit() or do[place1-1]=='.':
                num1=do[place1-1]+num1
                place1-=1
                if place1-1<0:
                    break
            while do[place2+1].isdigit() or do[place2+1]=='.' or do[place2+1]=='-':
                num2=num2+do[place2+1]
                place2+=1
                if place2+1>=len(do) or do[place2+1]=='-':
                    break
            ans=math.pow(float(num1), float(num2))
            do=do[:place-len(num1)]+str(ans)+do[place+len(num2)+1:]
        
        for i in range(do.count('√')):
            place=do.index('√')
            if place!=0:
                if do[place-1]!='+' and do[place-1]!='-' and do[place-1]!='*' and do[place-1]!='/':
                    a=int('')
            place1=place
            num=''
            while do[place1+1].isdigit() or do[place1+1]=='.':
                num=num+do[place1+1]
                place1+=1
                if place1+1>=len(do):
                    break
            ans=math.sqrt(float(num))
            do=do[:place]+str(ans)+do[place+len(num)+1:]
        
        for i in range(do.count('*')+do.count('/')):
            if do.count('*')==0:
                place=do.index('/')
                place1, place2=place, place
                num1, num2='', ''
                while do[place1-1].isdigit() or do[place1-1]=='.' or do[place1-1]=='-':
                    num1=do[place1-1]+num1
                    place1-=1
                    if place1-1<0 or do[place1]=='-':
                        break
                while do[place2+1].isdigit() or do[place2+1]=='.' or do[place2+1]=='-':
                    num2=num2+do[place2+1]
                    place2+=1
                    if place2+1>=len(do) or do[place2+1]=='-':
                        break
                ans=float(num1)/float(num2)
                do=do[:place-len(num1)]+str(ans)+do[place+len(num2)+1:]
            elif do.count('/')==0:
                place=do.index('*')
                place1, place2=place, place
                num1, num2='', ''
                while do[place1-1].isdigit() or do[place1-1]=='.' or do[place1-1]=='-':
                    num1=do[place1-1]+num1
                    place1-=1
                    if place1-1<0 or do[place1]=='-':
                        break
                while do[place2+1].isdigit() or do[place2+1]=='.' or do[place2+1]=='-':
                    num2=num2+do[place2+1]
                    place2+=1
                    if place2+1>=len(do) or do[place2+1]=='-':
                        break
                ans=float(num1)*float(num2)
                do=do[:place-len(num1)]+str(ans)+do[place+len(num2)+1:]
            else:
                p1=do.index('*')
                p2=do.index('/')
                place=max([p1, p2])
                place1, place2=place, place
                num1, num2='', ''
                while do[place1-1].isdigit() or do[place1-1]=='.' or do[place1-1]=='-':
                    num1=do[place1-1]+num1
                    place1-=1
                    if place1-1<0 or do[place1]=='-':
                        break
                while do[place2+1].isdigit() or do[place2+1]=='.' or do[place2+1]=='-':
                    num2=num2+do[place2+1]
                    place2+=1
                    if place2+1>=len(do) or do[place2+1]=='-':
                        break
                if place==p1:
                    ans=float(num1)*float(num2)
                elif place==p2:
                    ans=float(num1)/float(num2)
                do=do[:place-len(num1)]+str(ans)+do[place+len(num2)+1:]
        
        if 'e' not in do:
            do=do.replace('-', '+-')
            if do[0]=='+':
                do=do[1:]
            do_list=do.split('+')
            for i in range(len(do_list)):
                do_list[i]=float(do_list[i])
            do=math.fsum(do_list)
            if do%1==0:
                do=int(do)
        do=str(do).replace('.', ',')


        ins(' ')
        ins(do)
    except:
        if do!='':
            ins(' ')
            ins('ERROR')


ent=Entry(window, width=42)

clear_btn=Button(window, command=lambda:ins(' '), text=' Clear \nall', font='arial 13', width=5, height=2, bg='#dd0000')
pi_btn=Button(window, command=lambda:ins('π'), text='π', font='arial 13', width=3, height=2)
fact_btn=Button(window, command=lambda:ins('!'), text='n!', font='arial 13', width=3, height=2)
pow_btn=Button(window, command=lambda:ins('^'), text='^', font='arial 13', width=3, height=2)
wop_btn=Button(window, command=lambda:ins('√'), text='√', font='arial 13', width=3, height=2)
del_btn=Button(window, command=lambda:ins(''), text='Del', font='arial 13', width=5, height=2, bg='#dd0000')
btn_1=Button(window, command=lambda:ins('1'), text='1', font='arial 13', width=6, height=3, bg='#cc00cc')
btn_2=Button(window, command=lambda:ins('2'), text='2', font='arial 13', width=6, height=3, bg='#cc00cc')
btn_3=Button(window, command=lambda:ins('3'), text='3', font='arial 13', width=6, height=3, bg='#cc00cc')
btn_4=Button(window, command=lambda:ins('4'), text='4', font='arial 13', width=6, height=3, bg='#cc00cc')
btn_5=Button(window, command=lambda:ins('5'), text='5', font='arial 13', width=6, height=3, bg='#cc00cc')
btn_6=Button(window, command=lambda:ins('6'), text='6', font='arial 13', width=6, height=3, bg='#cc00cc')
btn_7=Button(window, command=lambda:ins('7'), text='7', font='arial 13', width=6, height=3, bg='#cc00cc')
btn_8=Button(window, command=lambda:ins('8'), text='8', font='arial 13', width=6, height=3, bg='#cc00cc')
btn_9=Button(window, command=lambda:ins('9'), text='9', font='arial 13', width=6, height=3, bg='#cc00cc')
float_btn=Button(window, command=lambda:ins(','), text=',', font='arial 13', width=6, height=3)
btn_0=Button(window, command=lambda:ins('0'), text='0', font='arial 13', width=6, height=3, bg='#cc00cc')
calc_bth=Button(window, command=calc, text='=', font='arial 13', width=6, height=3, bg='#00bb00')
plus_btn=Button(window, command=lambda:ins('+'), text='+', font='arial 13', width=6, height=3, bg='#eeee00')
minus_btn=Button(window, command=lambda:ins('-'), text='-', font='arial 13', width=6, height=3, bg='#eeee00')
mult_btn=Button(window, command=lambda:ins('*'), text='×', font='arial 13', width=6, height=3, bg='#eeee00')
div_btn=Button(window, command=lambda:ins('/'), text='/', font='arial 13', width=6, height=3, bg='#eeee00')


ent.place(x=0, y=30)

btn_1.place(x=0, y=140)
btn_2.place(x=63, y=140)
btn_3.place(x=126, y=140)
btn_4.place(x=0, y=210)
btn_5.place(x=63, y=210)
btn_6.place(x=126, y=210)
btn_7.place(x=0, y=280)
btn_8.place(x=63, y=280)
btn_9.place(x=126, y=280)
btn_0.place(x=63, y=350)

clear_btn.place(x=0, y=89)
del_btn.place(x=198, y=89)

pi_btn.place(x=54, y=89)
fact_btn.place(x=90, y=89)
pow_btn.place(x=126, y=89)
wop_btn.place(x=162, y=89)

plus_btn.place(x=189, y=140)
minus_btn.place(x=189, y=210)
mult_btn.place(x=189, y=280)
div_btn.place(x=189, y=350)
float_btn.place(x=0, y=350)
calc_bth.place(x=126, y=350)

window.mainloop()
