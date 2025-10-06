# Canada-Job-Vacancy-Analysis
This program allows users to compare job vacancies across two Canadian provinces based on the required education level. It reads data from a CSV file containing job vacancy statistics and generates a side-by-side bar chart visualizing the comparison.



## Overview

This program allows users to select any two Canadian provinces and compare job vacancies based on six education levels: 
- No education required  
- High school diploma  
- Non-university certificate  
- Diploma below bachelor's  
- Bachelor's degree  
- Diploma above bachelor's  

It parses the CSV file, aggregates the total job vacancies for each education level in each province, and visualizes the data as a side-by-side bar chart. This visualization makes it easy to see patterns in regional labor demand, such as which provinces offer more opportunities for lower-education jobs versus higher-education roles. The findings can help job seekers identify regions where their education level is in higher demand, guide educational planning, and inform research on workforce trends. By comparing two provinces directly, users gain a clear understanding of regional differences in job market requirements, revealing insights into how education aligns with job availability across Canada.



---

## Technologies Used

- Python 3.10+  
- CSV file processing  
- Matplotlib for data visualization  
- NumPy for numerical array handling  

---

## How to Run

1. **Install dependencies:**
   - Run:
     ```bash
     pip install -r requirements.txt
     ```

2. **Run the program:**
   - Run:
     ```bash
     python3 education.py
     ```

3. **Input provinces:**
   - When prompted, enter the first and second provinces you want to compare.

4. **View the results:**
   - A bar chart will be displayed comparing job vacancies by education level.

5. **Note:**  
   The `educationLevel.csv` file must be in the same directory as the Python script for the program to run successfully.
