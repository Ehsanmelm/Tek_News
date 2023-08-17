# FROM python:3.10

# WORKDIR /app

# # Install system dependencies for chrome and chromedriver
# RUN apt-get update \
#     && apt-get install -y wget curl unzip \
#     && apt-get clean

# # Install chrome
# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
#     && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
#     && apt-get update \
#     && apt-get install -y google-chrome-stable \
#     && rm -rf /var/lib/apt/lists/*

# ENV CHROMEDRIVER_VERSION 116.0.5845.96


# # Install chromedriver
# RUN wget -q https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip -O /tmp/chromedriver.zip \
#     && unzip /tmp/chromedriver.zip -d /usr/local/bin \
#     && rm /tmp/chromedriver.zip

# # # Install chromedriver
# # RUN wget -q https://chromedriver.storage.googleapis.com/LATEST_RELEASE -O /tmp/chrome_version \
# #     && wget -q https://chromedriver.storage.googleapis.com/$(cat /tmp/chrome_version)/chromedriver_linux64.zip -O /tmp/chromedriver.zip \
# #     && unzip /tmp/chromedriver.zip -d /usr/local/bin \
# #     && rm /tmp/chromedriver.zip

# # Install Python dependencies
# COPY requirements.txt .
# # RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install -r requirements.txt


# COPY . .


# FROM python:3.10

# WORKDIR /app

# # Install system dependencies for chrome and chromedriver
# RUN apt-get update \
#     && apt-get install -y wget curl unzip \
#     && apt-get clean

# # Install chrome
# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
#     && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
#     && apt-get update \
#     && apt-get install -y google-chrome-stable \
#     && rm -rf /var/lib/apt/lists/*

# # Specify the ChromeDriver version
# ENV CHROMEDRIVER_VERSION 116.0.5845.96

# # Install chromedriver
# RUN wget -q https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip -O /tmp/chromedriver.zip \
#     && unzip /tmp/chromedriver.zip -d /usr/local/bin \
#     && rm /tmp/chromedriver.zip

# # Install Python dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .


FROM python:3.10

WORKDIR /app

# Install system dependencies for chrome and chromedriver
RUN apt-get update \
    && apt-get install -y wget curl unzip \
    && apt-get clean

# Install chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Specify the ChromeDriver version
ENV CHROMEDRIVER_VERSION 116.0.5845.96

# Install chromedriver
RUN wget -q https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/${CHROMEDRIVER_VERSION}/linux64/chromedriver-linux64.zip -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin \
    && rm /tmp/chromedriver.zip

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .