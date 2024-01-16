# Optimal Matching

<!-- Stable roommate matching is a classical problem in the field of combinatorial optimization and algorithmic game theory. The problem involves finding a stable and mutually satisfactory set of roommate assignments in a scenario where individuals have preferences for potential roommates. -->

For n questions, the algorithm forms n-dimensional arrays for each candidate. Each dimension in the array stores a scalar representing an option selected by the candidate.

For this algorithm to work accurately, the form options for every question should be laid in a sequential order of preference (option a is closer to b than c).

I assume that using the sequential order of options, a person selecting options a,b,c,d would be a closer match with a,c,b,d than a,b,j,d.
