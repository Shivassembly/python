''' briliant.overloading

Multi processing : speed up program ,cpu bound programs will get most of it
* Running parallelling  syncronously based on opur hardware and CPUs


'''
import concurrent.futures
# import multiprocessing  #its not rewuired now
import time

start=time.perf_counter()


# def do_something():
#     print('Sleeping 1 second')
#     time.sleep(1)
#     print('Done Sleeping')

# # Passing an orgument

# def do_something(seconds):
#     print(f'Sleeping {seconds} second(s)')
#     time.sleep(seconds)
#     print('Done Sleeping')

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'  # this returns for  processpoolexecuter as future type

# do_something()
# do_something() #these statements will take 2 seconds as runs syncronaously

# do it in multiprocessing way





if __name__ == '__main__':

    # p1=multiprocessing.Process(target=do_something)
    # p2=multiprocessing.Process(target=do_something)
    # p1.start()
    # p2.start()
    #
    # p1.join()
    # p2.join()

    ## Running 10 processes parallelling
    # processes =[]
    #
    # for _ in range(10):
    #     p= multiprocessing.Process(target=do_something,args=[1.5])
    #     p.start()
    #     processes.append(p)
    #
    # for process in processes:
    #     process.join()

    with concurrent.futures.ProcessPoolExecutor() as executer:
        # f1=executer.submit(do_something,1.5)
        # f2=executer.submit(do_something,1.5)
        # print(f1.result())
        # print(f2.result())
        secs =[5,4,3,2,1]
        # results=[executer.submit(do_something,sec) for sec in secs]
        # for f in concurrent.futures.as_completed(results):
        #     print(f.result())
        results=executer.map(do_something,secs)

        for result in results:
            print(result)

    finish=time.perf_counter()
    print(f'Finished in {round(finish - start,2)} second(s)')
