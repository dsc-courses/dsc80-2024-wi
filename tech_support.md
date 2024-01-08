---
layout: page
title: 🙋‍♂️ Tech Support
description: Pointers on how to solve common technical issues.
nav_order: 4
---

# 🙋‍♂️ Tech Support
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}
---

{: .warning }
**Coming soon! 👀**

<!-- ## Introduction

Assignments in DSC 80 are mostly coding assignments, so it's important to make sure that your computing environment is set up properly. There are two ways to go about things: you can set up a local environment or use a remote environment that is largely pre-configured. On this page, we'll talk about both options.

Writing code locally, on your personal computer, is our preferred option. We won't lie – it involves a little more time to set up and a steeper learning curve. But in the long run, you'll likely find the local environment more comfortable and faster since you can customize it to your own needs. Additionally, setting up your own local Python environment is something you'll be expected to do when working as a data scientist, so it's a good idea to start now.

There has been a lot written about how to set up a Python environment, so we won't reinvent the wheel. This page will only be a summary; Google will be your main resource. But always feel free to come to a staff member's office hours if you have a question about setting up your environment, using Git, or similar — we're here to help.


---

## Working Locally (Recommended)

Working *locally* simply refers to developing code using software
installed on your own machine. For this class, the software you\'ll need
includes Python 3.8, a few specific Python packages, Git, and a text
editor.

### Mamba

`Mamba` is a fast, robust, and cross-platform package manager. Serving as a powerful alternative to the traditional `pip install` command, `mamba install` command ensures seamless compatibility between package versions, mitigating the risk of conflicts within your development environment. If you should need to install a new Python package, you can use the `mamba` command. Inside the terminal, type `mamba install <package_name>`, where `<package_name>` is replaced by the name of the package you want to install, and hit enter.


### Replicating the Gradescope Environment


Gradescope has a package environment which it uses to autograde your work. It is advised to create the same environment so that there are no issues due to version changes during development vs. evaluation. Please follow the below steps to create the environment with required
packages.

