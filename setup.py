#!/usr/bin/env python3
"""
Setup script for weekend-at-bernies
Helps configure the project for first-time use.
"""

import os
import subprocess
import sys

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return False

def check_git_repo():
    """Check if we're in a git repository."""
    return os.path.exists('.git')

def main():
    """Main setup function."""
    print("🚀 weekend-at-bernies Setup")
    print("=" * 40)
    
    # Check if we're in a git repo
    if not check_git_repo():
        print("❌ This doesn't appear to be a git repository.")
        print("Please run 'git init' first or clone this into an existing repo.")
        sys.exit(1)
    
    print("✅ Git repository detected")
    
    # Check Python version
    if sys.version_info < (3, 6):
        print("❌ Python 3.6+ is required")
        sys.exit(1)
    
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    
    # Test the daily commit script
    print("\n🧪 Testing daily commit script...")
    if run_command("python daily_commit.py", "Running daily commit test"):
        print("✅ Daily commit script is working!")
    else:
        print("❌ Daily commit script failed. Check your git configuration.")
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Push this repository to GitHub")
    print("2. Enable GitHub Actions in your repository settings")
    print("3. The script will run automatically daily at 9:00 AM UTC")
    print("4. You can also run 'python daily_commit.py' manually anytime")
    print("\nFor local automation, set up a cron job:")
    print("  crontab -e")
    print(f"  0 9 * * * cd {os.getcwd()} && python daily_commit.py")

if __name__ == "__main__":
    main()