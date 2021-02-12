# Curse of dimensionality

The curse of dimensionality refers to various phenomena that arise when analyzing and organizing data in high-dimensional spaces that do not occur in low-dimensional settings such as the three-dimensional physical space of everyday experience.  The expression was coined by Richard E. Bellman when considering problems in dynamic programming.Dimensionally cursed phenomena occur in domains such as numerical analysis, sampling, combinatorics, machine learning, data mining and databases. The common theme of these problems is that when the dimensionality increases, the volume of the space increases so fast that the available data become sparse. This sparsity is problematic for any method that requires statistical significance. In order to obtain a statistically sound and reliable result, the amount of data needed to support the result often grows exponentially with the dimensionality. Also, organizing and searching data often relies on detecting areas where objects form groups with similar properties; in high dimensional data, however, all objects appear to be sparse and dissimilar in many ways, which prevents common data organization strategies from being efficient.

### Domains

Combinatorics

In some problems, each variable can take one of several discrete values, or the range of possible values is divided to give a finite number of possibilities. Taking the variables together, a huge number of combinations of values must be considered. This effect is also known as the combinatorial explosion. Even in the simplest case of d {\displaystyle d} d binary variables, the number of possible combinations already is 2 d {\displaystyle 2^{d}} 2^{d}, exponential in the dimensionality. Naively, each additional dimension doubles the effort needed to try all combinations.
Sampling

There is an exponential increase in volume associated with adding extra dimensions to a mathematical space. For example, 102=100 evenly spaced sample points suffice to sample a unit interval (a "1-dimensional cube") with no more than 10−2=0.01 distance between points; an equivalent sampling of a 10-dimensional unit hypercube with a lattice that has a spacing of 10−2=0.01 between adjacent points would require 1020=[(102)10] sample points. In general, with a spacing distance of 10−n the 10-dimensional hypercube appears to be a factor of 10n(10-1)=[(10n)10/(10n)] "larger" than the 1-dimensional hypercube, which is the unit interval. In the above example n=2: when using a sampling distance of 0.01 the 10-dimensional hypercube appears to be 1018 "larger" than the unit interval. This effect is a combination of the combinatorics problems above and the distance function problems explained below.
Optimization

When solving dynamic optimization problems by numerical backward induction, the objective function must be computed for each combination of values. This is a significant obstacle when the dimension of the "state variable" is large.[3]
Machine Learning

In machine learning problems that involve learning a "state-of-nature" from a finite number of data samples in a high-dimensional feature space with each feature having a range of possible values, typically an enormous amount of training data is required to ensure that there are several samples with each combination of values.

A typical rule of thumb is that there should be at least 5 training examples for each dimension in the representation.[4] In machine learning and insofar as predictive performance is concerned, the curse of dimensionality is used interchangeably with the peaking phenomenon,[4] which is also known as Hughes phenomenon.[5] This phenomenon states that with a fixed number of training samples, the average (expected) predictive power of a classifier or regressor first increases as the number of dimensions or features used is increased but beyond a certain dimensionality it starts deteriorating instead of improving steadily.[6][7][8]

Nevertheless, in the context of a simple classifier (linear discriminant analysis in the multivariate Gaussian model under the assumption of a common known covariance matrix) Zollanvari et al. [9] showed both analytically and empirically that as long as the relative cumulative efficacy of an additional feature set (with respect to features that are already part of the classifier) is greater (or less) than the size of this additional feature set, the expected error of the classifier constructed using these additional features will be less (or greater) than the expected error of the classifier constructed without them. In other words, both the size of additional features and their (relative) cumulative discriminatory effect are important in observing a decrease or increase in the average predictive power.

Nearest neighbor search

The effect complicates nearest neighbor search in high dimensional space. It is not possible to quickly reject candidates by using the difference in one coordinate as a lower bound for a distance based on all the dimensions.[12][13]

However, it has recently been observed that the mere number of dimensions does not necessarily result in difficulties,[14] since relevant additional dimensions can also increase the contrast. In addition, for the resulting ranking it remains useful to discern close and far neighbors. Irrelevant ("noise") dimensions, however, reduce the contrast in the manner described above. In time series analysis, where the data are inherently high-dimensional, distance functions also work reliably as long as the signal-to-noise ratio is high enough.[15]
k-nearest neighbor classification

Another effect of high dimensionality on distance functions concerns k-nearest neighbor (k-NN) graphs constructed from a data set using a distance function. As the dimension increases, the indegree distribution of the k-NN digraph becomes skewed with a peak on the right because of the emergence of a disproportionate number of hubs, that is, data-points that appear in many more k-NN lists of other data-points than the average. This phenomenon can have a considerable impact on various techniques for classification (including the k-NN classifier), semi-supervised learning, and clustering,[16] and it also affects information retrieval.

### Blessing of dimensionality

Surprisingly and despite the expected "curse of dimensionality" difficulties, common-sense heuristics based on the most straightforward methods "can yield results which are almost surely optimal" for high-dimensional problems.[18] The term "blessing of dimensionality" was introduced in the late 1990s.[18] Donoho in his "Millennium manifesto" clearly explained why the "blessing of dimensionality" will form a basis of future data mining.[19] The effects of the blessing of dimensionality were discovered in many applications and found their foundation in the concentration of measure phenomena.[20] One example of the blessing of dimensionality phenomenon is linear separability of a random point from a large finite random set with high probability even if this set is exponentially large: the number of elements in this random set can grow exponentially with dimension. Moreover, this linear functional can be selected in the form of the simplest linear Fisher discriminant. This separability theorem was proven for a wide class of probability distributions: general uniformly log-concave distributions, product distributions in a cube and many other families (reviewed recently in [20]).

"The blessing of dimensionality and the curse of dimensionality are two sides of the same coin."[21] For example, the typical property of essentially high-dimensional probability distributions in a high-dimensional space is: the squared distance of random points to a selected point is, with high probability, close to the average (or median) squared distance. This property significantly simplifies the expected geometry of data and indexing of high-dimensional data (blessing),[22] but, at the same time, it makes the similarity search in high dimensions difficult and even useless (curse).[23]

Zimek et al.[11] noted that while the typical formalizations of the curse of dimensionality affect i.i.d. data, having data that is separated in each attribute becomes easier even in high dimensions, and argued that the signal-to-noise ratio matters: data becomes easier with each attribute that adds signal, and harder with attributes that only add noise (irrelevant error) to the data. In particular for unsupervised data analysis this effect is known as swamping.



Read more: https://en.wikipedia.org/wiki/Curse_of_dimensionality

