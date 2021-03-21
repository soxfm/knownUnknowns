# Gustafson's law
## Overview
---

In computer architecture, Gustafson's law (or Gustafson–Barsis's law) gives the theoretical speedup in latency of the execution of a task at fixed execution time that can be expected of a system whose resources are improved. It is named after computer scientist John L. Gustafson and his colleague Edwin H. Barsis, and was presented in the article Reevaluating Amdahl's Law in 1988.

### Application

Application in research

Amdahl's law presupposes that the computing requirements will stay the same, given increased processing power. In other words, an analysis of the same data will take less time given more computing power.

Gustafson, on the other hand, argues that more computing power will cause the data to be more carefully and fully analyzed: pixel by pixel or unit by unit, rather than on a larger scale. Where it would not have been possible or practical to simulate the impact of nuclear detonation on every building, car, and their contents (including furniture, structure strength, etc.) because such a calculation would have taken more time than was available to provide an answer, the increase in computing power will prompt researchers to add more data to more fully simulate more variables, giving a more accurate result.
Application in everyday computer systems

Amdahl's Law reveals a limitation in, for example, the ability of multiple cores to reduce the time it takes for a computer to boot to its operating system and be ready for use. Assuming the boot process was mostly parallel, quadrupling computing power on a system that took one minute to load might reduce the boot time to just over fifteen seconds. But greater and greater parallelization would eventually fail to make bootup go any faster, if any part of the boot process were inherently sequential.

Gustafson's law argues that a fourfold increase in computing power would instead lead to a similar increase in expectations of what the system will be capable of. If the one-minute load time is acceptable to most users, then that is a starting point from which to increase the features and functions of the system. The time taken to boot to the operating system will be the same, i.e. one minute, but the new system would include more graphical or user-friendly features.

### Limitations

Some problems do not have fundamentally larger datasets. As an example, processing one data point per world citizen gets larger at only a few percent per year. The principal point of Gustafson's law is that such problems are not likely to be the most fruitful applications of parallelism.

Algorithms with nonlinear runtimes may find it hard to take advantage of parallelism "exposed" by Gustafson's law. Snyder[3] points out an O(N3) algorithm means that double the concurrency gives only about a 26% increase in problem size. Thus, while it may be possible to occupy vast concurrency, doing so may bring little advantage over the original, less concurrent solution—however in practice there have still been considerable improvements.

Hill and Marty[4] emphasize also that methods of speeding sequential execution are still needed, even for multicore machines. They point out that locally inefficient methods can be globally efficient when they reduce the sequential phase. Furthermore, Woo and Lee[5] studied the implication of energy and power on future many-core processors based on Amdahl's law, showing that an asymmetric many-core processor can achieve the best possible energy efficiency by activating an optimal number of cores given the amount of parallelism is known prior to execution. 

