----
title: main path analysis
slugs: mpa
category: [ 'mathematics', 'systems', 'methods' ]
date: 2020-1-10
----

# Main Path Analysis

Main path analysis is a mathematical tool, first proposed by Hummon and Doreian in 1989, to identify the major paths in a citation network, which is one form of a directed acyclic graph (DAG). The method begins by measuring the significance of all the links in a citation network through the concept of ‘traversal count’ and then sequentially chains the most significant links into a "main path", which is deemed the most significant historical path in the target citation network. The method is applicable to any human activity that can be organized in the form of a citation network. The method is commonly applied to trace the knowledge flow paths or development trajectories of a science or technology field, through bibliographic citations or patent citations
It has also been applied to judicial decisions to trace the evolving changes of legal opinions.
Main path analysis has attracted scholars attention recently. Academic research related to main path analysis saw a fast growing since 2007. A list of academic articles that introduce, explain, apply, modify, or extend the method originated in Hummon and Doreian

## The Method

Main path analysis operates in two steps. The first step obtains the traversal counts of each link in a citation network. Several types of traversal counts are mentioned in the literature. The second step searches for the main paths by linking the significant links according to the size of traversal counts. One needs to prepare a citation network before proceeding for main path analysis. 

#### Preparing a Citation Network

It is necessary to prepare a citation network before starting main path analysis. In a citation network, the nodes represent the documents such as academic articles, patents, or legal cases. These nodes are connected using citation information. Citation networks are by nature directed because the two nodes on the opposite end of a link are not symmetrical in their roles. As regards to the direction, this article adopts the convention that the cited node points to the citing node, signifying the fact that knowledge in the cited node flows to the citing node. Citation network is also by nature acyclic, which means that a node can never chain back to itself if one moves along the links following their direction.

Several terms related to a citation network are defined here before proceeding further. Heads are the nodes the direction arrow leads to. Tails are the nodes on other ends of the direction arrow. Sources are the nodes that are cited but cite no others. Sinks cite other nodes but are not cited. Ancestors are the nodes that can be traced back to from a target node. Descendants are the nodes that one can reach from a target if one moves along the links following their direction. 


### Application

The method has been applied to three types of documenting system that maintain the tradition of making references to the previous documents. They are the academic article, patent, and judicial documenting system. 

### Software Implementation

Main path analysis is implemented in Pajek, a widely used social network analysis software written by Vladimir Batagelj and Andrej Mrvar of University of Ljubljana, Slovenia. To run main path analysis in Pajek, one needs to first prepare a citation network and have Pajek reads in the network. Next, in the Pajek main menu, computes the traversal counts of all links in the network applying one of the following command sequences (depending on the choice of traversal counts).

Network → Acyclic Network → Create Weighted Network + Vector → Traversal Weights → Search Path Link Count (SPC), or

Network → Acyclic Network → Create Weighted Network + Vector → Traversal Weights → Search Path Link Count (SPLC), or

Network → Acyclic Network → Create Weighted Network + Vector → Traversal Weights → Search Path Node Pairs (SPNP)

After traversal counts are computed, the following command sequences find the main paths.

For local main paths

Network → Acyclic Network → Create (Sub)Network → Main Paths → Local Search → Forward

For global main paths

Network → Acyclic Network → Create (Sub)Network → Main Paths → Global Search → Standard

For local key-route main paths

Network → Acyclic Network → Create (Sub)Network → Main Paths → Local Search → Key-Route

For global key-route main paths

Network → Acyclic Network → Create (Sub)Network → Main Paths → Global Search → Key-Route

In addition to key-route search, a more flexible search feature is added starting from Pajek version 5.03 (January 4, 2018). The new feature allows for local and global search passing through vertices defined by a cluster. The command sequences are as follows:

Network → Acyclic Network → Create (Sub)Network → Main Paths → Local Search → Key-Route → Through Vertices in Cluster

Network → Acyclic Network → Create (Sub)Network → Main Paths → Global Search → Key-Route → Through Vertices in Cluster 