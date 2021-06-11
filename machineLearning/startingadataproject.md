# Starting a Data Project

# What you will learn
In this guide, you'll learn to prepare yourself to start the project.

This will consist of learning how to look for sources that can help you solve the problem, building the project structure, building good documentation, securing your code and our data and others!

We'll make heavy use of a collection of awesome best practices from the [PLOS | Public Library of Science](https://www.plos.org/).
# Philosophy of Mathematics

I do have a few issues with the Zalamea book: mainly, as a reader, pinning down what a lot of the sentences really mean can be hard. This might be a combination perfectly reasonable things: the fact that it’s doing philosophy  – and it’s not analytic philosophy, which aspires to math-like rigour. (Indeed, one of the many ideas the book throws around is that of “synthetic philosophy”, modelled not after formal logic, but sheaf theory, with many local points of view and ways of relating them in areas where they overlap. Intuitively appealing, though it’s hard to see how to make it rigorous in the same way.)

So, many of the ideas are still formative, and the terms used to describe them are sometimes new coinages. Then, too, the combination of philosophical jargon and the fact that it’s translated from Spanish probably contribute. So I give the author the benefit of the doubt on this point and interpret the best I can. Even so, it’s still difficult for me to say exactly what some of it is saying. In any case, here I wanted to break down my understanding of some themes it is pointing out. There is more there than I have space to deal with here, but these are some major ones.

I had a somewhat similar response to David Corfield’s book, “Toward a Philosophy of Real Mathematics” (which Zalamea mentions in a chapter where he acknowledges some authors who have engaged the kind of issues he’s interested in). That is, both of them do well at pointing out topics which haven’t received much attention, but the main strength is by pointing out areas of actual mathematical activity, and describing what they’re like (for example, Corfield’s chapter on higher category theory, and Zalamea’s account of Grothendieck’s work). They both feel sort of preliminary, though, in that they’re pointing out areas where a lot more people need to study, argue, and generally thrash out various positions on the issues before (at least as far as I can see) one could hope to say the issues raised have actually been dealt with.

Themes

In any case, part of the point is that for a philosophical take on what mathematicians are actually studying, we need to look at some details. In the previous post I outlined the summary (from philosopher Albert Lautman) of the themes of “Elementary” and “Classical” mathematics. Lautman introduced five themes apropos to the “Modern” period – characterizing what was new compared to the “Classical” (say, pre-1900 or so). Zalamea’s claim, which seems correct to me, is that all of these themes are still present today, but some new ones have been added.

That is, mathematics is cumulative: all the qualities from previous periods stay important, but as it develops, new aspects of mathematics become visible. Thus, Lautman had five points, which are somewhat detailed, but the stand-out points to my mind include:

The existence of a great many different axiomatic systems and theories, which are not reducible to each other, but are related in various ways . Think of the profusion of different algebraic gadgets, such as groups, rings, quandles, magmas, and so on, each of which has its own particular flavour. Whereas Classical mathematics did a lot with, say, the real number system, the Modern period not only invented a bunch of other number systems and algebras, but also a range of different axiom systems for describing different generalizations. The same could be said in analysis: the work on the Calculus in the Classical period leads into the definition of a metric space and then a topological space in the Modern period, and an increasing profusion of specific classes of them with different properties (think of all the various separation axioms, for example, and the web of implications relating them).

The study of a rich class of examples of different axiomatic systems. Here the standout example to me is the classification of the finite groups, where the “semantics” of the classification is much more complex than the “syntax” of the theory. This reminds me of the game of Go (a.k.a. Wei Chi in China, or Baduk in Korea), which has gained some recent fame because of the famous AlphaGo victories. The analogy: that the rules of the game are very simple, but the actual practice of play is very difficult to master, and the variety of examples of games is huge. This is, essentially, because of a combinatorial explosion, and somewhat the same principle is at work in mathematics: the theory of groups has, essentially, just three axioms on one set with three structures (the unit, the inverse, and the multiplication – a 0-ary, unary, and binary operation respectively), so the theory is quite simple. Yet the classification of all the examples is complicated and full of lots of exceptions (like the sporadic simple groups), to the point that it was only finished in Contemporary times. Similar things could be said about topological spaces.

A unity of methods beyond apparent variety. An example cited being the connection between the Galois group of field extensions and the group of deck transformations of a certain kind of branched cover of spaces. In either case, the idea is to study a mathematical object by way of its group of automorphisms over some fixed base object – and in particular to classify intermediate objects by way of the subgroups of this big group. Here, the “base object” could refer to either a sub-field (which is a sub-object in the category of fields) or a base space for the cover (which is not – it’s a quotient, or more generically the target of a projection morphism). These are conceptually different kinds of things on the face of it, but the mechanism of studying “homomorphisms over” them is similar. In fact, following through the comparison reveals a unification, by considering the fields of functions on the spaces: a covering space then has a function field which is an extension of the base case, and the two apparently different situations turn out to correspond exactly.

