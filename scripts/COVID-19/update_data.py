# -*- coding: utf-8 -*-

import sys
import argparse
from datetime import datetime

import pandas as pd
import numpy  as np

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="COVID-19 Data Builder")
    parser.add_argument("root_path", help="Project Root", default="./")

    args = parser.parse_args()
    root_path = args.root_path

    greeceTimeline_df = pd.read_csv(root_path + "/COVID-19/greeceTimeline.csv")
    today = pd.to_datetime(datetime.today()).strftime("%-m/%-d/%-y")
    last_date = pd.to_datetime(greeceTimeline_df.columns[-1]).strftime("%-m/%-d/%-y")
    if today != last_date:
        greeceTimeline_df[today] = greeceTimeline_df[last_date]
        greeceTimeline_df.at[0, today] = np.nan # cases skip
        greeceTimeline_df.at[1, today] = np.nan # deaths skip
        # recovered copy
        greeceTimeline_df.at[3, today] = np.nan # hospitalized skip
        greeceTimeline_df.at[4, today] = np.nan # intensive_care skip
        # intubated copy
        # cumulative_rtpcr_tests_raw copy
        greeceTimeline_df.at[7, today] = np.nan # estimated_new_rtpcr_tests skip
        # cumulative_rapid_tests_raw copy
        greeceTimeline_df.at[9, today] = np.nan # esitmated_new_rapid_tests skip
        # estimated_new_total_tests copy
        # total cases copy
        greeceTimeline_df.to_csv(root_path + "/COVID-19/greeceTimeline.csv", index=False)
    sys.exit(0)
