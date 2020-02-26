print('\033c')

daily_fact = "40 years ago on this date\n\tThe Rubik's Cube makes its international debut\n\tat the Ideal Toy Corp. in Earl's Court, London"

print(f"\t\033[35;1m2020 - 1 - 29\n\n\t\033[36;1m{daily_fact}!\033[0m\n")


from dis import dis
import opcode

import random
import collections
import queue
import argparse
import time

DEFAULT_NUMBER_OF_TAXIS = 3
DEFAULT_END_TIME = 180
SEARCH_DURATION = 5
TRIP_DURATION = 20
DEPARTURE_INTERVAL = 5

Event = collections.namedtuple('Event', 'time proc action')


# BEGIN TAXI_PROCESS
def taxi_process(ident, trips, start_time=0):
    """Yield to simulator issuing event at each state change"""
    time = yield Event(start_time, ident, 'leave garage')
    for i in range(trips):
        time = yield Event(time, ident, 'pick up passenger')
        time = yield Event(time, ident, 'drop off passenger')

    yield Event(time, ident, 'going home')
    # end of taxi process
# END TAXI_PROCESS


# BEGIN TAXI_SIMULATOR
class Simulator:

    def __init__(self, procs_map):
        # FIFO -> First in First Out
        #         HEY I WAS IN LINE IN HERE FIRST, I GOT PRIORITY
        # LIFO -> Last in Last Out
        #         JUST USE THE LAST ONE
        self.events = queue.PriorityQueue()
        # Why do we say convert dictionary
        # when we know its a dictionary??
        # This copies the dictonary
        # Is that the reason
        self.procs = dict(procs_map)

    def run(self, end_time):
        """Schedule and display events until time is up"""
        # schedule the first event for each cab
        # Why do we call sorted???
        # How would this be unsorted????
        # does this reverse the sorted of what we got??
        for _, proc in sorted(self.procs.items()):
            # This primes each Coroutine
            # and adds only leave garage to the Queue
            first_event = next(proc)
            self.events.put(first_event)

        # main loop of the simulation
        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print('*** end of events ***')
                break
                # Break makes sense here, because its a while look
                # and this raises StopIteration????

            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event
            print('taxi:', proc_id, proc_id * '   ', current_event)

            # This is the Coroutine
            active_proc = self.procs[proc_id]
            next_time = sim_time + compute_duration(previous_action)
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            msg = '*** end of simulation time: {} events pending ***'
            print(msg.format(self.events.qsize()))
# END TAXI_SIMULATOR


def compute_duration(previous_action):
    """Compute action duration using exponential distribution"""

    if previous_action in ['leave garage', 'drop off passenger']:
        # new state is prowling
        interval = SEARCH_DURATION

    elif previous_action == 'pick up passenger':
        # new state is trip
        interval = TRIP_DURATION
    elif previous_action == 'going home':
        interval = 1
    else:
        raise ValueError('Unknown previous_action: %s' % previous_action)
    return int(random.expovariate(1/interval)) + 1


def main(end_time=DEFAULT_END_TIME, num_taxis=DEFAULT_NUMBER_OF_TAXIS,
         seed=None):
    """Initialize random generator, build procs and run simulation"""
    if seed is not None:
        random.seed(seed)  # get reproducible results

    # Generate a Dictionary, with the numerical keys
    # and a generator for each value

    # taxi_process(i, (i+1)*2, i*DEPARTURE_INTERVAL)

    # Is this a code smell
    # or is this elite python
    # or is it stupid example code

    # taxi_process(i, (i+1)*2, i*DEPARTURE_INTERVAL)
    # taxi_process(ident, trips, start_time=0):
    taxis = {
             i: taxi_process(i, trip_count_calc(i), start_time_calc(i))
             for i in range(num_taxis)
            }

    sim = Simulator(taxis)
    sim.run(end_time)

def start_time_calc(i):
    return i*DEPARTURE_INTERVAL

def trip_count_calc(i):
    return (i+1)*2


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                        description='Taxi fleet simulator.')
    parser.add_argument('-e', '--end-time', type=int,
                        default=DEFAULT_END_TIME,
                        help='simulation end time; default = %s'
                        % DEFAULT_END_TIME)
    parser.add_argument('-t', '--taxis', type=int,
                        default=DEFAULT_NUMBER_OF_TAXIS,
                        help='number of taxis running; default = %s'
                        % DEFAULT_NUMBER_OF_TAXIS)
    parser.add_argument('-s', '--seed', type=int, default=None,
                        help='random generator seed (for testing)')
    args = parser.parse_args()
    main(args.end_time, args.taxis, args.seed)

