"""
pipeline.py

python pipeline.py
"""
import subprocess
import datetime

def main():
    """機械学習"""

    for i in range(0,100):
        dt_now = datetime.datetime.now()
        print(f"[{dt_now}] Self play ({i+1})")
        subprocess.run([r"python", r"./selfplay_main.py",
                        r"--save-dir", r"archive",
                        r"--model", r"model/rl-model.bin",
                        r"--use-gpu", r"true"],
                    shell=False,check=False)
        
        dt_now = datetime.datetime.now()
        print(f"[{dt_now}] Train ({i+1})")
        subprocess.run([r"python", r"./train.py",
                        r"--rl", r"true",
                        r"--kifu-dir", r"archive"],
                    shell=False,check=False)

if __name__ == "__main__":
    main()
