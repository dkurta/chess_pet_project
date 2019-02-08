# Chess Pet Project
by Daniel Kurta

This project implements a small chessbot based on
the negamax-algorithm. It uses the python-chess library.

## UML

## Metrics

## Clean Code Development

## Build Management

## Continous Delivery

## DSL

## Functional Programming

## Logical Programming
(./logical_programming/graph_search.pl)

For a little Project in logical programming in Prolog, i adressed
the problem of the membership of a word to a Language given by a
deterministic finite automaton (DFA). The transfer function of the
DFA is represented in the knowledge base by the fact edge/3.
The rule isElementOfL/1 takes a word as input parameter and decides
 if a word, represented as a list is part of the language represented
 by the DFA with the help of the rule stateChange/3, which calls
 itself in a recursive way for wordes with a length > 2.

 Example Queries are

 isElementOfL([a, b, a]). which returns "True." or

isElementOfL([a, b, b, b]). which returns "False.".