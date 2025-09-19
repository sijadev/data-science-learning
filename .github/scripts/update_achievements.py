#!/usr/bin/env python3
"""
Update achievements based on GitHub activity and learning progress
"""
import os
import json
from datetime import datetime, date, timedelta
from github import Github


def calculate_achievement_metrics(repo):
    """Calculate metrics for achievement tracking"""
    # Calculate weeks since start
    start_date = date(2025, 9, 19)
    current_date = date.today()
    weeks_active = ((current_date - start_date).days // 7) + 1

    # Get commits in last 30 days
    since_date = datetime.now() - timedelta(days=30)
    recent_commits = list(repo.get_commits(since=since_date))

    # Get all issues
    all_issues = list(repo.get_issues(state='all'))
    closed_issues = [issue for issue in all_issues if issue.state == 'closed']
    learning_issues = [issue for issue in all_issues if any(label.name == 'type-learning' for label in issue.labels)]

    # Calculate streak (consecutive days with commits)
    commit_dates = set()
    for commit in repo.get_commits():
        commit_dates.add(commit.commit.author.date.date())

    streak = calculate_commit_streak(commit_dates)

    metrics = {
        "total_commits": repo.get_commits().totalCount,
        "recent_commits": len(recent_commits),
        "total_issues": len(all_issues),
        "closed_issues": len(closed_issues),
        "learning_issues": len(learning_issues),
        "weeks_active": weeks_active,
        "commit_streak": streak,
        "last_updated": datetime.now().isoformat()
    }

    return metrics


def calculate_commit_streak(commit_dates):
    """Calculate current commit streak"""
    if not commit_dates:
        return 0

    current_date = date.today()
    streak = 0

    # Start from today or yesterday
    check_date = current_date
    if current_date not in commit_dates:
        check_date = current_date - timedelta(days=1)

    while check_date in commit_dates:
        streak += 1
        check_date -= timedelta(days=1)

    return streak


def check_achievements(metrics):
    """Check which achievements have been unlocked"""
    achievements = []

    # Commitment achievements
    if metrics["commit_streak"] >= 7:
        achievements.append({
            "id": "weekly_warrior",
            "title": "🔥 Weekly Warrior",
            "description": f"Committed code for {metrics['commit_streak']} consecutive days",
            "unlocked_at": datetime.now().isoformat()
        })

    if metrics["commit_streak"] >= 30:
        achievements.append({
            "id": "monthly_master",
            "title": "🏆 Monthly Master",
            "description": f"Maintained a {metrics['commit_streak']}-day commit streak",
            "unlocked_at": datetime.now().isoformat()
        })

    # Learning achievements
    if metrics["learning_issues"] >= 10:
        achievements.append({
            "id": "knowledge_seeker",
            "title": "📚 Knowledge Seeker",
            "description": f"Created {metrics['learning_issues']} learning issues",
            "unlocked_at": datetime.now().isoformat()
        })

    if metrics["closed_issues"] >= 20:
        achievements.append({
            "id": "task_crusher",
            "title": "💪 Task Crusher",
            "description": f"Completed {metrics['closed_issues']} issues",
            "unlocked_at": datetime.now().isoformat()
        })

    # Milestone achievements
    if metrics["weeks_active"] >= 4:
        achievements.append({
            "id": "one_month",
            "title": "🗓️ One Month Strong",
            "description": f"Active for {metrics['weeks_active']} weeks",
            "unlocked_at": datetime.now().isoformat()
        })

    if metrics["weeks_active"] >= 12:
        achievements.append({
            "id": "quarter_champion",
            "title": "🌟 Quarter Champion",
            "description": f"Consistently learning for {metrics['weeks_active']} weeks",
            "unlocked_at": datetime.now().isoformat()
        })

    # Code achievements
    if metrics["total_commits"] >= 50:
        achievements.append({
            "id": "commit_master",
            "title": "⚡ Commit Master",
            "description": f"Made {metrics['total_commits']} total commits",
            "unlocked_at": datetime.now().isoformat()
        })

    if metrics["total_commits"] >= 100:
        achievements.append({
            "id": "centurion",
            "title": "🎯 Centurion",
            "description": f"Reached the {metrics['total_commits']} commit milestone",
            "unlocked_at": datetime.now().isoformat()
        })

    return achievements


def load_existing_achievements():
    """Load previously unlocked achievements"""
    achievements_file = 'achievements.json'
    if os.path.exists(achievements_file):
        with open(achievements_file, 'r') as f:
            return json.load(f)
    return {"unlocked": [], "metrics": {}}


def save_achievements(data):
    """Save achievements to file"""
    with open('achievements.json', 'w') as f:
        json.dump(data, f, indent=2)


def generate_achievements_badge():
    """Generate achievements badge for README"""
    data = load_existing_achievements()
    unlocked = data.get("unlocked", [])

    if not unlocked:
        return "🏃‍♂️ **Getting Started** - No achievements yet"

    # Count achievements by category
    categories = {
        "commitment": ["weekly_warrior", "monthly_master"],
        "learning": ["knowledge_seeker", "task_crusher"],
        "milestone": ["one_month", "quarter_champion"],
        "code": ["commit_master", "centurion"]
    }

    badge_text = "🏆 **Achievements Unlocked**: "
    achievement_icons = []

    for achievement in unlocked:
        if achievement["id"] in categories["commitment"]:
            achievement_icons.append("🔥")
        elif achievement["id"] in categories["learning"]:
            achievement_icons.append("📚")
        elif achievement["id"] in categories["milestone"]:
            achievement_icons.append("🗓️")
        elif achievement["id"] in categories["code"]:
            achievement_icons.append("⚡")

    badge_text += "".join(set(achievement_icons)) + f" ({len(unlocked)} total)"

    return badge_text


def create_achievement_notification(new_achievements):
    """Create issue notification for new achievements"""
    if not new_achievements:
        return None

    body = "# 🎉 New Achievements Unlocked!\n\n"
    body += "Congratulations! You've unlocked the following achievements:\n\n"

    for achievement in new_achievements:
        body += f"## {achievement['title']}\n"
        body += f"{achievement['description']}\n\n"

    body += "Keep up the great work! 🚀\n\n"
    body += "---\n*Automated by Achievement Tracker*"

    return {
        "title": f"🏆 Achievement Unlocked: {new_achievements[0]['title']}" + (f" (+{len(new_achievements)-1} more)" if len(new_achievements) > 1 else ""),
        "body": body,
        "labels": ["achievement", "automated"]
    }


def main():
    """Main execution"""
    # Setup GitHub
    token = os.environ['GITHUB_TOKEN']
    g = Github(token)
    repo = g.get_repo(os.environ['GITHUB_REPOSITORY'])

    # Calculate current metrics
    metrics = calculate_achievement_metrics(repo)

    # Check for new achievements
    current_achievements = check_achievements(metrics)

    # Load existing data
    existing_data = load_existing_achievements()
    existing_ids = {ach["id"] for ach in existing_data.get("unlocked", [])}

    # Find new achievements
    new_achievements = [ach for ach in current_achievements if ach["id"] not in existing_ids]

    # Update data
    all_achievements = existing_data.get("unlocked", []) + new_achievements
    updated_data = {
        "unlocked": all_achievements,
        "metrics": metrics,
        "last_updated": datetime.now().isoformat()
    }

    # Save updated achievements
    save_achievements(updated_data)

    # Create notification for new achievements
    if new_achievements:
        notification = create_achievement_notification(new_achievements)
        if notification:
            issue = repo.create_issue(
                title=notification["title"],
                body=notification["body"],
                labels=notification["labels"]
            )
            print(f"✅ Achievement notification created: {issue.html_url}")

    # Generate badge
    badge = generate_achievements_badge()
    print(f"📊 Achievement Status: {badge}")

    print(f"✅ Achievements updated. Total unlocked: {len(all_achievements)}")
    print(f"📈 Current metrics: {metrics['total_commits']} commits, {metrics['commit_streak']}-day streak")


if __name__ == "__main__":
    main()