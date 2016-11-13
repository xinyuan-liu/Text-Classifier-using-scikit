for((i=0;i<8;i++));do
    ./classify.py $i &
done
wait
echo DONE
