## Performance testing Using JMETER

**Setup JMETER using WSL**

- to run jmeter required jdk as well use below commands
```bash
sudo apt update
sudo apt install openjdk-17-jre -y
java -version
```
- download binary files from  this location 
- [Download](https://jmeter.apache.org/download_jmeter.cgi)
- Extract the same

- open wsl and cd ~
- mv /mnt/c/Users/NEW/Downloads/apache-jmeter-5.6.3/apache-jmeter-5.6.3/ jmeter
- use as per your username and move entire jmeter folder to jmeter inside ubuntu.

*set Environment variables*

```bash
# move to the bin folder
echo 'export JMETER_HOME=~/jmeter' >> ~/.bashrc
echo 'export PATH=$JMETER_HOME/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
# Check version
jmeter --version
# Incase permission denied use below command
chmod +x ~/jmeter/bin/jmeter
# Check version again

# now just run jmeter command 
jmeter
# it will start JMETER you can process with performace Testing
# Tetsing Screenshorts Included in pdf file Please check
```
