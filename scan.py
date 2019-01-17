#coding: utf-8
import subprocess

mac_list= {'田中':'18:31:bf:d7:ef:19', '西山':'88:bd:45:18:19:99', '鈴木':'a0:57:e3:96:83:a6', '村田':'88:e8:7f:ef:68:74', '山本':'24:5b:a7:77:fa:d6'}
reserchers = {'松田':0, '田中':0, '鈴木':0, '西山':0, '村田':0, '山本':0, '林':0}
for mac_resercher in mac_list:
	cmd = 'sudo l2ping -c 1 '+mac_list[mac_resercher]
	try:
		proc = subprocess.check_output(cmd.split()).decode()
		if '1 received' in proc:
			reserchers[mac_resercher] = 1
	except:
		pass

#print(reserchers)

with open('./reserchers','w') as f:
	for resercher in reserchers:
		if reserchers[resercher] == 1:
			f.write(resercher+'\n')
		else:
			#f.write(resercher+'\n')
			pass