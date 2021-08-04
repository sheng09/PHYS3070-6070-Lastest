Reset student??@compute2 and run commands below to start jupyter-lab in tha background


```bash
#1. login
# ssh student??@compute2.rses.anu.edu.au

#2. install python3 packages
pip3 install --user matplotlib
pip3 install --user cartopy
pip3 install --user numpy
pip3 install --user obspy
pip3 install --user pandas

#3. start jupyter-lab server
jupyter server --generate-config
jupyter server $password$
nohup jupyter-lab --port $XXXX$ --no-browser & # replace XXXX to four digits
```

```
```
