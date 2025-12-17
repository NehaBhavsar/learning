# Use official OpenJDK image
FROM azul/zulu-openjdk-alpine:17
# Set working directory
WORKDIR /app

# Copy Java source
COPY HelloWorld.java .

# Compile
RUN javac HelloWorld.java

# Run
CMD java HelloWorld && tail -f /dev/null