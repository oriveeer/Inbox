#!/bin/bash

#################################################################
# /var/log/messages get shell
#################################################################

WORK_DIR="/home/operatoradmin/work_shell"
messages2="${WORK_DIR}/messages"

time1=$(nl ${messages2} | grep "\ 12:..:..\ " | awk 'NR==1' | awk '{print $1}')
time2=$(nl ${messages2} | grep "\ 12:..:..\ " | awk 'END{print}' | awk '{print $1}')

echo ${time1}
echo ${time2}

sed -n "${time1},${time2}p" ${messages2} > kekka

echo "kanryo"

#################################################################
