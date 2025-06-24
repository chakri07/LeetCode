"""

You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. A recipe can also be an ingredient for other recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.

 

Example 1:

Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
Output: ["bread"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
Example 2:

Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
Example 3:

Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich","burger"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".

https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies
"""
from typing import List
from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        supplies = set(supplies)

        adj_list = defaultdict(list)
        in_degree = defaultdict(int)

        # i = receipve
        for i in range(len(ingredients)):
            for each in ingredients[i]:
                if each not in supplies:
                    adj_list[each].append(i)
                    in_degree[i] += 1
        
        queue = deque([])
        for i in range(len(recipes)):
            if i not in in_degree:
                queue.append(i)
        
        ans = []

        # print(adj_list)
        # print(in_degree)
        while queue:
            recp_idx = queue.popleft()
            ans.append(recipes[recp_idx])

            created_receipe = recipes[recp_idx]

            for dep in adj_list[created_receipe]:
                in_degree[dep] -= 1
                if in_degree[dep] == 0:
                    queue.append(dep)
            # print(queue)
        
        return ans

        