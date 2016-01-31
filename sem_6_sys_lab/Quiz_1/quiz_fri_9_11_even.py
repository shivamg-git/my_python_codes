from Tkinter import *
routing_table = [
["172.16.68.1",	1032,	"172.17.68.1"	,	100],
["172.16.68.2",	2043,	"172.17.68.2"	,	200],
["172.16.68.2",	3000,	"172.17.68.4"	,	300],
["172.16.68.3",	5000,	"172.17.68.2"	,	400],
["172.16.68.3",	7000,	"172.17.68.3"	,	50]]

file = open("x.txt",'w')
for r in routing_table:
	if r[0] == "172.16.68.2" and r[1] >= 3000 :
		file.write("DEST :" + r[2] + "\t Delay :" + str(r[3]))



root = Tk()
# Label(root,text="Source ip :").grid(row=0)
# Label(root,text = "port :").grid(row=1)

# interface_name = StringVar()
# entry_interface = Entry(root, textvariable = interface_name)
# entry_interface.grid(row=0, column=1)

# number_of_out_intrf = StringVar()
# entry_no_interface = Entry(root, textvariable = number_of_out_intrf)
# entry_no_interface.grid(row=1, column=1)
# b = Button(root,text="OK!", command=lambda :check())
# b.grid(row=0,column=3,rowspan=2,columnspan=2)

textField = Text(root)
textField.grid(row=3,columnspan=4)
file = open("x.txt",'r')
textField.insert(INSERT,file.read())
root.mainloop()