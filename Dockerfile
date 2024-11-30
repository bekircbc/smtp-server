# Use a lightweight image for MailHog
FROM mailhog/mailhog:latest

# Expose SMTP and HTTP ports
EXPOSE 1025 8025

# Command to start the server (already handled by the MailHog base image)
CMD ["MailHog"]