A “dialectical movement that is a back-and-forth between the One and the Many”. This is one of those jargon-sounding terms (especially the Hegelian-sounding term “dialectic”) and is a bit abstract. The examples given include:

    The way multiple variants on some idea are thought up, which in turn get unified into a more general theory, which in turn spawns its own variants, and so on. So, as people study different axiom systems for set theory, and their models, this diversity gets unified into the study of the general principles of how such systems all fit together. That is, as “meta-mathematics”, which considers which models satisfy a given theorem, which axioms are required to prove it, etc.
    The way branches of mathematics (algebra, geometry, analysis, etc.) diverge and develop their own distinct characters, only to be re-unified by mixing them together in new subjects: algebraic geometry, analytic number theory, geometric analysis, etc. intil they again seem like parts of a big interrelated whole. Beyond these obvious cases, the supposedly different sub-disciplines develop distinctive ideas, tools, and methods, but then borrow them from each other as fast as they specialize. This back-and-forth between specialization and cross-fertilization is thus an example of “dialectic”.

Zalamea suggests that in the Contemporary period, all these themes are still present, but that some new ones have become important as well:

“Structural Impurity of Arithmetic” – this is related to subjects outside my range of experience, like the Weil Conjectures and the Langlands Program, so I don’t have much to say about it, except to note that, by way of arithmetic functions like zeta functions, they relate number theory to algebraic curves and geometry, and constitute a huge research program that came into being in the Contemporary period (specifically the late 1960’s and early 1970’s). (Edward Frenkel described the Langlands program as “a kind of grand unified theory of mathematics” for this among other reasons.)

Geometrization of Mathematics – essentially, the migration of tools and methods originally developed for like the way topos theory turns logic into a kind of geometry in which the topology of a space provides the algebra of possible truth values. This feeds into the pervasive use of sheaves in modern mathematics, etc. Or, again, the whole field of noncommutative geometry, geometric ideas about space are interpreted as  (necessarily commutative) algebra of functions on that space with pointwise multiplication: differential operators like the Lagrangian, for instance, capture metric geometry, while bundles over a space have an interpretation in terms of modules over the algebra. These geometric concepts can be applied to noncommutative algebras A, thus treating them as if they were spaces.

“Schematization”, and becoming detached from foundations: in particular, the idea that what it means to study, for instance, “groups” is best understood in terms of the properties of the category of groups, and that an equivalent category, where the objects have some different construction, is just as good. You see this especially in the world of n-categories: there are many different definitions for the entities being studied, and there’s increasingly an attitude that we don’t really need to make a specific choice. The “homotopy hypotesis” for \infty-groupoids is an example of this: as long as these form a model of homotopy types, and their collectivity is a “homotopy theory” (with weak equivalences, fibrations, etc.) that’s homotopy-equivalent to the corresponding structure you get from another definition, they are in some sense “the same” idea. The subject of Univalent Foundations makes this very explicit.

“Fluxion and Deformation” of the boundaries of some previously fixed subject. “Fluxion” is one of those bits of jargon-sounding words which is suggestive, but I’m not entirely clear if it has a precise measing. This gets at the whole area of deformation theory, quantization (in all its various guises), and so on. That is, what’s happening here is that previously-understood structures which seemed to be discrete come to be understood as points on a continuum. Thus, for instance, we have q-deformation: this starts a bit earlier than the Contemporary period, with the q-integers, which are really power series in a variable q, which just amount to the integers they’re deformations of when q has the value 1. It really takes off later with the whole area of q-deformations of algebra – in which such power series take on the role of the base ring.  Both of these have been studied by people interested in quantum physics, where the parameter q, or the commutators in A are pegged to the Planck constant \hbar.

There’s also reflexivity of modern mathematics, theories applied to themselves. This is another one of those cases where it’s less clear to me what the term is meant to suggest (though examples given include fixed point theorems and classification theorems.)

There’s a list near the beginning of notable mathematicians who illustrate

Zalamea synthesizes these into three big trends described with newly coined terms: “eidal“, “quiddital“, and “archaeal” mathematics. He recognizes these are just convenient rules of thumb for characterizing broad aspects of contemporary research, rather than rigorously definable ideas or subfields. This is a part of the book which I find more opaque than the rest – but essentially the distinction seems to be as follows.

