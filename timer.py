import time
seg = input(" Digite o tempo em segs :")
def fseg(seg):
    mins=seg/60;
    secs=seg%60;
    timer=f'{mins}:{secs}'
    print(timer)
fseg(int(seg))

### função tempo esgotado
seg1 = input(" Digite novamente em segs ")
def fsege(seg1):
    while seg1>0:
        mins=seg1/60;
        secs=seg1%60;
        timer=f'{mins}:{secs}'
        seg1-=1
        ## o r irá substituir string
        print(timer,end="\r")
        time.sleep(1)
        print(timer)
fsege(int(seg))