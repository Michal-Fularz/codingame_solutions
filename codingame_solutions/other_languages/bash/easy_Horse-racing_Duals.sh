# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# taken from:
# http://stackoverflow.com/questions/7442417/how-to-sort-an-array-in-bash
function bubble_sort()
{   #
    # Sorts all positional arguments and echoes them back.
    #
    # Bubble sorting lets the heaviest (longest) element sink to the bottom.
    #
    local array=($@) max=$(($# - 1))
    while ((max > 0))
    do
        local i=0
        while ((i < max))
        do
            # -gt instead of \>
            if [ ${array[$i]} -gt ${array[$((i + 1))]} ]
            then
                local t=${array[$i]}
                array[$i]=${array[$((i + 1))]}
                array[$((i + 1))]=$t
            fi
            ((i += 1))
        done
        ((max -= 1))
    done
    echo ${array[@]}
}

ARRAY=()

read N
for (( i=0; i<N; i++ )); do
    read Pi
    ARRAY[i]=$Pi
done

# from
# http://stackoverflow.com/questions/10586153/split-string-into-an-array-in-bash
IFS=' ' read -a sorted <<< "$(bubble_sort ${ARRAY[@]})"

for (( i=0; i<N; i++ )); do
    echo ${sorted[i]} >&2
done

MIN_DISTANCE=999999
PREVIOUS_VALUE=$((sorted[0]))
CURRENT_VALUE=0
for (( i=1; i<N; i++ )); do
    CURRENT_VALUE=$((sorted[i]))
    
    CURRENT_DISTANCE=$(( CURRENT_VALUE - PREVIOUS_VALUE ))
    
    if [ $CURRENT_DISTANCE -lt $MIN_DISTANCE ]
    then
        MIN_DISTANCE=$CURRENT_DISTANCE
    fi
    
    #echo ${PREVIOUS_VALUE} >&2
    #echo ${CURRENT_VALUE} >&2
    #echo ${CURRENT_DISTANCE} >&2
    #echo ${MIN_DISTANCE} >&2
    
    PREVIOUS_VALUE=$((CURRENT_VALUE))
done


# Write an action using echo
# To debug: echo "Debug messages..." >&2

echo $MIN_DISTANCE