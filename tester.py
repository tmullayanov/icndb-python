#!/usr/bin/python3
import icndb

def main():
    print("Categories: {}".format(icndb.fetchCategories()))
    print("Getting random joke from icndb")
    print(icndb.fetchRandom())
    print("Getting joke about Octocat GitHub")
    print(icndb.fetchRandom(number=1, firstName="Octocat", lastName="GitHub"))


if __name__ == '__main__':
    main()