Roughly, eidal mathematics (from the Greek eidos or “idea”) seems to describe the kind that involves moving toward the abstract, and linking apparently unrelated fields of study. One big example referenced here is the Langlands program, which is a bunch of conjectures connecting number theory to geometry. Also under this umbrella he references category theory, especially via Lawvere, which subsumes many different fields into a common framework – each being the study of some particular category such as Top, perhaps by relating it to some other category (such as, in algebraic topology, Grp).

The new term quiddital mathematics (from Latin quidditas, “what exists” or literally “whatness”) appears to refer to the sort which is intimately connected to physics. The way ideas that originate in physics have driven mathematics isn’t totally new: Calculus is a classical example. But more recently, the study of operator algebras was driven by quantum mechanics, index theory which links differential operators and topology was driven by quantum field theory, and there’s a whole plethora of mathematics that has grown out of String Theory, CFT, TQFT, and so forth – which may or may not turn out to be real physics, but were certainly inspired by theorizing about it. And, while it hasn’t had as deep an effect on pure mathematics, as far as I know, I imagine this category would include those areas of study that arose out of other applied studies, such as the theory of networks or the dynamics of large complex systems.

The third new coinage, archaeal mathematics (from arche, or “origin”, also giving the word “archetype”) is another one whose meaning is harder for me to pin down, because the explanation is quite abstract. In the structure of the explanation, this seems to be playing a role that mediates between the first two: something that mediates moving between very abstract notions and concrete realizations of them. One essential idea here is the finding of “invariants”, though what this really seems to mean is more like finding a universal structure of a given type. A simple case might be that between the axioms of groups, and particular examples that show up in practice, we might have various free groups – they’re concrete but pure examples of the theory, and other examples come from imposing more relations on them.

I’m not entirely sure about these three categories, but I do think there’s a good point here. This is that there’s a move away from the specifics and toward general principles. The huge repertoire of “contemparary” mathematics can be sort of overwhelming, and highly detailed. The five themes listed by Lautman, or Zalamea’s additional five, are an attempt to find trends, or deal descriptively with that repertoire. But it’s still, in some ways, a taxonomy: a list of features. Reducing the scheme to these three, whether this particular system makes sense to you or not, is more philosophical: rather than giving a taxonomy, it’s an effort to find underlying reasons why these themes and not others are generating the mathematics we’re doing.  So, while I’m not completely convinced about this system as an account of what contemporary mathematics is about, I do find that thinking about this question sheds light on the mass of current math.

Some Thoughts

In particular, a question that I wonder about, which a project like this might help answer, is the question of whether the mathematics we’re studying today is inevitable. If, as the historical account suggests, mathematics is a time-bound process, we might well ask whether it could have gone differently. Would we expect, say, extraterrestrials, or artificial intelligences, or even human beings in isolated cultures, to discover essentially the same things as ourselves? That is, to what extent is the mathematics we’ve got culturally dependent, and

In Part I, I made an analogy between mathematics and biology, which was mainly meant to suggest why a philosophy of mathematics that goes beyond foundational questions – like the ontology of what mathematical objects are, and the logic of how proof works – is important. That is to say, mathematical questions themselves are worth studying, to see their structure, what kinds of issues they are asking about (as distinct from issues they raise by their mere existence), and so on. The analogy with biology had another face: namely, that what you discover when you ask about the substance of what mathematics looks at is that it evolves over time – in particular, that it’s cumulative. The division of mathematical practice into periods that Zalamea describes in the book (culminating in “Contemporary” mathematics, the current areas of interest) may be arbitrary, but it conveys this progression.

This biological analogy is not in the book, though I doubt it’s original to me. However, it is one that occurs to me when considering the very historically-grounded argument that is there. It’s reminiscent, to my mind, of the question of whether mathematics is “invented or discovered”. We could equally well ask whether evolution “invents” or “discovers” its products. That is, one way of talking about evolution pictures the forms of living things as pre-existing possibilities in some “fitness landscape”, and the historical process of evolving amounts to a walk across the landscape, finding local optima. Increases in the “height” of the fitness function lead, more or less by definition, to higher rates of reproduction, and therefore get reinforced, and so we end up in particular regions of the landscape.

This is a contentious – or at least very simplified – picture, since some would deny that the space of all possibilities could be specified in advance (for example, Lee Smolin and Stuart Kauffman have argued for this view.) But suppose for the moment it’s the case and let’s complete the analogy: we could imagine mathematics, similarly, as a pre-existing space of possibilities, which is explored over time. What corresponds to the “fitness” function is, presumably, whatever it is about a piece of mathematics that makes it interesting or uninteresting, and ensures that people continue to develop it.

