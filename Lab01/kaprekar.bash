#! /bin/bash

#---------------------------------------
# $Author: ee364b24 $
# $Date: 2018-01-16 14:44:36 -0500 (Tue, 16 Jan 2018) $
#---------------------------------------

# Do not modify above this line.

# If the number of arguments is not 1: exit 1
if (( $# != 1 ))
then
    echo "Usage: kaprekar.bash <non-negative integer>"
    exit 1
fi

# If the first argument is a negative integer: exit 1
if (( $1 < 0 ))
then
    echo "Usage: kaprekar.bash <non-negative integer>"
    exit 1
fi

# Local Declarations
numb=1
max=$1

while (( numb <= max ))
do
    let squared=$numb*$numb
    digit_num=$(echo $squared | wc -c)
    let digit_num=$digit_num-1
    #echo "$squared has $digit_num digits"
    # Split into 2 cases: even number of digits & odd number of digits
    # Even number of digits
    if (( digit_num%2 == 0 ))
    then
        let digit_num_half1=$digit_num/2
        let digit_num_half2=$digit_num_half1+1
        first_half=$(echo $squared | cut -c 1-$digit_num_half1)
        first_half_no_zeros=$((10#$first_half))
        second_half=$(echo $squared | cut -c $digit_num_half2-$digit_num)
        second_half_no_zeros=$((10#$second_half))
        let kaprekar_num=$first_half_no_zeros+$second_half_no_zeros
        # If it is kaprekar number, print the output
        if (( kaprekar_num == numb ))
        then
            echo "$numb, square=$squared, $second_half+$first_half=$kaprekar_num"
        fi
    # Odd number of digits
    elif (( digit_num%2 == 1 ))
    then
        let digit_num_half1=$digit_num/2
        let digit_num_half2=$digit_num_half1+1
        if (( digit_num == 1 ))
        then
            first_half=0
            first_half_no_zeros=0
            second_half=$squared
            second_half_no_zeros=$squared
        else
            first_half=$(echo $squared | cut -c 1-$digit_num_half1)
            first_half_no_zeros=$((10#$first_half))
            second_half=$(echo $squared | cut -c $digit_num_half2-$digit_num)
            second_half_no_zeros=$((10#$second_half))
        fi
        let kaprekar_num=$first_half_no_zeros+$second_half_no_zeros
        # If it is kaprekar number, print the output
        if (( kaprekar_num == numb ))
        then
            echo "$numb, square=$squared, $second_half+$first_half=$kaprekar_num"
        fi
    fi 

    # Increment numb by 1 after each iteration
    let numb=$numb+1
done  
    

# EXAMPLE
# d=1234
# q=$(echo $d | cut -c 1-2)
# echo $q

exit 0
