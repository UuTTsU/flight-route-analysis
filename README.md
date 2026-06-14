✈️ Flight Route Analysis

A data analysis project exploring 67,000+ global flight routes to uncover airline network patterns, busiest airport hubs, and flight distribution insights using Python and data visualization libraries.


📌 Project Overview

This project analyzes real-world flight route data sourced from the OpenFlights database. The goal was to understand how global airline networks are structured — which airlines dominate route counts, which airports serve as the biggest hubs, and how direct vs. connecting flights are distributed across the network.

This project was inspired by my previous work building Lucky Tour, a Django-based flight search web application — I wanted to go deeper and understand the data behind flight networks.


🛠️ Tools & Technologies

ToolPurposePython 3Core languagePandasData loading, cleaning, and aggregationNumPyNumerical operationsMatplotlibChart creationSeabornStatistical visualizations


📊 Key Findings


Top airlines by route count — A small group of carriers dominate global connectivity, operating significantly more routes than the average airline
Busiest departure hubs — Major international airports like FRA, CDG, and IST appear consistently as top source airports
Direct vs. connecting flights — The vast majority of listed routes are direct (0 stops), reflecting how route databases capture point-to-point connection


🚀 How to Run


Clone the repository:


bashgit clone https://github.com/UuTTsU/flight-route-analysis.git
cd flight-route-analysis


Install dependencies:


bashpip install pandas numpy matplotlib seaborn


Run the analysis:


bashpython main.py

Charts will be saved automatically as .png files in the project directory.


📁 Project Structure

flight-route-analysis/
│
├── main.py                  # Main analysis script
├── top_airlines.png         # Airlines by route count chart
├── busiest_airports.png     # Busiest airports chart
├── stops_distribution.png   # Direct vs connecting flights chart
└── README.md


👤 Author

Giorgi Utsunashvili


GitHub: @UuTTsU
Email: giorgiutsunashvili0@gmail.com
LinkedIn: Linkedin
