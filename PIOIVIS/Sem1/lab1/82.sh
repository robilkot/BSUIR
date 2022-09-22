maxnumber=0
i=0
date=$(date +'%d%m%Y')

while [ $i -lt 8 ]
do
i=`expr $i + 1`
if [[ $maxnumber -lt  ${date:${i}:1} ]]; then
maxnumber=${date:${i}:1}
fi
done

#FOR DEBUG  maxnumber=4

if [ $(( $maxnumber%2 )) -eq 0 ]; then
    case $maxnumber in
        2)
            filename=two
            ;;
        4)
            filename=four
            ;;
        6)
            filename=six
            ;;
        8)
            filename=eight
            ;;
        0)
            filename=zero
            ;;
    esac
    touch ${filename}.txt
    if test -f "${filename}.txt"; then
        echo File "${filename}.txt" created 
    else
        echo File creation error
    fi
else
echo Hello
fi