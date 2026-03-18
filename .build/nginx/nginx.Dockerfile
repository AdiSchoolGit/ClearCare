#FROM nginx:1.29.5-alpine-slim
FROM arm64v8/nginx:1.29.5-alpine-slim

# Remove the original config
#RUN rm /etc/nginx/nginx.conf

# Replace with new config
#COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

# Start Nginx when the container launches, no daemon to prevent session detachment
CMD ["nginx", "-g", "daemon off;"]
