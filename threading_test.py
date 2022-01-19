'''

threading vs processing
1.Concurrantlly

* When we have I/o bound like reading from disk /downloading from net then its better to run it in concurrently
* When its CPU bound task then  its good to used multi processing .
* see how to pass arguments to threads
* thread pool executer

'''
#import threading
import concurrent.futures
import time

start = time.perf_counter()

# def do_something():
#     print('Sleep 1 second')
#     time.sleep(1)
#     print('Done Sleeping')

def do_something(seconds):
    print(f'Sleep {seconds} second')
    time.sleep(seconds)
    return 'Done Sleeping'

# do_something() # To run the function syncronaously
# do_something()

# t1=threading.Thread(target=do_something)
# t2=threading.Thread(target=do_something)
#
# t1.start()
# t2.start()
#
# t1.join() #It joins the thread to the main process
# t2.join()

# Start 10 threads concurrently
# threads =[]
# for _ in range(10):
#     t=threading.Thread(target=do_something,args=[1.5])
#     t.start()
#     # t.join()  #It will join the main process before starting the new thread
#     threads.append(t)
#
# for thd in threads:
#     thd.join()

## run usinf threadpool executer

sl=[5,4,3,2,1]

with concurrent.futures.ThreadPoolExecutor() as executor:
    #f1=executor.submit(do_something,1)
    f1=executor.map(do_something, sl)
    #print(f1.result())


finish=time.perf_counter()
print(f'Finished in {round(finish-start)} second(s) ')