- **1. In Terminal, install `mamba` by running one of the [install scripts](https://github.com/conda-forge/miniforge#miniforge).**
  
**Unix-like platforms (Mac OS & Linux)**: Download the installer using curl or wget or your favorite program and run the script.

`curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh`<br>

or 

`wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh`

**Windows**: Download and execute the Windows installer. Follow the prompts, taking note of the options to "Create start menu shortcuts" and "Add Miniforge3 to my PATH environment variable". The latter is not selected by default due to potential conflicts with other software. Without Miniforge3 on the path, the most convenient way to use the installed software (such as commands `mamba`) will be via the "Miniforge Prompt" installed to the start menu.

run: `start /wait "" Miniforge3-Windows-x86_64.exe /InstallationType=JustMe /RegisterPython=0 /S /D=%UserProfile%\Miniforge3`

  
- **2. Download the [environment.yml](https://github.com/dsc-courses/dsc80-2023-fa/blob/gh-pages/resources/environment.yml) file.**

- **3. In Terminal, create a new conda environment**: `mamba env create -f environment.yml`.<br>
Notice that if you've put [environment.yml](https://github.com/dsc-courses/dsc80-2023-fa/blob/gh-pages/resources/environment.yml) in your Downloads folder or Desktop, you should replace `environment.yml` with the path to the file, for example: `mamba env create -f /Users/yourusername/Desktop/environment.yml`. Otherwise, you might get an error saying [environment.yml](https://github.com/dsc-courses/dsc80-2023-fa/blob/gh-pages/resources/environment.yml) does not exist.

- **4. Activate the environment**: `mamba activate dsc80`. If you’re using VSCode, you should select the Python kernel corresponding to the dsc80 environment to use it.

Every time you work on DSC 80, activate this environment by running
`mamba activate dsc80` in your terminal.

To open a Jupyter Notebook, use the `jupyter notebook` command in your terminal.

### `mamba` vs. `conda` vs. `pip`


Setting up a Python development environment is a crucial step for ensuring consistency and compatibility of your work. An environment is essentially a self-contained space where your project dependencies, libraries, and their respective versions are isolated from the rest of your system. While `pip` is a widely used package installer, it lacks built-in support for creating isolated environments. This limitation makes it challenging to maintain version consistency and avoid conflicts between packages. Consequently, we do not recommend relying solely on `pip install` for environment management, as it may inadvertently introduce incompatible package versions.

`Conda`, on the other hand, is a powerful tool that not only installs packages but also manages environments effortlessly. It allows you to create isolated environments and ensures compatibility among the packages within those environments. `Mamba` is a wrapper around `conda`, designed to optimize the installation process, making it notably faster than traditional `conda` installations. 


### Git

All of our course materials, including your assignments, are hosted on
GitHub in [this Git repository](https://github.com/dsc-courses/dsc80-2023-fa). This means that you'll need to download and use
[Git](https://git-scm.com/) in order to work with the course
materials.

Git is a *version control system*. In short, it is used to keep track of
the history of a project. With Git, you can go back in time to any
previous version of your project, or even work on two different versions
(or \"branches\") in parallel and \"merge\" them together at some point
in the future. We\'ll stick to using the basic features of Git in DSC
80.

There are Git GUIs, and you can use them for this class. You can also
use the command-line version of Git. To get started, you\'ll need to
\"clone\" the course repository. The command to do this is:

    git clone https://github.com/dsc-courses/dsc80-2023-fa

This will copy the repository to a directory on your computer. To bring
in the latest version of the repository, run **`git pull`** in your local repository. This will **not**
overwrite your work. In fact, Git is designed to make it very difficult
to lose work (although it\'s still possible!).

**Merge Conflicts**

You might face issues when using `git pull` regarding merge issues and branches. This is caused by files being updated on your side while we are also changing the [Git repository](https://github.com/dsc-courses/dsc80-2023-fa) by pushing new assignments on our side. Here are some steps you can follow to resolve it:

NOTE: Whenever working with GitHub pulls, merges, etc., it's a good idea to save your important work locally so that if you accidentally overwrite your files you still have the work saved. **Save your work locally before following the steps below.**

1. `git status` shows the current state of your Git working directory and staging area. It's a good sanity check to start with. You will probably see your project and lab files that you have worked on.
2. `git add .`  will add all your files to be ready to commit.
3. `git commit -m "some message of your choice"`  will commit the files, with some description in the quotations. This can be whatever you want, it won't matter.

At this stage, if you `git pull`, it should work. You should double-check that you have new files, as well as that your old files are unchanged. If they are changed then you should be able to just copy-paste from your local backup. If this does **not** work then you may have **merge conflicts**, follow the next steps:

4. `git checkout --theirs [FILENAME]`  will tell git that whenever a conflict occurs in `[FILENAME]` to keep your version. Run this for each file with a conflict.
5. `git add [FILENAME]` to mark each file with a conflict as resolved. 
6. `git rebase --continue` or `git merge`, depending on the setup. 



### Choosing a Text Editor or IDE

In this class, you will need to use a combination of editors for doing
your assignments: The python files should be developed with an IDE (for
syntax highlighting and running doctests) and the data/results should be
analyzed/presented in Jupyter Notebooks. Below is an incomplete list of
IDEs you might want to try. For more information about them, feel free
to ask the course staff.

If you're curious, Suraj uses VSCode to edit .py files and the vanilla Jupyter environment to edit notebooks.

-   The [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) text
    editor: see [below](#jupyterlab). Can be used to edit both notebooks and .py files.

-   [VSCode](https://code.visualstudio.com/): Microsoft Visual Studio Code. Currently very popular, and can also be used to edit both notebooks and .py files.

-   [sublime](https://www.sublimetext.com/): A favorite text editor of
    hackers, famous for its multiple cursors. A good, general-purpose
    choice.

-   [atom](https://atom.io/): GitHub's editor. Pretty nice fully
    featured IDE. Can only work locally.

-   [PyCharm (IntelliJ)](https://www.jetbrains.com/pycharm/): Those who
    feel at home coding Java. Can only work locally.

-   [nano](https://www.nano-editor.org/): available on most unix
    commandlines (e.g. DataHub Terminal). If you use this for more than
    changing a word or two, you\'ll hate your life.

-   [(neo)vim](https://neovim.io/): lightweight, productive text-editor
    that might be the most efficient way to edit text, if you can ever
    learn how to use it. Beware opening vim, as you may never figure out
    how to quit (literally). Justin Eldridge's text editor of choice.

-   [emacs](https://www.gnu.org/software/emacs/): A text editor for
    those who prefer a life of endless toil. Endlessly customizable, it
    promises everything, but you're never good enough to deliver. Its
    keyboard shortcuts are guaranteed to give you carpal tunnel.
    Aaron Fraenkel's text editor of choice.

## Working Remotely via DataHub

Working *remotely* means using an environment that someone else set up
for you on a computer far, far away, usually through the browser. This
is the way you wrote code in DSC 10, for instance. There\'s nothing
wrong with this, *per se*, and it is simpler, but you should think of
this option as developing with \"training wheels\". Eventually, you will
need to learn how to set up your own Python environment, and now is as
good a time as any.

There are servers available to use at
[datahub.ucsd.edu](datahub.ucsd.edu). These are a lot like the
DataHub servers that you used in DSC 10, however they are customized
for this course. After logging in with your UCSD account, you will be
taken the familiar juptyer landing page. The server you are logged into
has \~4GB of RAM available, and has Python with all the necessary
packages.

### ⚠️ Warning!

DataHub outages are not uncommon, and they can be expected to occur once
or twice per quarter (sometimes more). Outages typically last for a few
hours or less, but they can prevent you from working on your assignment.

Since we do not manage DataHub, we cannot make any guarantees about its
availability. DataHub crashes that prevent you from turning in or
working on your assignment near the deadline are typically handled via
the usual [slip day](../syllabus) mechanism. If DataHub
has been down for a long time (more than 24 hours), let us know and
we\'ll consider a blanket extension -- though this has very rarely
(never?) happened.

Our advice is to use a local development environment, or to at least
have one as available as a backup option. If you decide to use DataHub
as your first choice, you should keep an extra slip day or two in
reserve in case the server crashes.

### Installing or Updating Python Packages

To update a package (e.g. `pandas`) on DataHub, you\'ll need to use the
command line. To do this, open "New \> Terminal" and type:

`mamba install --user --upgrade pandas`

followed by the enter key to run the command.

One package that you\'ll likely need to install is `otter-grader`. This
package provides the autograder that checks your answers in the labs and
projects.

### JupyterLab

The remote servers have a development environment installed on them,
however, it's non-intuitive how to access it. Once on the landing page,
the url should read something like:

`https://datahub.ucsd.edu/user/USER/tree`

You can access the IDE (integrate development environment) by changing
\"tree\" to \"lab\". This brings up JupyterLab. The url should look
something like this:

`https://datahub.ucsd.edu/user/USER/lab`

For more information on this IDE, you can see read about it here. From
within JupyterLab, you can:

-   Use a Python console
-   Run Jupyter notebooks
-   Use a terminal (e.g. to pull git repos)
-   Develop Python code in .py files

### Git

Whether you work locally or use DataHub, you'll need to pull assignments from GitHub. If you work on DataHub, you'll **have** to pull from GitHub using the command-line. To do this, open "New \> Terminal" and, to get the course repository for the first time, type:

    git clone https://github.com/dsc-courses/dsc80-2023-fa

Then, open up the file-tree in the original Jupyter tab, and you should see all the
course files now there. If you have already cloned the repository, and
just want to get the latest files, type `git pull` and you should see
the updated files.

### Troubleshooting DataHub

**What if I accidentally clicked a different class instead of DSC 80 when logging into DataHub, or what if my DataHub doesn't load?**

1. If you are already logged into DataHub, click "Control Panel" in the top right. (If your DataHub never launched in the first place, proceed to the next step.)

2. In the toolbar at appears at [datahub.ucsd.edu](https://datahub.ucsd.edu), click "Services" then click "manual-resetter", then click "Reset". If a pop-up box appears, that's okay.

3. Log back into DataHub again and it should allow you to select a course – select DSC 80. -->
