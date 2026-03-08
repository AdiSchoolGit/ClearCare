FROM nginx:alpine

# Remove the original config
RUN rm /etc/nginx/nginx.conf

# Replace with new config
COPY ../.config/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

# Start Nginx when the container launches, no daemon to prevent session detachment
CMD ["nginx", "-g", "daemon off;"]
