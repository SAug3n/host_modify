# -*- coding: UTF-8 –*-.
import sys
def show_host():
	host_path="C:\Windows\System32\drivers\etc\hosts"
	host_file=open(host_path,"r")
	host_list=[]
	while 1:
		line = host_file.readline()
   		if not line:
   			break
   		host_list.append(line)
   	host_file.close()
   	return host_list

def host_write(host_list,ip,host_name):
	host_path="C:\Windows\System32\drivers\etc\hosts"
	host_file=open(host_path,"w")
	write=0
	content=""
	for line in range(len(host_list)):
		if(host_list[line][0]!="#" and (host_name==host_list[line].split(' ')[1])):
			host_list[line]=ip+' '+host_name+'\n'
			write=1
	if(write==0):
		host_list.append(ip+' '+host_name+'\n')
	for line in host_list:
		content+=line
	host_file.write(content)
	host_file.close()

def host_remove(host_list,host_name):
	write=0
	content=""
	for line in range(len(host_list)):
		if(host_list[line][0]!="#" and (host_name==host_list[line].split(' ')[1])):
			host_list[line]=''
			write=1
	if(write==1):
		for line in host_list:
			content+=line
		host_path="C:\Windows\System32\drivers\etc\hosts"
		host_file=open(host_path,"w")
		host_file.write(content)
		host_file.close()
	else:
		print 'no host to remove.'


if __name__=='__main__':
	operator=0

	if(len(sys.argv)==2):
		if(sys.argv[1]=='--show-host'):
			operator=1
			host_list=show_host()
			for i in host_list:
				print i,
		#if(sys.argv[1]=='--set-backup'):
		#if(sys.argv[1]=='--get-backup')

	if(len(sys.argv)==3):
		if(sys.argv[1]=='--remove'):
			operator=1
			host_list=show_host()
			host_remove(host_list,sys.argv[2])
			
	if(len(sys.argv)==4):
		if(sys.argv[1]=='--add'):
			operator=1
			host_list=show_host()
			host_write(host_list,sys.argv[2],sys.argv[3])

	if(operator==0):
		print '--show-host'
		#print '--set-backup'
		#print '--get-backup'
		print '--add ip hostname'
		print '--remove hostname'		