# The Log Hunter - Finding attacks in text files

log_file_path = "server_logs.txt"
attack_keyword = "Failed"
count = 0

print("--- SCANNING FOR ATTACKS ---")

# Opening the file safely
with open(log_file_path, "r") as file:
    # Loop through every line in the file
    for line in file:
        # Check if the word "Failed" is in that line
        if attack_keyword in line:
            print("ALERT FOUND:", line.strip())
            count += 1

print("----------------------------")
print(f"Total Attack Attempts Found: {count}")
