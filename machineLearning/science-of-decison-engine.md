# The science of the Decision Engine

Authored by Carl Edward Rasmussen (SecondMind)[https://www.secondmind.ai/insights/the-science-of-the-decision-engine/]

- Machine learning (ML) and artificial intelligence (AI) have been deployed in an extreme variety of areas, including for example image analysis, navigation systems, medical diagnostics and game playing among, many others. Despite the apparent diversity, a closer inspection reveals that the only way in which machine learning and AI contribute is by decision-making (either directly or indirectly). For example, a navigation system must suggest route(s), a diagnostic system has to present hypotheses and next steps, and a game player must decide on moves. If our ML and AI efforts don’t influence the actions we take, then we may as well not bother.
- We’re talking about decision-making in the broadest possible sense: making a single choice, ranking many alternatives, understanding the reasons underlying a decision, evaluating the possible consequences of decisions and so on. All these aspects are crucial if decisions are to be rational, understandable and trustworthy.

One may think that the design of a decision-making system would be highly dependent on the domain of application. But that is not the case. A crucial ingredient in the advancement of science is the notion of abstraction. For example, you don’t need to know everything about a planet to predict its trajectory. Knowing its mass and velocity are enough, the chemical composition, the surface temperature etc turn out to be irrelevant. Mass and velocity turn out to be exactly the right abstraction for planetary dynamics.

In 1833 Charles Babbage started working on the blueprint for a revolutionary idea, the Analytical Engine, the first instance of a general purpose computer. This idea was truly staggering, because it separated computation from the application area. It abstracted the notion of computation. Alan Turing much later in 1936 formalised this notion in the Turing Machine, a universal abstraction of computation. We are so familiar with these ideas of abstraction for computing today, that it is even difficult to contemplate anything else. Obviously a computer or smartphone is expected to be able to handle images, text, gestures, wifi, 5g, etc.

This is why we call our cloud software platform the Secondmind Decision Engine.

The Secondmind Decision Engine is built on the abstraction suitable for practical decision-making and contains the tools necessary. The universal ingredients are:

    an objective
    a list of possible actions
    knowledge

The objective is a quantitative specification of what we are trying to achieve. This could be quantifying a profit, or a resource use - typically some sort of aggregate measure that characterises the problem as a whole.

The action space is just a list of the possible courses of action which may be taken. This could be a simple buy/sell decision, or a much more complicated execution plan involving multiple system components. The actions are the only way in which the decision system can impact the world.

Finally, we need knowledge. Knowledge typically comes in two forms, explicit knowledge and data. Explicit knowledge may take the form of known physical properties of the system, approximate observed trends, expert experience or practitioner hunches. Data comes in the form of observations of key quantities, or proxies related to them, measured under conditions not too dissimilar to those prevalent at decision time. Models are quantitative mathematical tools which fuse explicit knowledge with data, and enable predictions about probable consequences of taking different actions.

It should be clear that it isn’t possible to formulate a meaningful 'decision problem' without all three ingredients above. The beauty of the framework of Bayesian decision-making under uncertainty is that these three ingredients are all we need. The formalism will be able to tell good decisions from bad, in the light of your available knowledge, as judged by your stated objectives. Irrespective of whether your domain is financial transactions, logistics planning or process control.

The core of the problem can be divided into two parts: inference and action selection.

Inference combines your knowledge about the domain with assumptions and experience in terms of data into a model. The model contains all the information we have about the problem at hand. Even so, there are typically aspects which we are not completely certain about. For example, a diagnosis system may not have seen many examples of patients with both hypertension and hepatitis. Since good decisions depend on the confidence of our knowledge, it is crucial that the model is able to faithfully represent levels of confidence. Probabilistic models are a principled mathematical framework which can naturally represent confidence.

In action selection, you use the predictions from your probabilistic model to evaluate the range of possible consequences of actions, in order to find the best action, rank actions, or understand the consequences of actions etc. This step may be complex because for each action, one has to take into account all of the possible consequences which are possible according to the model (weighted by their probability of occurring).

Many of the recent advances in machine learning and AI have been focused on the inference step, mainly on how to handle large and complex data sources. But a useful system will always comprise both inference and action selection. Systems building on these central pillars have many names such as Bayesian decision-making, decision-making under uncertainty, Bayesian optimization and reinforcement learning. But at a fundamental level, they all build on a single set of principles.

The Secondmind Decision Engine helps people to specify objectives and possible actions together with assumptions, expert knowledge and observed data about the phenomenon of interest. It uses inference to allow prediction of consequences of actions and computes the actions which are most likely to maximize your stated objectives.

Our goal is to empower people to address their decision problems within a principled system, providing a framework for them to make decisions in a systematic way. An intuitive end-to-end experience to do all the necessary algorithmic heavy lifting, while uniting the complementary strengths of both people and AI.