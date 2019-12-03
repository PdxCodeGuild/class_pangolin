import os
import sys
import time
from datetime import date
from datetime import time, timezone, datetime

#
# Complete the timeConversion function below.
#


def timeConversion(s):
    now = datetime.now(s)
    t = now.strftime("%H:%M:%S")

    return t


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
