# Assignment 0
Thoroughly read the syllabus sections on "Programming assignments" and "Grading", including the links referenced within. 
These sections give good tips, tricks, hints, and instructions for programming assignments, including how to submit via Git: 

https://taylor.git-pages.mst.edu/index_files/Security.html

## Virtual Machine (VM)
Install a virtual machine (Debian 10 this year), following the instructions on the website for configuring it.
https://taylor.git-pages.mst.edu/index_files/DataStructuresLab/Content/VirtualMachines.html

## Git
From within the virtual machine, open a terminal and clone this repository using the bash command line.
The resulting folder is your repository.
Use the `cd` command to enter the directory. 
This is where you should do and store your work for each assignment.

## Basic Bash
From within the virtual machine, read and perform the commands in the following guide on how to manage basic Linux/Unix command line work:
http://linuxcommand.org/lc3_learning_the_shell.php 
Read the whole thing; our next assignment will assume you know bash.

Add the `~/.bash_history` file (which shows your command history from the tutorial) into your repository; 
leave it named .bash_history (do not rename it).

Note: it is a hidden file (there is a . preceding it), so might not display as you expect in the git interface!
Commit your changes.

## Your first Python3 program
From within the virtual machine, add a file titled pa00.py to the repository.
It should take input via command line arguments, and generate output by writing a file.
For example

`python3 pa00.py sample_input.txt my_output.txt`

or 

`./pa00.py sample_input.txt my_output.txt`

would output a file that contained the same as `sample_output.txt`

I.e., the input file containing "hello world 6", would output a file with "hello world\n" in it 6 times.

Note: the filename and EXACT text should be used; capitalization matters, so check it!

## Testing
To test if your program works, do the following:

### diff
In the virtual machine, run at the bash command line:
```sh
$ cat sample_output.txt

$ python3 pa00.py "sample_input.txt" "my_output.txt"
or
$ ./pa00.py "sample_input.txt" "my_output.txt" # if you have the right shebang at the top of your file, and it is executable.

$ diff --color "sample_output.txt" "my_output.txt"
$ diff -y --color "sample_output.txt" "my_output.txt"

$ vim -d "sample_output.txt" "my_output.txt"
# To exit vim, type esc followed by :q
```
Take a screenshot of the result of these commands, and name it diff.png.
Capitalization matters, including of the png part. 
Check it!

### Debuggers: python3-pudb and python3-spyder 
1. Type the following:

```sh
pudb3 pa00.py
```
Practice stepping into the function and through the for loop with pudb.
Take a screenshot while you are stil in pudb3 (before quitting), and name it debug1.png.

2. Open the same file in Spyder3 and practice stepping through it using the debugger 
(read the manual for help).
Take a screenshot and name it debug2.png

## Basic bash 
Write a script, `pa00.sh` that acts the exact same as the python script above, 
but you run as follows instead:

`bash pa00.sh sample_input.txt my_output.txt`

or 

`./pa00.sh sample_input.txt my_output.txt`

## Git: add, commit, push
From within the virtual machine, add, commit, and push all the non-generated files. 
This means add your py and png files, but not files like a.out or *.pyc
Verify you can see the files on git-classes.
If you can see the correct files on git-classes in your master branch, your submission is complete.
Make sure all the requested files are in the root directory of the repository unless otherwise specified.

## Double check everything
Re-read the section of the syllabus titled: 
"Things you should check before you submit"
Make sure to check you do not have extra newlines, spaces, or mis-spellings.
Capitals matter, so double check file names and extensions.

## This time only, we are giving you the actual auto-grader BEFORE the assignment
This is for your fun and perspective, so you can see the kind of logic we might use.
This is a shallow example, and there will be more nuanced versions to come.
We will not generally give out the autograder itself, but may give hints to its function, or limited examples.
If you miss points because you did not at least read this code, we will have no mercy! 

Note: This time, you could game the autograder by just having some junk files with the right names; we do actually spot check manually quite a few students for our own validation, and reserve the right to dock points for such things as hard-coding! 

