## Performance testing Using JMETER

**Setup JMETER using WSL**

- download binary files from  this location 
- [Download](https://jmeter.apache.org/download_jmeter.cgi)
- Extract the same

- open wsl and cd ~
- mv /mnt/c/Users/NEW/Downloads/apache-jmeter-5.6.3/apache-jmeter-5.6.3/ jmeter
- use as per your username and move entire jmeter folder to jmeter inside ubuntu.

*set Environment variables*

```bash
echo 'export JMETER_HOME=~/jmeter' >> ~/ .bashrc
echo 'export PATH=$JMETER_HOME/bin:$PATH' >> ~/ .bashrc
source ~/ .bashrc

## Verify JMETER Version
jmeter --version

```
