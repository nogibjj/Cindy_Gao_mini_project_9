from mylib.lib import (
    load_dataset,
    get_mean,
    get_median,
    get_std,
    get_min,
    get_max,
    get_quantile,
)
import pandas as pd
import matplotlib.pyplot as plt


# General describe function
def general_describe(csv):
    df = load_dataset(csv)
    description = df.describe()
    return description


def custom_describe(csv, col):
    """custom describe"""
    df = load_dataset(csv)
    describe_dict = {
        "name": col,
        "mean": get_mean(df, col),
        "std": get_std(df, col),
        "median": get_median(df, col),
        "75 quantile": get_quantile(df, col, 0.75),
        "min": get_min(df, col),
        "max": get_max(df, col),
    }
    return describe_dict


# Data Manipulation Function - change the column name
def change_column_name(df, old_column_name, new_column_name):
    new_df = df.rename(columns={old_column_name: new_column_name})
    return new_df


# Save histogram to markdown
def create_murder_histogram(csv):
    df = load_dataset(csv)
    murder_2014 = df["2014_murders"]
    murder_2015 = df["2015_murders"]

    plt.figure(figsize=(10, 6))
    plt.hist(
        murder_2014.dropna(),
        bins=30,
        alpha=0.5,
        label="2014 Murders",
        color="blue",
        edgecolor="black",
    )
    plt.hist(
        murder_2015.dropna(),
        bins=30,
        alpha=0.5,
        label="2015 Murders",
        color="red",
        edgecolor="black",
    )

    plt.title("Histogram of Murders in 2014 and 2015")
    plt.xlabel("Number of Murders")
    plt.ylabel("Frequency")
    plt.legend(loc="upper right")
    plt.grid(True)
    plt.savefig("figure.png")


def create_line_chart(csv):
    df = load_dataset(csv)
    df_change = df[["state", "change"]]
    df_change = df_change.sort_values(by="state")
    df_change.set_index("state", inplace=True)
    plt.figure(figsize=(12, 6))
    plt.plot(df_change.index, df_change["change"], marker="o")
    plt.title("Change in Murder Rates by State in 2015")
    plt.xlabel("State")
    plt.ylabel("Change in Murder Rates (%)")
    plt.xticks(rotation=90)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# Save markdown with both diagrams
def save_to_md(csv):
    df = load_dataset(csv)
    description = df.describe()
    summary_table = description.to_markdown()

    with open("report.md", "w") as file:
        file.write("# Murder Data Analysis\n")
        file.write("Describe:\n")
        file.write(summary_table)
        file.write("<br><br>\n")
        file.write("## Histogram\n")
        file.write("![Histogram](Histogram_of_Murders_2014_2015.png)\n")
        file.write("## Line Chart\n")
        file.write("![Line Chart](Change_in_Murder_Rates_by_State_in_2015.png)\n")
