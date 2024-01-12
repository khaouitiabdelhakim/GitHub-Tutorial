## Github Tutorial
Trying to do all the github commands to see the result

Git is a powerful version control system used for tracking changes in source code during software development. Here's a list of common Git commands along with explanations and examples:

### 1. git init
   - Description: Initializes a new Git repository.
   - Example:
     ```bash
     git init
     ```

### 2. git clone
   - Description: Creates a copy of a remote repository on your local machine.
   - Example:
     ```bash
     git clone https://github.com/example/repo.git
     ```

### 3. git add
   - Description: Adds changes in the working directory to the staging area.
   - Example:
     ```bash
     git add file.txt
     ```

### 4. git commit
   - Description: Records changes from the staging area to the repository.
   - Example:
     ```bash
     git commit -m "Commit message"
     ```

### 5. git status
   - Description: Shows the status of changes as untracked, modified, or staged.
   - Example:
     ```bash
     git status
     ```

### 6. git log
   - Description: Displays a log of commits.
   - Example:
     ```bash
     git log
     ```

### 7. git pull
   - Description: Fetches changes from a remote repository and merges them into the current branch.
   - Example:
     ```bash
     git pull origin master
     ```

### 8. git push
   - Description: Uploads local changes to a remote repository.
   - Example:
     ```bash
     git push origin master
     ```

### 9. git branch
   - Description: Lists, creates, or deletes branches.
   - Example:
     ```bash
     git branch
     git branch new-feature
     ```

### 10. git checkout
   - Description: Switches branches or restores working tree files.
   - Example:
     ```bash
     git checkout branch-name
     ```

### 11. git merge
   - Description: Combines changes from different branches.
   - Example:
     ```bash
     git merge feature-branch
     ```

### 12. git remote
   - Description: Manages remote repositories.
   - Example:
     ```bash
     git remote -v
     ```

### 13. git fetch
   - Description: Fetches changes from a remote repository but does not merge them.
   - Example:
     ```bash
     git fetch origin
     ```

### 14. git diff
   - Description: Shows changes between commits, branches, etc.
   - Example:
     ```bash
     git diff
     ```

### 15. git reset
   - Description: Resets the current HEAD to a specified state.
   - Example:
     ```bash
     git reset --hard HEAD~1
     ```
### 16. You want from a branch labs to return to the latest satble version of the master

```bash
# Ensure you are on the labs branch
git checkout labs

# Fetch the latest changes from the remote repository
git fetch origin

# Reset the labs branch to match the master branch
git reset --hard origin/master

# Force-push the changes to the remote repository (be careful with force-push)
git push origin labs --force
```
