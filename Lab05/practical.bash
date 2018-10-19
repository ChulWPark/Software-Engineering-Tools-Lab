#! /bin/bash

#----------------------------------
# $Author: ee364b24 $
# $Date: 2018-02-14 19:48:20 -0500 (Wed, 14 Feb 2018) $
#----------------------------------

function part_a 
{               
    # Fill out your answer here. Do not include exit 0 in your code.
    Arr=(a.txt b.txt c.txt d.txt e.txt)
    let selector=$RANDOM%5              # random number between 0 and 4
    head -n 5 ${Arr[$selector]} | tail -n 3

    return
}                               

function part_b
{              
    # Fill out your answer here. Do not include exit 0 in your code.
    count1=0
    count2=0
    for file in myDir1/*
    do
        let count1=$count1+1
    done
    for file in myDir2/*
    do
        let count2=$count2+1
    done
    if (( $count1 == $count2 ))
    then
        echo "Similar"
    else
        echo "Different"
    fi

    return                     
}                              

function part_c
{
    # Fill out your answer here. Do not include exit 0 in your code.
    sort file.txt | uniq -d

    return
}

function part_d
{
    # Fill out your answer here. Do not include exit 0 in your code.
    count=0
    exec 3<temp.txt
    while read line
    do
        noc=$(echo "$line" | wc -c)
        if (( $noc >= 10 ))
        then
            let count=$count+1
        fi
    done <&3
    echo "temp.txt has $count lines with at least length ten"
    
    return
}

function part_e
{
    # Fill out your answer here. Do not include exit 0 in your code.
    python3.4 ece364.py 1>output.txt
    
    return
}

function part_f
{
    # Fill out your answer here. Do not include exit 0 in your code.
    tail -n +2 people.csv | sort -t',' -k4,4 -k6,6 -k1,1 -k2,2 | head -n 10 

    return
}

function part_g
{
    # Fill out your answer here. Do not include exit 0 in your code.
    count1=0
    count2=0
    for file in myDir/*.java
    do
        let count1=$count1+1
    done
    for file in myDir/*.c
    do
        let count2=$count2+1
    done
    let sum=$count1+$count2
    echo "$sum"

    return
}


function part_h
{
    # Fill out your answer here. Do not include exit 0 in your code.
    grep -c "VALENTINE" info.txt

    return
}

function part_i
{
    # Fill out your answer here. Do not include exit 0 in your code.
    numb=1
    sum=0
    # Create an empty file, just in case (because appending on the bottom)
    echo -n "" 1>abundant.txt
    while (( $numb <= 100 ))
    do
        let comp=$numb-1
        while (( $comp > 0 ))
        do
            let rem=$numb%$comp
            if (( $rem == 0 ))
            then
                let sum=$sum+$comp
            fi
            let comp=$comp-1
        done
        # If sum is greater then numb, it is an abundant number, so write
        if (( $sum > $numb ))
        then
            echo "$numb" 1>>abundant.txt
        fi
        # Increment numb by 1
        let numb=$numb+1
        # Reset sum for next numb
        sum=0
    done
    
    return
}


# To test your function, you can call it below like this:
echo "PART A"
part_a
echo "PART B"
part_b
echo "PART C"
part_c
echo "PART D"
part_d
echo "PART E"
part_e
echo "PART F"
part_f
echo "PART G"
part_g
echo "PART H"
part_h
echo "PART I"
part_i
