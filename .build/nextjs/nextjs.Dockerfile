FROM node:20-slim

WORKDIR /app

# Copy package files for dependency caching
COPY frontend/package.json frontend/package-lock.json ./

# Install dependencies
RUN npm install

# Copy frontend source
COPY frontend/ ./

# Build Next.js for production
RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
