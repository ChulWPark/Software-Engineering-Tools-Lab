#! /bin/bash

#---------------------------------------
# $Author: ee364b24 $
# $Date: 2018-01-19 10:56:52 -0500 (Fri, 19 Jan 2018) $
#---------------------------------------

# Do not modify above this line.

# If the number of arguments is not 1: exit 1
if (( $# != 1 ))
then
    echo "Usage: ./treasure.bash <filename>"
    exit 1
fi

# Store the map information into a string variable
map_info=$(cat $1)

# Set the new line as field separator so that it reads line by line
IFS=$'\n'

# Initialize row and column position
row_pos=0
col_pos=0

while (( 1 ))
do
    echo "($row_pos,$col_pos)"
    line_counter=0
    # Visiting the specific cell in the map
    for line in $map_info
    do
        if (( $line_counter == $row_pos ))
        then
            let a=$col_pos*3+1
            let b=$a+1
            row_pos_new=$(echo $line | cut -c $a)
            col_pos_new=$(echo $line | cut -c $b)
            if (( ($row_pos_new == $row_pos) && ($col_pos_new == $col_pos) ))
            then
                echo "Treasure found at: ($row_pos,$col_pos)"
                exit 0
            fi
        fi   
        let line_counter=$line_counter+1
    done
    # Treasure was not found, so update the position
    row_pos=$row_pos_new
    col_pos=$col_pos_new
done

# Exit successfully (just in case)
exit 0
