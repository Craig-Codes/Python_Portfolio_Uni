# Convert bandwidth in Mbps to bps to calculate network capacity in bps
max_bandwidth = 1000  # max bandwidth in Mbps
max_bandwidth_bps = max_bandwidth * 1000000  # 1000000 bits per Megabit
print("The network capacity in bps: ", max_bandwidth_bps)

# Calculate the current usage
number_of_users = 200  # number of concurrent users
bandwidth_app_a = 200000  # bandwidth of application A in bps
bandwidth_app_b = 100000  # bandwidth of application B in bps
current_usage = (number_of_users * bandwidth_app_a) + (number_of_users * bandwidth_app_b)
print("The current usage in bps: ", current_usage)

# Calculate the current available bandwidth
available_bandwidth = max_bandwidth_bps - current_usage
print("The current available bandwidth in bps: ", available_bandwidth)

# Calculate the new applications bandwidth
bandwidth_app_new = 350000  # bandwidth of new application in bps
app_new_usage = bandwidth_app_new * number_of_users
print("The new applications requirements in bps: ", app_new_usage)

# Calculate the total bandwidth available if new app is installed in Mbps
bandwidth_all_apps = current_usage + app_new_usage
total_bandwidth_remaining_bps = max_bandwidth_bps - bandwidth_all_apps
total_bandwidth_remaining_mbps = total_bandwidth_remaining_bps / 1000000
print("The bandwidth available if the new application is installed (in Mbps): ", total_bandwidth_remaining_mbps)
