Basics of Linux and SAC
====

# 1. Aha, log in to a Linux environment

Linux is always the best choice for scientific computing. Not-surprisingly,
the PHYS3070/PHYS6070 labs are in Linux environment. The linux environment can
be on your computer or on a remote server. In this lab, we choose the 2nd option
to make it simple. We have set up a remote server (`compute2`) at RSES for you. You can log in to it from your
computer no matter which operating system you are using, Windows or MacOS.

On Windows, you can download, install, and run [putty](https://www.putty.org/) to log in to the `compute2`.
You will need to install [xming](https://cc.jlab.org/windows/X11onWindows) as well for forwarding
graphic user interface. Those two softwares are pre-installed for you on RSES computers. If
you like, you can install and run them on your laptop. To use them, the manual is [here](https://github.com/sheng09/PHYS3070-6070-Lastest/blob/main/materials/Basics/How-to-access-RSES-server.pdf).

On MacOS, you can open the application `Terminal` and run commands below to log in:
```shell
ssh  -XY  your_user_name@compute2.rses.anu.edu.au
# after typing the password, you will be on the server compute2
```

**NOTE**. If you are off campus, you will need to install and run ANU [GlobalProtect](https://services.anu.edu.au/information-technology/login-access/remote-access). You may need to ask the GlobalProtect Service Desk to allow you the permission to access RSES servers. Contacts of the Service Desk are on the [GlobalProtect](https://services.anu.edu.au/information-technology/login-access/remote-access) website.

# 2. Basics of Linux
Here we just list a few frequently-used Linux commands:
- `ls` or `ls directory_name` : This will list the files in the current directory or the specified
directory or filename. When specifying a directory or filename you may use wildcards
such as `*` and `?`. An explanation of some wildcards is included in below.
- `cd directory_name` : Change the current working directory. In default,
`cd` will go to your home directory. `cd ..` will go up one directory. Obviously, `cd ../..` will go up for twice.
- `mkdir directory_name` : This creates a new directory with the user specified name.
- `touch filename` : Create an empty new file. Linux does not care the format of a file. It is user's choice to store
whatever things, plain texts or binary data, in a file.
- `cp file_to_copy new_file_name` or `cp -r folder_to_copy new_folder_name` : This copy a file or a folder.
- `mv file1 file2` : Move file1 to file2. If file2 is a directory than file1 is moved
to the directory named file2. If file2 is a filename, then Unix essential renames file1 to
file2
- `rm file1 files2...` or `rm -r folder1 folder2...` : Remove the files listed after the command. Linux will ask if you
want to remove each file before deletion. If you want to suppress the safeguard, type `rm -rf file1 file2...`.
I would not recommend using this option as you can accidentally delete files
- `pwd` : This simply returns the current directory.
- `man linux_command` : Display the manual page for any command. e.g., `man ls`.
- `echo a string` : Print a string.
- `cat file1 file2...` : Concatenate and displays text and ASCII files.
- `tail filename -n 10` : Display the end of a text or ASCII file for the last 10 lines. You can use other numbers.
- `head filename -n 10` : Display the beginning of a text or ASCII file for the first 10 lines. You can use other numbers.
- `gv filename` : Display a postscript file using ghostview.

You can also have a look at [The Linux command line for beginners](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview)

## Wildcards
Wildcards are generally used when searching for files but do not know or do not wish to type the entire file name.
- `*` matches any number of characters in a filename including none. For example `*.ps` would find all postscript files in a directory.
- `?` matches a single character in a filename.
- `[]` Usually used to find a range of files by name the brackets represent a single character. For example
- `[A-B]*.BHZ` would find all files that have `A` or `B` as the first letter and end with `.BHZ`.
- `~` expands to the name of your home directory.

## Edit a plain text file
Well, you can simply edit a plain text file with so many softwares. To make it simple,
you can use `gedit`. You can run the command:

```shell
gedit filename
```

that will open the gedit interface for you to edit the file. However, it will occupy your terminal until you close it.
So it is better to run it and put it in the background with the command:

```shell
gedit filename &
```

in which the character `&` at the end means to put the running program in the background. You can use it for any other programs. You
can list all your programs that are running in the background:

```shell
jobs
```

## Quiz
The quiz here is just for letting you test yourself.
- Can you make a new directory, and inside the directory create several new files?
- Can you write something to the new files, and print the content of the file?
- Can copy other files and folders somewhere else into this new fold?
- Make sure you do correct manipulations of files/folders in correct folder. If not sure, check where you are with `pwd`.

## More materials
The more you know about Linux, the easier your life will be with scientific computing. There are so many learning materials for free on internet. If you are happy, please read, practice, and test yourself.

# 3. Basics of SAC
SAC (Seismic Analysis Code) is a program used to analyze and display seismic data, usually earthquake waveforms, that
is stored in sac format. It has its own set of premade functions that will read, write, process, and display data. There will be further
explanation of these functions later in the semester.

You can simply run `sac` to start the SAC program in the terminal. Full manual for using SAC is [here](http://www.iris.edu/manuals/sac/manual.html).
