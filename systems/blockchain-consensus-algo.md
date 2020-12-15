	# BLOCKCHAIN CONSEUS ALGORITHM

	### Byzantine General's Problem
	The Byzantine army encircles a city intended for capture. The area around the city is large and so the army is organized into small camps which are each governed by a General. The Generals communicate via messengers who run between the camps. The army is trying to choose between two courses of action, attack or retreat. So long as the army acts in unison the outcome of either action will be successful. Problematically, there are Generals who are bad actors and messengers who cannot be trusted to communicate accurately. If success is determined by the camps performing the same action, how do you ensure unanimous participation?
	
	A few options immediately spring to mind — economically incentivize voting for the majority action or punish actors who vote against the majority action. What other ideas can you think of?
	
	The Byzantine General’s Problem describes a complex security issue faced by distributed systems that seek to make unanimous decisions in a broad network of individual actors that cannot be trusted. In a distributed system like the Bitcoin network, the network’s imperative is not to defeat an army, but to maintain an accurate ledger of transactions. Blockchain systems are governed by a set of rules that determine whether a course of action can be proceeded with, more specifically, whether the next block of data can be added to the chain. The rule in the bitcoin network is as follows: if a majority (51%) of network participants agree on the accuracy of a block then consensus is achieved, and the block is added to the chain.
	
	The most notable consensus mechanism is Proof of Work (PoW) which is the incumbent algorithm used to secure the Bitcoin and Ethereum networks.

** PoW: Proof of Work**
Proof of Work (PoW) is the most well-known and thoroughly tested of the consensus protocols and is the consensus algorithm used to secure the bitcoin network. In PoW systems, all participating network nodes, known as miners, expend time (on average 10 mins per block on the Bitcoin network) and computing power (that is expensive to produce) in competition to solve a cryptographic puzzle. The miner that solves the puzzle first, presents the next block to the network for verification and if successful, earns a reward as compensation. Interestingly, the verification process is extremely simple whilst the puzzle-solving process used to select the miner eligible to present the next block is highly taxing (by design). In a PoW system, the probability of mining a block is directly proportional to the quantity of computational power contributed by a miner. Because miners have contributed CapEx (mining rig) and OpEx (electricity and real estate costs) into validating transaction blocks, we can trust them to broadcast the truth: A miner can only be successful in earning a reward if he allocates his resources to mining the correct chain and presenting the correct block to the network, therefore he is economically incentivized to broadcast the truth. Indeed, there is a financial disincentive to mining a malicious fork of the main chain because it would simply be a wasted resource.
A common criticism of PoW consensus is that it is inefficient and costly. The computational energy spent by miners in competition to solve a cryptographic puzzle every time a new block is validated, adds no intrinsic value to the network (beyond selecting which miner will validate the next block) and has no positive externalities. Indeed, that is largely the point, forcing the expenditure of a costly resource for the sake of creating a deterrent against voting for a malicious fork. PoW systems also favor large mining companies whose economy of scale benefits and cheaper electricity costs prevent smaller participants from competing effectively. As a result, the Bitcoin network has become highly centralized with more than 2/3rds of the worlds mining power emerging from China, and a significant portion of the total hashing power in the hands of a few large companies. Centralization increases the risk of a failure in the bitcoin network, if a few large mining companies collude to achieve 51% of the networks hashing power then they could potentially rewrite the history of the Bitcoin ledger as they see fit.
This is a simplification of the PoW model and there is an incredible amount to learn from the PoW consensus mechanism that has propelled the bitcoin network to where it is today. However, because of the points discussed above (and others), some members of the blockchain community have explored alternative consensus mechanisms to PoW, most notably, Proof of Stake (PoS).

** Proof of Stake **:

Proof of Stake (PoS) emerged as a potential solution to the efficiency, security and scaling issues persistent in the Bitcoin and Ethereum PoW-based models. PoS proposes that the resource used to determine the validator of a block should be the blockchain’s native cryptocurrency rather than computational power like in the bitcoin network. Simplistically, the idea is that if an individual possesses native coins in a chain (a stake in the network), they have an interest in maintaining the accuracy of the ledger and we can trust them to broadcast the truth. The validator of a new block is chosen deterministically based on the quantity of coins/tickets held by a participant (this will be explored later). A block reward and transaction fees are awarded to the validator of a block.
There are certainly appealing properties of PoS systems when compared with PoW:
Energy efficient — no highly energy taxing competition to solve cryptographic puzzles to determine validators.
No technology arms race or mining pools that risk 51% attack.
No requirement to have expensive hardware. Staking nodes can be run on consumer grade software or a cheap VPS.
Reduced risk of 51% attack — Obtaining more than 51% of the network requires immense capital (controlling 51% of the circulating token supply).
Possible Scaling benefits
Greater decentralization
Equality in Consensus Algorithms
A routine criticism levelled against PoS systems is that it creates a scenario of inequality where the rich get richer. Consider that a validator is chosen proportionally based on the number of coins/tickets he possesses, more tokens, means more validations, means more block rewards, you get the idea. This argument is fallacious because it doesn’t address the inequity of the incumbent PoW system. In fact, one could argue that PoW mining is less egalitarian given the economies of scale, location-based energy price benefits and other factors that favour large mining companies. The cost of 1 unit of energy for an individual miner is more than the cost of 1 unit of energy for a large mining company, whereas is a PoS system 1 coin = 1 coin regardless of other factors.
In July 2019, there are more than 30+ Consensus algorithms that have been designed to validate transactions on a blockchain. PoW and PoS engines are still the most prevalent.
Now that you understand a little bit about consensus algorithms, let’s move on to Part 2 of the ‘How to set up a Fusion Node guide’ where we explore Fusion’s unique approach to Proof of Stake.