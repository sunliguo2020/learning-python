#import GetFileMd5
from GetFileMd5 import GetFileMd5
import os
if __name__ == '__main__':

	root_dir = r'F:\1T\邮件'

	for (root,dirs,files ) in os.walk(root_dir):

		for filename in files:
			if filename.endswith('.eml'):

				mail_file_path = os.path.join(root,filename)
				md5sum=GetFileMd5(mail_file_path)
				print(mail_file_path,md5sum)
				new_file_name=md5sum+'.eml'
				new_file_path = os.path.join(root_dir,new_file_name)
				print(new_file_path)
				os.renames(mail_file_path,new_file_path)