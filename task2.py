import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Create DataFrame using given data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "ProductA": [1200, 1350, 1600, 1500, 1700, 1800],
    "ProductB": [900, 950, 1100, 1050, 1150, 1250],
    "ProductC": [700, 750, 850, 800, 900, 950]
}

df = pd.DataFrame(data)

# Convert to long format for Plotly
df_long = df.melt(
    id_vars="Month",
    var_name="Product",
    value_name="Sales"
)

# Menu
print("\nChoose Visualization Type:")
print("1. Line Chart (Matplotlib)")
print("2. Bar Chart (Matplotlib)")
print("3. Plotly Interactive Line Chart")

choice = input("Enter your choice (1 / 2 / 3): ")

# Line Chart
if choice == "1":
    plt.plot(df["Month"], df["ProductA"], label="Product A")
    plt.plot(df["Month"], df["ProductB"], label="Product B")
    plt.plot(df["Month"], df["ProductC"], label="Product C")

    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.title("Monthly Sales - Line Chart")
    plt.legend()
    plt.show()

# Bar Chart
elif choice == "2":
    x = range(len(df["Month"]))
    plt.bar(x, df["ProductA"], width=0.25, label="Product A")
    plt.bar([i + 0.25 for i in x], df["ProductB"], width=0.25, label="Product B")
    plt.bar([i + 0.5 for i in x], df["ProductC"], width=0.25, label="Product C")

    plt.xticks([i + 0.25 for i in x], df["Month"])
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.title("Monthly Sales - Bar Chart")
    plt.legend()
    plt.show()

# Plotly Interactive Line Chart
elif choice == "3":
    fig = px.line(
        df_long,
        x="Month",
        y="Sales",
        color="Product",
        title="Monthly Sales (Interactive Line Chart)"
    )
    fig.show()

else:
    print("Invalid choice! Please select 1, 2, or 3.")
