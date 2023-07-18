""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation.
    """
    output_events = get_shutdown_events(logfile)
    output_event1 = output_events[0]
    output_event_last= output_events[-1]
    logstamp_to_datetime1 = logstamp_to_datetime(output_event1.split()[1])
    logstamp_to_datetime2 = logstamp_to_datetime(output_event_last.split()[1])
    logstamp_to_datetime1 = logstamp_to_datetime2-logstamp_to_datetime1
    return logstamp_to_datetime1


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
