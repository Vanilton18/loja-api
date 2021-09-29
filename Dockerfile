FROM vaniltonpinheiro/dep-loja:latest
COPY . $APP_PATH
RUN chmod +x wait-for-it.sh