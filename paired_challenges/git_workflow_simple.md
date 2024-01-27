# Git Workflow - Simple

## Paired Challenge

One of you will take on the role of "Person One" and the other the role of
"Person Two". Both people will be working with the same Git repository.

In this challenge, both will commit, push to and pull from the remote
repository, using the `main` branch alone, so that each person can see the
other's changes.

**Follow the steps carefully, one by one - if you skip things, it'll all start
to go wrong!**

## Steps

### Setup

Decide who will be "Person One" and who will be "Person Two".

Person One, logged into GitHub, should visit https://github.com/new and:

* Add themselves as the `Owner`
* Set a `Repository name` of `git_workflow_simple`
* Check `Private` for the permissions
* And leave all the other settings as they are, then click `Create repository`

Person Two should now give Person One their GitHub username.

Person One goes to the new repository's `Settings` -> `Collaborators` and adds
Person Two as a collaborator.

Person Two should check their email for an invitation, and accept it.

### Cloning the repository

_Both people_ on their own machines should run these steps in something like
iTerm or VS Code's terminal, in parallel (it doesn't matter who goes first or if
you clone at the same time):

* `cd` to the directory where you keep your programming projects (e.g.
  `~/development`), to which you could clone many Git repositories
  * Caution: this must not be within an existing Git repository!
* Copy the URL of the newly made repository - it'll be something like
  https://github.com/MyGitHubUsername/git_workflow_simple
* Type `git clone` then paste in the URL from before and press Enter

You should both see something like this at the terminal:

```
paulgilson@MASTAFF-Paul-Gilson-NG30MWVNXG /Projects % git clone https://github.com/MyGitHubUsername/git_workflow_simple
Cloning into 'git_workflow_simple'...
warning: You appear to have cloned an empty repository.
paulgilson@MASTAFF-Paul-Gilson-NG30MWVNXG /tmp %
```

* `cd git_workflow_simple` to move into the Git repository
* `git status` should show no changes - we've only just cloned it, so we've not
  modified anything yet:

```
paulgilson@MASTAFF-Paul-Gilson-NG30MWVNXG git_workflow_simple % git status
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

### First changes

Person Two will now make the first changes.

Add two files at the top-level of the repository (the directory you `cd`ed into
in the last step) called `person_two_file1` and `person_two_file2`. Add some
content (whatever you want) to both files. It's OK to use something simple like
text files here.

Type `git status` to see the two newly created files which have not yet been
added to be tracked in this repository.

One by one, run these steps for each file in turn:

* `git add <filename>`
* `git status` (will show the added, changed file)
* `git commit -m <some message of your choosing relating to the file>`

Then do `git status` again to see that there are no other changes.

Finally, do `git push`.

_Both people_ should now independently take a look on GitHub e.g.
https://github.com/MyGitHubUsername/git_workflow_simple - see if you can answer
these questions:

* Can you find the two new files at the top-level of the _remote_ repository on
  GitHub?
* Look to see where those 2 commits are shown - can you find a page that shows
  them both, in sequence?
* Look at each of the commits' details individually - can you see what was
  actually "changed" in those commits (it'll be a newly created file)?

### Collaboration

Person One at the command line should now pull the change Person Two previously
made - the newly added files - so that they can see those files locally.

To start with, run `ls` to confirm that Person One currently has neither of
those files locally.

Next, run `git pull` - what do you see happen at the terminal? What if you now
run `ls`, do the files now exist?

Lastly, run `git log` - what changes and commits does Person One now see?

### Continuation

At this point, Person One can make their own changes - either making new files,
editing existing ones or even deleting them - using `git add` then `git
commit` and `git push` to push the change(s) to GitHub, such that Person Two can
then `git pull` them locally.

Repeat these steps, one person making changes to `main` with the other pulling
those down locally, until you're both happy with:

* All of the Git commands used here
* Making changes which your pair is then able to pull and see locally
* Exploring those changes/commits in GitHub

## Note

In this challenge we haven't:

* Used different branches, only `main`
* Created any conflicting changes, as you never both worked on the same branch
  nor files at the same time

In other challenges and/or later in the course, we'll explore those things
further.


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Fgit_workflow_simple.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Fgit_workflow_simple.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Fgit_workflow_simple.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Fgit_workflow_simple.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Fgit_workflow_simple.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
