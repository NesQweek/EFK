FROM fluentd:v1.17.0-1.0

USER root

# Create log directory with appropriate permissions
RUN mkdir -p /fluentd/log \
    && chown -R fluent:fluent /fluentd/log \
    && chmod -R 755 /fluentd/log

# Install necessary plugins
RUN gem install fluent-plugin-elasticsearch fluent-plugin-grok-parser

USER fluent

# Copy the Fluentd configuration file
COPY fluent.conf /fluentd/etc/fluent.conf

# Run Fluentd with the specified configuration file
CMD ["fluentd", "-c", "/fluentd/etc/fluent.conf"]
