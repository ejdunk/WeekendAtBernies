#!/usr/bin/env python3
"""
WeekendAtBernies - Daily GitHub Commit Automation
A script that makes daily commits to maintain GitHub activity.
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
            "commit_history": []
        }
    
    def save_data(self, data):
        """Save data to JSON file."""
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def get_daily_fact(self):
        """Return a random daily fact."""
        facts = [
            "Octopuses have three hearts and blue blood",
            "Honey never spoils - archaeologists have found edible honey in ancient Egyptian tombs",
            "A group of flamingos is called a 'flamboyance'",
            "Bananas are berries, but strawberries aren't",
            "The shortest war in history lasted only 38-45 minutes",
            "A single cloud can weigh more than a million pounds",
            "Sharks have been around longer than trees",
            "The human brain uses about 20% of the body's total energy",
            "There are more possible games of chess than atoms in the observable universe",
            "Wombat poop is cube-shaped",
            "The Great Wall of China isn't visible from space with the naked eye",
            "A day on Venus is longer than its year",
            "Dolphins have names for each other",
            "The inventor of the Pringles can is buried in one",
            "Cleopatra lived closer in time to the Moon landing than to the construction of the Great Pyramid"
        ]
        return random.choice(facts)
    
    def already_committed_today(self, data):
        """Check if we've already made a commit today."""
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
    
    def make_commit(self):
        """Make the daily commit."""
        print("🚀 Starting daily commit process...")
        
        # Load existing data
        data = self.load_data()
        
        # Check if already committed today
        if self.already_committed_today(data):
            print(f"✅ Already committed today ({self.today})")
            print(f"📊 Total commits: {data['total_commits']}")
            print(f"📅 Current streak: {data['current_streak']} days")
            return
        
        # Update data
        data["total_commits"] += 1
        data["last_commit_date"] = self.today.isoformat()
        
        # Update streak
        if data["commit_history"]:
            last_date = datetime.fromisoformat(data["commit_history"][-1]["date"]).date()
            if (self.today - last_date).days == 1:
                data["current_streak"] += 1
            else:
                data["current_streak"] = 1
        else:
            data["current_streak"] = 1
        
        # Get daily fact
        daily_fact = self.get_daily_fact()
        
        # Create commit entry
        commit_entry = {
            "date": self.today.isoformat(),
            "commit_number": data["total_commits"],
            "streak_day": data["current_streak"],
            "fact": daily_fact,
            "timestamp": datetime.now().isoformat()
        }
        
        # Add to history (keep last 30 days)
        data["commit_history"].append(commit_entry)
        if len(data["commit_history"]) > 30:
            data["commit_history"] = data["commit_history"][-30:]
        
        # Save updated data
        self.save_data(data)
        
        # Create commit message
        commit_msg = f"Daily commit #{data['total_commits']} - {self.today.strftime('%B %d, %Y')}"
        
        # Log the commit
        log_entry = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {commit_msg} | Streak: {data['current_streak']} | Fact: {daily_fact}\n"
        with open(self.log_file, 'a') as f:
            f.write(log_entry)
        
        # Git operations
        print("📝 Adding files to git...")
        success, output = self.run_git_command("git add .")
        if not success:
            print(f"❌ Failed to add files: {output}")
            return
        
        print("💾 Making commit...")
        success, output = self.run_git_command(f'git commit -m "{commit_msg}"')
        if not success:
            print(f"❌ Failed to commit: {output}")
            return
        
        print("🚀 Pushing to remote...")
        success, output = self.run_git_command("git push")
        if not success:
            print(f"❌ Failed to push: {output}")
            return
        
        # Success message
        print(f"✅ Successfully committed and pushed: {commit_msg}")
        print(f"📊 Total commits: {data['total_commits']}")
        print(f"📅 Streak day: {data['current_streak']}")
        print(f"💡 Today's fact: {daily_fact}")

def main():
    """Main function."""
    committer = DailyCommitter()
    committer.make_commit()

if __name__ == "__main__":
    main()