# FROM python:3.11

# WORKDIR /app

# # RUN apt-get update && apt-get install -y chromium-driver

# RUN apt-get update && apt-get install -y wget gnupg ca-certificates

#    # Add Chrome repository and install Chrome browser
# RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
# RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
# RUN apt-get update && apt-get install -y google-chrome-stable

#    # Install ChromeDriver
# RUN apt-get install -yqq unzip
# RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$(google-chrome-stable --version | awk -F '[ .]' '{print $3}')/chromedriver_linux64.zip
# RUN unzip /tmp/chromedriver.zip -d /usr/local/bin/
# COPY  requirements.txt ./
# RUN pip install -r requirements.txt

# COPY . .

# FROM python:3.11

# WORKDIR /app

# # Install Chrome
# RUN apt-get update && apt-get install -y wget gnupg ca-certificates
# RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
# RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
# RUN apt-get update && apt-get install -y google-chrome-stable

# # Install ChromeDriver
# RUN apt-get install -yqq unzip
# RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$(google-chrome-stable --version | awk -F '[ .]' '{print $3}')/chromedriver_linux64.zip
# RUN unzip /tmp/chromedriver.zip -d /usr/local/bin/

# # Install required Python packages
# COPY requirements.txt ./
# RUN pip install -r requirements.txt

# # Copy project files
# COPY . .

# CMD ["/bin/bash"]

# FROM python:3.11

# WORKDIR /app

# # Install Chrome
# RUN apt-get update && apt-get install -y wget gnupg ca-certificates
# RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
# RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
# RUN apt-get update && apt-get install -y google-chrome-stable

# # Install ChromeDriver
# RUN apt-get install -yqq unzip
# RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/94.0.4606.61/chromedriver_linux64.zip
# RUN unzip /tmp/chromedriver.zip -d /usr/local/bin/

# # Install required Python packages
# COPY requirements.txt ./
# RUN pip install -r requirements.txt


# # Copy project files
# COPY . .

# CMD ["/bin/bash"]

# FROM python:3.10

# WORKDIR /app

# # Install Chrome
# RUN apt-get update && apt-get install -y wget gnupg ca-certificates
# RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-archive-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
# RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /usr/share/keyrings/google-archive-keyring.gpg

# RUN apt-get update && apt-get install -y google-chrome-stable

# COPY chromedriver.exe ./
# # Install ChromeDriver
# # RUN apt-get install -yqq unzip

# # RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/94.0.4606.61/chromedriver_linux64.zip
# # RUN unzip /tmp/chromedriver.zip -d /usr/local/bin/

# # RUN apt-get update && apt-get install -yqq curl
# # RUN CHROME_DRIVER_VERSION=`curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE` \
# #     && wget -O /tmp/chromedriver.zip "https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip" \
# #     && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
# #     && rm /tmp/chromedriver.zip
# # Install required Python packages
# COPY requirements.txt ./
# # RUN pip install -r requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt


# # Copy project files
# COPY . .

# CMD ["/bin/bash"]


# Adding trusting keys to apt for repositories
FROM python:3.10

# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# # Adding Google Chrome to the repositories
# RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# # Updating apt to see and install Google Chrome
# RUN apt-get -y update

# # Magic happens
# RUN apt-get install -y google-chrome-stable

# # Installing Unzip
# RUN apt-get install -yqq unzip

# # Download the Chrome Driver
# RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/ 
# RUN curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE
# RUN chromedriver_linux64.zip

# # Unzip the Chrome Driver into /usr/local/bin directory
# RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# # Set display port as an environment variable
# ENV DISPLAY=:99

# COPY . /app
# COPY requirements.txt ./
# WORKDIR /app

# RUN pip install --upgrade pip

# RUN pip install -r requirements.txt

# FROM python:3.10

# RUN apt-get update && apt-get install -y wget curl unzip

# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
# RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
# RUN apt-get update && apt-get install -y google-chrome-stable=115.0.5790.171

# COPY chromedriver.exe ./
# # RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/LATEST_RELEASE
# # RUN export CHROME_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)
# # RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/$CHROME_VERSION/chromedriver_linux64.zip
# # RUN unzip /tmp/chromedriver.zip -d /usr/local/bin/

# ENV DISPLAY=:99

# COPY . /app
# COPY requirements.txt /app/requirements.txt
# WORKDIR /app

# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt


# FROM python:3.10

# RUN apt-get update && apt-get install -y wget curl unzip

# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
# RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
# RUN apt-get update && apt-get install -y google-chrome-stable

# # COPY chromedriver.exe ./
# # RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/LATEST_RELEASE
# # RUN export CHROME_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)
# # RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/$CHROME_VERSION/chromedriver_linux64.zip
# # RUN unzip /tmp/chromedriver.zip -d /usr/local/bin/

