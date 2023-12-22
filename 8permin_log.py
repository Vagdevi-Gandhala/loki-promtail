# Create a logger
logger = logging.getLogger("python-logger")

# Add a FileHandler to write logs to a file
file_handler = logging.FileHandler("/var/log/python_logs/python.log")
logger.addHandler(file_handler)

# Generate 8 logs per minute
logs_per_minute = 8
seconds_per_log = 60 / logs_per_minute

while True:
    log_level = random.choice(["info", "warning", "error"])

    # Get system information
    system_name = platform.node()
    cpu_utilization = psutil.cpu_percent()

    message = {
        "system": system_name,
        "cpu": cpu_utilization,
        "log_level": log_level,
        "log_message": f"This is a {log_level} message."
    }
    logger.log(logging.getLevelName(log_level.upper()), json.dumps(message))

    # Simulate errors
    if log_level == "error":
        # Simulate an exception
        try:
            result = 1 / 0
        except Exception as e:
            error_message = {
                "system": system_name,
                "cpu": cpu_utilization,
                "log_level": log_level,
                "log_message": f"An error occurred: {str(e)}"
            }
            logger.error(json.dumps(error_message))

    time.sleep(seconds_per_log)

