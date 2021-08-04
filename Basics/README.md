Basics of Linux and SAC
====

# 1. Aha, log in to Linux environments

Linux is always the best choice for scientific computing. Not-surprisingly,
the PHYS3070/PHYS6070 labs are in Linux environment. The linux environment can
be on your local computer or on a remote server. In this lab, we choose the 2nd option
to make it simple. We have set up a remote server (`compute2`) at RSES for you.

You will log in to the `compute2` via two methods: 1) terminal method and 2)
Jupyter-lab method. Both are necessary for this lab. The former is necessary for
running SAC. The latter will be more handy for using Python3.

## 1.1 Terminal method
You need to download and install a few things. Choose your system and follow steps below.

- Windows
    - Download and install [OpenSSH](https://www.mls-software.com/files/setupssh-8.5p1-1.exe).
    - Download, install, and run [Xming](https://sourceforge.net/projects/xming/). If nothing happens, do no worry as the Xming is running properly in the background. You can check Xming in your system tray.
    - Run the `cmd` from Start, and run commands below.
    (**Note!!!** Please replace the user name `student01` with yours listed in the table below.)
        ```bash
        mkdir \dev
        mkdir \dev\tty
        set DISPLAY=127.0.0.1:0
        ssh -XY student01@compute2.rses.anu.edu.au
        ```
        Follow the prompts and type your password.

    **Alternatively**, if your cannot install OpenSSH (e.g., you do not have administrator permission), then you can use Putty following the steps [here](https://github.com/sheng09/PHYS3070-6070-Latest/blob/main/Basics/putty_windows.md#1-log-in-to-linux-server-via-putty).

- MacOS
    - Download, install and run [XQuartz](https://github.com/XQuartz/XQuartz/releases/download/XQuartz-2.8.1/XQuartz-2.8.1.dmg). You can just minimize or close all pop-up windows.
    - Run the application `Terminal`, and run commands below.
    (**Note!!!** Please replace the user name `student01` with yours listed in the table below.)
        ```bash
        ssh -XY student01@compute2.rses.anu.edu.au
        ```
        Follow the prompts and type your password.

- Linux
    - Open a terminal, and run commands below.
    (**Note!!!** Please replace the user name `student01` with yours listed in the table below.)
        ```bash
        ssh -XY student01@compute2.rses.anu.edu.au
        ```
        Follow the prompts and type your password.

## 1.2 Jupyter-lab method
Jupyter-lab is handy for using Python3. The same, You need to download and install a few things. Choose your system and follow steps below.

- Windows
    - If have not, please download and install [OpenSSH](https://www.mls-software.com/files/setupssh-8.5p1-1.exe).
    - Run a new `cmd` from Start, and run commands below.
    (**Note!!!** Please replace the 9000 with your four digits listed in the table below. Please replace the user name `student01` with yours listed in the table below.)
        ```bash
        ssh -N -L 8000:localhost:9000 student01@compute2.rses.anu.edu.au
        ```
    - Open a web browser on your local computer, and go to `http://localhost:8000`. In the webpage, use the password provided. (Ask sheng.wang(at)anu.edu.au for your password if you forget)

    If your cannot install or use OpenSSH (e.g., you do not have the administrator permission), then you can use Putty following the steps [here](https://github.com/sheng09/PHYS3070-6070-Latest/blob/main/Basics/putty_windows.md#2-log-in-to-jupyter-lab-via-putty).

- MacOS
    - If have not, please download and install [XQuartz](https://github.com/XQuartz/XQuartz/releases/download/XQuartz-2.8.1/XQuartz-2.8.1.dmg).
    - Open a new window for application `Terminal`, and run commands below.
    (**Note!!!** Please replace the 9000 with your four digits listed in the table below. Please replace the user name `student01` with yours listed in the table below.)
        ```bash
        ssh -N -L 8000:localhost:9000 student01@compute2.rses.anu.edu.au
        ```
    - Open a web browser on your local computer, and go to `http://localhost:8000`. In the webpage, use the password provided. (Ask sheng.wang(at)anu.edu.au for your password if you forget)

- Linux
    - Open a terminal, and run commands below.
    (**Note!!!** Please replace the 9000 with your four digits listed in the table below. Please replace the user name `student01` with yours listed in the table below.)
        ```bash
        ssh -N -L 8000:localhost:9000 student01@compute2.rses.anu.edu.au
        ```
    - Open a web browser on your local computer, and go to `http://localhost:8000`. In the webpage, use the password provided. (Ask sheng.wang(at)anu.edu.au for your password if you forget)

| Name       | 4 digits | User name | Password for ssh |  Password for Jupyter-lab|
|:-----------|:--------:|:---------:|:----------------:|:---:|
|Cole        | 9020     | student02 |                  |     |
|Maximilian  | 9030     | student03 |                  |     |
|Joshua      | 9040     | student04 |                  |     |
|Tianshi     | 9050     | student05 |                  |     |
|Jason       | 9060     | student06 |                  |     |
|Patrik      | 9080     | student08 |                  |     |
|Ruipeng     | 9090     | student09 |                  |     |

**NOTE**. If you are off campus, you need to install and run ANU [GlobalProtect](https://services.anu.edu.au/information-technology/login-access/remote-access). You may need to ask the GlobalProtect Service Desk for help. Contacts of the Service Desk are on the [GlobalProtect](https://services.anu.edu.au/information-technology/login-access/remote-access) website.

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
- Can copy files and folders somewhere else into this new fold?
- Can you re-name, remove some files and folders?
- Make sure you do correct manipulations of files/folders in correct folder. If not sure, check where you are with `pwd`.

## More materials
The more you know about Linux, the easier your life will be with scientific computing. There are so many learning materials for free on internet. If you are happy, please read, practice, and test yourself.


# 3. Basics of SAC
SAC (Seismic Analysis Code) is a program used to analyze and display seismic data, usually earthquake waveforms, that
is stored in sac format. It has its own set of premade functions that will read, write, process, and display data. There will be further
explanation of these functions later in the semester.

Log in to the `compute2` using the  "Terminal method". Then, simply run `sac` to start the SAC program. The sac has its own commands, and the frequently-used include:

- `r filename1 filename2...` : Read sac files into the memory.
- `qdp off` : Turn off the "quick and dirty plot" option.
- `p1` : Plot seismograms for the sac files in the memory.
- `ppk` : Interactive GUI for picking.
- `lh` : Print the header information that describe the seismograms.
- `bp c 0.05 0.2 n 2 p 2` : Apply bandpass filter to the seismograms. `c 0.05 0.2` means the frequency band is 0.05-0.2 Hz, `n 2` 2nd-order, `p 2` two-pass or zero-phase filter.
- `lp c 0.5 n 2 p 2` : Lowpass filter.
- `hp c 0.1 n 2 p 2` : highpass filter.

  Note: each time when you run a filter, it will modify the seismograms  and hence the original seismograms do not eixst in the memory. Therefore, you need to read the seismograms again if you want to change your filter settings.
- `w newfilename1 newfilename2...` : Write seismograms into files. The number of output filenames should match the number of seismograms in the memory.
- `w append _processed` : Another usage to write seismograms into files. It will automatically name the output filenames by appending text to each name in the current read filelist.
- `w over` : Use current read filelist as write filelist.  Overwrite files on disk with data in memory. Be careful to use this writing method.
- `wh` : Overwrites the headers on disk with those in memory. The writing will not touch the time series.
- `q`: Quit.

The tutor will present some examples. Full manual for using SAC is [here](http://ds.iris.edu/files/sac-manual/).


You may notice that there are terminals in Jupyter-lab. Yes, you can run `sac` in those terminals, but they do not support X window. That means it does not allow interactive SAC GUI that is necessary for manipulating seismograms.



# [NEXT Lab1](https://github.com/sheng09/PHYS3070-6070-Latest/tree/main/Lab1#lab1---locating-earthquakes)