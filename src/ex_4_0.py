""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def get_shutdown_events(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation
    """
    str1 = 'Shutdown initiated'
    with open(logfile, 'r') as inputfile:
        inputfiledata = inputfile.read()
    inputfiledataline = inputfiledata.splitlines()
    output_events = list()
    for rw in inputfiledataline:
        if str1 in rw :
            output_events.append(rw)
    return output_events


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")
