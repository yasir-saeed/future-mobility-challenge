import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a pandas DataFrame
df = pd.read_csv("https://apmonitor.com/pds/uploads/Main/auto_warmup.txt")
df.dropna(how='all', inplace=True)


# Check if "Time (sec)" column exists
if "Time (sec)" in df.columns:
    time_col = "Time (sec)"
elif "time" in df.columns:
    time_col = "time"
else:
    raise ValueError("Neither 'Time (sec)' nor 'time' column exists")


# Get the number of columns in the DataFrame
n_cols = len(df.columns) - 1

# Create the subplots
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 6))

# Initialize the counter for the subplots
counter = 0

# Plot the first subplot
ax.plot(df[time_col], df[df.columns[counter + 1]], label=df.columns[counter + 1])
ax.set_title(df.columns[counter + 1])

# Show the navigation buttons
nav_buttons = plt.axes([0.55, -0.03, 0.3, 0.1])
nav_buttons2 = plt.axes([0.15, -0.03, 0.3, 0.1])


next_button = plt.Button(nav_buttons, "Next", color="gray", hovercolor="blue")
previous_button = plt.Button(nav_buttons2, "Previous", color="gray", hovercolor="blue")


# Define the function to handle the next button click
def next_plot(event):
    global counter
    counter += 1
    if counter >= n_cols:
        counter = 0
    ax.clear()
    ax.plot(df[time_col], df[df.columns[counter + 1]], label=df.columns[counter + 1])
    ax.set_title(df.columns[counter + 1])
    plt.draw()


# Define the function to handle the previous button click
def prev_plot(event):
    global counter
    counter -= 1
    if counter < 0:
        counter = n_cols - 1
    ax.clear()
    ax.plot(df[time_col], df[df.columns[counter + 1]], label=df.columns[counter + 1])
    ax.set_title(df.columns[counter + 1])
    plt.draw()


# Connect the functions to the buttons
next_button.on_clicked(next_plot)
previous_button.on_clicked(prev_plot)

# Show the plot
plt.show()
