# encoding: utf-8

import sys
import commands
import time
import gc

import numpy

process=sys.argv[0]

def get_use_memory():
    global process
    return commands.getstatusoutput('ps aux | grep "{0}" | grep -v "grep"'.format(process))

def normalize_feature(node, delete_list):
    print 'normalize_feature_step1', get_use_memory()
    normal_features = []
    for i in range(0, node.shape[0]):
        feature_numpy = node[i, :]

        feature_numpy_d = numpy.delete(feature_numpy, delete_list, axis=0)
        normal_features.append(feature_numpy_d)
        del feature_numpy
        del feature_numpy_d

    print 'normalize_feature_step2', get_use_memory()
    np_normal_features = numpy.array(normal_features)
    print sys.getsizeof(np_normal_features) / float(1024) / float(1024)
    print 'normalize_feature_step3', get_use_memory()
    del normal_features
    gc.collect()
    print 'normalize_feature_step4', get_use_memory()
    return np_normal_features

#gc.set_debug(gc.DEBUG_STATS|gc.DEBUG_LEAK)

rows=10240
columns=1024
a = []
for i in range(0, rows):
    b = []
    for j in range(0, columns):
        b.append(float(i) * j)
    a.append(b)
    del b

print get_use_memory()

node_1 = numpy.array(a)
print sys.getsizeof(node_1) / float(1024) / float(1024)
print get_use_memory()
del a
gc.collect()
print get_use_memory()

node_2 = normalize_feature(node_1, [0, 100, 1000])
print sys.getsizeof(node_2) / float(1024) / float(1024)
print get_use_memory()

del node_1
del node_2
gc.collect()
print get_use_memory()
