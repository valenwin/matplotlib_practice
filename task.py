import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the data
df = pd.read_csv('data/AB_NYC_2019.csv')


# Data preprocessing
def preprocess_data(df):
    df['last_review'] = pd.to_datetime(df['last_review'])
    df = df.dropna()
    return df


df = preprocess_data(df)


# Function to save plots
def save_plot(fig, filename):
    fig.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close(fig)


# 1. Neighborhood Distribution of Listings
def plot_neighborhood_distribution(df):
    fig, ax = plt.subplots(figsize=(12, 6))

    neighborhood_counts = df['neighbourhood_group'].value_counts()
    bars = ax.bar(neighborhood_counts.index, neighborhood_counts.values,
                  color=plt.cm.Set3(np.arange(len(neighborhood_counts))))

    ax.set_title('Distribution of Airbnb Listings Across Neighborhood Groups', fontsize=16)
    ax.set_xlabel('Neighborhood Group', fontsize=12)
    ax.set_ylabel('Number of Listings', fontsize=12)

    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2., height,
                f'{height:,}',
                ha='center', va='bottom')

    plt.xticks(rotation=45)
    plt.tight_layout()

    save_plot(fig, 'visualizations/neighborhood_distribution.png')
    return fig


# 2. Price Distribution Across Neighborhoods
def plot_price_distribution(df):
    fig, ax = plt.subplots(figsize=(12, 6))

    sns.boxplot(x='neighbourhood_group', y='price', data=df, ax=ax)

    ax.set_title('Price Distribution Across Neighborhoods', fontsize=16)
    ax.set_xlabel('Neighborhood Group', fontsize=12)
    ax.set_ylabel('Price', fontsize=12)

    plt.xticks(rotation=45)
    plt.tight_layout()

    save_plot(fig, 'visualizations/price_distribution.png')
    return fig


# 3. Room Type vs. Availability
def plot_room_type_availability(df):
    fig, ax = plt.subplots(figsize=(12, 6))

    room_type_availability = df.groupby(['neighbourhood_group', 'room_type'])['availability_365'].mean().unstack()
    room_type_std = df.groupby(['neighbourhood_group', 'room_type'])['availability_365'].std().unstack()

    room_type_availability.plot(kind='bar', yerr=room_type_std, ax=ax)

    ax.set_title('Average Availability by Room Type and Neighborhood', fontsize=16)
    ax.set_xlabel('Neighborhood Group', fontsize=12)
    ax.set_ylabel('Average Availability (days)', fontsize=12)

    plt.legend(title='Room Type')
    plt.xticks(rotation=45)
    plt.tight_layout()

    save_plot(fig, 'visualizations/room_type_availability.png')
    return fig


# 4. Correlation Between Price and Number of Reviews
def plot_price_reviews_correlation(df):
    fig, ax = plt.subplots(figsize=(12, 6))

    for room_type in df['room_type'].unique():
        data = df[df['room_type'] == room_type]
        ax.scatter(data['price'], data['number_of_reviews'], alpha=0.5, label=room_type)

    ax.set_title('Price vs Number of Reviews', fontsize=16)
    ax.set_xlabel('Price', fontsize=12)
    ax.set_ylabel('Number of Reviews', fontsize=12)

    ax.legend()
    plt.tight_layout()

    save_plot(fig, 'visualizations/price_reviews_correlation.png')
    return fig


# 5. Time Series Analysis of Reviews
def plot_reviews_time_series(df):
    fig, ax = plt.subplots(figsize=(12, 6))

    for neighborhood in df['neighbourhood_group'].unique():
        data = df[df['neighbourhood_group'] == neighborhood].sort_values('last_review')
        ax.plot(data['last_review'], data['number_of_reviews'].rolling(window=30).mean(), label=neighborhood)

    ax.set_title('Number of Reviews Over Time by Neighborhood', fontsize=16)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Number of Reviews (30-day rolling average)', fontsize=12)

    ax.legend()
    plt.tight_layout()

    save_plot(fig, 'visualizations/reviews_time_series.png')
    return fig


# 6. Price and Availability Heatmap
def plot_price_availability_heatmap(df):
    fig, ax = plt.subplots(figsize=(12, 8))

    pivot = df.pivot_table(values='price', index='neighbourhood_group', columns='availability_365', aggfunc='mean')
    sns.heatmap(pivot, ax=ax, cmap='YlOrRd')

    ax.set_title('Price vs Availability Across Neighborhoods', fontsize=16)
    ax.set_xlabel('Availability (days)', fontsize=12)
    ax.set_ylabel('Neighborhood Group', fontsize=12)

    plt.tight_layout()

    save_plot(fig, 'visualizations/price_availability_heatmap.png')
    return fig


# 7. Room Type and Review Count Analysis
def plot_room_type_reviews(df):
    fig, ax = plt.subplots(figsize=(12, 6))

    review_counts = df.groupby(['neighbourhood_group', 'room_type'])['number_of_reviews'].sum().unstack()
    review_counts.plot(kind='bar', stacked=True, ax=ax)

    ax.set_title('Number of Reviews by Room Type and Neighborhood', fontsize=16)
    ax.set_xlabel('Neighborhood Group', fontsize=12)
    ax.set_ylabel('Number of Reviews', fontsize=12)

    plt.legend(title='Room Type')
    plt.xticks(rotation=45)
    plt.tight_layout()

    save_plot(fig, 'visualizations/room_type_reviews.png')
    return fig


if __name__ == "__main__":
    plot_neighborhood_distribution(df)
    plot_price_distribution(df)
    plot_room_type_availability(df)
    plot_price_reviews_correlation(df)
    plot_reviews_time_series(df)
    plot_price_availability_heatmap(df)
    plot_room_type_reviews(df)

    print("All visualizations have been generated and saved.")
