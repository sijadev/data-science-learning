#!/usr/bin/env python3
"""
GitHub Project Setup Script
Automatisiert die Erstellung von Issues, Labels und Milestones
"""

import requests
import json
import os
from datetime import datetime, timedelta

# Configuration
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")  # Setze als Umgebungsvariable
if not GITHUB_TOKEN:
    print("❌ Bitte setze GITHUB_TOKEN als Umgebungsvariable!")
    print("   export GITHUB_TOKEN='dein_neuer_token'")
    exit(1)

REPO_OWNER = "sijadev"
REPO_NAME = "data-science-learning"
PROJECT_NUMBER = 7

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def create_label(name, color, description=""):
    """Erstellt ein Label im Repository"""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/labels"
    data = {
        "name": name,
        "color": color,
        "description": description
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f"✅ Label erstellt: {name}")
    elif response.status_code == 422:
        error_msg = response.json().get('message', 'Unbekannter Fehler')
        errors = response.json().get('errors', [])
        if any('already_exists' in str(e) for e in errors):
            print(f"ℹ️  Label existiert bereits: {name}")
        else:
            print(f"❌ Fehler 422 bei Label {name}: {error_msg}")
            print(f"   Details: {errors}")
    else:
        print(f"❌ Fehler bei Label {name}: {response.status_code}")
        print(f"   Response: {response.text}")

def create_milestone(title, description="", due_on=None, state="open"):
    """Erstellt einen Milestone im Repository"""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/milestones"
    data = {
        "title": title,
        "description": description,
        "state": state
    }
    if due_on:
        data["due_on"] = due_on  # Format: 2024-12-31T23:59:59Z

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f"✅ Milestone erstellt: {title}")
        return response.json()["number"]
    elif response.status_code == 422:
        error_msg = response.json().get('message', 'Unbekannter Fehler')
        if 'already_exists' in error_msg.lower():
            print(f"ℹ️  Milestone existiert bereits: {title}")
            # Hole die Milestone-Nummer des existierenden Milestones
            milestones_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/milestones"
            response = requests.get(milestones_url, headers=headers)
            for milestone in response.json():
                if milestone['title'] == title:
                    return milestone['number']
        else:
            print(f"❌ Fehler 422 bei Milestone {title}: {error_msg}")
        return None
    else:
        print(f"❌ Fehler bei Milestone {title}: {response.status_code}")
        print(f"   Response: {response.text}")
        return None

def create_issue(title, body, labels=[], milestone=None):
    """Erstellt ein Issue im Repository"""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"
    data = {
        "title": title,
        "body": body,
        "labels": labels,
        "assignee": REPO_OWNER
    }
    if milestone:
        data["milestone"] = milestone

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f"✅ Issue erstellt: {title}")
        return response.json()["number"]
    elif response.status_code == 422:
        error_msg = response.json().get('message', 'Unbekannter Fehler')
        errors = response.json().get('errors', [])
        print(f"❌ Fehler 422 bei Issue {title}: {error_msg}")
        print(f"   Details: {errors}")
        # Häufige 422-Fehler
        if any('already_exists' in str(e) for e in errors):
            print(f"   → Issue mit diesem Titel existiert möglicherweise bereits")
        if any('label' in str(e).lower() for e in errors):
            print(f"   → Eines oder mehrere Labels existieren nicht")
        return None
    else:
        print(f"❌ Fehler bei Issue {title}: {response.status_code}")
        print(f"   Response: {response.text}")
        return None

def setup_labels():
    """Erstellt alle benötigten Labels"""
    labels = [
        ("phase-1-foundation", "0E8A16", "Months 1-3: Basics"),
        ("phase-2-ml", "FFA500", "Months 4-7: Machine Learning"),
        ("phase-3-production", "FF0000", "Months 8-12: Production"),
        ("type-learning", "1D76DB", "Course/Tutorial work"),
        ("type-project", "5319E7", "Portfolio project"),
        ("type-exercise", "28A745", "Practice/Challenges"),
        ("priority-high", "FF6B6B", "Must do this week"),
        ("priority-medium", "FFD93D", "Should do soon"),
    ]
    
    for name, color, desc in labels:
        create_label(name, color, desc)

def setup_milestones():
    """Erstellt Milestones für das Projekt"""
    from datetime import datetime, timedelta

    milestones = [
        {
            "title": "Week 1 - Foundation Setup",
            "description": "Python basics, environment setup, first project",
            "due_on": (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%dT23:59:59Z")
        },
        {
            "title": "Month 1 - Python Mastery",
            "description": "Complete Python fundamentals and basic projects",
            "due_on": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%dT23:59:59Z")
        },
        {
            "title": "Phase 1 - Foundation (3 Months)",
            "description": "Python, SQL, Statistics, Basic Data Analysis",
            "due_on": (datetime.now() + timedelta(days=90)).strftime("%Y-%m-%dT23:59:59Z")
        }
    ]

    milestone_numbers = {}
    for milestone in milestones:
        number = create_milestone(
            milestone["title"],
            milestone["description"],
            milestone.get("due_on")
        )
        if number:
            milestone_numbers[milestone["title"]] = number

    return milestone_numbers

def setup_week1_issues(milestone_number=None):
    """Erstellt Issues für Woche 1"""
    issues = [
        {
            "title": "🚀 Setup Development Environment",
            "body": """## Tasks
- [ ] Mamba Forge environment configured
- [ ] VS Code extensions installed
- [ ] Git repository structured
- [ ] Essential packages installed

## Verification
Run `python verify_setup.py` to confirm everything works""",
            "labels": ["phase-1-foundation", "type-learning", "priority-high"]
        },
        {
            "title": "📖 Complete Python Basics - Week 1",
            "body": """## Learning Goals
- [ ] Variables and Data Types (2h)
- [ ] Control Flow (2h)
- [ ] Functions and Modules (3h)
- [ ] File I/O basics (2h)

## Resources
- Python for Everybody - Chapters 1-4
- Complete 10 HackerRank challenges""",
            "labels": ["phase-1-foundation", "type-learning"]
        },
        {
            "title": "💻 Build Test Data Generator v1.0",
            "body": """## Requirements
- [ ] Generate random user data
- [ ] Support JSON/CSV output
- [ ] Command-line interface
- [ ] Error handling

## Deliverables
- Source code in `/projects/test-data-generator`
- README with usage examples""",
            "labels": ["phase-1-foundation", "type-project", "priority-high"]
        }
    ]
    
    for issue in issues:
        create_issue(issue["title"], issue["body"], issue["labels"], milestone_number)

if __name__ == "__main__":
    print("🚀 Setting up GitHub Project...")

    # Setup labels
    print("\n📏 Creating labels...")
    setup_labels()

    # Setup milestones
    print("\n🎯 Creating milestones...")
    milestones = setup_milestones()
    week1_milestone = milestones.get("Week 1 - Foundation Setup")

    # Create Week 1 issues
    print("\n📝 Creating Week 1 issues...")
    setup_week1_issues(week1_milestone)

    print("\n✅ Setup complete!")