# ENV DISPLAY=:99

# COPY . /app
# COPY requirements.txt /app/requirements.txt
# WORKDIR /app

# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt


# RUN apt-get update && apt-get install -y wget curl unzip

# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
# RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
# RUN apt-get update && apt-get install -y google-chrome-stable


# COPY . /app
# COPY requirements.txt /app/requirements.txt
# WORKDIR /app

# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# Install Chrome and Chromedriver

FROM python:3.10
# RUN apt-get update && apt-get install -y wget curl unzip

# RUN wget -q -O - https://dl-ssl.google.com/linux/linuxsigningkey.pub | apt-key add -
# RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
# RUN apt-get update && apt-get install -y google-chrome-stable

# RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/LATEST_RELEASE/chromedriver_linux64.zip && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# COPY . /app
# COPY requirements.txt /app/requirements.txt
# WORKDIR /app

# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt


# Install necessary packages
# RUN apt-get update && apt-get install -y curl unzip

# # Download Chrome
# RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
# RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
# RUN apt-get update && apt-get install -y google-chrome-stable

# # Download ChromeDriver (compatible version with Chrome)
# RUN CHROME_VERSION=$(google-chrome-stable --version | awk '{print $3}' | awk -F '[.]' '{print $1}') && \
#     CHROMEDRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION) && \
#     curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
#     unzip /tmp/chromedriver_linux64.zip -d /usr/bin && \
#     rm /tmp/chromedriver_linux64.zip

# ENV CHROMEDRIVER_PATH /usr/bin/chromedriver
# ENV CHROME_BIN /usr/bin/google-chrome-stable

# COPY . /app
# COPY requirements.txt /app/requirements.txt
# WORKDIR /app

# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# Set up environment variables for Chrome and ChromeDriver



# RUN apt-get update && apt-get install -y curl unzip

# # Download Chrome
# RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
# RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
# RUN apt-get update && apt-get install -y google-chrome-stable

# # Manually download and copy ChromeDriver
# # RUN curl -sS -o /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/115.0.5790.170/chromedriver_linux64.zip && \
# #     unzip /tmp/chromedriver.zip -d /usr/bin && \
# #     rm /tmp/chromedriver.zip && \
# #     chmod +x /usr/bin/chromedriver
# COPY chromedriver ./

# ENV CHROME_BIN /usr/bin/google-chrome-stable

# COPY . /app
# COPY requirements.txt /app/requirements.txt
# WORKDIR /app

# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt


RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    gnupg2 \
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libatspi2.0-0 \
    libcairo2 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libx11-6 \
    libx11-xcb1 \
    libxcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxi6 \
    libxrandr2 \
    libxrender1 \
    libxshmfence1 \
    libxss1 \
    libxtst6 \
    ca-certificates \
    fonts-liberation \
    libappindicator1 \
    libnss3 \
    lsb-release \
    xdg-utils \
    wget \
    unzip

# Install Google Chrome
# RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# RUN dpkg -i google-chrome-stable_current_amd64.deb
# RUN apt-get install -f -y

# # Install ChromeDriver
# RUN wget -q https://chromedriver.storage.googleapis.com/[VERSION_NUMBER]/chromedriver_linux64.zip
# RUN unzip chromedriver_linux64.zip -d /usr/local/bin/
# RUN chmod +x /usr/local/bin/chromedriver

# # Set the working directory in the container
# WORKDIR /app

# # Install Python dependencies
# COPY requirements.txt /code/
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# # Copy the Django project code to the container
# COPY . /app/

# RUN apt-get install -y libu2f-udev libvulkan1
# RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# RUN dpkg -i google-chrome-stable_current_amd64.deb
# RUN apt-get update
# RUN apt-get -f install -y

# # Install Chromedriver
# RUN apt-get install -yqq unzip
# RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/LATEST_RELEASE/chromedriver_linux64.zip
# RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# # Set display port and dbus env to avoid chrome error
# ENV DISPLAY=:99
# ENV DBUS_SESSION_BUS_ADDRESS=/dev/null

# # Install requirements
# COPY requirements.txt /app/requirements.txt
# RUN pip install -r /app/requirements.txt

# # Set the working directory
# WORKDIR /app

# # Copy the Django project
# COPY . /app/


# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y wget curl unzip \
    && apt-get clean

# Install Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Install Chromedriver
RUN wget -q https://chromedriver.storage.googleapis.com/LATEST_RELEASE -O /tmp/chrome_version \
    && wget -q https://chromedriver.storage.googleapis.com/$(cat /tmp/chrome_version)/chromedriver_linux64.zip -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin \
    && rm /tmp/chromedriver.zip

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django app code to the container
COPY . .