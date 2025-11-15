# Use Base Image
FROM node:22-alpine 
# Set working directory inside a container
WORKDIR /app
#Copy package.json first (for caching)
COPY package.json .
# install Dependency
RUN npm install
# copy rest code files
COPY . .
# Expose application Port
EXPOSE 3000
# Command to run application
CMD ["node", "index.js"]