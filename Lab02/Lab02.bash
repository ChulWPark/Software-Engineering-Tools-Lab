#! /bin/bash

#----------------------------------
# $Author: ee364b24 $
# $Date: 2018-01-23 15:06:19 -0500 (Tue, 23 Jan 2018) $
#----------------------------------

function part_1 
{               
    # Fill out your answer here
    
    # In order to ignore the first line because it's just an information
    # Shouldn't be considered when sorting
    num_lines=$(wc -l people.csv | cut -d " " -f 1)     # count the number of lines
    let without_first_line=$num_lines-1                 # number of lines - 1 (going to read that amount from the tail)
    tail -n $without_first_line people.csv | sort -k4,4 -k6,6 -k1,1 -k2,2 -t , | tail -n 9
    
    return                      
}                               

function part_2
{              
    # Fill out your answer here
    
    Arr=(a.txt b.txt c.txt d.txt e.txt)
    let selector=$RANDOM%5              # random number between 0 and 4
    # Read number of lines and check if it is odd or even
    how_many_lines=$(wc -l ${Arr[$selector]} | cut -d " " -f 1)
    let heading=($how_many_lines/2)+1
    if (( $how_many_lines%2 == 0 ))
    then
        head -n $heading ${Arr[$selector]} | tail -n 2
    else
        head -n $heading ${Arr[$selector]} | tail -n 1
    fi
    
    return                     
}                              

function part_3
{
    # Fill out your answer here
    
    # Go through all .c files in src folder
    for dotc in src/*.c
    do
        # count the number of characters
        noc=$(echo $dotc | wc -c)
        let noc=$noc-1
        # cut the path, which is src/
        filename=$(echo $dotc | cut -c 5-$noc)
        # compile, but compress the outputs from the compiler
        gcc -Wall -Werror $dotc -o ${dotc%.*}.o 2>temp.txt
        rm temp.txt
        oexist=0
        for doto in src/*.o
        do
            if [[ ${dotc%.*}.o == $doto ]]
            then
                if [[ -x $doto ]]
                then
                    oexist=1
                fi
            fi
        done
        if ((oexist == 1))
        then
            echo "$filename:  success"
        else
            echo "$filename:  failure"
        fi
        oexist=0
    done
    
    return
}

# To test your function, you can call it below like this:
#
echo ""
part_1
echo ""
part_2
echo ""
part_3
echo ""
