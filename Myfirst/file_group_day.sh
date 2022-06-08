#!/bin/bash
#########################################################################
# File Name: file_group_day.sh
# Author: sunliguo
# mail: sunliguo2006@qq.com
# Created Time: Mon 15 Jan 2018 01:18:05 PM CST
# 2019-05-14:添加shuf随机。
# 2019-05-18:添加统计文件个数file_count
# 2019-05-19:增加处理带有空格的文件名
# 2019-11-13:将移动文件放到后台执行
# 2019-12-28:将要处理的文件存到数组中去。按时间分组改为函数
########################################################################

PWD='./'
oldIFS=${IFS}
echo
echo "This script's PID $$"

#带有空格的文件名会统计2次
#file_count=`echo $file_list |wc -w`

#生成文件列表的数组
i=0
for file in `find $PWD -maxdepth 1 -type f|shuf`
do
  echo -e "\e[A$i"
  file_arr[$i]=$file
  (( a++ ))
done
unset i

#file_count=${#file_arr[@]}
#echo "file_arr's size " $file_count
#echo  ${file_arr[*]}

function file_group_day() {
echo "$$ start"
    for file_in in  $*
    do
        {
        #echo $file_in
        MOD_TIME=`stat -c %y $file_in|awk '{print $1}'`
        if [ ! -d $MOD_TIME ];then
          mkdir $MOD_TIME
        fi
        #\mv -iv $file_in $MOD_TIME/ >/dev/null 2>&1
        \mv -iv $file_in $MOD_TIME/
        }
    done
    echo "$$ stop"
}

file_first=0
arr_size=${#file_arr[@]}

echo "arr_size="$arr_size

while [ $file_first -lt $arr_size ]
do
  echo "file_first=$file_first"
  c=(${file_arr[@]:${file_first}:100})
  #echo ${c[@]}
  file_group_day ${c[@]} & >/dev/null 2>&1
  file_first=$(($file_first+100))
  #echo "file_first ="$file_first
done
wait
IFS=${oldIFS}