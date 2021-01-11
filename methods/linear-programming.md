----
title: Linear Programming
slugs: linear-programming
category: [ 'programming', 'optimization', 'mathematics', 'models', 'methods' ]
date: 2020-1-20
----

# Linear Programming
Linear programming (LP, also called linear optimization) is a method to achieve the best outcome (such as maximum profit or lowest cost) in a mathematical model whose requirements are represented by linear relationships. Linear programming is a special case of mathematical programming (also known as mathematical optimization).

More formally, linear programming is a technique for the optimization of a linear objective function, subject to linear equality and linear inequality constraints. Its feasible region is a convex polytope, which is a set defined as the intersection of finitely many half spaces, each of which is defined by a linear inequality. Its objective function is a real-valued affine (linear) function defined on this polyhedron. A linear programming algorithm finds a point in the polytope where this function has the smallest (or largest) value if such a point exists. 

### Uses
Linear programming is a widely used field of optimization for several reasons. Many practical problems in operations research can be expressed as linear programming problems.[3] Certain special cases of linear programming, such as network flow problems and multicommodity flow problems are considered important enough to have generated much research on specialized algorithms for their solution. A number of algorithms for other types of optimization problems work by solving LP problems as sub-problems. Historically, ideas from linear programming have inspired many of the central concepts of optimization theory, such as duality, decomposition, and the importance of convexity and its generalizations. Likewise, linear programming was heavily used in the early formation of microeconomics and it is currently utilized in company management, such as planning, production, transportation, technology and other issues. Although the modern management issues are ever-changing, most companies would like to maximize profits and minimize costs with limited resources. Therefore, many issues can be characterized as linear programming problems. 

### Examples
Covering and packing LPs commonly arise as a linear programming relaxation of a combinatorial problem and are important in the study of approximation algorithms.For example, the LP relaxations of the set packing problem, the independent set problem, and the matching problem are packing LPs. The LP relaxations of the set cover problem, the vertex cover problem, and the dominating set problem are also covering LPs.

Finding a fractional coloring of a graph is another example of a covering LP. In this case, there is one constraint for each vertex of the graph and one variable for each independent set of the graph. 

#### Complementary Slackness
 is possible to obtain an optimal solution to the dual when only an optimal solution to the primal is known using the complementary slackness theorem. The theorem states:

Suppose that x = (x1, x2, ... , xn) is primal feasible and that y = (y1, y2, ... , ym) is dual feasible. Let (w1, w2, ..., wm) denote the corresponding primal slack variables, and let (z1, z2, ... , zn) denote the corresponding dual slack variables. Then x and y are optimal for their respective problems if and only if

    xj zj = 0, for j = 1, 2, ... , n, and
    wi yi = 0, for i = 1, 2, ... , m.

So if the i-th slack variable of the primal is not zero, then the i-th variable of the dual is equal to zero. Likewise, if the j-th slack variable of the dual is not zero, then the j-th variable of the primal is equal to zero.

This necessary condition for optimality conveys a fairly simple economic principle. In standard form (when maximizing), if there is slack in a constrained primal resource (i.e., there are "leftovers"), then additional quantities of that resource must have no value. Likewise, if there is slack in the dual (shadow) price non-negativity constraint requirement, i.e., the price is not zero, then there must be scarce supplies (no "leftovers"). 

### Theory

Geometrically, the linear constraints define the feasible region, which is a convex polyhedron. A linear function is a convex function, which implies that every local minimum is a global minimum; similarly, a linear function is a concave function, which implies that every local maximum is a global maximum.

An optimal solution need not exist, for two reasons. First, if the constraints are inconsistent, then no feasible solution exists: For instance, the constraints x ≥ 2 and x ≤ 1 cannot be satisfied jointly; in this case, we say that the LP is infeasible. Second, when the polytope is unbounded in the direction of the gradient of the objective function (where the gradient of the objective function is the vector of the coefficients of the objective function), then no optimal value is attained because it is always possible to do better than any finite value of the objective function. 

note: originally rewritten from the (Wikipedia Page)[https://en.wikipedia.org/wiki/Linear_programming]