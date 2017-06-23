import traceback
from time import strftime, gmtime


def log(log_file):
    with open(log_file, "a") as f:
        f.write(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        f.write('\n')
        traceback.print_exc(file=f)
