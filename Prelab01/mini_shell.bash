#! /bin/bash

#---------------------------------------
# $Author: ee364b24 $
# $Date: 2018-01-14 21:41:19 -0500 (Sun, 14 Jan 2018) $
#---------------------------------------

# Do not modify above this line.

while (( 1 ))
do
    # Prompt the message and get the user input
    echo -n "Enter a command: "
    read user_input

    # Action according to the user_input
    if [[ $user_input == "hello" ]]
    then
        echo "Hello $USER"
    elif [[ $user_input == "quit" ]]
    then
        echo "Goodbye"
        echo ""
        exit 0
    elif [[ $user_input == "compile" ]]
    then
        # Go through all of the .c files in current directory
        for dotc in *.c
        do
            gcc -Wall -Werror $dotc -o ${dotc%.*}.o
            oexist=0
            # After compilation, go through all of the .o files
            for doto in *.o
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
                echo "Compilation succeeded for: $dotc"
            else
                echo "Compilation failed for: $dotc"
            fi
            oexist=0
        done
    elif [[ $user_input == "run" ]]
    then
        echo -n "Enter filename: "
        read filename
        echo -n "Enter arguments: "
        read arguments
        if [[ ! -e "$filename" ]]
        then
            echo "Invalid filename"
        elif [[ ! -x "$filename" ]]
        then
            echo "Invalid filename"
        else
            ./$filename $arguments
        fi
    else
        echo "Error: unrecognized input"
    fi
    echo ""
done

# Exit Successfully
exit 0
