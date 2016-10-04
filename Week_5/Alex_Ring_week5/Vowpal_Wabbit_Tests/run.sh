#train
python3 shuffle.py
rm predictions.txt
rm week5.model
vw -f week5.model --passes=10 --cache_file=iris.cache --kill_cache --oaa 3 --loss_function=logistic  < week5_train.vw

#test
vw -i week5.model -t -p ./predictions.txt < week5_test.vw
python3 accuracy.py
