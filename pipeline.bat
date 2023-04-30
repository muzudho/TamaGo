REM SET UP
REM ======
REM Reference / Make command for PyTorch install: [Get Started](https://pytorch.org/get-started/locally/)
REM             Example: `conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia`
REM
REM RUN
REM ===
REM Don't run from Visual Studio Code. Please use command prompt
REM `%windir%\system32\cmd.exe "/K" %USERPROFILE%\Anaconda3\Scripts\activate.bat %USERPROFILE%\Anaconda3`
REM
REM Example:
REM (base) C:\GitHub\TamaGo>pipeline.bat
REM
REM Reference / FOR statement: [MS-DOS .bat control flow for loop](https://www.ipentec.com/document/ms-dos-bat-control-flow-for-loop)
FOR /L %%v IN (1,1,100) DO (
    python ./selfplay_main.py --save-dir archive --model model/rl-model.bin --use-gpu true
    python ./get_final_status.py
    python ./train.py --rl true --kifu-dir archive
)
