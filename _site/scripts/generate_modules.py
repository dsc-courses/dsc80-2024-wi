"""Generate week-by-week schedule for website from CSV file.

Use this to convert from the course calendar spreadsheet to modules that work
with the course website template. Only run it on the weeks that haven't
occurred yet, otherwise it'll erase any manual work. Run from the root
directory of this repo, **not** from the scripts folder.

Usage:
    generate_modules.py CSV_FILE

Examples:
    python scripts/generate_modules.py scripts/fa23.csv
"""

import numpy as np
import pandas as pd
from docopt import docopt
from yaml import dump


def generate_modules(csv_file):
    df = (
        pd.read_csv(csv_file)
        .pipe(ffill_weeks)
        .pipe(parse_dates)
        .pipe(melt_into_events)
        .pipe(mark_exams_and_canceled_lectures)
        .pipe(number_events)
    )
    df.pipe(write_into_module_files)


def ffill_weeks(df):
    cols = {"week": df["Week"].ffill(), "week_title": df["Week Title"].ffill()}
    return df.assign(**cols).drop(columns=["Week", "Week Title"])


def parse_dates(df):
    return df.assign(
        date=pd.to_datetime(df["Date"], format="%a %m/%d/%y")
    ).drop(columns=["Date"])


def melt_into_events(df):
    return (
        df.melt(
            id_vars=["week", "week_title", "date"],
            value_vars=["Lecture", "Discussion", "Lab Due", "Project Due"],
            var_name="event_type",
            value_name="title",
        )
        .dropna(subset=["title"])
        .assign(week=lambda df: df["week"].astype(int))
        .sort_values("date")
    )


def mark_exams_and_canceled_lectures(
    df, cancelled_prefix="NO ", exam_substring="Exam"
):
    canceled = df["title"].str.startswith(cancelled_prefix)
    exams = df["title"].str.contains(exam_substring)
    marked_events = (
        df["event_type"].mask(canceled, "Canceled").mask(exams, "Exam")
    )
    return df.assign(event_type=marked_events)


def number_events(df):
    # Number lectures from 1-N, labs from 1-N, projects from 1-N, etc.
    #
    # [1] Labs: Need to take out Lab 1, Lab 2, etc. from the title
    # [2] Projects: Extract number from "Project 1 checkpoint", "Project 2", etc.
    # [3] Lectures: Number from 1-N
    # [4] Discussions: Number from 1-N
    # [5] Exams: Don't number
    # [6] Canceled: Don't number
    df = df.copy()

    # [1] Labs
    lab_titles_split = df.query('event_type == "Lab Due"')["title"].str.split(
        ": "
    )
    lab_numbers = lab_titles_split.str[0].str.upper()
    lab_titles = lab_titles_split.str[1]
    df.loc[lab_titles.index, "title"] = lab_titles

    # [2] Projects
    project_numbers = "PROJ " + df.query('event_type == "Project Due"')[
        "title"
    ].str.extract(r"Project (\d+)")

    # [3] Lectures
    lecs = df.query('event_type == "Lecture"')
    lec_numbers = "LEC " + pd.Series(
        np.arange(len(lecs)) + 1, lecs.index
    ).astype(str)

    # [4] Discussions
    discs = df.query('event_type == "Discussion"')
    disc_numbers = "DISC " + pd.Series(
        np.arange(len(discs)) + 1, discs.index
    ).astype(str)

    # [5] Exams
    exam_numbers = df.query('event_type == "Exam"').assign(
        event_numbers="EXAM"
    )["event_numbers"]

    # [6] Canceled
    # Don't actually need to handle to leave as NaN

    event_numbers = pd.concat(
        [lab_numbers, project_numbers, lec_numbers, disc_numbers, exam_numbers]
    )
    return df.assign(event_number=event_numbers)


def write_into_module_files(
    df,
    event_type_as_css_class={
        "Lab Due": "lab",
        "Project Due": "proj",
        "Lecture": "lecture",
        "Discussion": "disc",
        "Exam": "exam",
        "Canceled": "canceled",
    },
):
    def make_days(events):
        return [
            {
                "name": e.event_number,
                "type": event_type_as_css_class[e.event_type],
                "title": e.title,
            }
            if e.event_type != "Canceled"
            else {"markdown_content": e.title}
            for e in events.itertuples(index=False)
        ]

    def write_week_module_file(week_df):
        week = int(week_df["week"].iloc[0])
        week_title = week_df["week_title"].iloc[0]
        date_events = week_df.groupby("date").apply(make_days)
        days = [
            {"date": date.strftime(r"%Y-%m-%d"), "events": events}
            for date, events in date_events.items()
        ]
        week_data = dump(
            {
                "title": f"Week {week} – {week_title}",
                "weekNumber": week,
                "days": days,
            },
            sort_keys=False,
        )
        module_file_path = f"_modules/week-{week:02d}.md"
        with open(module_file_path, "w") as f:
            f.writelines(["---\n", week_data, "---\n"])
        print(f"Wrote: {module_file_path}")

    return df.groupby("week").apply(write_week_module_file)


if __name__ == "__main__":
    args = docopt(__doc__, version="1.0")
    generate_modules(args["CSV_FILE"])
