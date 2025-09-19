#!/usr/bin/env python3
"""
Generate weekly learning issues based on curriculum
"""
import os
import sys
from datetime import datetime, timedelta
from github import Github

# Curriculum Definition
CURRICULUM = {
    1: {
        "phase": "Python Basics",
        "topics": ["Variables & Data Types", "Functions", "Control Flow"],
        "project": "Test Data Generator v1",
        "resources": ["Python for Everybody Ch 1-4", "HackerRank Python"]
    },
    2: {
        "phase": "Python Advanced",
        "topics": ["OOP", "File I/O", "Error Handling"],
        "project": "Test Data Generator v2",
        "resources": ["Python for Everybody Ch 5-8", "Real Python OOP"]
    },
    3: {
        "phase": "Data Structures",
        "topics": ["Lists & Dicts Deep Dive", "Algorithms", "Complexity"],
        "project": "Data Structure Visualizer",
        "resources": ["LeetCode Easy Problems", "Python DS Course"]
    },
    # ... weitere Wochen bis 48
}

def create_learning_issue(repo, week_num):
    """Create weekly learning goals issue"""
    week_data = CURRICULUM.get(week_num, CURRICULUM[1])
    
    title = f"📚 Week {week_num}: {week_data['phase']}"
    
    body = f"""# Week {week_num} Learning Goals

## 🎯 Focus: {week_data['phase']}

### 📖 Topics to Cover
{chr(10).join(f"- [ ] {topic}" for topic in week_data['topics'])}

### 💼 Project
- [ ] {week_data['project']}

### 📚 Resources
{chr(10).join(f"- {resource}" for resource in week_data['resources'])}

### ⏰ Time Allocation
- **Theory:** 6 hours
- **Practice:** 6 hours  
- **Project:** 4 hours
- **Total:** 16 hours

### 📊 Success Metrics
- [ ] Complete all topic exercises
- [ ] Project milestone achieved
- [ ] 10+ commits this week
- [ ] Blog post draft (optional)

---
*Automated by GitHub Actions*
"""
    
    issue = repo.create_issue(
        title=title,
        body=body,
        labels=["type-learning", f"week-{week_num}", "phase-1-foundation"],
        assignee=repo.owner.login
    )
    
    return issue

def create_project_issue(repo, week_num):
    """Create weekly project milestone"""
    week_data = CURRICULUM.get(week_num, CURRICULUM[1])
    
    title = f"💼 Week {week_num} Project: {week_data['project']}"
    
    body = f"""# Project Milestone: {week_data['project']}

## 📋 Requirements
- [ ] Basic implementation
- [ ] Documentation
- [ ] Tests (if applicable)
- [ ] GitHub commit

## 🎯 Definition of Done
- Code works as expected
- README updated
- Pushed to GitHub

## 📅 Deadline
End of Week {week_num}

---
*Automated by GitHub Actions*
"""
    
    issue = repo.create_issue(
        title=title,
        body=body,
        labels=["type-project", f"week-{week_num}"],
        assignee=repo.owner.login
    )
    
    return issue

def main():
    week_num = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    
    # GitHub setup
    token = os.environ['GITHUB_TOKEN']
    g = Github(token)
    repo = g.get_repo(os.environ['GITHUB_REPOSITORY'])
    
    # Create issues
    learning_issue = create_learning_issue(repo, week_num)
    project_issue = create_project_issue(repo, week_num)
    
    print(f"✅ Created learning issue: {learning_issue.number}")
    print(f"✅ Created project issue: {project_issue.number}")

if __name__ == "__main__":
    main()