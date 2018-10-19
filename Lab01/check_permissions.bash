#! /bin/bash

#---------------------------------------
# $Author: ee364b24 $
# $Date: 2018-01-16 15:15:15 -0500 (Tue, 16 Jan 2018) $
#---------------------------------------

# Do not modify above this line.

# If the number of arguments is not 1: exit 1
if (( $# != 1 ))
then
    echo "Usage: check_permissions.bash <input file/directory>"
    exit 1
fi

lsl_output=$(ls -l -d $1)

# Check if it is a file or directory
checking=$(echo $lsl_output | cut -c 1)
if [[ $checking == "-" ]]
then
    echo "$1 is an ordinary file"
    echo ""
elif [[ $checking == "d" ]]
then
    echo "$1 is a directory"
    echo ""
fi

# Cut into three parts (owner, group others)
first_three1=$(echo $lsl_output | cut -c 2)
first_three2=$(echo $lsl_output | cut -c 3)
first_three3=$(echo $lsl_output | cut -c 4)
second_three1=$(echo $lsl_output | cut -c 5)
second_three2=$(echo $lsl_output | cut -c 6)
second_three3=$(echo $lsl_output | cut -c 7)
third_three1=$(echo $lsl_output | cut -c 8)
third_three2=$(echo $lsl_output | cut -c 9)
third_three3=$(echo $lsl_output | cut -c 10)

echo "Owner Permissions:"
echo ""
if [[ $first_three1 == "r" ]]
then
    echo "$1 is readable"
else
    echo "$1 is not readable"
fi
if [[ $first_three2 == "w" ]]
then
    echo "$1 is writable"
else
    echo "$1 is not writable"
fi
if [[ $first_three3 == "x" ]]
then
    echo "$1 is executable"
else
    echo "$1 is not executable"
fi
echo ""
echo "Group Permissions:"
echo ""
if [[ $second_three1 == "r" ]]
then
    echo "$1 is readable"
else
    echo "$1 is not readable"
fi
if [[ $second_three2 == "w" ]]
then
    echo "$1 is writable"
else
    echo "$1 is not writable"
fi
if [[ $second_three3 == "x" ]]
then
    echo "$1 is executable"
else
    echo "$1 is not executable"
fi
echo ""
echo "Others Permissions:"
echo ""
if [[ $third_three1 == "r" ]]
then
    echo "$1 is readable"
else
    echo "$1 is not readable"
fi
if [[ $third_three2 == "w" ]]
then
    echo "$1 is writable"
else
    echo "$1 is not writable"
fi
if [[ $third_three3 == "x" ]]
then
    echo "$1 is executable"
else
    echo "$1 is not executable"
fi
echo ""

exit 0
