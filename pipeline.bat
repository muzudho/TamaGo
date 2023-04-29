FOR /L %%v IN (1,1,100) DO (
    python selfplay_main.py --save-dir archive --model model/rl-model.bin --use-gpu true
    python get_final_status.py
    python train.py --rl true --kifu-dir archive
)
