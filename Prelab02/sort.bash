#! /bin/bash

#---------------------------------------
# $Author: ee364b24 $
# $Date: 2018-01-19 10:56:52 -0500 (Fri, 19 Jan 2018) $
#---------------------------------------

# Do not modify above this line.

# If the number of arguments is not 1: exit 1
if (( $# != 1 ))
then
    echo "Usage: ./sort.bash <filename>"
    exit 1
fi

# If the filename does not exist in current path: exit 2
if [[ ! -e $1 ]]
then
    echo "Error: $1 does not exist."
    exit 2
fi

# Sort by execution time (increasing order)
sort -n -k5 -t , $1 > sorted_by_exe_t.txt       # write to the output file
echo "The 5 fastest CPUs:"                      # echo message
head -n 5 sorted_by_exe_t.txt                   # print top 5 lines
echo ""                                         # new line

# Sort by CPI (increasing order)
sort -n -k4 -t , $1 > sorted_by_CPI.txt         # write to the output file
echo "The 3 most efficient CPUs:"               # echo message
head -n 3 sorted_by_CPI.txt                     # print top 3 lines
rm sorted_by_CPI.txt                            # remove the output file
echo ""                                         # new line

# Print all CPUs that have a cache size of 4, in order of increasing execution time
echo "The CPUs with cache size 4:"              # echo message
exec 3<sorted_by_exe_t.txt                      # open the output file (sorted by execution time) created above for reading
while IFS=, read a b c d e                      # read the entire contents line by line
do
    if [[ $b == "4" ]]                          # if the cache size is 4
    then
        echo "$a,$b,$c,$d,$e"                   # print that line
    fi
done <&3                                        # read it from sorted_by_exe_t.txt
rm sorted_by_exe_t.txt                          # remove the output file because it is no longer needed
echo ""                                         # new line

# Print the n slowest CPUs (prompt the user for n)
echo -n "Enter a value for n: "                 # echo message
read user_input                                 # prompt the user for n
sort -r -n -k5 -t , $1 > sorted_by_exe_t.txt    # sort by execution time in reverse order and write to the output file
echo "The $user_input slowest CPUs:"                     # echo message
head -n $user_input sorted_by_exe_t.txt         # print top n lines
rm sorted_by_exe_t.txt                          # remove the output file

# Print to a file called sorted_CPI.txt
sort -k1,1 -k4,4n -t , $1 > sorted_CPI.txt      # sort by processor name first, then by CPI and write to the output file

# Newline at the end
echo ""

# Exit successfully
exit 0
