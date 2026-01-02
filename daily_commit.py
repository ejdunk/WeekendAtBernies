#!/usr/bin/env python3
"""
weekend-at-bernies - Daily GitHub Commit Automation
A script that makes 1-7 random daily commits to maintain GitHub activity.
"""

import json
import os
import subprocess
import sys
from datetime import datetime, date
import random

class DailyCommitter:
    def __init__(self):
        self.data_file = "daily_data.json"
        self.log_file = "commit_log.txt"
        self.today = date.today()
        
    def load_data(self):
        """Load existing data or create new data structure."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                pass
        
        # Create initial data structure
        return {
            "total_commits": 0,
            "current_streak": 0,
            "start_date": self.today.isoformat(),
            "last_commit_date": None,
            "last_commit_count": 0,
            "commit_history": []
        }
    
    def save_data(self, data):
        """Save data to JSON file."""
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def get_random_commit_count(self, last_count):
        """Get a random number of commits (1-7) different from yesterday."""
        available_counts = [i for i in range(1, 8) if i != last_count]
        return random.choice(available_counts)
    
    def already_committed_today(self, data):
        """Check if we've already made commits today."""
        return data.get("last_commit_date") == self.today.isoformat()
    
    def run_git_command(self, command):
        """Run a git command and return the result."""
        try:
            result = subprocess.run(
                command, 
                shell=True, 
                capture_output=True, 
                text=True, 
                check=True
            )
            return True, result.stdout.strip()
        except subprocess.CalledProcessError as e:
            return False, e.stderr.strip()
    
    def make_commits(self):
        """Make the daily commits."""
        print("🚀 Starting daily commit process...")
        
        # Load existing data
        data = self.load_data()
        
        # Check if already committed today
        if self.already_committed_today(data):
            print(f"✅ Already committed today ({self.today})")
            print(f"📊 Total commits: {data['total_commits']}")
            print(f"📅 Current streak: {data['current_streak']} days")
            return
        
        # Determine number of commits for today
        commit_count = self.get_random_commit_count(data.get("last_commit_count", 0))
        print(f"🎲 Making {commit_count} commits today (different from yesterday's {data.get('last_commit_count', 0)})")
        
        # Update streak
        if data["commit_history"]:
            last_date = datetime.fromisoformat(data["commit_history"][-1]["date"]).date()
            if (self.today - last_date).days == 1:
                data["current_streak"] += 1
            else:
                data["current_streak"] = 1
        else:
            data["current_streak"] = 1
        
        # Make the commits
        successful_commits = 0
        for i in range(commit_count):
            # Update data for this commit
            data["total_commits"] += 1
            
            # Create commit message
            if commit_count == 1:
                commit_msg = f"Daily commit #{data['total_commits']} - {self.today.strftime('%B %d, %Y')}"
            else:
                commit_msg = f"Daily commit #{data['total_commits']} ({i+1}/{commit_count}) - {self.today.strftime('%B %d, %Y')}"
            
            # Save updated data before each commit
            data["last_commit_date"] = self.today.isoformat()
            data["last_commit_count"] = commit_count
            self.save_data(data)
            
            # Log the commit
            log_entry = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {commit_msg} | Streak: {data['current_streak']} | Commit {i+1} of {commit_count}\n"
            with open(self.log_file, 'a') as f:
                f.write(log_entry)
            
            # Git operations
            success, output = self.run_git_command("git add .")
            if not success:
                print(f"❌ Failed to add files for commit {i+1}: {output}")
                continue
            
            success, output = self.run_git_command(f'git commit -m "{commit_msg}"')
            if not success:
                print(f"❌ Failed to make commit {i+1}: {output}")
                continue
            
            successful_commits += 1
            print(f"✅ Commit {i+1}/{commit_count} completed")
        
        # Push all commits at once
        if successful_commits > 0:
            print("🚀 Pushing all commits to remote...")
            success, output = self.run_git_command("git push")
            if not success:
                print(f"❌ Failed to push commits: {output}")
                return
        
        # Create commit history entry
        commit_entry = {
            "date": self.today.isoformat(),
            "commit_count": successful_commits,
            "streak_day": data["current_streak"],
            "timestamp": datetime.now().isoformat()
        }
        
        # Add to history (keep last 30 days)
        data["commit_history"].append(commit_entry)
        if len(data["commit_history"]) > 30:
            data["commit_history"] = data["commit_history"][-30:]
        
        # Final save
        self.save_data(data)
        
        # Success message
        print(f"✅ Successfully completed {successful_commits} commits - {self.today.strftime('%B %d, %Y')}")
        print(f"📊 Total commits: {data['total_commits']}")
        print(f"📅 Streak day: {data['current_streak']}")

def main():
    """Main function."""
    committer = DailyCommitter()
    committer.make_commits()

if __name__ == "__main__":
    main()