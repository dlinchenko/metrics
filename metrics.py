import psutil
import sys


def cpu_stats():
    stats = dict(psutil.cpu_times()._asdict())
    for k in stats.keys():
        print('System.cpu.' + k + ' ' + str(stats[k]))


def mem_stats():
    stats_vm = dict(psutil.virtual_memory()._asdict())
    stats_sw = dict(psutil.swap_memory()._asdict())
    for k in stats_vm.keys():
        print('Virtual ' + k + ' ' + str(stats_vm[k]))
    for k in stats_sw.keys():
        print("Swap " + k + ' ' + str(stats_sw[k]))


def usage():
    print('metrics.py util can be used either to get CPU or Memory usage metrics\n'
          'for CPU usage run: metrics.py cpu\n'
          'for Memory usage run: metrics.py mem\n')


if __name__ == '__main__':
    if len(sys.argv) > 2 or len(sys.argv) == 1:
        usage()
    elif sys.argv[1] == 'mem':
        mem_stats()
    elif sys.argv[1] == 'cpu':
        cpu_stats()
    else:
        usage()