I don’t want to get too hung up on this analogy. One of the large-scale features Zalamea finds in contemporary mathematics is precisely one that makes it different from evolution in biology. Namely, while there is a tendency to diversification (the way evolution leads to speciation and an increase in the diversity of species over time), there is also a tendency for ideas in one area of mathematics to find application in another – as if living things had a tendency to observe each other and copy each others’ innovations. Evolution doesn’t work that way, and the reason why not has to do with specifics of exactly how living things evolve: sexual reproduction, and the fact that most organisms no longer transfer genes horizontally across species, but only vertically across generations. The pattern Zalamea points out suggests that, whatever method mathematicians are using to explore the landscape of possible mathematics, it has some very different features. One of which seems to be that it rewards results or concepts in one sub-discipline for which it’s easy to find analogies and apply them into many different areas. This tendency works against what might otherwise be a trend toward rampant diversification.

Still, given this historical outlook, one high-level question would be to try to describe what features make a piece of mathematics more rewarding and encourage its development. We would then expect that over time, the theorems and frameworks that get developed will have more of those properties. This would be for reasons that aren’t so much intrinsic to the nature of mathematics as for historical reasons. Then again, if we had a satisfactory high-level account of what current mathematics is about – something like what the three-way division into eidal, quiddital, and archaeal mathematics is aiming at – that would give us a way to ask whether only certain themes, and only certain subjects and theorems, could really succeed.

I’m not sure how much this gains us within mathematics, but it might tell us how we ought to regard the mathematics we have.


November 21, 2017
Thoughts on Philosophy of Contemporary Mathematics – I
Posted by Jeffrey Morton under Uncategorized
Leave a Comment

This post – which I’ve split up into parts – is a bit of a departure from talking about the subject matter of mathematical ideas, and more about mathematics in general. In particular, a while ago I was asked a question by a philosopher friend about topology and topos theory as he was trying to understand Alain Badiou’s writings about ontology. That eventually led to my reading a bit more about what recent philosophers have to say about mathematics, or to use it for. This eventually led me to look at Fernando Zalamea’s book “The Synthetic Philosophy of Contemporary Mathematics”. It’s not a new book, unless 2009 counts as new at this point 8 years later. But that’s okay: this isn’t a book review either (though I did find one here). However, it’s the book which was the main jumping off point for the thoughts I’m putting down here. It’s also an interesting book, which speaks to a lot of the same concerns that I’ve been interested in for a while, and while it has some flaws (which I’ll speak to briefly in part II), mostly I want to treat it as a starting point.

I suppose the first issue in talking about the philosophy of mathematics, if your usual audience is for talking about mathematics itself, is justifying why philosophy of mathematics in general ought to be of interest to mathematicians. I’m not sure if this is more, or less, true because I’m not a philosopher, but a mathematician, so my perspective isn’t a very sophisticated reader of the subject, but as someone seeing what it has to say about the field I practice. We mathematicians aren’t the only ones to be skeptical about philosophy and its utility, of course, but there are some particular issues there’s a lot of skepticism about – or at least which lead to a lack of interest.

Why Philosophy Then

My take is that “doing philosophy” is most relevant when you’re trying to carefully and systematically talk about subjects where the concepts that apply are open to doubt, and the principles of reasoning aren’t yet finally defined. This is why philosophers tend to make arguments, challenge each others’ terms, get accused of opacity (in some cases) and so on. It’s also one reason mathematicians tend to be wary of the process, since that’s not a situation we like. The subject matter could be anything, insofar as there are conceptual issues that need clarifying. One result is that, to the extent the project succeeds at pinning down particular concepts and methods, whole areas of philosophy have tended to get reframed under new names: “science”, a more systematic and stable version of the older “natural philosophy”, would be one example. To simplify the history a lot, we could say that by systematically describing something called the “scientific method”, or variations on the theme, science was distinguished from natural philosophy in general. But the thinking that came before this method was described explicitly, which led to its description, was philosophical thinking. The fact that what’s left is necessarily contentious and subject to debate is probably part of why academics in other fields are often dubious about philosophy.

Similarly, there’s the case of logic, which began its life in philosophy as an effort to set down systematic ways of being sure one is thinking rigorously (think Aristotle’s exposition of how syllogisms work). But later on it becomes a topic within mathematics (particularly following Boole turning it into a branch of algebra, which now bears his name). When it comes to philosophy of mathematics in particular, we could say that something similar happened as certain aspects of the topic got formalized and become the field now called “metamathematics” (which studies things such as whether given theorems are provable within specified axiom systems). So one reason philosophy might be important to mathematicians is that the boundary between the two is rather porous. Yet maybe the most common complaint you hear about philosophy is that it seems to have become stuck at just the period when this occurred – around 1900-1940 or so, motivated by things like Hilbert’s program, Cantorian set theory, Whitehead and Russell’s Principia, and Gödel’s theorem. So that boundary seems to have become less permeable.

