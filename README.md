# NYC Airbnb Data Analysis

This project analyzes the New York City Airbnb Open Data from 2019 using Python and various data visualization
libraries.

## Project Description

The script generates seven different visualizations to explore various aspects of the Airbnb listings in New York City,
including neighborhood distribution, pricing trends, availability, room types, and review patterns.

## Requirements

- Python 3.x
- pandas
- matplotlib
- seaborn
- numpy

You can install the required packages using pip:

```
pip install -r requirements.txt
```

## Data

The analysis uses the 'AB_NYC_2019.csv' file, which should be placed in the same directory as the script.

## Usage

1. Ensure all requirements are installed and the CSV file is in the correct location.
2. Run the script:

```
python task.py
```

3. The script will generate seven PNG files, each containing a different visualization.

## Visualizations Generated

1. Neighborhood Distribution of Listings
2. Price Distribution Across Neighborhoods
3. Room Type vs. Availability
4. Correlation Between Price and Number of Reviews
5. Time Series Analysis of Reviews
6. Price and Availability Heatmap
7. Room Type and Review Count Analysis

## Output

The script will save the following PNG files in the same directory:

- neighborhood_distribution.png
- price_distribution.png
- room_type_availability.png
- price_reviews_correlation.png
- reviews_time_series.png
- price_availability_heatmap.png
- room_type_reviews.png

## Author

Valentyna Lysenok
