import re
import os
import subprocess
from colorama import Fore

src = "tests/ipp-2022-tests/interpret-only/"
test_types = os.listdir(src)

stats = {
    "OK": 0,
    "ERR_RC": 0,
    "ERR_OUT": 0,
}

for t_type in test_types:
    samples = [f.split(".")[0] for f in os.listdir(src+t_type+"/")]
    samples.sort()
    samples = set(samples)

    for sample in samples:
        splitter = "="*40
        print(f"\n{splitter} {t_type}/{sample} {splitter}\n")

        sp = f"{src}{t_type}/{sample}"
        process = None
        out_fd = open("tmp.out", "w")
        with open(f"{sp}.src", "r") as input_fd:
            command = f"python3 interpret.py --source={sp}.src --input={sp}.in"
            print(f"{Fore.GREEN}INFO :{Fore.RESET} {command} >tmp.out")
            process = subprocess.Popen(command.split(), stdout=out_fd)
        
        out_fd.close()
        output, error = process.communicate()
        rc = process.returncode
        rc_ref = 0

        # test output
        with open(f"{sp}.rc", "r") as f_ref:
            rc_ref = int(f_ref.readline().strip())

        if rc_ref != rc:
            print(f"{Fore.RED}ERROR:{Fore.RESET} Return Code {rc_ref} (ref) != {rc}")
            stats["ERR_RC"] += 1
            continue
        else:
            print(f"{Fore.GREEN}INFO :{Fore.RESET} Return code OK!")

        with open(f"{sp}.out", "r") as f_ref:
            ref_out = "".join([line.strip() for line in f_ref])
            my_out = ""
            with open("tmp.out", "r") as f:
               my_out = "".join([line.strip() for line in f])

            if ref_out != my_out:
                print(f"{Fore.RED}ERROR:{Fore.RESET} Output")
                cmd = f"diff -u {sp}.out tmp.out"
                process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
                output, error = process.communicate()
                print(str(output))
                stats["ERR_OUT"] += 1
                continue
            else:
                print(f"{Fore.GREEN}INFO :{Fore.RESET} Output OK!")
            stats["OK"] += 1

print(
f'''
==== Stats ====
OK     : {stats["OK"]}
ERR_RC : {stats["ERR_RC"]}
ERR_OUT: {stats["ERR_OUT"]}
'''
)

