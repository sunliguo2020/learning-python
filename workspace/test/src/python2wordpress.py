#! /usr/bin/person  
import os,urllib2,re,time,MySQLdb,sys #���ر�������Ҫ���õ���ģ�� 
reTitle          = re.compile('<font[^>]*>(.*?)<\/font> <font[^>]*') # ����һ��ȡ���±�������� 
reNeiron         = re.compile('[1-9|A-Z|a-z].*')   #����һ��ȡ��ȡ�������ݵ�����(ע��������ȡ�����Ĳ��Ǻܾ�ϸ����Ҫ�������������ٽ�����ȡ������ֻ��ȡһ�����) 
retiqu          = re.compile('^(?!MARGINWIDTH|BR).*.[^>|}]$')  #���ﶨ��һ�����򣬽�����reNeiron��ȡ�������ַ����ٽ���ϸ����   
shijian=1190944000  #����������һ��ʱ����� 
Str1="\\n---------------- BLOG OF YAO" #���û�ã���ʼ��׼���ӵ�������ģ�����û�ӽ�ȥ�� 
bianhao=2859   #������wordpress �����±�ţ�ֱ�Ӳ鿴wp-posts���id �ֶε����һ�����֡�   
for i in range(1,1500): #ѭ��1500�飬Ҳ���ǲɼ�1500ƪ���¡�     
Str2="" #�ȸ�ֵ��Str2 ��ֵ     
ltime=time.localtime(shijian)        
timeStr=time.strftime("%Y%m%d",ltime) #�����佫�����ʱ�����Ϊʱ�䣬��ʽΪ19700101�����ĸ�ʽ     
url="http://www.jokeswarehouse.com/cgi-bin/viewjoke2.cgi?id=%s" %timeStr #����Ҫ�ɼ�����վ����ת�����ʱ��������url�����     
a=urllib2.urlopen(url).read() #�������ҳ��Դ�������������ֵ��a;      
Title=reTitle.findall(a)  #ʹ�� reTitle���������ȡ������     
print "=========================================================================================================="     
for titles in map(None,Title): #������ȡ�����ı���ǰ����һ�� []  ��������Ҫд��forѭ����ǰ���[]ȥ������ת�����ֱ�Ӳ���mysql��ĸ�ʽ��         
titles=MySQLdb.escape_string(titles)      
Neiron=re.findall(reNeiron,a) #����reNeiron��ȡ����ŵ�����ģ�ͳ�������Щ�����Զ��ŷָ������顣     
for i in map(None,Neiron): # ������ѭ������Neiron����������ÿ��ֵ��         
x=re.findall(retiqu,i)#���� retiqu������������ϸ�������ݡ�         
for str in x:              
str=MySQLdb.escape_string(str)              
Str2 += str+"\\n" #�������ѭ�������ǰ����ݼӵ�һ�𣬲���ֵ��Str2��������������Str2��������������е��������ݡ�     
shijian += 86400 #ÿѭ��һ�Σ��Ͱ�shijian�����������һ�졣     
bianhao += 1   #ÿѭ��һ�Σ��Ͱ�bianhao�����������һ     
try:  #��������mysqldb�������ݿ⣬�����������Ƿ�ɹ���       
conn=MySQLdb.connect("XXXX.XXXX.XXXX.XXXX","user","passwd","dbname",charset="utf8", init_command="set names utf8")      
except MySQLdb.OperationalError,message:         
 print "like error"    
cursor=conn.cursor()  #�����ǲ���wordpress���ݿ��������䣬���Ǵ�mysqlbinlog���浼�����ģ������ǿ��Բ������ݿ⣬����������������ʾ����ҳ�ġ�������д������������     
sql="INSERT INTO wp_posts (post_author,post_date,post_date_gmt,post_content,post_content_filtered,post_title,post_excerpt,post_status,post_type,comment_status,ping_status,post_password,post_name,to_ping,pinged,post_modified,post_modified_gmt,post_parent,menu_order,guid) VALUES (\'1\',\'2011-06-01 22:12:25\',\'2011-05-09 04:12:25\',\'\',\'\',\'Auto Draft\',\'\',\'inherit\',\'revision\',\'open\',\'open\',\'\',\'100-revision\',\'\',\'\',\'2011-06-01 22:12:25\',\'2011-05-09 04:12:25\',\'%s\',\'0\',\'\')" %bianhao      
sql2="UPDATE wp_posts SET post_author = 1, post_date = \'2011-06-01 22:12:25\', post_date_gmt = \'2011-06-01 22:12:25\', post_content =\'%s\', post_content_filtered = \'\', post_title = \'%s\', post_excerpt = \'\', post_status = \'publish\', post_type = \'post\', comment_status = \'open\', ping_status = \'open\', post_password = \'\', post_name = \'%s\', to_ping = \'\', pinged = \'\', post_modified = \'2011-06-01 22:12:25\', post_modified_gmt = \'2011-05-09 04:12:30\', post_parent = 0, menu_order = 0, guid = \'http://www.moncleronlineshops.com/?p=%s\' WHERE ID = %s" %(Str2,titles,titles,bianhao,bianhao)      
cursor.execute(sql)      
cursor.execute(sql2) #�������ݿⲢִ����������䡣     
cursor.close()      
conn.close()  #�ر����ݿ⡣     
sys.exit() 
