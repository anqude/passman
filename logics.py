def qr_share(site,login, password):
	import qrcode
	qr = qrcode.QRCode()
	qr.add_data('site = '+site+' login = '+login+' password = '+password)
	return(qr.print_ascii())

def qr_image(site,login, password,fg_color,bg_color):
	import qrcode
	qr = qrcode.QRCode()
	qr.add_data('site = '+site+' login = '+login+' password = '+password)
	try:
		qr.make(fit=True)
	except:
		return False
	img = qr.make_image(fill_color=fg_color, back_color=bg_color)
	img.save("qr.png")
	return True
def encrypt(fpassword):
	import pyAesCrypt
	pyAesCrypt.encryptFile('credentials', 'credentials.aes', fpassword)
	import os
	os.remove("./credentials")
def decrypt(fpassword):
	import pyAesCrypt
	pyAesCrypt.decryptFile('credentials.aes', 'credentials', fpassword)
	import os
	os.remove("./credentials.aes")


def read_info_file(fpassword):
    info_list = []
    try:
        decrypt(fpassword)
        with open('credentials', 'r') as f:
            for string in f.readlines():
                site = string.split('site: ')[1].split(' ')[0]
                login = string.split('login: ')[1].split(' ')[0]
                password = string.split('password: ')[1].split(' ')[0]
                cur_time = string.split('date: ')[1].strip()
                info_list.append((site, login, password, cur_time))
        encrypt(fpassword)
    except:
        pass
    return info_list


def write_to_file(site,login, password,fpassword):
	try:
		decrypt(fpassword)
	except:
		pass
	from time import gmtime, strftime
	cur_time=strftime("%Y-%m-%d %H:%M:%S", gmtime()).replace(" ","_")
	with open('credentials', 'a') as f:
		f.write('site: '+site+' login: '+login +' password: '+ password +' date: '+(cur_time) + "\n")
	try:
		encrypt(fpassword)
	except:
		pass

def rewrite_to_file(lst,fpassword):
	try:
		decrypt(fpassword)
		with open('credentials', 'w') as f:
			for i in lst:	
				f.write('site: '+i[0]+' login: '+i[1]+' password: '+i[2]+' date: '+i[3] + "\n")
		encrypt(fpassword)
	except:
		pass

def edit_info_file(index,new_site,new_login,new_pas,fpassword):
	lst=read_info_file(fpassword)
	lst=list(map(list, lst))
	lst[index][0]=new_site
	lst[index][1]=new_login
	lst[index][2]=new_pas
	rewrite_to_file(lst,fpassword)
