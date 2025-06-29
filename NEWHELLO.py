medical_cause = input("Do you have medical cause? (yes/no): ")


attendance = float(input("Enter your attendance percentage: "))


if medical_cause.lower() == "yes":
    if attendance >= 65:
        print("✅ You are eligible for the exam (medical reason).")
    else:
        print("❌ Not eligible. Attendance too low even with medical reason.")
else:
    if attendance >= 80:
        print("✅ You are eligible for the exam.")
    else:
        print("❌ Not eligible. Attendance must be at least 80%.")