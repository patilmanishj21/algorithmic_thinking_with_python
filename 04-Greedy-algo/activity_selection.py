# Example: Activity Selection Problem
# Input: Start and end times of activities
# Goal: Select max number of non-overlapping activities

# Greedy Step:
# Always choose the activity that ends earliest.

activities = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9)]

# Sort by end time
activities.sort(key=lambda x: x[1])


selected = []
end_time = 0

for start, end in activities:
    print(start,end)
    if start >= end_time:
        selected.append((start, end))
        end_time = end

print("Selected activities:", selected)