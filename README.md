# Zombie Horde

A datapack dedicated to the zombie horde modpack. 

## Installation
First make a fork of this repo. Click fork at the top of the screen. After, you can clone the repo using
```
git@github.com:{YOUR_USERNAME}/ZombieHorde.git
```
If you are not able to clone, it may be because you have not added your SSH key to gitlab. If so, go to [SSH Key Settings](https://gitlab.com/profile/keys)

Then next thing after you clone the repo is to link the main repository.
```
cd web
git remote add blessed git@github.com:ChromeSkullex/ZombieHorde.git
```
This allows your local git instance to connect to the main repo.


## Contributing

1. Create a branch after your named ticket number. `git checkout -b {branch-name}` (`-b` creates a new branch) 
2. Do your changes. 
2. Review your changes
2. Stash your changes once everything is reviewed.
3. Commit with a detailed message on what you changed/added/removed.
4. Push your commited changes to your git repo by `git push origin {branch-name}`
5. Create a pull request on the main repository [ChromeSkullex/ZombieHorde](https://github.com/ChromeSkullex/ZombieHorde/tree/main)


## Pulling changes (Rebase)
If a new change have been made to the main repo, do these steps.
1. Ensure you are in your main branch `git checkout main`
2. Pull from the main repo by doing: `git pull blessed main`
3. Go to the branch you need to rebase by doing: `git rebase main`
