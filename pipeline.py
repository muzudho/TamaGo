"""
pipeline.py

python pipeline.py
"""
import subprocess

def main():
    """機械学習"""
    subprocess.run([r"python", r"./selfplay_main.py",
                    r"--save-dir", r"archive",
                    r"--model", r"model/rl-model.bin",
                    r"--use-gpu", r"true"],
                   shell=False,check=False)
    subprocess.run([r"python", r"./train.py",
                    r"--rl", r"true",
                    r"--kifu-dir", r"archive"],
                   shell=False,check=False)

if __name__ == "__main__":
    main()
