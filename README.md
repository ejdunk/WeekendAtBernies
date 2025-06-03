# WeekendAtBernies 💀 

A simple Python script that automatically makes daily commits to your GitHub repository to maintain contribution activity and practice automation.

## Features

- **Daily Commits**: Automatically commits once per day with unique messages
- **Data Tracking**: Keeps track of commit streaks and statistics in JSON format
- **Commit Logging**: Maintains a log file of all automated commits
- **Fun Facts**: Includes random daily facts in the commit data
- **GitHub Actions**: Automated execution using GitHub Actions workflow
- **Smart Scheduling**: Won't make duplicate commits on the same day

## Files Generated

- `daily_data.json` - Stores commit statistics and history
- `commit_log.txt` - Human-readable log of all commits
- Both files are automatically created and updated

## Quick Setup

### Option 1: GitHub Actions (Recommended)
1. Create a new repository on GitHub
2. Add the Python script as `daily_commit.py`
3. Create `.github/workflows/daily-commit.yml` with the workflow file
4. Push to your repository
5. The script will run daily at 9:00 AM UTC automatically

### Option 2: Local Cron Job
1. Clone your repository locally
2. Run the script manually: `python daily_commit.py`
3. Set up a cron job to run it daily:
   ```bash
   # Edit crontab
   crontab -e
   
   # Add this line (runs daily at 9 AM)
   0 9 * * * cd /path/to/your/repo && python daily_commit.py
   ```

## Manual Usage

Run the script anytime to make a commit (if one hasn't been made today):

```bash
python daily_commit.py
```

Output example:
```
🚀 Starting daily commit process...
✅ Successfully committed and pushed: Daily commit #15 - March 15, 2024
📊 Total commits: 15
📅 Streak day: 15
```

## Data Structure

The `daily_data.json` file stores:
- Total number of automated commits
- Current streak counter
- Start date of the project
- Last commit date
- Recent commit history (last 30 days)

## Customization Ideas

- Modify the `get_daily_fact()` function to include your own content
- Change the commit message format
- Add more data tracking (weather, quotes, etc.)
- Integrate with APIs for dynamic content
- Add email notifications for milestone streaks

## Requirements

- Python 3.6+
- Git repository with push access
- For GitHub Actions: Repository with Actions enabled

## Notes

- The script prevents duplicate commits on the same day
- All git operations include error handling
- Compatible with any Git hosting service (GitHub, GitLab, etc.)
- No external Python dependencies required

## License

Feel free to fork, modify, and use this project for your own GitHub activity automation!

---

*This project helps maintain GitHub contribution graphs and is perfect for learning automation basics.*
