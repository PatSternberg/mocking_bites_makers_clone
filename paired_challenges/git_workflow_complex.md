# Git Workflow - Complex

## Paired Challenge

One of you will take on the role of "Person One" and the other the role of
"Person Two". Both people will be working with the same Git repository.

In this challenge, you'll be using different branches for your work. The changes
one person makes will be "peer reviewed" by the other in GitHub, before they are
safely merged into the `main` branch ready for everyone to use.

**Follow the steps carefully, one by one - if you skip things, it'll all start
to go wrong!**

## Steps

### Setup

Please follow the [Setup steps from the "simple" version of this
challenge](./git_workflow_simple.md) but _use a different repository name_
(of your choosing) so that you are both set up and ready to go.

### Cloning the repository

_Both people_ should now clone the repository locally then `cd` into it. There
should be no files there initially, for either person.

Run `git branch` to confirm that your local repository is the `main` branch (it
should be, there's only one branch in this newly created repository).

### First changes

_We're going to start by making some changes in the `main` branch, just in order
to get things going._

Person One on the `main` branch should now add one or more files locally, then
add, commit and finally push those changes to GitHub. It's OK to use something
simple like text files here.

Person Two should then pull those changes to their local `main` branch.

### New branch

Person Two on GitHub should now create a new branch for this repository. From
the main "Code" page for the non-empty repository, find where it says `1 branch`
and click that, then choose to add a `New branch` and give it the name
`changes_to_try_a_pull_request`. (We use branch names related to the expected
work that'll go into them.)

Person Two should now, on their command line, pull the recent changes (the newly
added branch). Look at the output from Git - what can you see has been pulled?

Switch to the new branch, with `git checkout person_two_branch` (or `git switch
person_two_branch` - it'll do the same thing).

Finally, make some changes for this branch and push them to GitHub.

### Peer review & Pull Request

_Person One will now act as a peer reviewer of Person Two's work that has been
done safely in a branch that's not the `main` branch._

Person Two should go to GitHub and switch to `person_two_branch` from the
drop-down on the main repository page. Next, locate the `Compare & pull
request` button. Adjust the title if you wish, optionally add a comment, then
`Create pull request` to make the Pull Request.

From the right-hand side of the Pull Request - often called a "PR" - find your
collaborator and set them for review.

Person One should access GitHub and from the `Pull requests` tab, find Person
Two's PR and the request for a review of their work.

Review the changes under `Files changed` and, when done, click `Review changes`,
select `Approve` and add a comment. Finally, approve the PR.

### Merging

Person Two should now check out their PR on GitHub, and locate the approval
comment from Person One.

From the PR, click to `Merge pull request` then `Confirm merge`. This will merge
the branch and its changes back into the `main` branch, bringing those carefully
reviewed changes to the `main` branch.

Lastly, click `Delete branch` to keep things tidy, as we no longer need that
branch. (_N.B. you can restore deleted branches, if ever necessary._)

Both people should now in their terminals switch to the `main` branch and then
pull the recent changes - what do you see?

Type `git branch` to see a list of active branches. If either of you have any
that have since been deleted, type `git branch -d <branch_name>` to tidy things
up locally.

### Repeat

From the `New branch` section above, repeat the steps but swap roles - this
time, Person One will make a new branch (with a different but still appropriate
name) and make changes to existing files, Person Two will act as the peer
reviewer.

## Extension

If you want to make things more interesting (one extra :hot_pepper:!):

* Have the peer reviewer request some changes, effectively rejecting the first
  version of the Pull Request ("PR"), such that the branch creator and change maker has
  to make some more changes before the PR is approved.
* Have both people create and work on some branches at the same time. For now,
  make sure you're both either just creating new files or editing files the
  other person isn't editing too!


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Fgit_workflow_complex.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Fgit_workflow_complex.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Fgit_workflow_complex.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Fgit_workflow_complex.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Fgit_workflow_complex.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
