#! /bin/bash

#---------------------------------------
# $Author: ee364b24 $
# $Date: 2018-01-14 01:40:28 -0500 (Sun, 14 Jan 2018) $
#---------------------------------------

# Do not modify above this line.

# If the number of arguments is not 2: exit 1
if (( $# != 2 ))
then
    echo "Usage: ./collect_stats.bash <file> <sport>"
    exit 1
fi

# If the first argument is a non-existent file: exit 2
if [[ ! -e "$1" ]]
then
    echo "Error: $1 does not exist"
    exit 2
fi

# Assigns file descriptor 3 to $1 for reading
exec 3<$1

# Initialize variables
total_athletes=0
total_medals=0
medals_max=0

# Read the input file until it hits EOF
while IFS=, read name sport num_medals
do
    if [[ $sport == $2 ]]
    then
        let total_athletes=$total_athletes+1
        let total_medals=$total_medals+$num_medals
        if (( $num_medals > medals_max ))
        then
            medals_max=$num_medals
            won_most_medals=$name
        fi
    fi
done <&3

# Print the output to stdout
echo "Total athletes: $total_athletes"
echo "Total medals won: $total_medals"
echo "$won_most_medals won the most medals: $medals_max" 

exit 0
