########################################
#统计当前文件下的各种视频文件的时间信息#
########################################

import os
import subprocess

#获得视频的小时、分钟、秒数等时间信息
def get_vid_time(vidname):
	newcmd = 'ffprobe -i '+'"'+vidname+'"'+' -show_entries format=duration -v quiet -of csv="p=0"'
	returned_output = subprocess.check_output(newcmd)
	time_sec = (float)(returned_output.decode('utf-8'))
	time_hour = time_sec/3600
	time_min = time_sec/60
	return (time_hour,time_min,time_sec)

#rootpath =  '.'	
rootpath =  'F:\\电视剧'
abspath = os.path.abspath(rootpath)

def getfileinfo(fname):
	if os.path.isfile(fname):
		#print(fname)
		if fname.endswith('.mp4') or fname.endswith('.mkv'):
			print(fname)
			#print('小时数：'+str(get_vid_time(fname)[0]))
			print('分钟数：'+str(get_vid_time(fname)[1]))
			#print('秒数：'+str(get_vid_time(fname)[2]))
			print(30*'-')			
	elif os.path.isdir(fname):
		for subf in os.listdir(fname):
			subfname = os.path.join(fname,subf)
			getfileinfo(subfname)

	
for f in os.listdir(rootpath):
	fpath = os.path.join(rootpath,f)
	getfileinfo(fpath)
	
			