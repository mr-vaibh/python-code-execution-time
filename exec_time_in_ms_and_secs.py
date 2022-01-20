import datetime
def func(seconds=False):

    start_time = datetime.datetime.now()
    end_time = datetime.datetime.now()
#your code here
    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds() *0.001
    if (seconds==False):
        pass
    else:

        end_time = datetime.datetime.now()

        time_diff = (end_time - start_time)
        execution_time_seconds = time_diff.total_seconds()
        return(execution_time,'- in milliseconds & in seconds - ',execution_time_seconds) 

    return('execution time in milliseconds - ',execution_time)

z=func(seconds=True)
print(z)