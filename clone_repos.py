import os

def cloneGithubProject(url):
    print("cloaning: ", url)
    os.system("git clone ".format(url))

def main():
    with open("./repos") as file:
        for line in file.readlines():
            cloneGithubProject(line)
        file.close()

if __name__ == "__main__":
    main()