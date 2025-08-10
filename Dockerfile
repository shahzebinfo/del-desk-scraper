FROM node:18-slim

# Install Chromium and required libs + chromedriver
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    fonts-liberation \
    libnss3 libxss1 libasound2 libatk-bridge2.0-0 libgtk-3-0 libx11-xcb1 libxcb1 \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy only package files first for faster install
COPY package*.json ./
RUN npm ci --only=production

# Copy rest of the app
COPY . .

# Ensure environment variable for chrome binary (used in code)
ENV CHROME_BIN=/usr/bin/chromium
ENV DISPLAY=:99

CMD ["npm", "start"]
