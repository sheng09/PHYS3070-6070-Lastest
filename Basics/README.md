Basics of Linux and SAC
====

# 1. Aha, log in to a Linux environment

Linux is always the best choice for scientific computing. Not-surprisingly,
the PHYS3070/PHYS6070 labs are in Linux environment. The linux environment can
be on your computer or on a remote server. In this lab, we choose the 2nd option
to make it simple. We have set up a remote server (`compute2`) at RSES for you. It is based on
Jupyter-lab, handy to use. You can log in from your
computer no matter which operating system you are using, Windows or MacOS. You need to download and install a few things. Choose your system and follow steps below.


## Windows 7
- Download and install [OpenSSH](https://www.mls-software.com/files/setupssh-8.5p1-1.exe).
- Download, install, and run [xming](https://sourceforge.net/projects/xming/).
- Run the `cmd` from Start, and run commands below:
    ```bash
    # NOTE: 1. Please replace the 9000 with your four digits listed in the table below
    # NOTE: 2. Please replace the account name student01 with yours listed in the table below
    ssh -N -L 8888:localhost:9000 student01@compute2.rses.anu.edu.au
    # You may need to type the password here
    ```
- Open a web browser on your local computer, and go to `http://localhost:8888`. In the webpage, use the password provided. (Ask sheng.wang(at)anu.edu.au for your password if you forget)

## Windows 10 or Higher versions
- Some versions of Windows 10 have built-in `OpenSSH` tools. You may need to check Microsoft [help](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse).
Or you can just  download and install [OpenSSH](https://www.mls-software.com/files/setupssh-8.5p1-1.exe). (btw, complain to Microsoft for problems and bad experiences.)
- Download, install, and run [xming](https://sourceforge.net/projects/xming/).
- Run the `cmd` from Start, and run commands below:
    ```bash
    # NOTE: 1. Please replace the number 9000 with your four digits listed in the table below
    # NOTE: 2. Please replace the account name student01 with yours listed in the table below
    ssh -N -L 8888:localhost:9000 student01@compute2.rses.anu.edu.au
    # You may need to type the password here
    ```
- Open a web browser on your local computer, and go to `http://localhost:8888`. In the webpage, use the password provided. (Ask sheng.wang(at)anu.edu.au for your password if you forget)

## MacOS
- Download and install [XQuartz](https://github.com/XQuartz/XQuartz/releases/download/XQuartz-2.8.1/XQuartz-2.8.1.dmg).
- Run the application `Terminal`, and run commands below:
    ```bash
    # NOTE: 1. Please replace the number 9000 with your four digits listed in the table below
    # NOTE: 2. Please replace the account name student01 with yours listed in the table below
    ssh -N -L 8888:localhost:9000 student01@compute2.rses.anu.edu.au
    # You may need to type the password here
   ```
- Open a web browser on your local computer, and go to `http://localhost:8888`. In the webpage, use the password provided. (Ask sheng.wang(at)anu.edu.au for your password if you forget)

| Name               | 4 digits | User name | Password for ssh |  Password for Jupyter-lab|
|:-------------------|:--------:|:---------:|:----------------:|:---:|
|Cole Johnson        | 9020     | student02 |                  |     |
|Maximilian Williams | 9030     | student03 |                  |     |
|Joshua Taubman      | 9040     | student04 |                  |     |
|Tianshi Zhou        | 9050     | student05 |                  |     |
|Jason Aramideh      | 9060     | student06 |                  |     |
|Patrik Rilko        | 9070     | student07 |                  |     |


**NOTE**. If you are off campus, you will need to install and run ANU [GlobalProtect](https://services.anu.edu.au/information-technology/login-access/remote-access). You may need to ask the GlobalProtect Service Desk to allow you the permission to access RSES servers. Contacts of the Service Desk are on the [GlobalProtect](https://services.anu.edu.au/information-technology/login-access/remote-access) website.

# 2. Basics of Linux
In the Jupyter-lab, you can launch a `Terminal`, then Linux here you go:)

Here we list a few frequently-used Linux commands:
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

You can also have a look at [The Linux command line for beginners](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview).

## Wildcards
Wildcards are generally used when searching for files but do not know or do not wish to type the entire file name.
- `*` matches any number of characters in a filename including none. For example `*.ps` would find all postscript files in a directory.
- `?` matches a single character in a filename.
- `[]` Usually used to find a range of files by name the brackets represent a single character. For example
- `[A-B]*.BHZ` would find all files that have `A` or `B` as the first letter and end with `.BHZ`.
- `~` expands to the name of your home directory.

## Edit a plain text file
Well, you can edit a plain text file in many ways. In Jupyter-lab, you can find all your files in the left panel. Double-click a file and then you can edit it. (**DO NOT** forgot to save the file after editing.)

## Quiz
The quiz here is just for letting you test yourself.
- Can you make a new directory, and inside the directory create several new files?
- Can you write something to the new files, and print the content of the files?
- Can copy other files and folders somewhere else into this new fold?
- Can you re-name, remove those files and folders?
- Make sure you do correct manipulations of files/folders in correct folder. If not sure, check where you are with `pwd`.

## More materials
The more you know about Linux, the easier your life will be with scientific computing. There are so many learning materials for free on internet. If you are happy, please read, practice, and test yourself.


# 3. Basics of SAC
SAC (Seismic Analysis Code) is a program used to analyze and display seismic data, usually earthquake waveforms, that
is stored in sac format. It has its own set of premade functions that will read, write, process, and display data. There will be further
explanation of these functions later in the semester.

In the Jupyter-lab, lanuch a `Terminal` and simply run `sac` to start the SAC program. Full manual for using SAC is [here](http://ds.iris.edu/files/sac-manual/).
