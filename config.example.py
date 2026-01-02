"""
Configuration example for weekend-at-bernies
Copy this to config.py and modify as needed.
"""

# Range for random daily commits (min, max)
COMMIT_RANGE = (1, 7)

# Commit message format (use {number} and {date} placeholders)
COMMIT_MESSAGE_FORMAT = "Daily commit #{number} - {date}"

# Alternative commit message formats you can use:
# COMMIT_MESSAGE_FORMAT = "🤖 Automated commit #{number} on {date}"
# COMMIT_MESSAGE_FORMAT = "Day {number}: Keeping the streak alive! ({date})"
# COMMIT_MESSAGE_FORMAT = "📅 {date} - Commit #{number} for consistency"

# Git user configuration (optional - will use global git config if not set)
GIT_USER_NAME = None  # "Your Name"
GIT_USER_EMAIL = None  # "your.email@example.com"

# File names (change if you want different file names)
DATA_FILE = "daily_data.json"
LOG_FILE = "commit_log.txt"

# Maximum number of days to keep in commit history
MAX_HISTORY_DAYS = 30

# Enable/disable features
VERBOSE_OUTPUT = True