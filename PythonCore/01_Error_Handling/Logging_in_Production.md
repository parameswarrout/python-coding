# Python Logging for Production Code

## Table of Contents
1. [Introduction to Logging](#introduction)
2. [Logging Levels](#logging-levels)
3. [Basic Logging Setup](#basic-logging-setup)
4. [Log Formatting](#log-formatting)
5. [Logging to Files](#logging-to-files)
6. [Advanced Logging Configuration](#advanced-configuration)
7. [Production Logging Best Practices](#production-best-practices)
8. [Structured Logging](#structured-logging)
9. [Logging in Web Applications](#web-application-logging)
10. [Log Management and Rotation](#log-management)

## Introduction {#introduction}

Logging is a critical component of production applications. It provides visibility into application behavior, helps diagnose issues, and enables monitoring of system health. Python's built-in `logging` module offers a flexible framework for emitting log messages from Python programs.

Unlike `print()` statements, logging provides:
- Different severity levels
- Configurable output destinations
- Structured formatting
- Performance considerations
- Integration with external systems

## Logging Levels {#logging-levels}

Python's logging module defines several standard levels indicating the severity of events:

```python
import logging

# Standard logging levels in order of increasing severity
logging.DEBUG     # 10 - Detailed diagnostic information
logging.INFO      # 20 - Confirmation of normal operation
logging.WARNING   # 30 - Indication of potential problems
logging.ERROR     # 40 - Error events that caused a specific operation to fail
logging.CRITICAL  # 50 - Very serious errors that may cause program termination

# Example of different log levels
logger = logging.getLogger(__name__)

logger.debug("Detailed diagnostic information")
logger.info("Application is running normally")
logger.warning("Potential issue detected")
logger.error("An error occurred")
logger.critical("Critical error - application may terminate")
```

## Basic Logging Setup {#basic-logging-setup}

### Simple Configuration

```python
import logging

# Basic configuration - sets up a handler and formatter
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Create a logger
logger = logging.getLogger(__name__)

# Log messages
logger.debug("This won't appear due to level setting")
logger.info("Application started")
logger.warning("This is a warning")
logger.error("An error occurred")
```

### Named Loggers

```python
import logging

# Create named loggers for different modules/components
app_logger = logging.getLogger('myapp')
db_logger = logging.getLogger('myapp.database')
api_logger = logging.getLogger('myapp.api')

# Configure the root logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Use different loggers
app_logger.info("Application initialized")
db_logger.warning("Database connection slow")
api_logger.error("API request failed")
```

## Log Formatting {#log-formatting}

### Format String Options

```python
import logging

# Different format options
formatter = logging.Formatter(
    fmt='%(asctime)s | %(levelname)-8s | %(name)s | %(funcName)s:%(lineno)d | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Common format attributes:
# %(name)s - Name of the logger
# %(levelname)s - Text logging level
# %(asctime)s - Human-readable time
# %(filename)s - Filename portion of pathname
# %(lineno)d - Source line number
# %(funcName)s - Function name
# %(message)s - The logged message

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

logger.info("Formatted log message")
```

### Custom Formatter

```python
import logging
from datetime import datetime

class ColoredFormatter(logging.Formatter):
    """Custom formatter with colors for different log levels"""
    
    COLORS = {
        'DEBUG': '\033[36m',    # Cyan
        'INFO': '\033[32m',     # Green
        'WARNING': '\033[33m',  # Yellow
        'ERROR': '\033[31m',    # Red
        'CRITICAL': '\033[35m', # Magenta
        'RESET': '\033[0m'      # Reset
    }
    
    def format(self, record):
        log_color = self.COLORS.get(record.levelname, self.COLORS['RESET'])
        record.levelname = f"{log_color}{record.levelname}{self.COLORS['RESET']}"
        return super().format(record)

# Usage
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setFormatter(ColoredFormatter('%(asctime)s - %(levelname)s - %(message)s'))

logger.addHandler(handler)
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
```

## Logging to Files {#logging-to-files}

### Basic File Logging

```python
import logging

# Configure logging to write to a file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('application.log'),
        logging.StreamHandler()  # Also log to console
    ]
)

logger = logging.getLogger(__name__)
logger.info("Application started")
logger.error("An error occurred")
```

### Rotating File Handler

```python
import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

# Rotating file handler - rotates when file reaches max size
rotating_handler = RotatingFileHandler(
    'application.log',
    maxBytes=1024*1024,  # 1MB
    backupCount=5       # Keep 5 backup files
)

# Timed rotating handler - rotates at specific intervals
timed_handler = TimedRotatingFileHandler(
    'daily.log',
    when='midnight',    # Rotate at midnight
    interval=1,         # Every 1 day
    backupCount=30      # Keep 30 days of logs
)

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
rotating_handler.setFormatter(formatter)
timed_handler.setFormatter(formatter)

logger.addHandler(rotating_handler)
logger.addHandler(timed_handler)

# Use the logger
logger.info("This message goes to both rotating and timed log files")
```

## Advanced Logging Configuration {#advanced-configuration}

### Configuration with Dictionary

```python
import logging
import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'detailed': {
            'format': '%(asctime)s [%(levelname)s] %(name)s:%(lineno)d: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'detailed',
            'filename': 'app.log',
            'maxBytes': 10485760,  # 10MB
            'backupCount': 5,
        },
    },
    'loggers': {
        '': {  # Root logger
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False
        },
        'myapp': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False
        }
    }
}

# Apply configuration
logging.config.dictConfig(LOGGING_CONFIG)

# Use loggers
logger = logging.getLogger(__name__)
app_logger = logging.getLogger('myapp')

logger.info("Root logger message")
app_logger.info("App logger message")
```

### Configuration with YAML (Alternative)

```python
import logging.config
import yaml

# YAML configuration (would typically be in a separate file)
yaml_config = '''
version: 1
disable_existing_loggers: false

formatters:
  standard:
    format: "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
  json:
    format: '{"timestamp": "%(asctime)s", "level": "%(levelname)s", "logger": "%(name)s", "message": "%(message)s"}'

handlers:
  console:
    class: logging.StreamHandler
    level: INFO
    formatter: standard
    stream: ext://sys.stdout
  
  file:
    class: logging.handlers.RotatingFileHandler
    level: DEBUG
    formatter: standard
    filename: app.log
    maxBytes: 10485760
    backupCount: 5

loggers:
  myapp:
    level: DEBUG
    handlers: [console, file]
    propagate: false
'''

# Load YAML config (requires PyYAML: pip install pyyaml)
# config = yaml.safe_load(yaml_config)
# logging.config.dictConfig(config)
```

## Production Logging Best Practices {#production-best-practices}

### Structured Logging with Context

```python
import logging
import json
from datetime import datetime
from functools import wraps

class ContextFilter(logging.Filter):
    """Add contextual information to log records"""
    
    def __init__(self):
        super().__init__()
        self.context = {}
    
    def add_context(self, **kwargs):
        self.context.update(kwargs)
    
    def remove_context(self, *keys):
        for key in keys:
            self.context.pop(key, None)
    
    def filter(self, record):
        for key, value in self.context.items():
            setattr(record, key, value)
        return True

# Create logger with context
logger = logging.getLogger(__name__)
context_filter = ContextFilter()

handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(user_id)s - %(request_id)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
handler.addFilter(context_filter)

logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Add context
context_filter.add_context(user_id=12345, request_id='req-abc-123')
logger.info("User performed action")
```

### Decorator for Function Logging

```python
import logging
import functools
from typing import Any, Callable

def log_function_call(logger: logging.Logger = None, level: int = logging.INFO):
    """Decorator to log function calls and their results"""
    
    def decorator(func: Callable) -> Callable:
        nonlocal logger
        if logger is None:
            logger = logging.getLogger(func.__module__)
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            logger.log(level, f"Calling {func_name} with args={args}, kwargs={kwargs}")
            
            try:
                result = func(*args, **kwargs)
                logger.log(level, f"{func_name} completed successfully")
                return result
            except Exception as e:
                logger.error(f"{func_name} failed with error: {str(e)}", exc_info=True)
                raise
        
        return wrapper
    return decorator

# Usage
@log_function_call(level=logging.DEBUG)
def divide_numbers(a: int, b: int) -> float:
    """Divide two numbers"""
    return a / b

result = divide_numbers(10, 2)
print(f"Result: {result}")

try:
    result = divide_numbers(10, 0)
except ZeroDivisionError:
    print("Division by zero handled")
```

### Error Handling with Logging

```python
import logging
import traceback
from typing import Optional

def safe_execute(operation_name: str, logger: logging.Logger, func, *args, **kwargs):
    """Safely execute a function with comprehensive logging"""
    
    try:
        logger.info(f"Starting operation: {operation_name}")
        result = func(*args, **kwargs)
        logger.info(f"Operation {operation_name} completed successfully")
        return result
    except Exception as e:
        logger.error(
            f"Operation {operation_name} failed: {str(e)}",
            extra={
                'operation': operation_name,
                'error_type': type(e).__name__,
                'args': str(args)[:100],  # Limit length for security
                'kwargs_keys': list(kwargs.keys())
            },
            exc_info=True  # Include full traceback
        )
        raise

# Example usage
def risky_operation(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

logger = logging.getLogger(__name__)

try:
    result = safe_execute("division", logger, risky_operation, 10, 2)
    print(f"Result: {result}")
except Exception as e:
    print(f"Operation failed: {e}")

try:
    result = safe_execute("division", logger, risky_operation, 10, 0)
except Exception as e:
    print(f"Operation failed: {e}")
```

## Structured Logging {#structured-logging}

### JSON Logging

```python
import logging
import json
from datetime import datetime
from io import StringIO

class JsonFormatter(logging.Formatter):
    """Custom formatter to output logs as JSON"""
    
    def format(self, record):
        log_entry = {
            'timestamp': datetime.utcfromtimestamp(record.created).isoformat(),
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno,
        }
        
        # Add exception info if present
        if record.exc_info:
            log_entry['exception'] = self.formatException(record.exc_info)
        
        # Add extra fields
        if hasattr(record, '__dict__'):
            for key, value in record.__dict__.items():
                if key not in log_entry and key not in ['name', 'msg', 'args', 'levelname', 
                                                       'levelno', 'pathname', 'filename', 
                                                       'module', 'lineno', 'funcName', 
                                                       'created', 'msecs', 'relativeCreated', 
                                                       'thread', 'threadName', 'processName', 
                                                       'process', 'getMessage', 'exc_info', 
                                                       'exc_text', 'stack_info']:
                    log_entry[key] = value
        
        return json.dumps(log_entry)

# Configure JSON logging
json_logger = logging.getLogger('json_logger')
json_handler = logging.StreamHandler()
json_handler.setFormatter(JsonFormatter())
json_logger.addHandler(json_handler)
json_logger.setLevel(logging.INFO)

# Use JSON logger
json_logger.info("User login", extra={'user_id': 123, 'ip_address': '192.168.1.1'})
json_logger.error("Database connection failed", extra={'host': 'db.example.com', 'port': 5432})
```

### Using Structlog for Structured Logging

```python
# Note: Requires installation: pip install structlog
# For demonstration purposes only

'''
import structlog
import logging
import sys

# Configure structlog
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.processors.JSONRenderer()
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

# Create logger
logger = structlog.get_logger()

# Use structured logging
logger.info("User action", user_id=123, action="login", ip="192.168.1.1")
logger.error("Database error", db_host="localhost", error_code=500)
'''
```

## Logging in Web Applications {#web-application-logging}

### Flask Logging Example

```python
# Note: Requires Flask: pip install flask
# For demonstration purposes only

'''
from flask import Flask, request, g
import logging
import uuid

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.before_request
def before_request():
    # Generate request ID for tracking
    g.request_id = str(uuid.uuid4())
    g.start_time = time.time()
    
    logger.info("Request started", extra={
        'request_id': g.request_id,
        'method': request.method,
        'url': request.url,
        'remote_addr': request.remote_addr
    })

@app.after_request
def after_request(response):
    duration = time.time() - g.start_time
    logger.info("Request completed", extra={
        'request_id': g.request_id,
        'status_code': response.status_code,
        'duration_ms': round(duration * 1000, 2)
    })
    return response

@app.route('/')
def home():
    logger.info("Home page accessed", extra={'request_id': g.request_id})
    return "Hello, World!"

@app.route('/error')
def error_route():
    logger.error("Error route accessed", extra={'request_id': g.request_id})
    return "Error occurred", 500

if __name__ == '__main__':
    app.run(debug=True)
'''
```

### Django Logging Configuration

```python
# Django settings.py equivalent configuration
DJANGO_LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'django.log',
            'maxBytes': 1024*1024*15,  # 15MB
            'backupCount': 10,
            'formatter': 'verbose',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console', 'file']
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}
```

## Log Management and Rotation {#log-management}

### Custom Log Rotation with Size and Time

```python
import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime

class SizeAndTimeRotatingHandler(RotatingFileHandler):
    """Custom handler that rotates based on both size and time"""
    
    def __init__(self, filename, max_bytes=0, backup_count=0, encoding=None, delay=False, when='midnight', interval=1):
        super().__init__(filename, max_bytes, backup_count, encoding, delay)
        self.when = when
        self.interval = interval
        self.last_rollover = datetime.now()
    
    def should_rollover(self, record):
        """Override to check both size and time conditions"""
        if self.stream is None:
            self.stream = self._open()
        
        # Check size condition
        if self.maxBytes > 0:
            msg = "%s\n" % self.format(record)
            if self.stream.tell() + len(msg.encode('utf-8')) >= self.maxBytes:
                return 1
        
        # Check time condition (simplified)
        now = datetime.now()
        if (now - self.last_rollover).days >= self.interval:
            return 1
        
        return 0

# Usage example
logger = logging.getLogger('size_time_logger')
handler = SizeAndTimeRotatingHandler(
    'app_combined.log',
    max_bytes=1024*1024,  # 1MB
    backup_count=5,
    when='midnight',
    interval=1
)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Generate some log entries
for i in range(10):
    logger.info(f"Log entry {i}")
```

### Log Aggregation Helper

```python
import logging
import logging.handlers
import os
from pathlib import Path

class LogAggregator:
    """Helper class to manage application logging setup"""
    
    def __init__(self, app_name: str, log_dir: str = "logs"):
        self.app_name = app_name
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)
        
        # Create different log files for different purposes
        self.setup_loggers()
    
    def setup_loggers(self):
        """Setup different loggers for different purposes"""
        
        # Main application logger
        self.app_logger = self._create_logger(
            f"{self.app_name}.app",
            self.log_dir / "app.log",
            logging.INFO
        )
        
        # Error logger
        self.error_logger = self._create_logger(
            f"{self.app_name}.error",
            self.log_dir / "error.log",
            logging.ERROR
        )
        
        # Audit logger
        self.audit_logger = self._create_logger(
            f"{self.app_name}.audit",
            self.log_dir / "audit.log",
            logging.INFO
        )
    
    def _create_logger(self, name: str, log_file: Path, level: int):
        """Create a logger with rotating file handler"""
        
        logger = logging.getLogger(name)
        logger.setLevel(level)
        
        # Create rotating file handler
        handler = logging.handlers.RotatingFileHandler(
            log_file,
            maxBytes=10*1024*1024,  # 10MB
            backupCount=5
        )
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
        )
        handler.setFormatter(formatter)
        
        # Add handler to logger
        logger.addHandler(handler)
        
        return logger
    
    def get_logger(self, name: str = None):
        """Get a logger by name"""
        if name is None:
            return self.app_logger
        return logging.getLogger(f"{self.app_name}.{name}")

# Usage
aggregator = LogAggregator("my_web_app")

# Use different loggers
app_log = aggregator.get_logger()
error_log = aggregator.get_logger("error")
audit_log = aggregator.get_logger("audit")

app_log.info("Application started")
error_log.error("Database connection failed")
audit_log.info("User login", extra={"user_id": 123})
```

## Environment-Specific Configuration

```python
import logging
import os

def setup_logging(env: str = None):
    """Setup logging based on environment"""
    
    if env is None:
        env = os.getenv('ENVIRONMENT', 'development')
    
    if env == 'production':
        # Production logging - log to files with rotation
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.handlers.RotatingFileHandler(
                    'production.log',
                    maxBytes=10*1024*1024,  # 10MB
                    backupCount=10
                )
            ]
        )
    elif env == 'staging':
        # Staging - log to both file and console with more detail
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
            handlers=[
                logging.StreamHandler(),
                logging.handlers.RotatingFileHandler(
                    'staging.log',
                    maxBytes=5*1024*1024,  # 5MB
                    backupCount=5
                )
            ]
        )
    else:
        # Development - log to console with debug level
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(levelname)s - %(name)s - %(funcName)s:%(lineno)d - %(message)s',
            handlers=[logging.StreamHandler()]
        )

# Usage
setup_logging(os.getenv('ENVIRONMENT', 'development'))
logger = logging.getLogger(__name__)
logger.info("Logging configured for environment")
```

## Summary

Effective logging in production Python applications involves:

1. **Proper configuration** of log levels, formatters, and handlers
2. **Structured logging** for better analysis and monitoring
3. **Log rotation** to manage disk space
4. **Contextual information** to aid debugging
5. **Environment-specific configurations** for different deployment stages
6. **Performance considerations** to minimize impact on application speed
7. **Security awareness** to avoid logging sensitive information

Remember to regularly review and monitor your logs as they are often the first indication of issues in production systems.