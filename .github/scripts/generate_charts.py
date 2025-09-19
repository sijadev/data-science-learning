#!/usr/bin/env python3
"""
Generate progress charts and visualizations for achievement tracking
"""
import json
import os
from datetime import datetime, date, timedelta
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import pandas as pd
import numpy as np
from collections import defaultdict
import subprocess

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

class ProgressChartGenerator:
    def __init__(self):
        self.data_file = Path("challenge/details/progress_data.json")
        self.charts_dir = Path("assets/charts")
        self.charts_dir.mkdir(parents=True, exist_ok=True)

        # Load data
        self.load_data()

        # Collect git statistics
        self.collect_git_stats()

    def load_data(self):
        """Load progress data from JSON"""
        if self.data_file.exists():
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {
                "achievements_unlocked": [],
                "total_points": 0,
                "statistics": {},
                "daily_stats": [],
                "start_date": "2025-09-19"
            }

    def collect_git_stats(self):
        """Collect detailed git statistics"""
        try:
            # Get commit history
            result = subprocess.run(
                ["git", "log", "--pretty=format:%H|%an|%ae|%at|%s", "--numstat"],
                capture_output=True,
                text=True
            )

            self.commits = []
            self.daily_commits = defaultdict(int)
            self.hourly_commits = defaultdict(int)
            self.file_changes = defaultdict(lambda: {"added": 0, "deleted": 0})

            # Parse git log
            current_commit = None
            for line in result.stdout.split('\n'):
                if '|' in line and not '\t' in line:
                    # Commit info line
                    parts = line.split('|')
                    if len(parts) >= 5:
                        commit_hash, author, email, timestamp, message = parts[:5]
                        commit_date = datetime.fromtimestamp(int(timestamp))

                        current_commit = {
                            'hash': commit_hash,
                            'date': commit_date,
                            'message': message,
                            'additions': 0,
                            'deletions': 0
                        }
                        self.commits.append(current_commit)

                        # Track daily commits
                        day_key = commit_date.strftime('%Y-%m-%d')
                        self.daily_commits[day_key] += 1

                        # Track hourly patterns
                        hour_key = commit_date.hour
                        self.hourly_commits[hour_key] += 1

                elif '\t' in line and current_commit:
                    # File change line
                    parts = line.split('\t')
                    if len(parts) == 3:
                        added, deleted, filename = parts
                        if added != '-':
                            current_commit['additions'] += int(added)
                        if deleted != '-':
                            current_commit['deletions'] += int(deleted)

                        # Track file changes
                        if filename.endswith('.py'):
                            self.file_changes[filename]['added'] += int(added) if added != '-' else 0
                            self.file_changes[filename]['deleted'] += int(deleted) if deleted != '-' else 0

        except Exception as e:
            print(f"Error collecting git stats: {e}")
            self.commits = []
            self.daily_commits = {}
            self.hourly_commits = {}
            self.file_changes = {}

    def generate_all_charts(self):
        """Generate all charts"""
        print("📊 Generating charts...")

        # Generate individual charts
        self.generate_overview_dashboard()
        self.generate_commit_history_chart()
        self.generate_activity_heatmap()
        self.generate_code_growth_chart()

        print("✅ All charts generated!")

    def generate_overview_dashboard(self):
        """Generate main dashboard with key metrics"""
        fig = plt.figure(figsize=(16, 10))
        fig.suptitle('🚀 Data Science Journey Dashboard', fontsize=20, fontweight='bold')

        # Calculate metrics
        total_commits = len(self.commits)
        total_days = (date.today() - date(2025, 9, 19)).days + 1
        commits_per_day = total_commits / max(total_days, 1)
        total_additions = sum(c['additions'] for c in self.commits)
        total_deletions = sum(c['deletions'] for c in self.commits)
        active_days = len(self.daily_commits)

        # Grid layout
        gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

        # 1. Commit Timeline
        ax1 = fig.add_subplot(gs[0, :2])
        if self.daily_commits:
            dates = pd.to_datetime(list(self.daily_commits.keys()))
            values = list(self.daily_commits.values())
            ax1.plot(dates, values, marker='o', linewidth=2, markersize=6)
            ax1.fill_between(dates, values, alpha=0.3)
            ax1.set_title('📈 Daily Commit Activity', fontweight='bold')
            ax1.set_xlabel('Date')
            ax1.set_ylabel('Commits')
            ax1.grid(True, alpha=0.3)
            ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m'))

        # 2. Stats Cards
        ax2 = fig.add_subplot(gs[0, 2])
        ax2.axis('off')
        stats_text = f"""📊 KEY METRICS

Total Commits: {total_commits}
Active Days: {active_days}
Avg/Day: {commits_per_day:.1f}

Lines Added: {total_additions:,}
Lines Deleted: {total_deletions:,}
Net Lines: {total_additions - total_deletions:,}

Achievement Points: {self.data.get('total_points', 0)} XP
Current Week: {(total_days // 7) + 1}"""

        ax2.text(0.1, 0.9, stats_text, transform=ax2.transAxes,
                fontsize=11, verticalalignment='top')

        # 3. Hour Distribution
        ax3 = fig.add_subplot(gs[1, 0])
        if self.hourly_commits:
            hours = list(range(24))
            values = [self.hourly_commits.get(h, 0) for h in hours]
            bars = ax3.bar(hours, values, color='skyblue', edgecolor='navy', alpha=0.7)

            # Highlight most active hours
            max_val = max(values) if values else 0
            for i, (h, v) in enumerate(zip(hours, values)):
                if v == max_val and max_val > 0:
                    bars[i].set_color('orange')

            ax3.set_title('⏰ Commits by Hour', fontweight='bold')
            ax3.set_xlabel('Hour of Day')
            ax3.set_ylabel('Total Commits')
            ax3.set_xticks(range(0, 24, 3))

        # 4. Language Distribution
        ax4 = fig.add_subplot(gs[1, 1])
        languages = {'Python': 70, 'Markdown': 20, 'YAML': 5, 'JSON': 5}
        colors = ['#3776ab', '#000000', '#cb171e', '#f0db4f']
        wedges, texts, autotexts = ax4.pie(
            languages.values(),
            labels=languages.keys(),
            autopct='%1.1f%%',
            colors=colors,
            explode=[0.1, 0, 0, 0]
        )
        ax4.set_title('💻 Language Distribution', fontweight='bold')

        # 5. Progress Bar
        ax5 = fig.add_subplot(gs[1, 2])
        ax5.axis('off')
        progress = ((total_days // 7) + 1) / 48 * 100  # Week progress

        # Draw progress bar
        bar_height = 0.3
        bar_y = 0.5

        # Background
        ax5.barh(bar_y, 100, height=bar_height, color='lightgray', alpha=0.3)
        # Progress
        ax5.barh(bar_y, progress, height=bar_height, color='green', alpha=0.7)

        ax5.set_xlim(0, 100)
        ax5.set_ylim(0, 1)
        ax5.text(50, 0.7, f'Journey Progress: {progress:.1f}%',
                ha='center', fontsize=12, fontweight='bold')
        ax5.text(50, 0.3, f'Week {(total_days // 7) + 1} of 48',
                ha='center', fontsize=10)

        # 6. Recent Achievements
        ax6 = fig.add_subplot(gs[2, :])
        ax6.axis('off')

        achievements_text = "🏆 Recent Achievements\n\n"
        if self.data.get('achievements_unlocked'):
            for ach in self.data['achievements_unlocked'][-5:]:
                achievements_text += f"• {ach}\n"
        else:
            achievements_text += "No achievements yet - make your first commit!"

        ax6.text(0.05, 0.9, achievements_text, transform=ax6.transAxes,
                fontsize=10, verticalalignment='top')

        plt.savefig(self.charts_dir / 'dashboard.png', dpi=150, bbox_inches='tight')
        plt.close()

    def generate_commit_history_chart(self):
        """Generate commit history chart"""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

        if self.commits:
            # Prepare data
            df = pd.DataFrame([
                {
                    'date': c['date'].date(),
                    'additions': c['additions'],
                    'deletions': c['deletions']
                }
                for c in self.commits
            ])

            # Group by date
            daily_stats = df.groupby('date').agg({
                'additions': 'sum',
                'deletions': 'sum'
            }).reset_index()

            # Cumulative sum
            daily_stats['cumulative_lines'] = (daily_stats['additions'] - daily_stats['deletions']).cumsum()

            # Plot additions/deletions
            ax1.bar(daily_stats['date'], daily_stats['additions'],
                   label='Lines Added', color='green', alpha=0.7)
            ax1.bar(daily_stats['date'], -daily_stats['deletions'],
                   label='Lines Deleted', color='red', alpha=0.7)
            ax1.set_title('📝 Code Changes Over Time', fontweight='bold')
            ax1.set_xlabel('Date')
            ax1.set_ylabel('Lines Changed')
            ax1.legend()
            ax1.grid(True, alpha=0.3)

            # Plot cumulative growth
            ax2.plot(daily_stats['date'], daily_stats['cumulative_lines'],
                    marker='o', linewidth=2, color='blue')
            ax2.fill_between(daily_stats['date'], 0, daily_stats['cumulative_lines'],
                            alpha=0.3, color='blue')
            ax2.set_title('📈 Cumulative Code Growth', fontweight='bold')
            ax2.set_xlabel('Date')
            ax2.set_ylabel('Total Lines')
            ax2.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig(self.charts_dir / 'commit_history.png', dpi=150, bbox_inches='tight')
        plt.close()

    def generate_activity_heatmap(self):
        """Generate GitHub-style activity heatmap"""
        fig, ax = plt.subplots(figsize=(14, 4))

        # Prepare data for last 12 weeks
        end_date = date.today()
        start_date = end_date - timedelta(weeks=12)

        # Create matrix for heatmap (weeks x days)
        weeks = 12
        days = 7
        activity_matrix = np.zeros((days, weeks))

        # Fill matrix with commit data
        current_date = start_date
        for week in range(weeks):
            for day in range(days):
                if current_date <= end_date:
                    date_str = current_date.strftime('%Y-%m-%d')
                    activity_matrix[day, week] = self.daily_commits.get(date_str, 0)
                current_date += timedelta(days=1)

        # Create heatmap
        im = ax.imshow(activity_matrix, cmap='YlOrRd', aspect='auto', vmin=0)

        # Set labels
        ax.set_title('📅 12-Week Activity Heatmap', fontweight='bold', pad=20)
        ax.set_ylabel('Day of Week')
        ax.set_xlabel('Week')

        # Set y-axis labels
        days_labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        ax.set_yticks(range(7))
        ax.set_yticklabels(days_labels)

        # Set x-axis labels (week numbers)
        week_labels = [f'W{i+1}' for i in range(weeks)]
        ax.set_xticks(range(weeks))
        ax.set_xticklabels(week_labels)

        # Add colorbar
        cbar = plt.colorbar(im, ax=ax)
        cbar.set_label('Commits', rotation=270, labelpad=15)

        # Add text annotations
        for week in range(weeks):
            for day in range(days):
                value = int(activity_matrix[day, week])
                if value > 0:
                    ax.text(week, day, str(value),
                           ha="center", va="center", color="black", fontsize=8)

        plt.tight_layout()
        plt.savefig(self.charts_dir / 'activity_heatmap.png', dpi=150, bbox_inches='tight')
        plt.close()

    def generate_code_growth_chart(self):
        """Generate code growth chart by file type"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

        if self.file_changes:
            # Top 10 most changed files
            file_stats = []
            for filename, stats in self.file_changes.items():
                if filename.endswith('.py'):
                    file_stats.append({
                        'file': filename.split('/')[-1][:20],  # Truncate long names
                        'changes': stats['added'] + stats['deleted']
                    })

            file_stats = sorted(file_stats, key=lambda x: x['changes'], reverse=True)[:10]

            if file_stats:
                files = [f['file'] for f in file_stats]
                changes = [f['changes'] for f in file_stats]

                bars = ax1.barh(range(len(files)), changes, color='steelblue')
                ax1.set_yticks(range(len(files)))
                ax1.set_yticklabels(files)
                ax1.set_xlabel('Total Changes (lines)')
                ax1.set_title('📂 Most Changed Files', fontweight='bold')
                ax1.grid(True, alpha=0.3, axis='x')

                # Color code by size
                max_changes = max(changes)
                for i, (bar, change) in enumerate(zip(bars, changes)):
                    if change > max_changes * 0.7:
                        bar.set_color('darkred')
                    elif change > max_changes * 0.4:
                        bar.set_color('orange')

        # Weekly commit trend
        if self.daily_commits:
            # Group by week
            weekly_commits = defaultdict(int)
            for date_str, count in self.daily_commits.items():
                date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
                week_num = (date_obj - date(2025, 9, 19)).days // 7 + 1
                weekly_commits[week_num] += count

            if weekly_commits:
                weeks = sorted(weekly_commits.keys())
                commits = [weekly_commits[w] for w in weeks]

                ax2.plot(weeks, commits, marker='o', linewidth=2, markersize=8, color='green')
                ax2.fill_between(weeks, commits, alpha=0.3, color='green')
                ax2.set_xlabel('Week Number')
                ax2.set_ylabel('Commits')
                ax2.set_title('📊 Weekly Commit Trend', fontweight='bold')
                ax2.grid(True, alpha=0.3)

                # Add trend line
                if len(weeks) > 1:
                    z = np.polyfit(weeks, commits, 1)
                    p = np.poly1d(z)
                    ax2.plot(weeks, p(weeks), "r--", alpha=0.5, label='Trend')
                    ax2.legend()

        plt.tight_layout()
        plt.savefig(self.charts_dir / 'code_growth.png', dpi=150, bbox_inches='tight')
        plt.close()

def main():
    generator = ProgressChartGenerator()
    generator.generate_all_charts()

    print("✅ Charts generated successfully!")
    print(f"📁 Charts saved to: {generator.charts_dir}")

if __name__ == "__main__":
    main()