On the other hand, one of the big takeaways from Zalamea’s book is that the philosophy of mathematics needs to pick up on some of the themes which have appeared in mathematics itself in the “contemporary” period (roughly, since about 1950). So the two fields have a history of exchanging ideas, and potential to keep doing so.

One of these is the sort of thing you see in the context of toposes of sheaves on a site (let’s say it’s a topological space, for definiteness). A sheaf is a kind of object which is defined by what it looks like locally in each open set of the space, which is constrained by having to fit together nicely by gluing on overlaps – with the sheaf condition describing how to pass from local to global. Part of Zalamea’s program is that philosophy of mathematics should embrace this view: it’s the meaning of the word “Synthetic” in the title, as contrasted with “Analytic” philosophy, which is more in the spirit of the foundational approach of breaking down structures into their simplest components. Instead, the position is that lots of different perspectives, each useful for understanding one theme, some part or aspect of mathematics, can be developed, and integrated together by being careful to account for how to reconcile them in areas where they both have something to say. This is another take on the same sort of notion I was inspired by when I chose the name of this blog, so naturally, I’m predisposed to be interested.

Now, maybe it’s not surprising that the boundary between the two areas of thought has been less permeable of late: the part of the 20th century when this seems to have started was also when many fields of academia started to become more specialized as the body of knowledge in each became so huge that it was all anyone could do to master one special discipline. (One might also point to things like the way science became a much bigger group enterprise, as witness things like the Manhattan Project, which led into big government-funded agencies doing “big science” in an institutional setting where specialization and the division of labour was the norm. But that’s a big digression and probably needs more data to support it than I’ve actually got.)

Anyway, Whitehead and Russell’s work seems to have been the last time a couple of philosophers famously made a direct contribution to mathematics. There, the point was to nail down a definite answer to the question of how we know truth, what mathematical entities are, how logic functions and gives rise to more complex mathematics, and so on. When Gödel, working as a mathematician, showed how it was incomplete, and was construed as doing mathematics (and if you read his paper, it’s hard to construe it as much else), that probably contributed a lot to mathematicians drifting away from philosophers, many of whom continued to be interested in the same questions.

Big and Small Scales

Still, even if we just take set-theoretic foundations for granted (which is no longer quite as universal as it used to be), there’s a distinction here. Just because mathematics can be reduced to set theory and logic, this doesn’t mean that the philosophy of mathematics has to reduce to the philosophy of set theory and logic. Whatever the underlying foundations, an account of what happens at large scales might have very different features. Someone with physics inclinations might describe it as characterizing the “effective theory” of mathematics – the way fluid dynamics is an effective theory of particular kinds of big statistical ensembles of atoms, and there are interesting things to say about each level in its own right.

Another analogy that occurs to me is with biology. Suppose we accept that biology ultimately reduces to chemistry, in the sense that all living things are made of chemicals, which behave exactly as a thorough understanding of chemistry would say they do. This doesn’t imply that, in thinking about biology, there’s nothing to think about except chemistry: the philosophy of biology would have its own issues, because biology entails new concepts, regardless of whether there happens to be some non-chemical “vital fluid” that makes living things different from non-living things. To say that there is no such vital fluid is an early, foundational, part of the philosophy of biology, in this analogy. It doesn’t exhaust what there is to say about living things, though, or imply that one should just fall back on the philosophy of chemistry. A big-picture consideration of biology would have to take into account all sorts of knowledge and ideas that get used in the field.

The mechanism of evolution, for example, doesn’t depend on the thermodynamic foundations of life: it can be applied to processes based on all sorts of different substrates – which is how it could inspire the concept of genetic algorithms. Similarly, the understanding of ecosystems in terms of complex systems – starting with simple situations like predator-prey models and building up from there – doesn’t depend at all on what kind of organisms are involved, or even that they are living things. Both of these are bodies of knowledge, concepts, and methods of analysis, that play a big role in studying living things, but that aren’t related at all to the foundational questions of what kind of physical implementation they have. Someone thinking through the concepts in the field would have to take them into account and take into account their own internal logic.

The situation with mathematics is similar: high-level accounts of what kinds of ideas have an influence on mathematical practice could be meaningful no matter what context they appear in. In fact, one of the most valuable things a non-rigorous approach – that of philosophy rather than, say, metamathematics as such – has to offer is that it can comment when the same themes show up even in formally very different sub-disciplines within mathematics. Recognizing these sorts of themes, before they can be formalized and made completely precise, is part of describing what mathematicians are up to, and what the significant features of that practice may be. Discovering those features, and hopefully pinning them down enough to get one or more ways to formalize them that are rigorous to use, is one of the jobs philosophy ought to be able to do. Zalamea suggests a few such broad patterns, which I’ll try to unpack and comment on a little in Part II of this post.xz
Do you know the joy when you find a _giant diamond cluster in Minecraft_?

