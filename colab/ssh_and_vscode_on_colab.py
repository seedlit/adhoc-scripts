# useful article - https://towardsdatascience.com/colab-free-gpu-ssh-visual-studio-code-server-36fe1d3c5243

# STEP1:  you have to do is register a free account on ngrok. Then, you need to copy your auth token.

# refer - https://stackoverflow.com/questions/48459804/how-can-i-ssh-to-google-colaboratory-vm
# STEP2 - Install colab_ssh
!pip install colab_ssh --upgrade
from colab_ssh import launch_ssh
launch_ssh("YOUR_NGROK_AUTH_TOKEN", "SOME_PASSWORD")

"""You should get the connection parameters (pay attention to the port).
Now you can connect to the Colab VM by using the provided details, 
for example: ssh -p 15892 root@0.tcp.ngrok.io, 
where 15892 is the random port number you need to change. 
Naturally, you will be prompted for the previously set password."""

# After connection with VM, you can install your preferred utilities
# sudo apt install htop
# pip3 install --upgrade pip
# sudo apt-get install python3.7-dev python3.7-venv

# to copy files between VM and local
# scp -P 14620 root@4.tcp.ngrok.io:/root/ee/repo/netherlands_dsms.zip ./


# Connecting with VS Code in browser
# Now, let’s download, install and run the server version of Visual Studio Code.
!curl -fsSL https://code-server.dev/install.sh | sh > /dev/null
!code-server --bind-addr 127.0.0.1:9999 --auth none &
# Note that the second command will keep running
# Now in a terminal, run this command
ssh -L 9999:localhost:9999 root@0.tcp.ngrok.io -p 14407
# open http://127.0.0.1:9999/ in browser


# to install conda - https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-20-04
# getting started with conda - https://conda.io/projects/conda/en/latest/user-guide/getting-started.html



