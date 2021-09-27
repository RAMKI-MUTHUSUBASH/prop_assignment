from tkinter import *
class MyWindow:
 def __init__(self, win):
	 self.lbl21=Label(win, text='INPUT:',fg='navy',bg='light cyan')
	 self.lbl1=Label(win, text='Compressor Pressure Ratio:', fg='navy',bg='light cyan')
	 self.lbl2=Label(win, text='Turbine Inlet Temperature (in K):', fg='navy',bg='light cyan')
	 self.lbl3=Label(win, text='Isentropic Efficency Of Compressor::', fg='navy',bg='light cyan')
	 self.lbl4=Label(win, text='Isentropic Efficency Of Turbine:', fg='navy',bg='light cyan')
	 self.lbl5=Label(win, text='Mechanical Transmission Efficency:', fg='navy',bg='light cyan')
	 self.lbl6=Label(win, text='Combustion efficency:', fg='navy',bg='light cyan')
	 self.lbl7=Label(win, text='Heat-Exchanger Effectiveness:', fg='navy',bg='light cyan')
	 self.lbl8=Label(win, text='Pressure loss in Combustion chamber:', fg='navy',bg='light cyan')
	 self.lbl9=Label(win, text='Pressure loss in Heat-Exchanger air-side(in comp.deliv.press):', fg='navy',bg='light cyan')
	 self.lbl10=Label(win, text='Pressure loss in Heat-Exchanger gas-side(in comp.deliv.press):', fg='navy',bg='light cyan')
	 self.lbl11=Label(win, text='Ambient Pressure(in bar):', fg='navy',bg='light cyan')
	 self.lbl12=Label(win, text='Ambient temperature(in K):', fg='navy',bg='light cyan')
	 self.t1=Entry()
	 self.t2=Entry()
	 self.t3=Entry()
	 self.t4=Entry()
	 self.t5=Entry()
	 self.t6=Entry()
	 self.t7=Entry()
	 self.t8=Entry()
	 self.t9=Entry()
	 self.t10=Entry()
	 self.t11=Entry()
	 self.t12=Entry()
	 self.lbl21.place(x=100, y=0)
	 self.lbl1.place(x=100, y=50)
	 self.t1.place(x=450, y=50)
	 self.lbl2.place(x=100, y=100)
	 self.t2.place(x=450, y=100)
	 self.lbl3.place(x=100, y=150)
	 self.t3.place(x=450, y=150)
	 self.lbl4.place(x=100, y=200)
	 self.t4.place(x=450, y=200)
	 self.lbl5.place(x=100, y=250)
	 self.t5.place(x=450, y=250)
	 self.lbl6.place(x=100, y=300)
	 self.t6.place(x=450, y=300)
	 self.lbl7.place(x=100, y=350)
	 self.t7.place(x=450, y=350)
	 self.lbl8.place(x=100, y=400)
	 self.t8.place(x=450, y=400)
	 self.lbl9.place(x=100, y=450)
	 self.t9.place(x=450, y=450)
	 self.lbl10.place(x=100, y=500)
	 self.t10.place(x=450, y=500)
	 self.lbl11.place(x=100, y=550)
	 self.t11.place(x=450, y=550)
	 self.lbl12.place(x=100, y=600)
	 self.t12.place(x=450, y=600)
	 self.lbl22=Label(win, text='OUPUT:',fg='red',bg='light cyan')
	 self.lbl13=Label(win, text='Temp Eqn of Compressor Work(in K):',fg='red',bg='light cyan')
	 self.lbl14=Label(win, text='Turbine Work Req to drive Compressor/uint mass flow(in KJ/Kg)',fg='red',bg='light cyan')
	 self.lbl15=Label(win, text='Temp Eqn of Total Turbine Work:',fg='red',bg='light cyan')
	 self.lbl16=Label(win, text='Total Turbine Work/unit mass flow(in KJ/Kg):',fg='red',bg='light cyan')
	 self.lbl17=Label(win, text='Specfic WOrk Output(in KJ/Kg):',fg='red',bg='light cyan')
	 self.lbl18=Label(win, text='Fuel to Air Ratio:',fg='red',bg='light cyan')
	 self.lbl19=Label(win, text='Specific Fuel Consumption(in Kg/KWh):',fg='red',bg='light cyan')
	 self.lbl20=Label(win, text='Cycle Efficency:',fg='red',bg='light cyan')
	 self.t13=Entry()
	 self.t14=Entry()
	 self.t15=Entry()
	 self.t16=Entry()
	 self.t17=Entry()
	 self.t18=Entry()
	 self.t19=Entry()
	 self.t20=Entry()
	 self.lbl22.place(x=600, y=0)
	 self.lbl13.place(x=600, y=50)
	 self.t13.place(x=1000, y=50)
	 self.lbl14.place(x=600, y=100)
	 self.t14.place(x=1000, y=100)
	 self.lbl15.place(x=600, y=150)
	 self.t15.place(x=1000, y=150)
	 self.lbl16.place(x=600, y=200)
	 self.t16.place(x=1000, y=200)
	 self.lbl17.place(x=600, y=250)
	 self.t17.place(x=1000, y=250)
	 self.lbl18.place(x=600, y=300)
	 self.t18.place(x=1000, y=300)
	 self.lbl19.place(x=600, y=350)
	 self.t19.place(x=1000, y=350)
	 self.lbl20.place(x=600, y=400)
	 self.t20.place(x=1000, y=400)
	 self.b=Button(win, text='Calculate',fg='purple',bg='light cyan', command=self.Calculate)
	 self.b.place(x=600, y=650)
 def Calculate(self):
	 cpr=float(self.t1.get()) 		#4
	 t03=float(self.t2.get())  		#1100
	 nc=float(self.t3.get())		#0.85
	 nt=float(self.t4.get())		#0.87
	 nm=float(self.t5.get())		#0.99
	 nb=float(self.t6.get())		#0.98
	 hee=float(self.t7.get())   	#0.80
	 delpb=float(self.t8.get())		#0.02	
	 delpha=float(self.t9.get())	#0.03
	 delphg=float(self.t10.get())	#0.84
	 pa=float(self.t11.get())		#1
	 ta=float(self.t12.get())		#288
	 cpa=1.005
	 cpg=1.148
	 qnet=43100
	 tf=0.0094

	 self.t13.delete(0, 'end')
	 res13=(ta/nc)*((pow(cpr,((1.4-1)/1.4)))-1)
	 res13=round(res13,4)
	 self.t13.insert(END, str(res13))
	 self.t14.delete(0, 'end')
	 res14=(cpa*res13)/nm
	 res14=round(res14,4)
	 self.t14.insert(END, str(res14))
	 self.t15.delete(0, 'end')
	 p02=cpr/pa
	 p03=p02*(1-delpb-delpha)
	 p04=pa+delphg
	 res15=nt*t03*(1-(pow((p04/p03),((1.3333-1)/1.3333))))
	 res15=round(res15,4)
	 self.t15.insert(END, str(res15))
	 self.t16.delete(0, 'end')
	 res16=cpg*res15
	 res16=round(res16,4)
	 self.t16.insert(END, str(res16))
	 self.t17.delete(0, 'end')
	 res17=res16-res14
	 res17=round(res17,4)
	 self.t17.insert(END, str(res17))
	 self.t18.delete(0, 'end')
	 t02=res13+ta
	 t04=t03-res15
	 t05=(0.80*(t04-t02))+t02
	 res18=tf/nb
	 res18=round(res18,4)
	 self.t18.insert(END, str(res18))
	 self.t19.delete(0, 'end')
	 res19=(3600*res18)/res17
	 res19=round(res19,4)
	 self.t19.insert(END, str(res19))
	 self.t20.delete(0, 'end')
	 res20=3600/(res19*qnet)
	 res20=round(res20,4)
	 self.t20.insert(END, str(res20))

window=Tk()
mywin=MyWindow(window)
window.title('Propulsion')
window.geometry("1200x800+10+10")
window['background']='light cyan'
window.mainloop()