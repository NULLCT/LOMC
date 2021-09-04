#!/usr/bin/env python3

import glob

problem = \
"""
\"\"\"

Problem Statement
The Kingdom of Takahashi is made up of N towns and N−1 roads, where the towns are numbered 1 through N. The i-th road (1≤i≤N−1) connects Town a 
i
​
  and Town b 
i
​
 , so that you can get from every town to every town by using some roads. All the roads have the same length.

You will be given Q queries. In the i-th query (1≤i≤Q), given integers c 
i
​
  and d 
i
​
 , solve the following problem:

Takahashi is now at Town c 
i
​
  and Aoki is now at Town d 
i
​
 . They will leave the towns simultaneously and start traveling at the same speed, Takahashi heading to Town d 
i
​
  and Aoki heading to Town c 
i
​
 . Determine whether they will meet at a town or halfway along a road. Here, assume that both of them travel along the shortest paths, and the time it takes to pass towns is negligible.
Constraints
2≤N≤10 
5
 
1≤Q≤10 
5
 
1≤a 
i
​
 <b 
i
​
 ≤N(1≤i≤N−1)
1≤c 
i
​
 <d 
i
​
 ≤N(1≤i≤Q)
All values in input are integers.
It is possible to get from every town to every town by using some roads.
Input
Input is given from Standard Input in the following format:

N Q
a 
1
​
  b 
1
​
 
a 
2
​
  b 
2
​
 
⋮
a 
N−1
​
  b 
N−1
​
 
c 
1
​
  d 
1
​
 
c 
2
​
  d 
2
​
 
⋮
c 
Q
​
  d 
Q
​
 
Output
Print Q lines. The i-th line (1≤i≤Q) should contain Town if Takahashi and Aoki will meet at a town in the i-th query, and Road if they meet halfway along a road in that query.

Sample Input 1 
Copy
4 1
1 2
2 3
2 4
1 2
Sample Output 1 
Copy
Road
In the first and only query, Takahashi and Aoki simultaneously leave Town 1 and Town 2, respectively, and they will meet halfway along the 1-st road, so we should print Road.

Sample Input 2 
Copy
5 2
1 2
2 3
3 4
4 5
1 3
1 5
Sample Output 2 
Copy
Town
Town
In the first query, Takahashi and Aoki simultaneously leave Town 1 and Town 3, respectively, and they will meet at Town 2, so we should print Town.

In the first query, Takahashi and Aoki simultaneously leave Town 1 and Town 5, respectively, and they will meet at Town 3, so we should print Town.

Sample Input 3 
Copy
9 9
2 3
5 6
4 8
8 9
4 5
3 4
1 9
3 7
7 9
2 5
2 6
4 6
2 4
5 8
7 8
3 6
5 6
Sample Output 3 
Copy
Town
Road
Town
Town
Town
Town
Road
Road
Road
\"\"\"
"""


def comp(path: str) -> str:
    with open(path) as file:
        return file.read()


def main():
    files = glob.glob("./data/*")
    result = ""
    for file in files:
        result += comp(file)

    print(problem+result)


if __name__ == "__main__":
    main()

