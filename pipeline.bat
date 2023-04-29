REM Reference / Make command for PyTorch install: [Get Started](https://pytorch.org/get-started/locally/)
REM             Example: `conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia`
REM Reference / FOR statement: [MS-DOS .bat control flow for loop](https://www.ipentec.com/document/ms-dos-bat-control-flow-for-loop)
FOR /L %%v IN (1,1,100) DO (
    python ./selfplay_main.py --save-dir archive --model model/rl-model.bin --use-gpu true
    python ./get_final_status.py
    python ./train.py --rl true --kifu-dir archive
)
