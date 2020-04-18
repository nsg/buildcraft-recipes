import glob
import json
import pprint


def out(f, jr, recipe):
    result = jr["result"]["item"]
    data = jr["result"].get("data", 0)
    amount = jr["result"].get("amount", 1)

    f.write(f"## {result}\n")

    if "pattern" in jr:
        pattern = jr["pattern"]
        f.write(
            f"Source: [{recipe}](https://github.com/BuildCraft/BuildCraft/blob/8.0.x-1.12.2/{recipe})\n"
        )

        f.write(f"data: {data}| |amount: {amount}\n-|-|-\n")
        for pattern_row in pattern:
            for index, mat in enumerate(list(reversed(list(pattern_row)))):
                if mat == " ":
                    f.write(f" _ | ")
                else:
                    ore = jr["key"][mat].get("ore")
                    mat_lookup = jr["key"][mat].get("item", ore)
                    if index < 2:
                        f.write(f" {mat_lookup} | ")
                    else:
                        f.write(f" {mat_lookup}")
            f.write("\n")
    else:
        ingredients = json.dumps(jr["ingredients"], sort_keys=True, indent=4)
        f.write("```\n")
        f.write(f"{ingredients}\n")
        f.write("```\n")


def main():
    open("recipes.md", "w").close()
    recipes = glob.glob("source/buildcraft_resources/assets/*/recipes/*.json")

    for recipe in recipes:
        try:
            jr = json.load(open(recipe))
            f = open("recipes.md", "a")

            if type(jr) == dict and "result" in jr:
                out(f, jr, "/".join(recipe.split("/")[1:]))

            f.close()
        except KeyError as e:
            print(f"I failed to parse the file {recipe}")
            print(e)


main()
