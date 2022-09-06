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

echo $maxnumber