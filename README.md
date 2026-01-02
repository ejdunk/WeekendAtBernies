# weekend-at-bernies 💀 

A simple Python script that automatically makes random daily commits (1-7 per day) to your GitHub repository to maintain contribution activity and practice automation.

## Features

- **Random Daily Commits**: Automatically commits 1-7 times per day with unique messages
- **Smart Variation**: Never repeats the same number of commits as the previous day
- **Data Tracking**: Keeps track of commit streaks and statistics in JSON format
- **Commit Logging**: Maintains a log file of all automated commits
- **GitHub Actions**: Automated execution using GitHub Actions workflow
- **Smart Scheduling**: Won't make duplicate commits on the same day

## Project Files

- `daily_commit.py` - Main automation script
- `setup.py` - Easy setup and testing script
- `config.example.py` - Configuration template for customization
- `.github/workflows/daily-commit.yml` - GitHub Actions workflow
- `daily_data.json` - Stores commit statistics and history (auto-generated)
- `commit_log.txt` - Human-readable log of all commits (auto-generated)

## Files Generated

- `daily_data.json` - Stores commit statistics and history
- `commit_log.txt` - Human-readable log of all commits
- Both files are automatically created and updated

## Quick Setup

### Option 1: GitHub Actions (Recommended)
1. Clone or fork this repository
2. Run the setup script: `python setup.py`
3. Push to your GitHub repository
4. Enable GitHub Actions in your repository settings
5. The script will run daily at 9:00 AM UTC automatically

### Option 2: One-Click Setup
1. Fork this repository on GitHub
2. GitHub Actions will automatically start running daily
3. No additional setup required!

### Option 3: Local Cron Job
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
✅ Making 3 commits today (different from yesterday's 5)
✅ Successfully completed 3 commits - January 02, 2026
📊 Total commits: 18
📅 Streak day: 15
```

## Data Structure

The `daily_data.json` file stores:
- Total number of automated commits
- Current streak counter
- Start date of the project
- Last commit date
- Daily commit counts for variation tracking
- Recent commit history (last 30 days)

## Customization Ideas

- Change the commit message format
- Modify the range of daily commits (currently 1-7)
- Add more data tracking (timestamps, etc.)
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
