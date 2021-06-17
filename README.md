# Server Setup

### Update the system

```
$ sudo apt update && sudo apt -y upgrade && sudo apt -y autoremove
```

### Change user password

```
$ sudo passwd {username}
```

### Create sudo user

```
$ sudo adduser {user}
$ sudo adduser {user} sudo
```

Create user without home

```
sudo adduser --system --no-create-home USERNAME
```

### Install Open SSH server

```
$ sudo apt install openssh-server
```

### Install basic server software

```
$ sudo apt install supervisor htop ufw python3 snapd curl unzip
$ sudo snap install core && sudo snap refresh core
```

### Generate SSH key

```
# Ed25519 algorithm
$ ssh-keygen -t ed25519 -C christopher.guzman.monsalvo@gmail.com

# 4096 bits
$ ssh-keygen -t rsa -b 4096 -C christopher.guzman.monsalvo@gmail.com
```

Show ssh key
```
# Ed25519 algorithm
$ cat ~/.ssh/id_ed25519.pub

# 4096 bits
$ cat ~/.ssh/id_rsa.pub
```

### Copy SSH ID identity to server

```
$ ssh-copy-id christopher@host.com
```

### Installing Git Prompt
[Repository](https://github.com/magicmonty/bash-git-prompt)

```
$ git clone https://github.com/magicmonty/bash-git-prompt.git ~/.bash-git-prompt --depth=1
```
Add to the ~/.bashrc:

```
if [ -f "$HOME/.bash-git-prompt/gitprompt.sh" ]; then
    GIT_PROMPT_ONLY_IN_REPO=1
    source $HOME/.bash-git-prompt/gitprompt.sh
fi
```

Reload the bash:

```
. ~/.bashrc
```

# Installing Docker

```
$ sudo apt install docker.io
$ sudo systemctl enable docker
$ sudo groupadd docker
$ sudo usermod -aG docker $USER
$ newgrp docker
```

Installing docker-compose

```
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
$ sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```


# Installing Open JDK

```
$ sudo apt install -y openjdk-11-jre-headless openjdk-11-jdk-headless
```

View java alternatives
```
$ sudo update-alternatives --display java
```

Uninstall Open Java
```
$ sudo apt-get purge openjdk-*
```

# Installing Java Oracle

[Reference](https://docs.datastax.com/en/jdk-install/doc/jdk-install/installOracleJdkDeb.html)

Create the JDK directory

```
$ sudo mkdir -p /usr/lib/jvm
```

Go to [Oracle web page](https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html) and download the JDK file "Linux x64 Compressed Archive" - **jdk-8u281-linux-x64.tar.gz**.

Uncompress the JDK file:

```
$ sudo tar zxfv jdk-8u281-linux-x64.tar.gz -C /usr/lib/jvm
```

Install the new alternative
```
$ sudo update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/jdk1.8.0_291/bin/java" 1

$ sudo update-alternatives --install "/usr/bin/javac" "javac" "/usr/lib/jvm/jdk1.8.0_291/bin/javac" 1
```

Set the new alternative as default
```
$ sudo update-alternatives --set java /usr/lib/jvm/jdk1.8.0_291/bin/java
$ sudo update-alternatives --set javac /usr/lib/jvm/jdk1.8.0_291/bin/javac
```

# Installing Gradle

[Reference](https://gradle.org/install/)

Download and unzip gradle from [here](https://gradle.org/install/)

```
$ sudo mkdir /opt/gradle
$ sudo unzip -d /opt/gradle gradle-7.0-bin.zip
```

Add gradle to the PATH environment variable in `.bashrc` file

```
$ vim ~/.bashrc
```

Add:

```
export PATH=${PATH}:/opt/gradle/gradle-7.0/bin
```

Reload the bash
```
$ . ~/.bashrc
```


# Installing Android SDK

Create the `android-sdk` folder into `/opt` directory

```
$ sudo mkdir /opt/android-sdk
$ sudo chmod 777 -R /opt/android-sdk
```

Get the android SDK from [here](https://developer.android.com/studio#downloads)

Navigate to 'Command line tools only' and download it.

Unzip and copy it into `/opt/android-sdk/`

```
$ unzip -d /opt/android-sdk commandlinetools-linux-6858069_latest.zip
```

Got to Android SDK and create the latest folder
```
$ cd /opt/android-sdk/cmdline-tools
$ sudo mkdir latest
```

Move files into latest folder
```
$ sudo mv NOTICE.txt bin/ lib/ source.properties latest/
```

Add env variables to `~/.bashrc` file
```
export ANDROID_SDK_ROOT=/opt/android-sdk
export JAVA_HOME=/usr/lib/jvm/jdk1.8.0_291
export PATH=${PATH}:/opt/android-sdk/cmdline-tools/latest/bin
```

Reload the bash
```
$ . ~/.bashrc
```

Install Android SDK

[sdkmanager reference](https://developer.android.com/studio/command-line/sdkmanager)
```
$ sdkmanager "platform-tools" "platforms;android-29" "build-tools;29.0.3"
```

# Data Bases

### Install MySQL

```
$ sudo apt install mysql-server
```

### Install PostgreSQL
```
$ sudo apt install postgresql postgresql-contrib postgis
```
# Web Servers

### Nginx
```
$ sudo apt install nginx
```

Create app folder and deploy folders
```
$ sudo mkdir /var/www/apps
$ sudo chmod -R 777 /var/www/apps
$ cd /var/www/apps
$ mkdir qa staging master
```

# Apache
```
$ sudo apt install apache2
$ sudo a2enmod rewrite
$ sudo a2enmod ssl
$ sudo apt install php php-cli php-mcrypt libapache2-mod-php php-mysql
$ sudo apt-get install php-xml
$ sudo apt-get install php-mbstring
$ sudo apt-get install php-curl
```

### Python & VirtualEnvs
```
$ sudo apt install libpq-dev python-dev python3-dev build-essential python-setuptools postgresql-server-dev-all python3-distutils
```

Installing PIP

```
$ wget https://bootstrap.pypa.io/get-pip.py
$ sudo python3 get-pip.py
$ sudo pip install virtualenv virtualenvwrapper
```

Create env folder
```
$ sudo mkdir /opt/virtualenvs && sudo chmod -R 777 /opt/virtualenvs
```

Add env variables

```
$ vim ~/.bashrc
```
Add:
```
alias python=python3
alias pip=pip3
VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=/opt/virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```
Reload the bash:
```
$ . ~/.bashrc
```

### Installing NodeJS

[NodeJS](https://github.com/nodesource/distributions/blob/master/README.md)

[Fix watchers](https://www.nicesnippets.com/blog/solved-system-limit-for-number-of-file-watchers-reached-reactjs)

```
# Using Ubuntu
$ curl -fsSL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs

# Fix watchers
$ echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf
$ sudo sysctl -p
```

# Installing Jenkins

[Reference](https://www.jenkins.io/doc/book/installing/linux/)

```
$ wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -

# Or

$ wget -qO - https://pkg.jenkins.io/debian-stable/jenkins.io.key |
  sudo gpg --no-default-keyring --keyring gnupg-ring:/etc/apt/trusted.gpg.d/jenkins.gpg --import -
  
$ sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > \
    /etc/apt/sources.list.d/jenkins.list'
$ sudo apt update && sudo apt -y install jenkins
```

[Configure Nginx for jenkins](https://www.jenkins.io/doc/book/system-administration/reverse-proxy-configuration-nginx/)


Create SSH key for jenkins

[Reference](https://devops4solutions.medium.com/setup-ssh-between-jenkins-and-github-6ec7c7933244)

```
$ sudo -su jenkins
$ ssh-keygen
$ eval $(ssh-agent -s)
$ ssh-add ~/.ssh/id_rsa
```

Get public Key to be set in Github

```
$ sudo cat /var/lib/jenkins/.ssh/id_rsa.pub
```

Get private key to be set in Jenkins

```
$ sudo cat /var/lib/jenkins/.ssh/id_rsa
```

Run sudo on Jenkins without password

[Reference](https://sgoyal.net/2016/11/18/run-a-shell-from-jenkins-using-sudo-ubuntu/)

```
$ sudo visudo -f /etc/sudoers
```

Add:

```
jenkins ALL=(ALL) NOPASSWD: ALL
```

Save and run sudo commands with Jenkins and not pass any password

Add git credentials

```
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```


# Apache Cordova

[Reference](https://cordova.apache.org/)

Install Apache Cordova globally
```
$ sudo npm install -g cordova
```

Create Cordova App
```
$ cordova create cordova-app
```

Add platforms
```
$ cd cordova-app
$ cordova platform add browser
$ cordova platform add android
```

Run in the browser
```
$ cordova run browser
```

Build android App
```
$ cordova build android
```

# Create a React App with TypeScript

[Reference to create React App](https://create-react-app.dev/docs/adding-typescript/)

[Reference to add Sass](https://www.cluemediator.com/how-to-add-sass-or-scss-in-react)

Create the app and add Sass

```
$ npx create-react-app my-app --template typescript
$ npm i node-sass
```


# Working with MySQL

Login into the shell
```
$ mysql -h localhost -u root -p
```
Switch to DB
```
mysql> use mysql;
```
Change user password
```
mysql> SET PASSWORD FOR 'user'@'hostname' = PASSWORD('new-password');
mysql> FLUSH PRIVILEGES;
```

Create MySQL user
```
mysql> CREATE USER 'user'@'localhost' IDENTIFIED BY 'password'
mysql> GRANT ALL PRIVILEGES ON * . * TO 'user'@'localhost';
mysql> FLUSH PRIVILEGES;
```
Delete user
```
mysql> DROP USER 'user@'localhost';
```


# Working with PostgreSQL

Login into the shell
```
$ sudo -su postgres
$ psql
```

Common actions:
```
# Connect to DB
$ \c DBNAME

# List tables
$ \dt

# Create user
$ CREATE USER root PASSWORD 'root';

# Create Database
$ CREATE DATABASE sample WITH OWNER root;
$ GRANT ALL PRIVILEGES ON DATABASE sample TO root;

#Delete database
$ DROP DATABASE sample;
```

### Backup database
[Reference](https://www.digitalocean.com/community/tutorials/how-to-backup-postgresql-databases-on-an-ubuntu-vps)
```
$ sudo su - postgres
$ pg_dump postgres > postgres_db.bak
$ createdb -T template0 restored_database
$ psql restored_database < database.bak
```

### Using PostGIS
[Reference](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-postgis-on-ubuntu-14-04)
```
$ sudo -su postgres
$ psql -d DATABASE_NAME
$ CREATE EXTENSION postgis;
$ SELECT PostGIS_version();
```

# MongoDB

Dump Mongo DB
```
$ sudo mongodump --db newdb
```

DB backups

[Reference](https://www.digitalocean.com/community/tutorials/how-to-back-up-restore-and-migrate-a-mongodb-database-on-ubuntu-14-04)

```
$ sudo mkdir /var/backups/mongobackups
```

Single backup
```
$ sudo mongodump --db newdb --out /var/backups/mongobackups/`date +"%m-%d-%y"`

```

MongoDB backups with crontab
```
$ sudo crontab -e
```

Add:
```
3 3 * * * mongodump --out /var/backups/mongobackups/`date +"%m-%d-%y"`
```

Restore Mongo DB

```
$ sudo mongorestore --db newdb --drop /var/backups/mongobackups/01-20-16/newdb/
```


# Working with Supervisor

Create a file
```
$ sudo vim /etc/supervisor/conf.d/long_script.conf
```

Add:
```
[program:long_script]
directory=/home/user/
command=long.sh
autostart=true
autorestart=true
stderr_logfile=/var/log/long.err.log
stdout_logfile=/var/log/long.out.log
```

Reload the system
```
$ sudo supervisorctl reread
$ sudo supervisorctl update
```

Status, stop and start workers
```
$ sudo supervisorctl status
$ sudo supervisorctl stop <name>
$ sudo supervisorctl start <name>
$ sudo supervisorctl restart <name>
```


# Setting up UWF firewall

[Reference](https://www.digitalocean.com/community/tutorials/how-to-setup-a-firewall-with-ufw-on-an-ubuntu-and-debian-cloud-server)

```
$ sudo ufw status
```

Allow or deny ports or apps
```
$ sudo ufw allow ssh
$ sudo ufw allow 22/tcp
$ sudo ufw allow 443/tcp
$ sudo ufw allow 80/tc
$ sudo ufw deny 80/tcp
$ sudo ufw delete allow ssh
$ sudo ufw delete allow 80/tcp
$ sudo ufw status numbered
```

See the list of apps
```
$ sudo ufw app list
```

Enable / disable firewall

```
$ sudo ufw disable
$ sudo ufw enable
```

# Backup and install PIP requirements

```
$ pip freeze -l > requiriments.txt
$ pip install -r requiriments.txt
```

# Working with VirtualEnv

Use a virtualenv
```
$ workon <name>
```

List all virtualenv
```
$ workon
```

Create a virtualenv
```
$ mkvirtualenv -p /usr/bin/python3 <name>
```

Delete a virtualenv
```
$ rmvirtualenv <name>
```

# Supervisor + GUInicorn + Django

```
[program:app]
command=/home/${user}/.virtualenvs/app/bin/gunicorn --bind 0.0.0.0:4001 --workers 1 --reload  webpage.wsgi:application
directory=/var/www/apps/app/webpage/
autostart=true
autorestart=true
stderr_logfile=/var/log/apps/app/error.log
stdout_logfile=/var/log/apps/app/output.log
```


# Adding GZIP to Nginx

[Reference](https://www.digitalocean.com/community/tutorials/how-to-add-the-gzip-module-to-nginx-on-ubuntu-14-04)

```
$ sudo nano /etc/nginx/nginx.conf
```

Add:
```
gzip on;
gzip_disable "msie6";

gzip_vary on;
gzip_proxied any;
gzip_comp_level 6;
gzip_buffers 16 8k;
gzip_http_version 1.1;
gzip_min_length 256;
gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript application/vnd.ms-fontobject application/x-font-ttf font/opentype image/svg+xml image/x-icon;
```


# Nginx proxy configuration
```
server {
  listen   80;

  server_name iguzman.com www.iguzman.com.mx;

  location /static/ {
    autoindex on;
    expires 30d;
    add_header Vary Accept-Encoding;
    access_log off;
    alias /var/www/apps/iguzman/webpage/static/;
  }

  location / {
    proxy_pass http://127.0.0.1:4000/;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection 'upgrade';
    proxy_set_header Host $host;
    proxy_cache_bypass $http_upgrade;
  }
}
```


# SSL Free certificates

Installing Certbot on Nginx

[Reference](https://certbot.eff.org/lets-encrypt/ubuntufocal-nginx)


Verifying Snap
```
$ sudo apt update && sudo apt install snapd
```

Installing certbot
```
$ sudo snap install --classic certbot
$ sudo ln -s /snap/bin/certbot /usr/bin/certbot
```

Adding certificate to Apache server:
```
$ sudo certbot --apache -d example.com -d www.example.com
$ sudo service apahce2 restart
```

Adding certificate to Nginx server
``` 
$ sudo certbot --nginx -d example.com -d www.example.com
$ sudo service nginx restart
```

Renewing certificates automatically

```
$ sudo certbot renew --dry-run
```

```
$ sudo crontab -e
```

Add:
```
15 3 * * * /usr/bin/certbot renew --quiet
```


# Raspberry

To Share Wifi - Ethernet Connetion

```
$ nm-connection-editor
```

Get IP
```
$ sudo dhclient -r
```

Enable SSH Interface
```
$ sudo raspi-config
```
> Interfacing Options -> SSH -> YES -> OK

Some libraries
```
$ sudo apt-get install software-properties-common libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk
```
