
# SonarQube Setup on macOS

###  1. Install Homebrew
If you don’t have Homebrew installed, run:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Verify:
```bash
brew --version
```

---

###  2. Install Java (SonarQube requires Java 17 or later)
```bash
brew install openjdk@17
brew link --force --overwrite openjdk@17
```

Set environment variables (add to `~/.zshrc` or `~/.bashrc`):
```bash
export JAVA_HOME=$(/usr/libexec/java_home -v17)
export PATH=$JAVA_HOME/bin:$PATH
```

Verify:
```bash
java -version
```

---

##  Install and Configure PostgreSQL

Install PostgreSQL:
```bash
brew install postgresql
brew services start postgresql
```

Create SonarQube database and user:
```bash
psql postgres
```
Inside PostgreSQL shell:
```sql
CREATE USER sonar WITH ENCRYPTED PASSWORD 'sonar';
CREATE DATABASE sonarqube OWNER sonar;
GRANT ALL PRIVILEGES ON DATABASE sonarqube TO sonar;
\q
```

---

## Download and Setup SonarQube

Download the latest LTS version:
```bash
cd /opt
sudo curl -O https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-10.6.0.92116.zip
```

Unzip and rename:
```bash
sudo unzip sonarqube-10.6.0.92116.zip
sudo mv sonarqube-10.6.0.92116 sonarqube
```

---

##  Configure SonarQube

Edit configuration:
```bash
sudo nano /opt/sonarqube/conf/sonar.properties
```

Uncomment and set the following:
```
sonar.jdbc.username=sonar
sonar.jdbc.password=sonar
sonar.jdbc.url=jdbc:postgresql://localhost/sonarqube

sonar.web.host=127.0.0.1
sonar.web.port=9000
```

Save and exit (`Ctrl + O`, `Ctrl + X`).

---

## Adjust Virtual Memory

SonarQube’s Elasticsearch requires higher memory limits.

```bash
sudo sysctl -w vm.max_map_count=262144
```

To make permanent:
```bash
sudo nano /etc/sysctl.conf
```
Add this line:
```
vm.max_map_count=262144
```
Then restart your system.

---

##   Start SonarQube

Navigate to the macOS binary folder:
```bash
cd /opt/sonarqube/bin/macosx-universal-64
```

Start SonarQube:
```bash
./sonar.sh start
```

Check status:
```bash
./sonar.sh status
```

Stop SonarQube:
```bash
./sonar.sh stop
```

---

##  Access the Web Interface

Once SonarQube is running, open:
[http://localhost:9000](http://localhost:9000)

**Default credentials:**
```
Username: admin
Password: admin
```

You’ll be asked to change the password on first login.


