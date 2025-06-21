# F.A.L.C.O.N. - CLI Version
# Focus & Alignment Layer for Conscious Optimization & Navigation

import json
import os
from datetime import datetime

DATA_FILE = "falcon_data.json"

# Initialize data file if not exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({"logs": [], "streak": 0, "last_success_date": None}, f)

# Load data
def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Save data
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Log daily mission
def log_today():
    print("\n🔰 Logging Today's Mission")
    date = datetime.now().strftime("%Y-%m-%d")
    top_goals = [input(f"Top Goal #{i+1}: ") for i in range(3)]
    threats = input("Distractions expected today: ")
    plan = input("Anti-distraction strategy: ")

    log = {
        "date": date,
        "top_goals": top_goals,
        "threats": threats,
        "strategy": plan,
        "focus_blocks": [],
        "reflection": ""
    }

    data = load_data()
    data["logs"].append(log)
    save_data(data)
    print("✅ Mission logged successfully.")

# Log focus block
def log_focus():
    data = load_data()
    if not data["logs"]:
        print("⚠️ No daily log found. Log today first.")
        return
    block = input("Task Focused On: ")
    duration = input("Duration (mins): ")
    depth = input("Focus Depth (1-5): ")

    data["logs"][-1]["focus_blocks"].append({
        "task": block,
        "duration": duration,
        "depth": depth
    })
    save_data(data)
    print("🕒 Focus block added.")

# Log reflection
def log_reflection():
    data = load_data()
    if not data["logs"]:
        print("⚠️ No daily log found. Log today first.")
        return
    print("\n🧠 Reflect on your day:")
    win = input("What did you win at today? ")
    drift = input("Where did you drift or get distracted? ")
    plan = input("What will you improve tomorrow? ")

    reflection = f"Wins: {win}\nDrift: {drift}\nPlan: {plan}"
    data["logs"][-1]["reflection"] = reflection
    save_data(data)
    print("✅ Reflection saved.")

# View last entry
def view_last():
    data = load_data()
    if not data["logs"]:
        print("⚠️ No logs available.")
        return
    last = data["logs"][-1]
    print(f"\n📅 Date: {last['date']}")
    print("🎯 Top Goals:")
    for i, goal in enumerate(last["top_goals"], 1):
        print(f"  {i}. {goal}")
    print(f"⚠️ Distractions: {last['threats']}")
    print(f"🛡 Strategy: {last['strategy']}")
    print("🕒 Focus Blocks:")
    for b in last["focus_blocks"]:
        print(f"  - {b['task']} ({b['duration']} mins, depth {b['depth']})")
    print(f"🧠 Reflection:\n{last['reflection']}")

# Reset protocol (Guts Mode)
def guts_reset():
    print("\n⚔️ GUTS RESET PROTOCOL INITIATED")
    print("Step 1: Stand up, drink water")
    print("Step 2: Do 10 pushups or jumping jacks")
    print("Step 3: Say your mission out loud")
    print("Step 4: Visualize your empire")
    print("Step 5: Start a 25-minute deep focus session NOW")

# Update streak system
def update_streak():
    data = load_data()
    today = datetime.now().strftime("%Y-%m-%d")
    last = data.get("last_success_date")

    if last == today:
        print("Streak already updated for today.")
        return

    if last:
        last_date = datetime.strptime(last, "%Y-%m-%d")
        delta = (datetime.now() - last_date).days
        if delta == 1:
            data["streak"] += 1
        else:
            data["streak"] = 1
    else:
        data["streak"] = 1

    data["last_success_date"] = today
    save_data(data)
    print(f"🔥 Streak updated: {data['streak']} days strong!")

# CLI Menu
def main():
    while True:
        print("\n=== 🦅 F.A.L.C.O.N. CLI ===")
        print("1. Log Today’s Mission")
        print("2. Add Focus Block")
        print("3. Reflect on the Day")
        print("4. View Last Entry")
        print("5. Activate GUTS Reset Protocol")
        print("6. Update Discipline Streak")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            log_today()
        elif choice == '2':
            log_focus()
        elif choice == '3':
            log_reflection()
        elif choice == '4':
            view_last()
        elif choice == '5':
            guts_reset()
        elif choice == '6':
            update_streak()
        elif choice == '7':
            print("Goodbye, Commander.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
