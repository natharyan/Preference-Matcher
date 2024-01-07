# Optimal Matching

Stable roommate matching is a classical problem in the field of combinatorial optimization and algorithmic game theory. The problem involves finding a stable and mutually satisfactory set of roommate assignments in a scenario where individuals have preferences for potential roommates.

This algorithm is a modification of the stable roommate matching algorithm for finding optimal pairs using n-dimensional arrays.

Each dimension in an array stores a scalar representing an option selected by a user for a question.

For this algorithm to work accurately, the form options for every question should be laid in a sequential order of preference (option a is closer to b than c).

I assume that using the sequential order of options, a person selecting options a,b,c,d would be a closer match with a,c,b,d than a,b,j,d.