If yes, you need to know that you've just hit a big one:
take your time to explore the [**Ten Rules Collection**](https://collections.plos.org/ten-simple-rules).


## Prerequisites
All the previous Purgatorio guides.

## Time to complete
10 minutes.

# Index
- [Collect Information](#Hunting-for-Information)
- [Building a Knowledge Tree](#Building-a-Knowledge-Tree)
- [Choosing a Project Structure](#Choosing-a-Project-Structure)
- [Reproducibility](#Reproducibility)
- [Versioning](#Versioning)
- [Documentation](#Documentation)
- [Prepare to Fail](#Prepare-to-Fail)

Let's dive right in!


### Hunting for Information
A vital phase when starting a project is to search for information that can help you. These can be of any kind:
- Tutorials
- Documentation
- Existing projects
- Research Papers
- ...

This guide will not teach you how to use [Google](https://www.google.com/), because you will already know if you are reading these lines :-).

By the way, probably not everyone knows about [**these Google tricks**](https://smallbiztrends.com/2019/03/google-tricks.html)...

But there are a few tips that can come in handy when you start "amassing" knowledge that will then come in handy.

#### Understand what you're looking for
The first thing to do when dealing with a new problem is to make sure you're looking for the right things. Are you sure the problem is called that for example? Image segmentation is different from image classification! [This Google guide](https://developers.google.com/machine-learning/problem-framing/cases) can help you be sure of the name of your problem.

This may seem trivial, but many useful resources are not found because the correct keywords are not typed into the search engine.

Consider the use of the [5 Whys technique](https://en.wikipedia.org/wiki/Five_whys) to better understand the problem you're trying to solve.

#### Don't re-invent the wheel
Are you sure that someone hasn't already solved your problem? In that case, if you needed it to solve a real problem you'd already have the dish ready, while if you're doing it to learn you have a base from which to start! Also, observing the code of others is very effective for learning.
In the latter case, it is still advisable to try to re-implement the solution.

To look if someone has solved the same problem the first place to look is [Github](https://github.com/), the platform where every developer puts Open Source code.
Another interesting place can be [Kaggle](https://www.kaggle.com/), the site of the Data Science challenges, where thousands of practitioners and experts challenge each other on real problems, and whose works are available in the form of Notebooks.

Let's suppose for example that I want to solve a problem related to time series: I can type on Kaggle "analysis of time series" and I will probably find dozens of Notebooks that show how to solve a similar problem, and from which you can observe the approach. What a great source of inspiration!

Also check out [TensorFlow Hub](https://www.tensorflow.org/hub), [ModelZoo](https://modelzoo.co/) and [Papers with Code](https://paperswithcode.com/). These three platforms are full of pre-trained models that can come in handy, or even solve your problem already! :)

#### Find communities
Join communities of people interested in the topic (e.g. [Reddit](www.reddit.com)): here you can find discussions, search by keywords (e.g. "time series analysis"), and ask questions, with experts who will answer and help you.

Try to form specific, well-written questions, to minimize the time used by the respondent. For example, the question "how do I analyze a time series?" is too general, and a short Google search is all it takes to get the answer.

Instead, a question like "to analyze a time series and train a model that predicts 2 steps forward in the future, is it better to approach X or approach Y?".

If the questions are too general or show laziness they'll likely remain unanswered...

Some subreddits you can subscribe to are:

- [r/MachineLearning](https://www.reddit.com/r/MachineLearning/)
- [r/LearnMachineLearning](https://www.reddit.com/r/learnmachinelearning/)
- [r/DeepLearning](https://www.reddit.com/r/deeplearning/)
- [r/DataScience](https://www.reddit.com/r/datascience/)
- [r/LearnDataScience](https://www.reddit.com/r/learndatascience/)

Two other good places to post (well structured) questions are:
- [HackerNews](https://news.ycombinator.com/)
- [Quora](https://www.quora.com/)

#### Building a Knowledge Tree

Given the speed of scientific research in the world of data, every day a new approach to your problem could be discovered that proposes a much better solution than the previous one. The only way to get up to date is to read research papers!
Reading papers is difficult though, they are often full of mathematical, and statistical concepts, with complex theories. The important thing, however, is to be able to understand the concepts, and maybe try to apply them to your problem.

Also often remember that Paper With Code collects the code to implement any paper! Often already after a couple of days from the release, there is code available in various frameworks, ready to be tried on your problem.

However, when you are confronted for the first time with a new problem _you do not know which paper to start with_, also because usually, the papers refer to all previous papers that have tried to solve the same problem, and assume that the reader has some kind of knowledge about the problem.

So what to do?

Use the **Papers Tree strategy**:

- Find the last survey paper about the sub-field of Data Science you're trying to solve
- Read carefully this paper, and understand which are the foundations and try to figure out which are the most important papers the sub-field is based on. Usually, the history of the field is covered, citing the most important papers, and this gives you an overview of which were the important steps of the research, up to the state of the art in the approach to the problem.

Following the example above, this paper -> [A Survey of the Recent Architectures of Deep Convolutional Neural Networks](https://arxiv.org/abs/1901.06032) contains a detailed map of the most important papers on convolutional networks (neural networks that work well with images and videos) and their evolutions, up to the most advanced architectures.

Now you just have to look for the most important (or interesting) papers mentioned, organized is a time-aware tree!

A good practice is to use [Zotero](https://www.zotero.org/), a document manager that allows you to keep track of all your research.

You can then repeat this process in a more specific way, for example by looking for a survey paper on convolutional networks applied to the diagnosis of medical images.

Once you collected the mosst important papers for your research, document your exploration!

Tools like MindMup[https://www.mindmup.com/] can help you in this task.

Consider the [Rhizomaps](http://spdrdng.com/posts/rhizomapping-rhizomaps-rhizomatic-learning-mindmapping-speed-reading-tip-17-take-notes-with-mindmaps-and-rhizomaps) approach too, it really helps in dumping our thoughts on paper.


#### Warning
Before reading any paper [**read this!**](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf)

It's a paper that explains how to read a paper. Yes, we at Virgilio like recursion.

### Choosing a Project Structure
Choosing a project structure is vital to managing the complexities that result from the evolution of the project. Without a clear structure, you'll find yourself with randomly scattered files, dataset versions with similar names, so much so that it hurts your head!

Well organized code tends to be self-documenting in that the organization itself provides context for your code without much overhead. People will thank you for this because they can:

- Collaborate more easily with you on this analysis
- Learn from your analysis about the process and the domain
- Feel confident in the conclusions at which the project arrives


But the first person to thank the ordered project structure is you! When we look at the code we wrote months ago, we often don't remember anything!

> "Mmmm... I don't remember if the good file was analysis.py, analysis_final.py, analysis_1.py" :-)

For these reasons, good people have developed a fantastic project, [**Cookiecutter**](https://drivendata.github.io/cookiecutter-data-science/), which wants to standardize the structure of projects by providing a sensible and flexible template.

To create the project skeleton just install the package:
```
pip install cookiecutter
```

and then use:

```
cookiecutter https://github.com/drivendata/cookiecutter-data-science
```

You can customize the template according to your needs, just clone the repo, modify it and then use:

```
cookiecutter https://github.com/...... your repo .....
```

Cookiecutter projects have the following structure:


![Figure 1-1](cookiecutter.png "1")

[Here](https://drivendata.github.io/cookiecutter-data-science/) you can find how to use it and the motivations behind the structure choices, and [here](https://cookiecutter.readthedocs.io/en/latest/readme.html) you can find the docs.

Take a look at some example project structures, in particular go and check [these cookiecutter project templates](https://github.com/neomatrix369/awesome-ai-ml-dl/blob/master/Programming-in-Python.md#cookie-cutter-python-project-templates).


#### Metadata and file names
Another important issue with regard to the overall order of the project and the management of its complexity is the management of the data and metadata associated with them.

[**This awesome cheatsheet**](https://www.axiomdatascience.com/best-practices/DataManagementCheatSheet.html) contains everything you need to know about **data management and file names best practices**: keep it under your pillow!


### Reproducibility

Why are we talking about [**reproducibility**](https://en.wikipedia.org/wiki/Reproducibility)?

The field name in the Data **Science** indicates that the work process is scientific (Data Science, even with software as a component, is not pure software, which is reproducible by definition).

From [this article](https://towardsdatascience.com/data-sciences-reproducibility-crisis-b87792d88513):
> Reproducible experiments are the foundation of every scientific field and, indeed, even the scientific method itself.

 Karl Popper said it best in [The Logic of Scientific Discovery](http://strangebeautiful.com/other-texts/popper-logic-scientific-discovery.pdf): “non-reproducible single occurrences are of no significance to science.”

If you’re the only person in the world who can achieve a particular result, others may find it difficult to trust you, especially if they have spent time and effort attempting to reproduce your work.

It is reckless and irresponsible to build a product or theory on a singular unconfirmed anecdote, and if you present anecdote as a reliable phenomenon, it can consume time and resources that would otherwise be spent on actual productive work.

Reproducibility has a number of indirect advantages, in addition to being sure to present good results (analysis or model predictions):

- It saves time in various ways, for example by saving the intermediate steps of data processing and cleaning, so that you don't have to redo all the steps
- Allows you to automate various parts of the project workflow
- Allows others to reproduce results
- Allows others to understand each phase without confusion
- Reproducible design is easier to document
- Allows you to take over the project after months or years, and be sure to get the most out of it

Here you can find articles and papers that explain to you how to ensure a high reproducibility across all the phases of the project:

- [Reproducibility in Science](https://ropensci.github.io/reproducibility-guide/)
- [Replicability is not Reproducibility: Nor is it Good Science](http://cogprints.org/7691/7/ICMLws09.pdf)
- [Best Practices for Reproducible, Collaborative Data Science (Video)](https://www.youtube.com/watch?v=vP9Iup8xhKA)

Once you've walked through the above resources, you'll be equipped with best practices to ensure that your code will be highly reproducible, and again, people will be grateful to you!

**Especially, the future yourself will be happy in finding reproducible and automated results, months lateror years !!!**

**Must read:**
- [**Ten Simple Rules for Reproducible Computational Research**](http://dx.plos.org/10.1371/journal.pcbi.1003285)
- [**Ten Simple Rules for Reproducible Research in Jupyter Notebooks**](https://arxiv.org/ftp/arxiv/papers/1810/1810.08055.pdf)

### Versioning

In order to make reproducible projects, and also for peace in the heart of every programmer, learn to use [**Git**](https://git-scm.com/)!

Git is a versioning system that allows you to always have under control every change in your code, be able to go back, and be sure that your code will never be lost!

Git is defined as **Distributed Version Control System**: What does it mean?

From [this article](https://www.freecodecamp.org/news/what-is-git-and-how-to-use-it-c341b049ae61/):

- Control System: This basically means that Git is a content tracker. So Git can be used to store content — it is mostly used to store code due to the other features it provides.

- Version Control System: The code which is stored in Git keeps changing as more code is added. Also, many developers can add code in parallel. So Version Control System helps in handling this by maintaining a history of what changes have happened. Also, Git provides features like branches and merges, which I will be covering later.

- Distributed Version Control System: Git has a remote repository that is stored in a server and a local repository that is stored in the computer of each developer. This means that the code is not just stored in a central server, but the full copy of the code is present in all the developers’ computers. Git is a Distributed Version Control System since the code is present in every developer’s computer. I will explain the concept of remote and local repositories later in this article.

_Any existing software project that is not under version control is considered a dead project, and the responsible developers are considered crazy._

Data Science projects (which make heavy use of software) are no different, indeed!

They also have the _additional problem of data versioning_, which is the raw material on which you work most.

Always having the versions of the data, from raw (just collected) to clean, keeping every intermediate processing phase, is perhaps the most important [best practice](https://medium.com/thelaunchpad/retracing-your-steps-in-machine-learning-ml-versioning-74d19a66bd08) when doing a Data Science project.

[**Here**](https://rogerdudler.github.io/git-guide/index.html) you can find a simple guide to Git. Learn it, it's freaking worth (and necessary).

Documenting your work with Git is crucial: read [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/).

**Must read:**
[**Ten Simple Rules for Taking Advantage of Git and GitHub**](http://dx.plos.org/10.1371/journal.pcbi.1004947)

### Documentation

Like any project, documenting the work done is fundamental to the success of the project.

We don't need to list the benefits that good documentation brings to a project, so we immediately understand what are the best practices to keep in mind when we produce documentation for our projects.

If you still want to learn more, read [this article](https://towardsdatascience.com/why-you-should-document-your-work-as-a-data-scientist-a265af8a373?gi=bc5bae43230e) and [this other](https://hackernoon.com/why-you-should-document-your-self-documenting-code-1105a8a6852e).

[**This guide**](https://managing-qualitative-data.org/modules/2/a/) explains in detail how to document data collection and its organization.

Read also [Ten simple rules for documenting scientific software](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6301674/).

You can choose among different ways to document your project, but Virgilio recommends you to use [Sphinx](http://www.sphinx-doc.org/en/master/), the official Python automated docs library.

Remember that documenting your code and project steps it's **NEVER wasted time**.

**Must read:**
[**Ten simple rules for documenting scientific software**](http://dx.plos.org/10.1371/journal.pcbi.1006561)


### Conclusions

After reading this guide and the resources it contains, you should be equipped with all the necessary best practices when starting a new Data Science project.

In the next sections of Purgatorio you will begin to put these practices into practice, and you will see how grateful you are to yourself!


----
