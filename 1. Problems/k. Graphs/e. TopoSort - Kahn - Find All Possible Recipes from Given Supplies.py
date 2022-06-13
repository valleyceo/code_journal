# LC 2115. Find All Possible Recipes from Given Supplies

'''
You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.
'''
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        return self.kahnAlgorithm(recipes, ingredients, supplies)

    # O(R*R*I) time | O(R + S) space
    def naiveIteration(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supply_set = set(supplies)
        recipe_map = {}

        for recipe, ingredient_list in zip(recipes, ingredients):
            recipe_map[recipe] = ingredient_list

        res = []
        update_recipe = True

        while update_recipe:
            update_recipe = False
            removed = []

            for recipe, r_list in recipe_map.items():

                included = True

                for ing in r_list:
                    if ing not in supply_set:
                        included = False
                        break

                if included:
                    res.append(recipe)
                    removed.append(recipe)
                    update_recipe = True

            for rem in removed:
                recipe_map.pop(rem)
                supply_set.add(rem)

        return res

    # O(V + E) time | O(V) space
    def kahnAlgorithm(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indeg = defaultdict(int)
        graph = defaultdict(list)

        for recipe, ingredient_list in zip(recipes, ingredients):
            indeg[recipe] = len(ingredient_list)

            for ingredient in ingredient_list:
                graph[ingredient].append(recipe)

        res = []
        queue = deque(supplies)
        recipes = set(recipes)

        while queue:
            ingredient = queue.popleft()

            if ingredient in recipes:
                res.append(ingredient)

            for recipe in graph[ingredient]:
                indeg[recipe] -= 1

                if indeg[recipe] == 0:
                    queue.append(recipe)

        return res
