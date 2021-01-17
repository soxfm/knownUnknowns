# Bayesian Machine Learning
---

## Overview

- Bayesian statistics is a branch of statistics where quantities of interest (such as parameters fo a statistical model) are treatead as random variablers, and one draws conclusions by analyzing the posterior distribution over these quantities given the observed data. 
- While the core ideas are decades old, Bayesian ideas have had a big impact upon machine learning due to their flexibility in providing the necessary framework for building structured models of real world problems. 

### Core Topics
---
#### Central Topics
> What is Bayesian machine learning? Generally, Bayesian methods are trying to solve one of the following problems:

- parameter estimation. Suppose you have a statistical model of some domain, and you want to use it to make predictions. Or maybe you think the parameters of the model are meaningful, and you want to fit them in order to learn something about the world. The Bayesian approach is to compute or approximate the posterior distribution over the parameters given the observed data.

    Often, you want to use the model to choose actions. Bayesian decision theory is a framework for doing this.
- model comparison: You may have several different models under consideration, and you want to know which is the best match to your data. A common case is that you have several models of the same form of differing complexities, and you want to trade off the complexity with the degree of fit.

    Rather than choosing a single model, you can define a prior over the models themselves, and average the predictions with respect to the posterior over models. This is known as Bayesian model averaging.

#### Non-Bayesian Techniques

- As background, it's useful to understand how to fit generative models in a non-Bayesian way. One reason is that these techniques can be considerably simpler to implement, and often they're good enough for your goals. Also, the Bayesian techniques bear close similarities to these, so they're often helpful analogues for reasoning about Bayesian techniques.

- Most basically, you should understand the notion of generalization, or how well a machine learning algorithm performs on data it hasn't seen before. This is fundamental to evaluating any sort of machine learning algorithm. You should also understand the following techniques:
  + Maximum likelihood: a criterion for fitting the parameters of a generative model
  + regulation: a method for preventing overfitting
  + EM algo: an algorithm for fitting generative models where each data point has associated latent ( or unobserved ) variables.

#### Basic Inference Algorithms

In general, Bayesian inference requires answering questions about the posterior distribution over a model's parameters (and possibly latent variables) given the observed data. For some simple models, these questions can be answered analytically. However, most of the time, there is no analytic solution, and we need to compute the answers approximately.

- If you need to implement your own Bayesian inference algorithm, the following are probably the simplest options:
  - MAP estimation, where you approximate the posterior with a point estimate on the optimal parameters. This replaces an integration problem with an optimization problem. This doesn't mean the problem is easy, since the optimization problem is often itself intractable. However, it often simplifies things, because software packages for optimization tend to be more general and robust than software packages for sampling.
  - Gibbs sampling, an iterative procedure where each random variable is sampled from its conditional distribution given the remaining ones. The result is (hopefully) an approximate sample from the posterior distribution.

You should also understand the following general classes of techniques, which include the majority of the Bayesian inference algorithms used in practice. Their general formulations are too generic to be relied on most of the time, but there are a lot of special cases which are very powerful:
- Markov chain Monte Carlo, a general class of sampling-based algorithms based on running Markov chains over the parameters whose stationary distribution is the posterior distribution.
- In particular, Metropolis-Hastings (M-H) is a recipe for constructing valid MCMC chains. Most practical MCMC algorithms, including Gibbs sampling, are special cases of M-H.
- Variational inference, a class of techniques which try to approximate the intractable posterior distribution with a tractable distribution. Generally, the parameters of the tractable approximation are chosen to minimize some measure of its distance from the true posterior. 

#### Models

The following are some simple examples of generative models to which Bayesian techniques are often applied.

    mixture of Gaussians, a model where each data point belongs to one of several "clusters," or groups, and the data points within each cluster are Gaussian distributed. Fitting this model often lets you infer a meaningful grouping of the data points.
    factor analysis, a model where each data point is approximated as a linear function of a lower dimensional representation. The idea is that each dimension of the latent space corresponds to a meaningful factor, or dimension of variation, in the data.
    hidden Markov models, a model for time series data, where there is a latent discrete state which evolves over time.

While Bayesian techniques are most closely associated with generative models, it's also possible to apply them in a discriminative setting, where we try to directly model the conditional distribution of the targets given the observations. The canonical example of this is Bayesian linear regression.

##### Bayesian model comparisson

The section on inference algorithms gave you tools for approximating posterior inference. What about model comparison? Unfortunately, most of the algorithms are fairly involved, and you probably don't want to implement them yourself until you're comfortable with the advanced inference algorithms described below. However, there are two fairly crude approximations which are simple to implement:

    the Bayesian information criterion (BIC), which simply takes the value of the MAP solution and adds a penalty proportional to the number of parameters
    the Laplace approximation, which approximates the posterior distribution with a Gaussian centered around the MAP estimate.


- MetaAcademy : (Further Notes)[https://metacademy.org/roadmaps/rgrosse/bayesian_machine_learning]


