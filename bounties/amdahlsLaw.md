# Amdahl's Law
## Overview
---

In computer architecture, Amdahl's law (or Amdahl's argument[1]) is a formula which gives the theoretical speedup in latency of the execution of a task at fixed workload that can be expected of a system whose resources are improved. It is named after computer scientist Gene Amdahl, and was presented at the AFIPS Spring Joint Computer Conference in 1967.

Amdahl's law is often used in parallel computing to predict the theoretical speedup when using multiple processors. For example, if a program needs 20 hours to complete using a single thread, but a one-hour portion of the program cannot be parallelized, therefore only the remaining 19 hours (p = 0.95) of execution time can be parallelized, then regardless of how many threads are devoted to a parallelized execution of this program, the minimum execution time cannot be less than one hour. Hence, the theoretical speedup is limited to at most 20 times the single thread performance,
  (1/1-p = 20)

### Definition

Amdahl's Law can be formuated in the following way:
  S latency(s) = 1 / 1-p + p/s

  where:
  - s latency is the theoretical speedup of the execution of the whole task;
  - s is the number of threads across which the parallel portion is split;
  - p is the proportion of the execution time that the part benefiting from improved resources orginally ocuppied

shows that the theoretical speedup of the execution of the whole task increases with the improvement of the resources of the system and that regardless of the magnitude of the improvement, the theoretical speedup is always limited by the part of the task that cannot benefit from the improvement.

Amdahl's law applies only to the cases where the problem size is fixed. In practice, as more computing resources become available, they tend to get used on larger problems (larger datasets), and the time spent in the parallelizable part often grows much faster than the inherently serial work. In this case, Gustafson's law gives a less pessimistic and more realistic assessment of the parallel performance.


### Derivation

A task executed by a system whose resources are improved compared to an initial similar system can be split up into two parts:

    a part that does not benefit from the improvement of the resources of the system;
    a part that benefits from the improvement of the resources of the system.

An example is a computer program that processes files from disk. A part of that program may scan the directory of the disk and create a list of files internally in memory. After that, another part of the program passes each file to a separate thread for processing. The part that scans the directory and creates the file list cannot be sped up on a parallel computer, but the part that processes the files can.

The execution time of the whole task before the improvement of the resources of the system is denoted as T {\displaystyle T} T. It includes the execution time of the part that would not benefit from the improvement of the resources and the execution time of the one that would benefit from it. The fraction of the execution time of the task that would benefit from the improvement of the resources is denoted by p {\displaystyle p} p. The one concerning the part that would not benefit from it is therefore 1 − p {\displaystyle 1-p} {\displaystyle 1-p}. Then:

    T = ( 1 − p ) T + p T . {\displaystyle T=(1-p)T+pT.} 

It is the execution of the part that benefits from the improvement of the resources that is accelerated by the factor s {\displaystyle s} s after the improvement of the resources. Consequently, the execution time of the part that does not benefit from it remains the same, while the part that benefits from it becomes:

    p s T . {\displaystyle {\frac {p}{s}}T.} {\frac {p}{s}}T.

The theoretical execution time T ( s ) {\displaystyle T(s)} {\displaystyle T(s)} of the whole task after the improvement of the resources is then:

    T ( s ) = ( 1 − p ) T + p s T . {\displaystyle T(s)=(1-p)T+{\frac {p}{s}}T.} {\displaystyle T(s)=(1-p)T+{\frac {p}{s}}T.}

Amdahl's law gives the theoretical speedup in latency of the execution of the whole task at fixed workload W {\displaystyle W} W, which yields

    S latency ( s ) = T W T ( s ) W = T T ( s ) = 1 1 − p + p s . {\displaystyle S_{\text{latency}}(s)={\frac {TW}{T(s)W}}={\frac {T}{T(s)}}={\frac {1}{1-p+{\frac {p}{s}}}}.} {\displaystyle S_{\text{latency}}(s)={\frac {TW}{T(s)W}}={\frac {T}{T(s)}}={\frac {1}{1-p+{\frac {p}{s}}}}.}

### Parallel Programs

If 30% of the execution time may be the subject of a speedup, p will be 0.3; if the improvement makes the affected part twice as fast, s will be 2. Amdahl's law states that the overall speedup of applying the improvement will be:

    S latency = 1 1 − p + p s = 1 1 − 0.3 + 0.3 2 = 1.18. {\displaystyle S_{\text{latency}}={\frac {1}{1-p+{\frac {p}{s}}}}={\frac {1}{1-0.3+{\frac {0.3}{2}}}}=1.18.} {\displaystyle S_{\text{latency}}={\frac {1}{1-p+{\frac {p}{s}}}}={\frac {1}{1-0.3+{\frac {0.3}{2}}}}=1.18.}

For example, assume that we are given a serial task which is split into four consecutive parts, whose percentages of execution time are p1 = 0.11, p2 = 0.18, p3 = 0.23, and p4 = 0.48 respectively. Then we are told that the 1st part is not sped up, so s1 = 1, while the 2nd part is sped up 5 times, so s2 = 5, the 3rd part is sped up 20 times, so s3 = 20, and the 4th part is sped up 1.6 times, so s4 = 1.6. By using Amdahl's law, the overall speedup is

    S latency = 1 p 1 s 1 + p 2 s 2 + p 3 s 3 + p 4 s 4 = 1 0.11 1 + 0.18 5 + 0.23 20 + 0.48 1.6 = 2.19. {\displaystyle S_{\text{latency}}={\frac {1}{{\frac {p1}{s1}}+{\frac {p2}{s2}}+{\frac {p3}{s3}}+{\frac {p4}{s4}}}}={\frac {1}{{\frac {0.11}{1}}+{\frac {0.18}{5}}+{\frac {0.23}{20}}+{\frac {0.48}{1.6}}}}=2.19.} S_{\text{latency}}={\frac {1}{{\frac {p1}{s1}}+{\frac {p2}{s2}}+{\frac {p3}{s3}}+{\frac {p4}{s4}}}}={\frac {1}{{\frac {0.11}{1}}+{\frac {0.18}{5}}+{\frac {0.23}{20}}+{\frac {0.48}{1.6}}}}=2.19.

Notice how the 5 times and 20 times speedup on the 2nd and 3rd parts respectively don't have much effect on the overall speedup when the 4th part (48% of the execution time) is accelerated by only 1.6 times. 


## Relation to the law of Diminishing Returns

Amdahl's law is often conflated with the law of diminishing returns, whereas only a special case of applying Amdahl's law demonstrates law of diminishing returns. If one picks optimally (in terms of the achieved speedup) what to improve, then one will see monotonically decreasing improvements as one improves. If, however, one picks non-optimally, after improving a sub-optimal component and moving on to improve a more optimal component, one can see an increase in the return. Note that it is often rational to improve a system in an order that is "non-optimal" in this sense, given that some improvements are more difficult or require larger development time than others.

Amdahl's law does represent the law of diminishing returns if on considering what sort of return one gets by adding more processors to a machine, if one is running a fixed-size computation that will use all available processors to their capacity. Each new processor added to the system will add less usable power than the previous one. Each time one doubles the number of processors the speedup ratio will diminish, as the total throughput heads toward the limit of 1/(1 − p).

This analysis neglects other potential bottlenecks such as memory bandwidth and I/O bandwidth. If these resources do not scale with the number of processors, then merely adding processors provides even lower returns.

An implication of Amdahl's law is that to speedup real applications which have both serial and parallel portions, heterogeneous computing techniques are required.[4] For example, a CPU-GPU heterogeneous processor may provide higher performance and energy efficiency than a CPU-only or GPU-only processor.

