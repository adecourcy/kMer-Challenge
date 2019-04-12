# Purpose

This was a small program written as a "challenge" program for a computational biology class. Given a set of strings of DNA, the problem is to find a substring common to all DNA strings. The substring is of length "k", on which soft constraints are knowns (e.g., it is definitely longer than 5, almost certainly shorter than 30). It is also the case that the substring might have random alterations in each DNA string (e.g. ABC might appear as ACC), as well as insertions (e.g. ABC might appear as AABC) or deletions (e.g. ABC might appear as AC).

Basically, this program uses a branch-and-bound algorithm to try and find the correct substring.
