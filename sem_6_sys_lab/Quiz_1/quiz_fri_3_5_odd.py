import re
from Tkinter import *

switches = [["Int#1",5,"172.16.68.0","50ms"],["Int#2",2,"172.16.78.0","25ms"],["Int#3",10,"172.16.08.0","75ms"]]

def check():
	file = open("data.txt","w")
	interface_name1 = str(interface_name.get())
	current_switch =[]
	for switch in switches:
		if switch[0] == interface_name1:
			current_switch = switch
	number_of_out_intrf = int(entry_no_interface.get())

	total_delay = int(re.search(r'[0-9]*',current_switch[3]).group())

	if number_of_out_intrf <= current_switch[1] and total_delay*number_of_out_intrf <= 300:
		file.write("\nInterface name: " + current_switch[0])
		file.write("\nNumber of output interfaces: " + str(number_of_out_intrf))
		file.write("\nEstimated delay : " + str(total_delay*number_of_out_intrf) + " ms")
		file.write("\nAssigned Ip addresses: ")
		
		subnet_ip =  re.search(r'.*\.', current_switch[2], flags=0).group()
		for i in range(number_of_out_intrf):
			file.write(subnet_ip + str(i) + ",")
	else:
		file.write("error!")
	file.close()
	file = open("data.txt",'r')
	textField.delete(0.0,END)
	textField.insert(INSERT,file.read())


root = Tk()	
Label(root,text="`Interface Name :").grid(row=0)
Label(root,text = "no of interface :").grid(row=1)

interface_name = StringVar()
entry_interface = Entry(root, textvariable = interface_name)
entry_interface.grid(row=0, column=1)

number_of_out_intrf = StringVar()
entry_no_interface = Entry(root, textvariable = number_of_out_intrf)
entry_no_interface.grid(row=1, column=1)

b = Button(root,text="OK!", command=lambda :check())
b.grid(row=0,column=3,rowspan=2,columnspan=2)

textField = Text(root)
textField.grid(row=3,columnspan=4)
root.mainloop()




