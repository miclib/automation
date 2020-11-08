#!/bin/bash
#
# print commonly used env vars
#
#
#
clear
#
echo "------------------------------------------------"
echo "system information: " $(uname -a)
echo "uptime: " $(uptime)
set |grep BASH_VERSION
set |grep EDITOR
set |grep GROUPS
set |grep HISTFILE
set |grep HISTSIZE
set |grep HOME
set |grep HOSTNAME
set |grep SHELL
echo "shell:"  $(readlink /bin/sh)
echo "-------------------------------------------------"
echo "  "
echo "List partitions" 
lsblk
