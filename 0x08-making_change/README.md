# Coin Change Problem Solver

## Description
This project aims to solve the classic coin change problem using both greedy algorithms and dynamic programming approaches. The objective is to find the minimum number of coins required to make up a given total amount, given a list of coin denominations.

## Approach
The project implements two main strategies to solve the coin change problem:
- **Greedy Algorithm**: This approach selects the largest denomination coin that fits into the remaining amount at each step. While it may not always provide the optimal solution, it can be efficient for certain sets of coin denominations.
- **Dynamic Programming**: This approach breaks down the problem into smaller sub-problems and utilizes memoization to store solutions to overlapping sub-problems. It guarantees an optimal solution and is suitable for a wide range of coin denomination sets.

## Requirements
- Python 3.4.3
- Ubuntu 20.04 LTS
- PEP 8 style (version 1.7.x)

## Files
- `greedy_coin_change.py`: Contains the implementation of the greedy algorithm for the coin change problem.
- `dynamic_programming_coin_change.py`: Contains the implementation of the dynamic programming approach for the coin change problem.
