'''

threading vs processing
1.Concurrantlly

'''

import time

start = time.perf_counter()

def do_something():
    print('Sleep 1 second')
    time.sleep(1)
    print('Done Sleeping')


do_something()

finish=time.perf_counter()
print(f'Finished in {round(finish-start)} second(s)')
