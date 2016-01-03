#!/usr/bin/python3
import icndb

def main():
    print("Categories: {}".format(icndb.fetchCategories()))
    print("Getting random joke from icndb")
    print(icndb.fetchRandom())
    print("\nGetting joke about Octocat GitHub")
    print(icndb.fetchRandom(number=1, firstName="Octocat", lastName="GitHub"))
    print("\nGetting joke by ID: 13\n{}".format(icndb.fetchByID(13)))

    print("\nGetting 3 jokes in one turn:")
    print(icndb.fetchRandom(number=3))

    print("\nGetting random joke from NERDY category")
    print(icndb.fetchRandom(limitTo=["nerdy"]))


if __name__ == '__main__':
    main()
