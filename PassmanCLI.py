from logics import *

def rewrite_to_file(lst):
	try:
		decrypt(fpassword)
		with open('credentials', 'w') as f:
			for i in lst:	
				f.write('site: '+i[0]+' login: '+i[1]+' password: '+i[2]+' date: '+i[3] + "\n")
		encrypt(fpassword)
	except:
		pass



def edit_info_file(index1):
	lst=read_info_file(fpassword)
	lst=list(map(list, lst))
	for i in range(len(lst)):
		for j in range(len(lst[i])):
			if lst[i][j]==index1:
				index1=i
			
	if type(index1) is str:
		print("Incorrect site name")
	else:
		log=input("New login:")
		pas=input("New password:")
		lst[index1][1]=log
		lst[index1][2]=pas
		rewrite_to_file(lst)

def share_passw(index1):
	lst=read_info_file(fpassword)
	lst=list(map(list, lst))
	for i in range(len(lst)):
		for j in range(len(lst[i])):
			if lst[i][j]==index1:
				index1=i		
	if type(index1) is str:
		print("Incorrect site name")
	else:
		qr_share(lst[index1][0],lst[index1][1],lst[index1][2])
	
if __name__ == "__main__":
	from stdiomask import getpass
	fpassword = getpass('Введите пароль: ')
	while True:
		mode=int(input("select mode: 1-write, 2-read, 3-edit, 4-share \n"))
		if mode==1:
			website=input("Website: ")
			login=input("Login: ")
			password=input("Password: ")
			write_to_file(website,login,password,fpassword)
		if mode==2:
			lst=read_info_file(fpassword)
			print("==================================")
			for i in lst:
				for j in i:
					print(j)
				print("==================================")
		if mode==3:
			lst=read_info_file(fpassword)
			print("==================================")
			for i in lst:
				for j in i:
					print(j)
				print("==================================")
			index1=(input("Enter site name:"))
			edit_info_file(index1)
		if mode==4:
			lst=read_info_file(fpassword)
			print("==================================")
			for i in lst:
				for j in i:
					print(j)
				print("==================================")
			index1=(input("Enter site name:"))
			share_passw(index1)
