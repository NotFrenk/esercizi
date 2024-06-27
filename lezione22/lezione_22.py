import time

threads:list = []

def thread_function(name):
    print(f'time - {time.time()}')
    time.sleep(2)
    print(f'{name} time - {time.time()}')

import threading
for i in range(3):

    x = threading.Thread(target=thread_function, args=(1, ))
    threads.append(x)
    x.start()

for t in threads:
    
    t.join()

print(f'prima di thread')
x.start()
print(f'thread partito')
x.join()
print('thread finito?????')