#train
python3 shuffle.py
rm predictions.txt
rm PA2.model
vw -f PA2.model --passes=3 --cache_file=iris.cache --kill_cache --oaa 3 --loss_function=logistic  < PA2_train.vw

#test
vw -i PA2.model -t -p ./predictions.txt < PA2_test.vw
python3 accuracy.py



#92.5, 92.5, 90.4166, 92.916, 92.5
#91.25, 91.66, 93.75, 92.083, 91.66
#93.75, 91.631, 94.166, 92.5, 91.66
