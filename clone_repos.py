import sys
import os

def cloneGithubProject(url, name):
    print("cloaning: ")
    command = "git clone {} {}".format(url, name)
    print(command)
    os.system(command)

def main():

    if len(sys.argv) < 3:
        print("Error!")
        print("Use: python clone_repos.py [filename] [--prefix=repositorio]")
        return

    filename = sys.argv[1]
    prefix = sys.argv[2].split("=")[1]

    with open(filename, 'r+') as file:
        for idx, repo in enumerate(file.readlines(), start=1):
            cloneGithubProject(repo.rstrip('\n'), "{}-{}".format(prefix, idx))
        file.close()

if __name__ == "__main__":
    main()