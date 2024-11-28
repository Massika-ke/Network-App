import threading

#create the threads
def create_threads(list, function):

    threads =[]

    for ip in list:
        th = threading.Thread(target = function, args= (ip,)) #args is a tuple with a single element
        th.start()
        threads.append(th)

    for th in threads:
        th.join() #Waits for all threads to terminate