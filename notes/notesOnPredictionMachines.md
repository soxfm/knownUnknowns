# Notes on 'Prediction Machines: The Simple Economics of Artificial Intelligence'

Economic approach to understanding impact of ML.

Better ML = cheaper predictions

    number of predictions
    engineering effort
    cost of mis-predictions => cost of automating decision-making

Economies of scale for first two.

Declining returns on scale for accuracy but maybe not declining returns on outcome.

    eg better than competitor
    eg crossing cost threshold for deployment

Current limitations:

    generalizing out of sample
    generalizing from limited data by analogy to other domain
    inferring causality / countering dependence between decision-making and data collection
        => controlled experiments

Break decision process into components.

    some tasks are replaceable by ML
    others still require humans (= complements)

Complements go up in value as ML tasks get cheaper - leverage.

    eg data capture, sensors
    eg physical automation

Judgment is a strong complement (ie objective / reward functions). Probably needs to stay in-house.

Job = collection of tasks, not monolithic. Grouping will shift but human tasks will remain.

High-level implications:

    may need to reengineer orgs to take advantage
    affects C-level strategy - can’t delegate to IT dept
    internal costs vs externalities

Possible models:

    ML predicts outcomes, human chooses preferred outcome
        eg maps offers several routes optimizing for different criteria
    ML acts in high-confidence regions, delegates to human in low-confidence regions
        will your human have experience / attention to handle? eg pilots vs autopilot

Risks:

    bias => liability
    black swan events
    adversarial inputs
    interrogation

Misc:

    99.8 -> 99.9 accuracy is half number of mistakes