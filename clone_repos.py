import os

def cloneGithubProject(url, name):
    print("cloaning: ")
    command = "git clone {} {}".format(url, name)
    print(command)
    os.system(command)

def main():
    with open("./repos", 'r+') as file:
        for idx, repo in enumerate(file.readlines(), start=1):
            cloneGithubProject(repo.rstrip('\n'), "dama-{}".format(idx))
        file.close()

if __name__ == "__main__":
    main()