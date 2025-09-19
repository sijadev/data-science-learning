#!/usr/bin/env python3
"""
Generate weekly progress report with metrics
"""
import os
import json
from datetime import datetime, date, timedelta
from github import Github
import matplotlib.pyplot as plt
import pandas as pd

def calculate_week_number():
    """Calculate current week number since start"""
    start_date = date(2025, 9, 19)
    current_date = date.today()
    week_num = ((current_date - start_date).days // 7) + 1
    return min(week_num, 48)

def collect_github_metrics(repo, week_num):
    """Collect GitHub activity metrics"""
    # Calculate date range for this week
    start_date = date(2025, 9, 19) + timedelta(weeks=week_num-1)
    end_date = start_date + timedelta(days=6)
    
    # Collect commits
    commits = list(repo.get_commits(
        since=datetime.combine(start_date, datetime.min.time()),
        until=datetime.combine(end_date, datetime.max.time())
    ))
    
    # Collect closed issues
    closed_issues = list(repo.get_issues(
        state='closed',
        since=datetime.combine(start_date, datetime.min.time())
    ))
    
    # Collect open issues
    open_issues = list(repo.get_issues(state='open'))
    
    metrics = {
        "week": week_num,
        "commits": len(commits),
        "issues_closed": len(closed_issues),
        "issues_open": len(open_issues),
        "files_changed": len(set(file.filename for commit in commits for file in commit.files)),
        "lines_added": sum(file.additions for commit in commits for file in commit.files),
        "lines_deleted": sum(file.deletions for commit in commits for file in commit.files)
    }
    
    return metrics

def generate_progress_chart(metrics_history):
    """Generate progress visualization"""
    df = pd.DataFrame(metrics_history)
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle('Weekly Progress Dashboard', fontsize=16)
    
    # Commits over time
    axes[0, 0].plot(df['week'], df['commits'], marker='o')
    axes[0, 0].set_title('Commits per Week')
    axes[0, 0].set_xlabel('Week')
    axes[0, 0].set_ylabel('Number of Commits')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Issues completed
    axes[0, 1].bar(df['week'], df['issues_closed'], color='green', alpha=0.7)
    axes[0, 1].set_title('Issues Completed')
    axes[0, 1].set_xlabel('Week')
    axes[0, 1].set_ylabel('Issues')
    
    # Code changes
    axes[1, 0].plot(df['week'], df['lines_added'], label='Added', color='green')
    axes[1, 0].plot(df['week'], df['lines_deleted'], label='Deleted', color='red')
    axes[1, 0].set_title('Code Changes')
    axes[1, 0].set_xlabel('Week')
    axes[1, 0].set_ylabel('Lines')
    axes[1, 0].legend()
    
    # Cumulative progress
    df['cumulative_commits'] = df['commits'].cumsum()
    axes[1, 1].fill_between(df['week'], df['cumulative_commits'], alpha=0.3)
    axes[1, 1].plot(df['week'], df['cumulative_commits'], marker='o')
    axes[1, 1].set_title('Cumulative Progress')
    axes[1, 1].set_xlabel('Week')
    axes[1, 1].set_ylabel('Total Commits')
    
    plt.tight_layout()
    
    # Save chart
    chart_path = f'reports/week{df["week"].iloc[-1]}-progress.png'
    plt.savefig(chart_path, dpi=150, bbox_inches='tight')
    
    return chart_path

def generate_report(metrics):
    """Generate markdown report"""
    week_num = metrics['week']
    
    report = f"""# 📊 Week {week_num} Progress Report

*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*

## 📈 Metrics Overview

| Metric | Value | Status |
|--------|-------|--------|
| Commits | {metrics['commits']} | {'✅' if metrics['commits'] >= 5 else '⚠️'} |
| Issues Closed | {metrics['issues_closed']} | {'✅' if metrics['issues_closed'] >= 2 else '⚠️'} |
| Files Changed | {metrics['files_changed']} | - |
| Lines Added | {metrics['lines_added']} | - |
| Lines Deleted | {metrics['lines_deleted']} | - |

## 🎯 Week Status
- **Target Hours:** 16-20
- **Commits Target:** 5+ {'✅ Achieved' if metrics['commits'] >= 5 else f"❌ Missed (got {metrics['commits']})"}
- **Open Issues:** {metrics['issues_open']}

## 📝 Recommendations
"""
    
    if metrics['commits'] < 5:
        report += "- ⚠️ Increase commit frequency - aim for daily commits\n"
    if metrics['issues_closed'] < 2:
        report += "- ⚠️ Focus on closing open issues\n"
    if metrics['issues_open'] > 10:
        report += "- ⚠️ Too many open issues - prioritize and close\n"
    
    report += """
## 📅 Next Week Preview
Check the [Project Board](https://github.com/users/sijadev/projects/6) for upcoming tasks.

---
*Automated by GitHub Actions*
"""
    
    return report

def main():
    # Setup
    token = os.environ['GITHUB_TOKEN']
    g = Github(token)
    repo = g.get_repo(os.environ['GITHUB_REPOSITORY'])
    
    week_num = calculate_week_number()
    
    # Collect metrics
    metrics = collect_github_metrics(repo, week_num)
    
    # Load historical data
    history_file = 'reports/metrics_history.json'
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            metrics_history = json.load(f)
    else:
        metrics_history = []
    
    metrics_history.append(metrics)
    
    # Save updated history
    os.makedirs('reports', exist_ok=True)
    with open(history_file, 'w') as f:
        json.dump(metrics_history, f, indent=2)
    
    # Generate chart
    if len(metrics_history) > 1:
        chart_path = generate_progress_chart(metrics_history)
        print(f"✅ Chart generated: {chart_path}")
    
    # Generate report
    report = generate_report(metrics)

    # Create reports directory if it doesn't exist
    os.makedirs('reports', exist_ok=True)

    report_path = f'reports/week{week_num}-report.md'

    with open(report_path, 'w') as f:
        f.write(report)
    
    print(f"✅ Report generated: {report_path}")
    
    # Set environment variable for workflow
    print(f"WEEK_NUM={week_num}")
    os.environ['WEEK_NUM'] = str(week_num)

if __name__ == "__main__":
    main()