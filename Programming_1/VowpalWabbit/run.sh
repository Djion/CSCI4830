#train
python3 shuffle.py
rm predictions.txt
rm iris.model
vw -f iris.model --passes=10 --cache_file=iris.cache --kill_cache --oaa 3 --loss_function=hinge < iris_train.vw

#test
vw -i iris.model -t -p ./predictions.txt < iris_test.vw
python3 accuracy.py
