# [Mariana](https://ti.arc.nasa.gov/opensource/projects/mariana/) Open Sourced ML/AI Algorithms

Just one of many available to better mankind.

Mariana is an algorithm that efficiently optimizes the hyperparameters for Support Vector Machines for regression and classification. It currently uses Simulated Annealing for optimization but can be extended to use a variety of stochastic optimization techniques including, Markov Chain Monte Carlo, Sequential Monte Carlo, and Genetic Algorithms. Mariana can be applied to the text portion of reports, determining the likely categories that each report falls into, and calculating a confidence for each classification.

Mariana¹s innovation is it automates the search for the optimum hyperparameters. It does so by randomly selecting a set of hyperparameters. Next it builds a model from the training data and tests the model's performance using the validation set. That performance is compared to previous performances, and if the current set of hyperparameters are better than the previous one, then it records the hyperparameters. This process is repeated until there are no noticeable improvements in performance or at a predefined stopping point.

