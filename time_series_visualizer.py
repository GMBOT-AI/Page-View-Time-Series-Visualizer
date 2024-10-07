import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')
df.index=pd.to_datetime(df.index)
# Clean data
df = df[(df['value']>=df['value'].quantile(0.025)) & (df['value']<=df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    plt.figure(figsize=(12,8))
    plt.plot(df.index, df['value'], color='red')
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.grid(True)
    plt.show()
    fig = plt.gcf()  # Get the current figure object

    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():

    df_bar = df.copy()
    df_bar['Year']=df.index.year
    df_bar['Month']=df.index.month
    avg_views=df_bar.groupby(['Year','Month'])['value'].mean().unstack()

    fig = plt.gcf()  # Get the current figure object

    plt.figure(figsize=(12,8))
    avg_views.plot(kind='bar', stacked=False)
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title='Month' ,labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                                    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

    plt.show()


    fig = plt.gcf()  # Get the current figure object

    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    fig,axes = plt.subplots(1,2, figsize=(12,8))

    sns.boxplot(x='year',y='value',data=df_box)
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    sns.boxplot(x='month',y='value', data=df_box)
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig = plt.gcf()  # Get the current figure object

    fig.savefig('box_plot.png')
    return fig
