import streamlit as st


# Seitenleiste
st.sidebar.markdown('<style>div.row-widget.stRadio div{color: white;}</style>', unsafe_allow_html=True)
# st.sidebar.write('<font color="white">Main Menu</font>', unsafe_allow_html=True)
page = st.sidebar.radio(" ", ["Home", "Project Description", 
                              "Exploration Analysis - NASA", 
                              "Exploration Analysis - FAO", 
                              "Exploration Analysis - OWID", 
                            "Modeling preparation",
                            "Ordinary Least Squares Regression", 
                            "Supervised machine learning and ensemble models",
                            "Time-series modeling with SARIMA",
                            "Time-series modeling with LSTM",
                              "Conclusion", "Credits"])


# st.sidebar.image('name_globe.png', width=100, use_column_width='always')
st.sidebar.image('name_globe.png', use_column_width=True, width=100)


#####
if page == 'Home':

    # Add the image to the home page
    st.image("Startseite_6.jpg",  use_column_width=True)


#####

if page == "Project Description":
    st.markdown(
        """
        <style>
        .centered-title {
            font-size: 28px;
            text-align: center;
            border-top: 2px solid black; /* https://www.w3schools.com/colors/colors_picker.asp */
            border-bottom: 2px solid black;
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<h1 class="centered-title">Project Description</h1>', unsafe_allow_html=True)


    st.markdown("<br><br>", unsafe_allow_html=True)
    
    st.markdown('<h2 style="font-size: 24px;">Aim</h2>', unsafe_allow_html=True)
    st.write("The **aim** of our data analysis project *World Temperature* is to determine the global warming (and disruption) of the earth's climate over the last few centuries and decades.")

    st.markdown("***")
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown('<h2 style="font-size: 24px;">Context</h2>', unsafe_allow_html=True)
    st.write("**Context and economic point of view:**")
    st.write("Global warming has become an issue that demands the attention of businesses worldwide. The integration of global warming into business is a multifaceted endeavor encompassing environmental responsibility, risk management, innovation, and corporate social responsibility. From an economic point of view, addressing global warming and transitioning to sustainable practices can bring several benefits and opportunities for businesses. Ultimately, the integration of global warming into business is an imperative for organizations seeking long-term success while addressing the urgent need to combat climate change.")
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("**From a scientific point of view:**")
    st.write("The project strives to contribute to the documentation of the current status of climate change, advance the development of models and predictions, and develop scientific recommendations to limit global warming and protect the environment.")
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("**From a technical point of view:**")
    st.write("From a technical perspective, the project involves data collection, processing, and analysis operations, the application of machine learning algorithms for prediction, and user-friendly data visualization tools for effective communication of results. The technological demands of this project are comprehensive, but they are critical for its success.")

    st.markdown("***")
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<h2 style="font-size: 24px;">Objectives</h2>', unsafe_allow_html=True)
    st.write("1. Analyze how the temperature has changed over the last few centuries and decades on earth.")
    st.write("2. Generate insights about factors contributing to this development, with a particular focus on CO2 emissions.")
    st.write("3. Develop models that forecast future temperature changes based on the available historical data. This involves feature and model selection, training, validating and testing and evaluating predictive models that can aid in understanding potential future climate scenarios.")

    st.markdown("***")
    st.markdown("<br>", unsafe_allow_html=True)

    markdown_text = '<h2 style="font-size: 24px;">Research Questions</h2>'
    st.markdown(markdown_text, unsafe_allow_html=True)
    st.write("1. _Historical Trend Analysis_:  \n How have CO2 emissions and global temperatures changed over time? ")
    st.write("2. _Exploratory Relationship Analysis_:  \n  What is the nature of the relationship between CO2 emissions and global temperature changes? ")
    st.write("3. _Predictive Modeling and Forecasting_:  \n  Can we accurately predict future temperature changes based on the data included in the modeling?")

    st.markdown("***")
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<h2 style="font-size: 24px;">The following sets of data were used to achieve the objectives of our project</h2>', unsafe_allow_html=True)
    st.write('  I. [The NASA GISS Surface Temperature Analysis (GISTEMP) version 4](https://data.giss.nasa.gov/gistemp/)')
    st.write(' II. [The Our World in Data CO2 and Greenhouse Gas Emissions dataset](https://github.com/owid/co2-data)')
    st.write('III. [The FAO Annual Surface Temperature Change dataset](https://www.fao.org/faostat/en/#data/ET)')

    st.write('The datasets will be explored in the following sections.  \n  At first basic properties of each dataset will be delineated in the section Exploratory Analysis. In the modeling part we will have a more in detail look at some of the key variables of the dataset with regard to the objectives of our data analysis project.')


if page == "Credits":
    st.markdown(
        """
        <style>
        .centered-title {
            font-size: 28px;
            text-align: center;
            border-top: 2px solid black;
            border-bottom: 2px solid black;
            padding: 10px;
        }
        .linkedin-logo {
            width: 30px;
            height: 30px;
            cursor: pointer;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<h1 class="centered-title">Credits</h1>', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
   
    with col1:
        st.write("**Members of the project team:**")
        st.markdown("<br><br><br><br><br><br>", unsafe_allow_html=True)
        st.write("**Resources:**")
        st.markdown("<br><br><br><br><br><br><br>", unsafe_allow_html=True)
        #st.write("**Project report: uploaden?**") # upload report
   
    with col2:
        st.write("Sebastian Poppitz")
        st.write("Sophia Thanushan")
        st.write("Marisa Wastell")
        st.markdown("<br>", unsafe_allow_html=True)
        st.write("Francesco Madrisotti (Tutor)")
        st.markdown("<br>", unsafe_allow_html=True)
        st.write("[NASA GISTEMP Data](https://data.giss.nasa.gov/gistemp/)")
        st.write("[OWID CO2 Data](https://github.com/owid/co2-data)")
        st.write("[FAO Annual Surface Temperature Change dataset](https://www.fao.org/faostat/en/#data/ET)")
        
    with col3:     
        linkedin_icon = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"

        st.markdown(
            f'<a href="https://www.linkedin.com/in/sebastian-poppitz-459a0289/" target="_blank">'
            f'<img class="linkedin-logo" src="{linkedin_icon}" alt="LinkedIn" width="100" height="100" />'
            f'</a>', 
            unsafe_allow_html=True
            )


        st.markdown(
            f'<a href="https://www.linkedin.com/in/sophia-thanushan-12063542" target="_blank">'
            f'<img class="linkedin-logo" src="{linkedin_icon}" alt="LinkedIn" />'
            f'</a>', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'<a href="https://www.linkedin.com/in/marisa-wastell-3828b858/" target="_blank">'
            f'<img class="linkedin-logo" src="{linkedin_icon}" alt="LinkedIn" />'
            f'</a>', 
            unsafe_allow_html=True
        )

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<span style='font-size: 12px;'>\*For each member of the group, specify the level of expertise around the problem addressed:</span>  \n<span style='font-size: 12px;'>   None of the members have prior knowledge with respect to in-depth climate data analysis.</span>", unsafe_allow_html=True)


# linkedIn logo 1 https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Logo.svg.original.svg
# linkedIn logo 2 https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg


# Load main libraries and modules

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from bokeh.plotting import figure, show, output_notebook
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool




##### Exploration Analysis - NASA
#### NASA Dataset Darstellung

if page == "Exploration Analysis - NASA":
    st.markdown(
        """
        <style>
        .centered-title {
            font-size: 28px;
            text-align: center;
            border-top: 2px solid black;
            border-bottom: 2px solid black;
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    

#    st.sidebar.write("Subpages:")
 #   subpage = st.sidebar.radio("", ["NASA", "FAO", "OWID"])

    
    #if subpage == "NASA":
     #   st.title("NASA Data Analysis")
        # Fügen Sie hier den Inhalt für die NASA-Analyse hinzu
    
    #elif subpage == "FAO":
     #   st.title("FAO Data Analysis")
        # Fügen Sie hier den Inhalt für die FAO-Analyse hinzu
    
    #elif subpage == "OWID":
     #   st.title("OWID Data Analysis")



    st.markdown('<h1 class="centered-title">Exploration Analysis - NASA</h1>', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    st.write('Exploratory analyses are used to gain initial insight into the data, identify data quality issues, discover patterns and generate hypotheses. They are the starting point for further analyses and research in which specific questions are answered or models are developed.')
    st.write('Various representations and visualisations of the data set now follow.')

    st.markdown("#### The NASA dataset")
    
    st.write('**Intro**')
    st.write('The GISS Surface Temperature Analysis version 4 (GISTEMP v4), published by the National Aeronautics and Space Administration (NASA) Goddard Institute for Space Studies, provides an approximation of the global surface temperature variation. Temperature change indicates deviations from the typical or expected temperature for a specific location and time.')
    st.write('In the context of GISS analysis, the term "normal" refers to the average temperature during the 30-year period from 1951 to 1980 for that specific place and time of year. This base period is specific to GISS and not universally applicable.')
    st.write('Overview of the NASA temperature dataset, including descriptive statistics and basic properties: This step provides a first insight into the dataset, including the available variables and the general structure.')

    df_NASA = pd.read_csv('ZonAnn.Ts+dSST.csv')

    # Konvertieren der Jahre in ganze Zahlen und Formatieren auf zwei Dezimalstellen
    formatted_df_NASA = df_NASA.copy()
    formatted_df_NASA['Year'] = formatted_df_NASA['Year'].astype(int)
    
    # Formatieren der Werte in den Spalten 'Glob' bis '90N-64N'
    formatted_df_NASA[['Glob', 'NHem', 'SHem', '24N-90N', '24S-24N', '90S-24S', '64N-90N', '44N-64N','24N-44N', 'EQU-24N', '24S-EQU', '44S-24S', '64S-44S', '90S-64S']] = formatted_df_NASA[['Glob', 'NHem', 'SHem', '24N-90N', '24S-24N', '90S-24S', '64N-90N', '44N-64N','24N-44N', 'EQU-24N', '24S-EQU', '44S-24S', '64S-44S', '90S-64S']].applymap("{:.2f}".format)

    # Wenden Sie bedingte Formatierung für Farben an
    def color_negative_red(val):
        if val != 'Year':
            color = 'red' if float(val) > 0 else 'blue'
            return f'color: {color}'
        return ''
    
    formatted_df_NASA = formatted_df_NASA.style.\
        applymap(color_negative_red, subset=formatted_df_NASA.columns[1:])
    
    # Zeige nur die ersten 5 Zeilen der Daten
    st.dataframe(formatted_df_NASA, height=300, width=700)  # Höhe und Breite anpassen

    # Einklappbarer Bereich für die Beschreibung des DataFrames
    with st.expander("Descriptive statistics of the NASA dataset"):
        st.dataframe(df_NASA.describe())
    
    # Einklappbarer Bereich für die Beschreibung des DataFrames
    with st.expander("Properties of the NASA dataset"):
        st.markdown("###### Dimensions")
        st.markdown(f"- Number of Rows: {df_NASA.shape[0]}\n"
                    f"- Number of Columns: {df_NASA.shape[1]}\n")
        st.markdown("")
        st.markdown("###### Data types")
        st.markdown("- 14 variables are of data type float,\n"
                    "- 1 variable is of dtype integer\n")
        st.markdown("")
        st.markdown("###### Missing values")
        st.markdown("- There are no missing values in the dataset\n")
        st.markdown("")
        st.markdown("###### Variables")
        st.markdown("- The year of the measures\n"
                    "- 'Glob': This column represents the global average temperature anomaly. It provides the average temperature anomaly across the entire Earth, combining data from all latitudes and longitudes.\n"
                    "- 'NHem': This column represents the temperature anomaly for the Northern Hemisphere. It includes data from all latitudes in the Northern Hemisphere, from the equator (0 degrees latitude) to the North Pole (90 degrees latitude).\n"
                    "- 'SHem': This column represents the temperature anomaly for the Southern Hemisphere. It includes data from all latitudes in the Southern Hemisphere, from the equator (0 degrees latitude) to the South Pole (-90 degrees latitude).\n"
                    "- The rest of the variables represent latitude bands, indicating different regions of the Earth. E.g. the column '24N-90N' represents the latitude band from 24 degrees North to 90 degrees North, covering the Arctic region.")

    if st.checkbox("Show NA", key="NA_checkbox"):
         st.dataframe(df_NASA.isna().sum())


    st.markdown("***")


#### The box-and-whisker plot
    st.markdown("#### The box-and-whisker plot")
    st.write('**Intro**')
    st.write('Analysis of box-whisker plots for temperature anomalies in different regions of the NASA data set is essential to gain a better understanding of the distribution and dispersion of these data. Box-whisker plots provide a compact and informative representation of the statistical distribution and allow important aspects of the data to be grasped at a glance.')
    
    # Select the columns for the box-and-whisker plot
    columns = ['Glob', 'NHem', 'SHem', "24N-90N", "24S-24N", "90S-24S", "64N-90N", "44N-64N", "24N-44N",
           "EQU-24N", "24S-EQU", "44S-24S", "64S-44S", "90S-64S"]

    # Create the box-and-whisker plot
    fig, ax = plt.subplots(figsize=(10, 6))
    df_NASA[columns].boxplot(ax=ax)

    # Customize the plot
    plt.title('Temperature Anomalies - Box-and-Whisker Plot')
    plt.xlabel('Scope')
    plt.ylabel('Temperature Anomaly')
    plt.xticks(rotation=45)

    # Display the plot in Streamlit
    st.pyplot(fig)

    st.write("**Summary of Statistics and Box-and-Whisker Plot Observations:**")
    st.write("*  The range of data (min-max) for most variables falls between -1 and 1. Only two variables (64N-90N, 90S-64S) exceed these boundaries.")
    st.write("*  The standard deviation is less than 0.5 for 10 variables, less than 1.0 for 3 variables, and less than 1.5 °C for 1 variable.")
    st.write("*  In most variables, the mean and median values are closely aligned, indicating a low impact of outliers on the mean. This is consistent with the box and whisker plot, where outliers are visible for 'Glob,' 'NHem,' '24-90N,' '64N-90N,' '24N-44N,' '24S-EQU,' and '90S-64S.' For all other variables, the box-whisker plot does not show outliers.")
    st.write("*  For most variables (except '90S-64S'), the spread from maximum to Q2 is larger than from minimum to Q2. Since Q2 is very close to 0 °C, this suggests that there are more temperature changes above average for that specific year.")
    st.write("*  64N-90N (North Pole): In the North Pole region, a greater variability in temperature change is observed. Anomaly values extend upwards to over +2 degrees Celsius (and sometimes even over +3 degrees Celsius), while the box extends downward to about -1.8 degrees Celsius.")


    st.markdown("***")



#### Frequency distribution for all variables of df_NASA
if page == "Exploration Analysis - NASA":
    st.markdown("#### Frequency distribution")
    st.write('Analysing the frequency distribution using histograms for temperature anomalies in different regions of the NASA dataset provides valuable insights into the nature of climate data. Histograms are an extremely effective tool for displaying the distribution of temperature anomalies in different geographical regions and time periods in a descriptive way. They allow patterns and trends in temperature data to be highlighted, differences and similarities to be recognised and exceptional events to be identified.') 
    st.write('The following charts show the frequency distribution of temperature change for the different regions.')
    
    columns_to_plot = ['Glob', 'NHem', 'SHem', '24N-90N', '24S-24N', '90S-24S', '64N-90N', '44N-64N',
                       '24N-44N', 'EQU-24N', '24S-EQU', '44S-24S', '64S-44S', '90S-64S']
    num_cols = 2
    num_rows = -(-len(columns_to_plot) // num_cols)
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(20, 14))

    for i, column in enumerate(columns_to_plot):
        if df_NASA[column].dtype in [int, float]:
            row = i // num_cols
            col = i % num_cols

            sns.histplot(df_NASA[column], kde=True, ax=axes[row, col])
            axes[row, col].set_title(f'Temperature anomalies for "{column}"')
            axes[row, col].set_xlabel('Temperature anomaly')
            axes[row, col].set_ylabel('Frequency distribution')

    plt.tight_layout()

    # Anzeigen des Plots in Streamlit
    st.pyplot(fig)
    st.write('<span style="font-size: 12px;">&ast; For better readability, click on the graphic and then on the symbol with the two arrows to enlarge the graphic.</span>', unsafe_allow_html=True)

    st.write('**Observations:**')
    st.write('*  The charts display temperature changes across the Northern and Southern Hemispheres, segmented by high, mid, and low latitudes. Each section uses histograms to represent the frequency of temperature changes, with the x-axis showing temperature shifts and the y-axis indicating occurrences.')
    st.write('*  There is a general trend of increasing temperatures across both hemispheres and all latitudinal bands.')
    st.write('*  Different latitudes show varying degrees of temperature change, indicating specific areas might be more affected.')
    st.write('*  The charts suggest global warming trends, with the Northern and Southern Hemispheres both experiencing temperature shifts.')

    st.markdown("E.g. the histogram of global temperature change shows:")
    st.write("*  The most frequent values of temperature change range between -0.2 and 0.")
    st.write("*  The frequency distribution is skewed to the right, which could indicate that the data is not normally distributed.")


    st.markdown("***")



#### OUTLIER ANALYSIS
if page == "Exploration Analysis - NASA":
    st.markdown("#### Interquartile Range (IQR) Outlier Analysis")
    
    st.write('**Intro**')
    st.write('The Interquartile Range (IQR) method has been employed to gain deeper insights into outlier distribution. Outliers are valuable as they signal unexpected events and highlight actual data changes. Detecting outliers helps unravel intricate data patterns and identify the underlying causes of unusual occurrences.') 
    st.write('Data points that are more than 1.5 * IQR above the third quartile or below the first quartile are considered potential outliers. Using a threshold of 1.5 for the IQR (interquartile range) is a common practice to identify outliers. It covers a wider range and allows the identification of potential outliers that fall outside the middle 50% range.')
    st.write('The following table shows the results of the analysis:')
    
    # Erstellen einer Kopie des ursprünglichen DataFrames, um unerwünschte Änderungen zu vermeiden
    df_NASA_yearformat = df_NASA.copy()
    
    # Konvertieren der 'Year'-Spalte in Ganzzahlen
    df_NASA_yearformat['Year'] = df_NASA_yearformat['Year'].astype(int)

    # Initialize an empty list to store dataframes with outliers for each column
    outliers_list = []

    # Iterate over columns of the dataframe (excluding the first column 'Year')
    for column in df_NASA.columns[1:]:

        # Extract temperature values for the current column
        temperatures = df_NASA[column]

        # Calculate the first quartile (Q1) and third quartile (Q3) of the data
        q1 = temperatures.quantile(0.25)
        q3 = temperatures.quantile(0.75)

        # Compute the Interquartile Range (IQR)
        iqr = q3 - q1

        # Define lower and upper bounds for outliers based on the IQR
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        # Identify and extract rows that are outliers for the current column
        outliers_iqr = df_NASA[(temperatures < lower_bound) | (temperatures > upper_bound)][['Year', column]]
        
        # Anpassen des Namens der Spalte 'Year'
        outliers_iqr = outliers_iqr.rename(columns={'Year': 'Year'})

        # Hinzufügen der Spalte 'Variable' für die Originalspalte
        outliers_iqr['Variable'] = column
        
        # Hinzufügen der Spalte 'OutlierValue' für den Ausreißerwert
        outliers_iqr['OutlierValue'] = temperatures[(temperatures < lower_bound) | (temperatures > upper_bound)]
        
        # Append the dataframe with outliers for the current column to the list
        outliers_list.append(outliers_iqr)

    # Concatenate all outlier dataframes into a single dataframe
    outliers_df = pd.concat(outliers_list)

    # Group the outliers by year, aggregating the variable names and their corresponding outlier values
    grouped_outliers = outliers_df.groupby('Year').agg({
        'Variable': list,
        'OutlierValue': list
    }).reset_index()
    
    # Konvertieren der 'Year'-Spalte in Ganzzahlen
    grouped_outliers['Year'] = grouped_outliers['Year'].astype(int)

    # Display the grouped outliers
    st.write('**Grouped Outliers:**')
    st.markdown(
        grouped_outliers.style.set_properties(**{'background-color': 'transparent', 
                                                'color': 'black', 
                                                'text-align': 'center'}).render(), 
        unsafe_allow_html=True
    )

    st.write('')
    st.write('')
    st.write("**Should we eliminate outliers in the NASA dataset?**  \n"
             "Outliers may contain important information relevant to the understanding of the phenomenon temperature change. Even small deviations in the data can be considered significant. Therefore it might make sense to consider outliers with a multiplier of 1.5 and keep them, thus consider them as part of the variation in the data.")

    st.write('**The results indicate the following:**')
    st.write('In 1928 and 1930, unusual cold anomalies were observed in the southernmost latitudes (90S-64S), with values of −2.13 and −2.61. From 2015 to 2022, there was a noticeable uptick in outlier frequency, with predominantly positive anomalies signaling higher temperatures. Specific observations include:')
    st.write('*  2015: High anomalies in the Northern Hemisphere (NHem) and 24N-44N.')
    st.write('*  2016: Outliers across regions, notably a 3.25 anomaly in 64N-90N.')
    st.write('*  2017: High anomalies like 2016, particularly in 64N-90N.')
    st.write('*  2018-2020: Continued high anomalies, with 2020 mirroring 2016s pattern.')
    st.write('*  2021 & 2022: Persistent high anomalies in the areas of the northern Hemisphere')
    st.write('Overall, the data indicates a rising trend in temperature anomalies, especially in the areas of the northern Hemisphere. This trend is concerning due to its potential implications for climate change.')

    st.markdown("***")


#### 'Time series: Temperature anomalies by hemisphere'
if page == "Exploration Analysis - NASA":
    st.markdown("#### Time Series")
    st.write('**Intro**')
    st.write('Visualizing time series data with line charts is a powerful tool for studying long-term trends and patterns. They provide a clear view of the historical development of temperature anomalies in different geographic regions. By visualizing these data, we can see changes over time, identify seasonal variations, and analyze potential long-term trends.')
    
# Visualisierung der Zeitreihen für die ausgewählten Spalten
if page == "Exploration Analysis - NASA":

    # Benutzerdefinierte Farbpalette für jede Spalte
    color_palette = plt.cm.get_cmap('tab20', len(df_NASA.columns[1:]))

    # Voreingestellte Auswahl und Widget für die Auswahl der Regionen hinzufügen
    default_selected_regions = ["Glob", "NHem", "SHem"]  # Voreingestellte Auswahl
    selected_regions = st.multiselect("Select Regions", df_NASA.columns[1:], default=default_selected_regions)

    if not selected_regions:
        st.warning("Please select at least one region for visualization.")
    else:
        # Erstellen der Matplotlib-Figur und Achsenobjekte
        fig, ax = plt.subplots(figsize=(10, 6))

        # Benutzerdefinierte Achsenwerte festlegen
        years = df_NASA['Year']
        ax.set_xticks(years[::10])  # Jedes 10. Jahr anzeigen
        ax.set_xticklabels(years[::10], rotation=45)  # Drehung der Jahresbeschriftungen für bessere Lesbarkeit
        ax.set_xlabel('Year')
        ax.set_ylabel('Temperature anomaly')

        # Iterieren über jede ausgewählte Region und erstellen Sie einen Linienplot
        for region in selected_regions:
            # Wählen Sie die Farbe aus der Farbpalette basierend auf dem Index der Spalte
            color = color_palette(selected_regions.index(region))

            # Erstellen eines Linienplots für die ausgewählte Region
            ax.plot(years, df_NASA[region], label=region, color=color)

        ax.legend()

        # Anzeigen der Matplotlib-Figur in Streamlit
        st.pyplot(fig)
        
        st.write('**Observations and Conclusion:**')
        st.write('The chart shows an increasing negative temperature change until approx. 1910 and increasing positive temperature change from approx. 1910 onwards until the latest data.')
        st.write("Comparing temperature anomalies between the Northern and the Southern hemisphere shows that, especially since the year 2000, temperature anomalies have been more positive in the Northern Hemisphere than in the Southern one.")
            
        st.write('The graph indicates that temperature changes have been steadily increasing on average in recent years. This suggests that it is getting warmer on a global scale.')
        # st.write("If the temperature anomalies in the Northern Hemisphere have been consistently stronger or higher than those in the Southern Hemisphere since the year 2000, it suggests that the Northern Hemisphere has experienced more significant temperature increases or higher positive temperature anomalies compared to the Southern Hemisphere during that time period.")
        
        # Aufklappbare Beschreibung für "Findings"
        with st.expander("Further info"):
            st.write("This visualization allows you to compare temperature anomalies across different regions, helping to understand variations in temperature trends.")
            st.write('Take a look at the region 90S-64S: The strong fluctuations in the period between 1920 and 1960 (range: -2.5 and 1) are striking.')
            st.write('Around the 90s temperature anomalies are recorded in the positive value range for all regions.')            
            st.write("Temperature anomalies have been more positive in the Northern Hemisphere. This observation aligns with the overall understanding of climate change, as the Northern Hemisphere has been shown to experience more pronounced warming trends compared to the Southern Hemisphere. It could be attributed to various factors, including differences in land distribution, ocean currents, atmospheric circulation patterns, and human activities concentrated in the Northern Hemisphere.")
            st.write("However, it's important to note that this interpretation is based on the assumption that the temperature anomalies are reliable and accurately represent the actual temperature changes in each hemisphere. Additionally, further analysis and examination of the data would be necessary to confirm the consistency and significance of these observed differences.")
 

    st.markdown("***")




#### Climate Stripes
if page == "Exploration Analysis - NASA":
    st.markdown("#### Climate Stripes")

    st.write('**Intro**')
    st.write("Here, you'll find climate stripes, which provide a simple and intuitive way to visualize climate change and temperature trends. They offer a quick and clear representation of Earth's warming, making it easy to identify long-term temperature trends.")

    from matplotlib.colors import LinearSegmentedColormap

    selected_columns = ['Glob', 'NHem', 'SHem', '24N-90N', '24S-24N', '90S-24S', '64N-90N', '44N-64N', '24N-44N', 'EQU-24N', '24S-EQU', '44S-24S', '64S-44S', '90S-64S']

    # Erstellen der Farbpaletten für positive (rot) und negative (blau) Werte
    cmap = LinearSegmentedColormap.from_list('climate_stripes', ['blue', 'white', 'red'], N=256)

    years = df_NASA['Year']

    for selected_column in selected_columns:
        data = df_NASA[selected_column]

        # Erstellen des Diagramms
        fig, ax = plt.subplots(figsize=(12, 1))
        norm = plt.Normalize(data.min(), data.max())

        colors = [cmap(norm(val)) for val in data]

        ax.bar(years, [1] * len(years), color=colors, width=1)

        ax.set_xlim(min(years), max(years))
        
        # Anpassen der x-Achsenticks in 20-Jahres-Schritten
        x_ticks = range(min(years), max(years), 20)
        ax.set_xticks(x_ticks)
        
        # Hinzufügen der Jahreszahlen zu den x-Achsenticks
        ax.set_xticklabels([str(year) for year in x_ticks])
        
        ax.set_yticklabels([])
        
        # Achsenbeschriftungen hinzufügen
        ax.set_xlabel('Year')  # X-Achsenbeschriftung
        ax.set_ylabel('Value')  # Y-Achsenbeschriftung

        # Farblegende unterhalb des Diagramms platzieren
        cbar = plt.colorbar(plt.cm.ScalarMappable(cmap=cmap, norm=norm), ax=ax, orientation='horizontal', pad=0.60)
        cbar.set_label(f'Color for {selected_column}')

        # Diagramm anzeigen
        plt.title(f'Climate Stripes for {selected_column}')
        st.pyplot(fig)  # Zeigen Sie das Diagramm mit Streamlit an

    st.write('**Observations:**')
    st.write('It appears that in recent decades, the majority of regions around the world have experienced predominantly positive temperature anomalies, especially since the 1980s / 1990s. However, there is an exception for the 90S-64S (South Pole) regions, where greater temperature variance is evident.')


    st.markdown("***")



#### Scatter plots
import math
from scipy.stats import linregress

if page == "Exploration Analysis - NASA":
    st.markdown("#### Scatter plots")
    st.write('**Intro**')
    st.write('Scatter plots with linear regression lines provide visual insight into the relationship between years and temperature anomalies for different regions. These plots make it possible to identify trends, patterns, and correlations in temperature data.') 
    st.write('The linear regressions help quantify the direction and strength of these relationships and provide important insights into how climate has evolved in different regions over the years.')
    st.write('To obtain a more profound comprehension of temperature variations over time across various latitudinal bands, a Pearson correlation analysis was performed for each latitude. Additionally, scatter plots were created to visualize the relationship between temperature change and the corresponding year.')
    
    # Number of columns
    num_cols = len(df_NASA.columns) - 1  # Ignore the year-column

    # Calculate the number of rows and columns in the subplot grid
    num_rows = math.ceil(num_cols / 3)
    num_cols_subplot = min(num_cols, 3)

    # Create a Matplotlib figure to hold all subplots
    fig, axes = plt.subplots(num_rows, num_cols_subplot, figsize=(15, 4 * num_rows))

    # Iterate over all columns except the first one (Year)
    for i, column in enumerate(df_NASA.columns[1:]):
        # Calculate the row and column index in the subplot grid
        row_idx = i // 3
        col_idx = i % 3

        # Create a scatter plot
        ax = axes[row_idx, col_idx] if num_rows > 1 else axes[col_idx]
        ax.scatter(df_NASA['Year'], df_NASA[column])
        ax.set_xlabel('Year')
        ax.set_ylabel(column)
        ax.set_title(f'Scatter Plot: Year vs. {column}')

        # Linear Regression
        slope, intercept, r_value, p_value, std_err = linregress(df_NASA['Year'], df_NASA[column])
        line = slope * df_NASA['Year'] + intercept
        ax.plot(df_NASA['Year'], line, color='red')

        # Add the correlation coefficient and p-value as text
        ax.text(0.8, 0.1, f'r = {r_value:.2f}\n p = {p_value:.4f}', transform=ax.transAxes)

    # Remove empty subplots if necessary
    if num_cols_subplot < 3:
        for i in range(num_cols_subplot, 3):
            fig.delaxes(axes[row_idx, i])

    plt.tight_layout()

    # Display the Matplotlib figure with Streamlit
    st.pyplot(fig)
    st.write('<span style="font-size: 12px;">&ast; For better readability, click on the graphic and then on the symbol with the two arrows to enlarge the graphic.</span>', unsafe_allow_html=True)


    st.write('**The plots and correlations reveal:**')
    st.write('*  A consistent temperature increase over time, as all linear regression trends are positive. For the year vs. 90S-64S (South Pole) plot, there is significant scatter, showing weak correlation. This suggests that while the South Pole has seen varied temperatures, using just the year is not enough to predict these anomalies.') 
    st.write('*  A noticeable temperature dip occurred in approx. 1910 / 1920s and from the 1950s to 1980s (except in regions like SHem, 24S-24N, and 90S-64S). This non-uniform decrease hints at regional influences on temperature shifts, warranting further study.')


#########################################################################################################
##### FAO 
if page == "Exploration Analysis - FAO":
    st.markdown(
        """
        <style>
        .centered-title {
            font-size: 28px;
            text-align: center;
            border-top: 2px solid black;
            border-bottom: 2px solid black;
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    

    st.markdown('<h1 class="centered-title">Exploration Analysis - FAO</h1>', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    st.write('Exploratory analyses are used to gain initial insight into the data, identify data quality issues, discover patterns and generate hypotheses. They are the starting point for further analyses and research in which specific questions are answered or models are developed.')
    st.write('Various representations and visualisations of the data set now follow.')

    st.markdown("#### The FAO dataset")
    
    st.write('**Intro**')
    st.write("This dataset provides annual estimates of the mean surface temperature change measured with respect to a baseline climatology (corresponding to the period 1951-1980). Estimates of changes in the mean surface are available for the years 1961-2021 by country and for the World. They are presented in degrees Celsius.")
    st.write("The dataset has been retrieved from the International Monetary Fund (IMF) climate change dashboard website, which is based on the FAOSTAT Temperature change dataset. The Data is based on publicly available GISTEMP data distributed by the National Aeronautics and Space Administration Goddard Institute for Space Studies (NASA-GISS).")
    st.write("The time series temperature change at a point is calculated as a weighted average of the GISTEMP data over all stations within a given radius, with the closest stations weighted most heavily.")
    st.write('Overview of the FAO dataset, including descriptive statistics and basic properties: This step provides a first insight into the dataset, including the available variables and the general structure.')

    df_FAO = pd.read_csv('Annual_Surface_Temperature_Change.csv')
    
    if 'ObjectId' in df_FAO.columns:
        df_FAO.drop('ObjectId', axis=1, inplace=True)  # 'ObjectId' aus dem DataFrame entfernen

    st.dataframe(df_FAO)

# Einklappbarer Bereich für die Beschreibung des DataFrames
    with st.expander("Descriptive statistics of the FAO dataset"):
        st.dataframe(df_FAO.describe())
        st.markdown('The summary statistics of the annual temperature change columns allow several insights:')
        st.markdown('**1. Mean Temperature Change:** The mean temperature change varies from year to year. In recent years (e.g., from 2013 to 2022), the mean temperature change has been mostly positive, indicating a general warming trend.')
        st.markdown('**2. Standard Deviation:** The standard deviation has shown some variability across the years, indicating that the temperature changes are not consistent across countries.')
        st.markdown('**3. Minimum and Maximum:** The range of temperature changes has increased in recent years, with both extreme highs and lows recorded.')
        st.markdown('**4. Percentiles:** The 25th, 50th (median), and 75th percentiles provide insights into the distribution of temperature changes. For most years, the median is positive, reaffirming the general warming trend.')
    
    # Einklappbarer Bereich für die Beschreibung des DataFrames
    with st.expander("Properties of the FAO dataset"):
        st.markdown("###### Dimensions")
        st.markdown(f"- Number of Rows: {df_FAO.shape[0]}\n"
                    f"- Number of Columns: {df_FAO.shape[1]}\n")
        st.markdown("")
        st.markdown("###### Data types")
        st.markdown("- 62 variables are of data type float,\n"
                    "- 1 variable is of dtype integer\n"
                    "- 9 variables are of dtype object\n")
        st.markdown("")
        st.markdown("###### Missing values")
        st.markdown("- There are 1492 missing values in the dataset\n")

    # Checkbox, um die Anzeige der NA-Werte ein-/auszuschalten
    if st.checkbox("Show NA", key="NA_checkbox"):
         st.dataframe(df_FAO.isna().sum())

    
    st.markdown("***")


### Outlier Detection
import plotly.express as px

if page == "Exploration Analysis - FAO":
    st.markdown("### Outlier Detection")

    st.write('**Intro**')
    st.write('Outlier detection are critical steps in data analysis to identify potential anomalies and unusual values in the data. Filtering out outliers is of great importance because they can skew the results and conclusions of our analyses.')
    st.write('The interquartile range (IQR) method is a proven technique for detecting outliers. It is based on the distribution of the data and helps us identify values that deviate significantly from the majority of the data. The choice of IQR multiplier (1.5 or 3) affects the sensitivity of outlier detection.')
    st.write('In this context, we have developed an interactive application that allows you to select the IQR multiplier and visualize the outliers in the temperature data.')
    
    # Assuming df is your dataframe
    id_vars = df_FAO.columns.tolist()[:9]
    df_melted = pd.melt(df_FAO, id_vars=id_vars, var_name='Year', value_name='Temperature Change')

    # Sort values
    df_FAO_sorted = df_melted.sort_values(['Country', 'Year'])

    # Clean "Year" column
    df_FAO_sorted['Year'] = df_FAO_sorted['Year'].apply(lambda x: x[1:]).astype('string')

    # Calculate the IQR (Interquartile Range)
    Q1 = df_FAO_sorted['Temperature Change'].quantile(0.25)
    Q3 = df_FAO_sorted['Temperature Change'].quantile(0.75)
    IQR = Q3 - Q1

    # Set the thresholds
    lower_threshold_1_5 = Q1 - 1.5 * IQR
    upper_threshold_1_5 = Q3 + 1.5 * IQR
    lower_threshold_3 = Q1 - 3 * IQR
    upper_threshold_3 = Q3 + 3 * IQR


if page == "Exploration Analysis - FAO":
    st.markdown("Choose the IQR Multiplier:")
    
    iqr_multiplier = st.selectbox("Select IQR Multiplier:", [1.5, 3])

    if iqr_multiplier == 1.5:
        st.write("You have chosen to use the IQR multiplier of 1.5.")
        outliers = (df_FAO_sorted['Temperature Change'] < lower_threshold_1_5) | (df_FAO_sorted['Temperature Change'] > upper_threshold_1_5)
        outlier_color = 'red'
    else:
        st.write("You have chosen to use the IQR multiplier of 3.")
        outliers = (df_FAO_sorted['Temperature Change'] < lower_threshold_3) | (df_FAO_sorted['Temperature Change'] > upper_threshold_3)
        outlier_color = 'blue'

    st.dataframe(df_FAO_sorted[outliers])

    
    
    # Create an expander for sum of outliers
    with st.expander("Sum of Outliers by Country"):
        outliers_sum = df_FAO_sorted[outliers].groupby('Country').size()
        st.dataframe(outliers_sum.rename("Outliers Count"))
        st.write('<span style="font-size: 12px;">*Click on the column heading to sort in ascending / descending order.</span>', unsafe_allow_html=True)

    st.markdown("***")

#### scatter plot
    st.write("#### Scatter Plot:")
    st.write('**Intro**')
    st.write('The chart below presents the distribution of temperature changes over different time periods, highlighting particularly unusual deviations. Scatter plots are an effective tool for identifying outliers in the data, recognising relationships and gaining a deeper understanding of the underlying processes and trends.')

    fig = px.scatter(
        df_FAO_sorted,
        x='Year',
        y='Temperature Change',
        color=outliers,
        color_discrete_map={True: outlier_color, False: 'green'},
        labels={'Temperature Change': 'Temperature Change (°C)'}
    )

    st.plotly_chart(fig)

    st.write('**Should we eliminate outliers in the FAO dataset?**')
    st.write('Outliers can contain important information relevant to understanding the phenomenon of temperature variability and CO2 increase. Even small variations in the data can be considered significant. Therefore, it may be useful to consider and retain outliers, i.e., to consider them as part of the variation in the data.')
    st.write('**The results indicate the following:**')
    st.write('The number of positive outliers in the FAO dataset has been steadily increasing since approx. 2014, reaching its highest value in 2020. This could be due to the fact that in some countries, temperature changes are significantly higher than the global average, leading them to be identified as outliers.')
   
    st.markdown("***")


#### annual average surface temperature change

if page == "Exploration Analysis - FAO":
    st.markdown("#### Surface temperature change: line graph")
    st.write('**Intro**')
    st.write("Line charts allow a clear representation of trends and changes. The following graph shows the annual average surface temperature change from 1961 to 2022.")
    
    # Extract the temperature columns
    temp_columns = df_FAO.columns[10:]

    # Calculate annual average temperature change
    annual_avg_temp_change = df_FAO[temp_columns].mean()

    # Create the plot
    fig, ax = plt.subplots(figsize=(15, 7))
    annual_avg_temp_change.plot(ax=ax)
    
    # Adding observations
    plt.title('Annual Average Surface Temperature Change (1964-2022)')
    plt.xlabel('Year')
    plt.ylabel('Temperature Change (°C)')
    plt.grid(True)

    # Show the plot in the Streamlit app
    st.pyplot(fig)
    
    st.write('The graph allows for various **observations**:')
    # Overall Trend observation
    st.write("**1. Overall Trend:** The graph clearly shows an upward trend in the annual average surface temperature change, especially in the recent decades. This indicates a consistent increase in global warming.")
    
    # Fluctuations observation
    st.write("**2. Fluctuations:** While there's a general upward trend, there are also periodic fluctuations. Some years show a sharp increase in temperature change, while others show a decrease.")
    
    # Recent Years observation
    st.write("**3. Recent Years:** The last decade, in particular, seems to have some of the highest temperature changes, emphasizing the urgency of addressing climate change.")
    

    st.markdown("***")

    
    
#### interactive map
import plotly.express as px

if page == "Exploration Analysis - FAO":
    st.markdown("#### Surface temperature change: map")
    st.write('**Intro**')
    st.write("This analysis explores the annual average surface temperature change from 1964 to 2022 and visualizes the temperature change per country on a map.")


    # Unpivot the DataFrame
    id_vars = df_FAO.columns.tolist()[:10]
    df_melted = pd.melt(df_FAO, id_vars=id_vars, var_name='Year', value_name='Temperature Change')
    df_FAO_unpivot = df_melted.sort_values(['Country', 'Year'])

    # Clean "Year" column
    df_FAO_unpivot['Year'] = df_FAO_unpivot['Year'].apply(lambda x: x[1:]).astype(int)
    df_FAO_unpivot['Year'] = df_FAO_unpivot['Year'].astype(str)

    # Get min and max temperature for color range
    min_temp = df_FAO_unpivot['Temperature Change'].min()
    max_temp = df_FAO_unpivot['Temperature Change'].max()

    # Create the choropleth map
    fig = px.choropleth(df_FAO_unpivot,
                        locations="ISO3",
                        color="Temperature Change",
                        hover_name="Country",
                        animation_frame="Year",
                        height=600,
                        color_continuous_scale=px.colors.sequential.Plasma,
                        range_color=(min_temp, max_temp),
                        projection="natural earth"
    )

    # Show the map in the Streamlit app
    st.plotly_chart(fig)
    
    st.write('<span style="font-size: 12px;">*Explore the spatial distribution of temperature changes over years and get a clear impression of global climate trends by clicking the play button.</span>', unsafe_allow_html=True)

    # Observation
    st.write("It becomes apparent that in 2022, the highest temperature change has occurred particularly in Europe and parts of Northern Africa and Asia.")


    st.markdown("***")



#### treemap
import squarify

# Intro
if page == "Exploration Analysis - FAO":
    st.markdown("#### Surface temperature change: treemap")

    st.write('**Intro**')
    st.write('Treemaps are a useful way of visualising hierarchies and provide a way of presenting complex data structures in a clear way.')
    st.write("The following treemap is an interactive visualization tool to understand the countries with the highest temperature changes in a specific year.")
    st.write("For the year 2022, the countries with the highest temperature changes are (in degree Celsius):")
    
    # Identify top 5 countries with the highest temperature changes for 2022
    top_countries_2022 = df_FAO[["Country", "F2022"]].sort_values(by="F2022", ascending=False)

    # Get top 5 countries
    top_5_countries = top_countries_2022.head(5)

    # Create the treemap using Plotly Express
    fig = px.treemap(top_5_countries, path=['Country'], values='F2022',
                     color='F2022', color_continuous_scale='Blues')

    # Display the interactive treemap
    st.plotly_chart(fig)

    # Observation
    st.write('**Observation:**')
    st.write("Notably, all of these countries are in Europe.")


    st.markdown("***")



#### Surface temperature change
if page == "Exploration Analysis - FAO":
    st.markdown("#### Surface temperature change:")
    st.write('**Intro**')
    st.write("The following visualization shows the annual surface temperature change for three selected countries with different levels of temperature change: France, the United States, and Botswana.")

    # List of selected countries for the visualization
    selected_countries = ["France", "United States", "Botswana"]

    # Filter dataset for the selected countries
    selected_data = df_FAO[df_FAO["Country"].isin(selected_countries)]

    # Create a Figure and Axes for the plot
    plt.figure(figsize=(15, 7))

    for country in selected_countries:
        country_data = selected_data[selected_data["Country"] == country].iloc[0][temp_columns]
        plt.plot(country_data.index, country_data.values, label=country)


    plt.title(f'Annual Surface Temperature Change for {selected_countries} (1961-2022)')
    plt.xlabel('Year')
    plt.ylabel('Temperature Change (°C)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.xticks(rotation=45)

    # Display the plot in Streamlit
    st.pyplot(plt)

    # Observations
    st.write("1. <font color='blue'>France:</font> France shows a general upward trend in temperature change over the years, with periodic fluctuations. Recent years, especially the past decade, have some of the highest temperature changes.",  unsafe_allow_html=True)
    st.write("2. <font color='orange'>United States:</font> The temperature change in the United States also exhibits an upward trend over the years. There are noticeable fluctuations, but the overall trend is consistent with increasing temperatures.",  unsafe_allow_html=True)
    st.write("3. <font color='green'>Botswana:</font> Botswana's temperature change trend is interesting. While it also has an upward trend similar to the other countries, there are years, especially in the recent decade, where the temperature change is relatively lower. The fluctuations in Botswana's data seem more pronounced compared to the other two countries.",  unsafe_allow_html=True)



#################################################################################################################
### OwID

if page == "Exploration Analysis - OWID":
    st.markdown(
        """
        <style>
        .centered-title {
            font-size: 28px;
            text-align: center;
            border-top: 2px solid black;
            border-bottom: 2px solid black;
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    

    st.markdown('<h1 class="centered-title">Exploration Analysis - OWID</h1>', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    st.write('Exploratory analyses are used to gain initial insight into the data, identify data quality issues, discover patterns and generate hypotheses. They are the starting point for further analyses and research in which specific questions are answered or models are developed.')
    st.write('Various representations and visualisations of the data set now follow.')

    st.markdown("#### The OWID dataset")
    
    st.write('**Intro**')
    st.write('The CO2 and Greenhouse Gas Emissions dataset is a collection of key metrics maintained by Our World in Data. It is updated regularly and includes data on CO2 emissions (annual, per capita, cumulative and consumption-based), other greenhouse gasses, energy mix, and other relevant metrics.')
    st.write('Overview of the OWID dataset, including statistics and basic properties: This step provides a first insight into the dataset, including the available variables and the general structure.')

    df_OWID = pd.read_csv('owid-co2-data.csv')
    df_OWID['year'] = df_OWID['year'].astype(str)
    
   
    st.dataframe(df_OWID)

# Einklappbarer Bereich für die Beschreibung des DataFrames
    with st.expander("Descriptive statistics of the OWID dataset"):
        st.dataframe(df_OWID.describe())
        st.markdown('**Looking at the OWID data set, the summary statistics indicate various things:**')
        st.markdown('*  In various variables, the mean and median value differ substantially (e.g. co2: 379.98 mean vs 3.10 median. This mismatch could 1) indicate the presence of outliers skewing the value distribution, 2) a high number of missing values denoted as "0", skewing the distribution')
        st.markdown('*  The large difference between the Q3 and Q4 and the max value in various variables (e.g. co2, total_ghg) indicates the existence of very high outlier values. This assumption is supported by the shape of the boxplot for one of the variables in question.')

    # Einklappbarer Bereich für die Beschreibung des DataFrames
    with st.expander("Properties of the OWID dataset"):
        st.markdown("###### Dimensions")
        st.markdown(f"- Number of Rows: {df_OWID.shape[0]}\n"
                    f"- Number of Columns: {df_OWID.shape[1]}\n")
        st.markdown("")
        st.markdown("###### Data types")
        st.markdown("- 71 variables are of data type float\n"
                    "- 1 variable is of dtype integer\n"
                    "- 2 variables are of dtype object\n")
        st.markdown("")
        st.markdown("###### Missing values")
        st.markdown("- Exist in almost all of the variables in the data set\n"
                    "- Vary greatly in share of total entries among variables\n")
        st.markdown("")
        st.markdown("###### Variables")
        st.markdown("- The data set consists mainly of numerical variables on co2 emissions with different scopes like emissions per emission source and the scope of aggregation (like total, shared, cumulative, per capita)\n"
                    "- Other context metrics like year, population, country and GDP\n"
                    "- For an in-detail description see https://github.com/owid/co2-data\n")
        

    st.markdown("***")


#####  missing values OWID

if page == "Exploration Analysis - OWID":
    st.markdown("#### Missing values")

    # Create a function that calculates the percentage of missing values in each column of your dataset.
    def missing_values_table(df):
    # Total missing values
      mis_val = df.isnull().sum()

    # Percentage of missing values
      mis_val_percent = 100 * mis_val / len(df)

    # Make a table with the results
      mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)

    # Rename the columns
      mis_val_table_ren_columns = mis_val_table.rename(columns={0: 'Missing Values', 1: '% of Total Values'})

    # Sort the table by percentage of missing descending
      mis_val_table_ren_columns = mis_val_table_ren_columns[mis_val_table_ren_columns.iloc[:, 1] != 0].sort_values('% of Total Values', ascending=True).round(1)

    # Return the dataframe with missing information
      return mis_val_table_ren_columns
    
    # Calculate the missing values table
    missing_table = missing_values_table(df_OWID)

    # Display the missing values table using st.dataframe
    st.dataframe(missing_table)
    st.write('<span style="font-size: 12px;">*Click on the column heading to sort in ascending / descending order.</span>', unsafe_allow_html=True)


    st.write('**Having a more in detail look at the amount of missing values in the data set shows that:**')
    st.markdown('  * There is a large amount of missing values in the data set, accumulating to 56,62% of all values in the data set.')
    st.markdown('  * The amount of missing values varies a great deal across variables,')
    st.markdown('  * Some variables have a comparably low percentage of missing values and are below 1/3 of all entries (e.g. share_global_luc_co2, co2),')
    st.markdown('  * while others with amount of missing values exceed 90% of entries (e.g. consumption_co2, other_industry_co2).')
   
    st.write('The high share of missing values across a large part of the variables in the OWID data set (ranging from 15.3% to 94.9% across variables) poses some challenges to data selection and data preprocessing that might influence interpretability of the results further down the road.')

    st.markdown("***")


#### Time series: Global CO2 emissions from fossil fuels'
from scipy.stats import pearsonr
if page == "Exploration Analysis - OWID":
    st.markdown('#### Time series:') 
    st.markdown('#### 1. Global CO2 emissions from fossil fuels')

    st.write('**Intro**')
    st.write('Line charts are an effective way to determine, for example, whether emissions have increased or decreased over time, whether there are seasonal fluctuations and whether there are longer-term trends.')
    st.write('The following chart shows the annual total production-based emissions of carbon dioxide (CO2) from fossil fuels, excluding land-use change, measured in tonnes. Fossil emissions measure the quantity of carbon dioxide (CO2) emitted from the burning of fossil fuels, and directly from industrial processes such as cement and steel production This is based on territorial emissions, which do not account for emissions embedded in traded goods.')

    # Extract World data from the data set
    df_OWID = pd.read_csv('owid-co2-data.csv')
    df_OWID_world = df_OWID[df_OWID['country'] == 'World']

    # Calculate the Pearson correlation coefficient and p-value
    corr_coeff, p_value = pearsonr(df_OWID_world['year'], df_OWID_world['co2'])

    # Format the p-value in scientific notation with lowercase
    p_value_formatted = "{:e}".format(p_value)

    # Create a Plotly figure with interactivity
    fig = px.line(df_OWID_world, x='year', y='co2', labels={'co2': 'Million tonnes'})
    fig.update_layout(
        xaxis_title='Year',
        yaxis_title='Million tonnes',
        showlegend=False
    )
    fig.add_annotation(
        text=f'r: {corr_coeff:.2f}<br>p-value: {p_value_formatted}',
        x=0.95,
        y=0.05,
        xref='paper',
        yref='paper',
        showarrow=False,
        font=dict(size=12)
    )

    # Display the Plotly figure using st.plotly_chart()
    st.plotly_chart(fig)

    st.write('**Observations and Conclusion**')
    st.write('*  The graph shows a steady increase in emissions over time since 1850 (presumably due to increasing industrialization), with a steep increase from 1950 to 2021. We can also observe a dip in emissions in 2020. This could be due to the covid epidemic peaking in that year.')
    st.write('*  The Pearson correlation coefficient between year and CO2 is 0.8, indicating a strong positive correlation, which indicates that there is a positive relationship between time and CO2 emissions.')
    st.write('*  The p-value of 1.22e-61 is very small, indicating that the observed correlation between time and CO2 emissions is very significant. Therefore, we can say with high confidence that there is a real relationship between years and CO2 emissions.')
    

    st.markdown("***")


import altair as alt
if page == "Exploration Analysis - OWID":
    st.markdown("#### 2. CO2 emissions by income level")

    st.write("The upcoming chart shows the development of CO2 emissions (from fossil fuels, not including CO2 emissions by land use change) across time by income level.")

    # Extract income-level data
    values_to_extract = ['High-income countries', 'Low-income countries', 'Upper-middle-income countries']
    df_income = df_OWID[df_OWID['country'].isin(values_to_extract)]
    df_income = df_income.rename(columns={'country': 'Income level'})

    # Create an Altair chart
    chart = alt.Chart(df_income).mark_line().encode(
        x=alt.X('year:O', title='Year'),  # 'O' steht für Ordinal, um die Jahre als Ganzzahlen darzustellen
        y='co2',
        color='Income level',
        tooltip=['year', 'co2']
    ).properties(
        width=600
    )

    # Display the Altair chart using st.altair_chart
    st.altair_chart(chart)

    st.write("**The visualization indicates:**")
    st.write("  * Great disparities, especially between low-income countries to upper-middle and high-income countries, with the largest share of CO2 emitted from the latter two.")
    st.write("  * Comparing upper-middle and high-income countries, we can see high-income countries emitting the largest amount of CO2 until around 2000, where upper-middle-income countries surpassed them in CO2 emissions.")


    st.markdown("***")


##### CO2 per capita emissions by income level across time
if page == "Exploration Analysis - OWID":
    st.markdown('#### 3. CO2 per capita emissions by income level')

    st.write("**Intro**")
    st.write("The picture changes when looking at CO2 per capita emissions across the same regions.")

    # Extract income-level data
    values_to_extract = ['High-income countries', 'Low-income countries', 'Upper-middle-income countries']
    df_income = df_OWID[df_OWID['country'].isin(values_to_extract)]

    # Create an Altair chart with interactivity
    chart = alt.Chart(df_income).mark_line().encode(
        x=alt.X('year:O', title='Year'),  # 'O' steht für Ordinal, um die Jahre als Ganzzahlen darzustellen
        y='co2_per_capita',
        color='country',
        tooltip=['year', 'co2_per_capita']
    ).properties(
        width=600
    ).interactive()

    # Display the Altair chart using st.altair_chart
    st.altair_chart(chart)

    st.write('**When looking at CO2 emissions per capita (fossil fuels, no land use change), we can observe:**')
    st.write('  * Although in absolute numbers CO2 emissions are higher in upper-middle-income countries, high-income countries per capita emissions are by far the highest.')
    st.write('  * CO2 per capita emissions in low-income countries are very low in comparison to high and middle-income countries.')
    st.write('  * These value disparities might suggest that there is a relationship between income level and CO2 emissions per capita.')


    st.markdown("***")


#### Global CO2 Emissions by Emission Source
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool

if page == "Exploration Analysis - OWID":
    st.markdown("#### 4. Global CO2 Emissions by Emission Source")
    
    st.write("**Intro**")
    st.write("This chart shows the global annual CO2 emissions by emission source.")

    # Filtern der Welt-Daten
    df_OWID_world = df_OWID[df_OWID['country'] == 'World']

    # Erstellen einer ColumnDataSource für Bokeh
    source = ColumnDataSource(df_OWID_world)

    # Erstellen einer interaktiven Bokeh-Figur
    q = figure(width=600, height=400, y_axis_label='Million tonnes')

    # Erstellen eines Farb- und Legenden-Mappings
    mapping = {
        'land_use_change_co2': ('land use change', 'blue'),
        'cement_co2': ('cement', 'red'),
        'coal_co2': ('coal', '#8e8c7f'),
        'gas_co2': ('gas', 'green'),
        'flaring_co2': ('flaring', '#647f5f'),
        'oil_co2': ('oil', '#e0e000'),
        'other_industry_co2': ('other industries', '#ff00a0')
    }

    # Schleife über das Mapping, um Linien, Tooltip und Hover-Tool für jede Spalte zu erstellen
    for col, (label, color) in mapping.items():
        r = q.line(x='year', y=col, legend_label=label, color=color, source=source)
        tooltips = [('Year', '@year'), (label, f'@{col}')]
        h = HoverTool(renderers=[r], tooltips=tooltips)
        q.add_tools(h)

    # Legendenposition einstellen
    q.legend.location = "top_left"

    # Bokeh-Diagramm in Streamlit anzeigen
    st.bokeh_chart(q)

    # Informationen über das Diagramm anzeigen
    st.write("**The chart reveals:**")
    st.write("  * Coal emissions data starts from 1750, while others begin around 1850 / 1880.")
    st.write("  * The primary CO2 emission sources are coal, oil, gas, and land use change.")
    st.write("  * Land use change emissions have slightly declined recently, but coal, oil, and gas emissions have risen.")
    st.write("  * Emissions from cement, flaring, and other industries are notably lower than the main sources.")
    
    st.markdown("***")

   
    #### TREEMAP OF 10 COUNTRIES WITH THE HIGHEST CUMULATIVE CO2 EMISSIONS

if page == "Exploration Analysis - OWID":
    st.markdown("#### Treemap")
    
    st.write('**Intro**')
    st.write('This treemap visualisation provides a clear insight into the CO2 emissions data of the ten countries with the highest cumulative CO2 production based on production data for the year 2021. A treemap is an effective way of presenting complex data hierarchically and allows the contributions of individual countries to global CO2 emissions to be seen at a glance. This serves to identify the major players in terms of CO2 emissions.')
    
    # Remove non-country rows
    Values_to_remove =  ['Africa', 'Africa (GCP)','Asia', 'Asia (GCP)','Asia (excl. China and India)','Central America (GCP)',
                         'Europe', 'Europe (GCP)', 'Europe (excl. EU-27)', 'Europe (excl. EU-28)','High-income countries','International transport',
                         'Low-income countries', 'OECD (GCP)','Oceania', 'Oceania (GCP)','Panama Canal Zone (GCP)', 'South America', 'South America (GCP)',
                         'Upper-middle-income countries', 'Kuwaiti Oil Fires (GCP)', 'North America (excl. USA)', 'European Union (28)', 'North America', 'Lower-middle-income countries',
                         'European Union (27)', 'Middle East (GCP)', 'Non-OECD (GCP)', 'North America (GCP)', 'European Union (27) (GCP)', 'World']

    df_countries = df_OWID[~df_OWID['country'].isin(Values_to_remove)]

    # Keep the most recent
    df_countries_latest = df_countries[df_countries.year == 2021]

    # Sort for largest values
    df_countries_latest = df_countries_latest.sort_values(by='cumulative_co2', ascending=False)

    # Keep the 10 countries with the highest values
    df_countries_latest_high = df_countries_latest.head(10)

    # Erstellen des Treemaps mit plotly.express
    fig = px.treemap(
        df_countries_latest_high,
        path=['country'],
        values='cumulative_co2',
        color='cumulative_co2',
        color_continuous_scale='Blues',
        hover_data={'cumulative_co2': True}
    )
    
    # Anzeigen des Treemaps
    st.plotly_chart(fig)

    st.write('**Observations:**')
    st.write("*  We can see that the United States has the highest total amount of cumulative CO2 emissions (421,906.844 millions tonnes of CO2), followed by China, Russia, Germany, the United Kingdom, and Japan.")
    st.markdown("*  In order to better assess the level of CO2 emissions, it can be helpful to make comparisons with everyday emissions or other easily understandable references. Here is a concrete example: The CO2 emissions of a one-way long-haul flight from Berlin to New York is approximately 1 tonne of CO2 (6'400 km, 1 passenger)")
    st.write("*  You can calculate the CO2 emissions of flights using the [myclimate emissions calculator](https://co2.myclimate.org/de/flight_calculators/new).")


    st.markdown("***")



###### Exploring the relationship between temperature change and CO2 emissions  
    
    st.markdown("#### Global Temperature Change and CO2 Emissions")
    
    st.write('**Intro**')
    st.write('The following scatter plot shows the relationship of global change in temperature and CO2 emissions (from fossil fuels, not including CO2 emissions by land use change).')

    # Merge NASA temperature change data with OWID CO2 data
    df_OWID = pd.read_csv('owid-co2-data.csv')
    df_OWID_world = df_OWID[df_OWID['country'] == 'World']
    df_NASA = pd.read_csv('ZonAnn.Ts+dSST.csv')
    df_OWID_NASA_merged = df_OWID_world.merge(df_NASA[['Year', 'Glob']], how='left', left_on='year', right_on='Year')
    
    # Rename temperature change column
    df_OWID_NASA_merged = df_OWID_NASA_merged.rename(columns={'Glob': 'temp_change'})
    
    # Calculate Pearson correlation coefficient and p-value
    df_OWID_NASA_merged_nonan = df_OWID_NASA_merged.dropna(subset=['temp_change', 'co2'])
    correlation_coefficient, p_value = pearsonr(df_OWID_NASA_merged_nonan['temp_change'], df_OWID_NASA_merged_nonan['co2'])

    # Create a scatter plot
    fig, ax = plt.subplots()
    sns.scatterplot(x='co2', y='temp_change', data=df_OWID_NASA_merged, ax=ax)
    ax.set_ylabel('Deviation from mean temperature in Celsius')
    ax.set_xlabel('CO2')

    # Annotate the Pearson correlation coefficient and p-value on the plot
    p_value_formatted = "{:0.2e}".format(p_value)  # Format p-value in scientific notation
    textstr = f'Pearson correlation coefficient: {correlation_coefficient:.3f}\np-value: {p_value_formatted}'
    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=8,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    # Show the plot
    st.pyplot(fig)
    
    st.write('**Observations and Conclusion:**')
    st.write("*  This scatter plot indicates a strong positive relationship between temperature change and CO2 emissions. This is in line with the results of a Pearson correlation test:")
    st.write("   - The Pearson correlation coefficient is {:.3f}, indicating a strong positive correlation.".format(correlation_coefficient))
    st.write("   - The p-value is {}, which is highly significant, suggesting a strong correlation between these factors.".format(p_value_formatted))
    st.write("*  Based on these findings, we can assume a strong relationship between CO2 emissions and the change in temperature.")






# MODELING PREPARATION

if page == 'Modeling preparation':
    st.markdown(
        """
        <style>
        .centered-title {
            font-size: 28px;
            text-align: center;
            border-top: 2px solid black;
            border-bottom: 2px solid black;
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<h1 class="centered-title">Modeling Preparation</h1>', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True) 


    # Modeling problem definition
    st.markdown("#### What kind of machine learning problem is your project like?")  
    st.markdown("""
    The project involves predicting **temperature changes** based on historical **CO2 emissions** data. 
    This prediction of a continuous value (temperature change) based on input features makes it a **regression problem**.
    The **aggregation level** the problem is modeled at is the **global** level.
    """)

    st.markdown("***")


    # Feature selection
    st.markdown('#### Feature selection')
    st.markdown('The initial stage involves initial data processing and selecting steps for identifying suitable features for the modeling. The following preprocessing operations have been applied to the OWID data set, which includes the variables we are interested in as features for our modeling:')

    # Create a DataFrame
    dict_feature_selection = {
        'Step': [1, 2, 3, 4, 5, 7, 8],
        'Action': [
            'Remove all entries before the year 1880',
            'Replacing values of “0” with np.NaN',
            'Remove all columns with a percentage of missing values > 50%',
            'Remove all variables focused on shares',
            'Remove all variables focused on growth',
            'Removing variables focused on per capita emissions',
            'Extracting variables focusing on cumulative emissions'
        ],
        'Justification': [
            'Data of target variable starting from 1880',
            'Emission values of 0 are very unlikely and indicate missing values',
            'Manage bias of imputation techniques',
            'These variables focus on country shares of total global shares, which should ideally be at 100% at global level analysis and therefore do not provide meaningful information at this level of aggregation',
            'Manage collinearity and dimensionality of data set',
            'Manage collinearity and dimensionality of data set',
            'Focus on more stable long-term impact assessment, reduce impact of outliers'
        ],
        'Remaining columns': [74, 74, 42, 28, 24, 17, 9]
    }

    df_feature_selection = pd.DataFrame(dict_feature_selection)

    # Display the table in Streamlit
    st.table(df_feature_selection)

    # Using markdown to display bullet list
    st.markdown("""
    The variables still present after the processing steps fall into four categories:
    - Annual aggregated cumulative CO2 emissions 
    - Annual cumulative CO2 emissions by emission source (one variable each for cement, coal, gas, oil, and land use change)
    - Time: Year
    - Socioeconomic variables: Population
    """)

    st.markdown("***")


    # Note: The triple double quotes (""") are used for multi-line strings in Python.
    # Model selection

    import streamlit as st

    st.markdown('#### Model Selection')
    st.markdown("""
    To forecast temperature change influenced by CO2 emissions, we selected a **diverse range of modeling techniques**. 
    Utilizing a wide range of models of **different complexities** and with different **advantages** and **limitations** allows us to **identify the 
    models with the most promising performance** in prediction temperature change based on the data at hand. 
    The insights generated in this way might **contribute to optimizing both data input and model optimization** in future modeling projects. 
    """)
    
    # OLS
    st.markdown("###### 1. OLS (Ordinary Least Squares):")
    st.write("""
    - **Type:** Linear regression method.
    - **Advantages:** Coefficient interpretability; efficiency.
    - **Limitations:** Assumes linearity; sensitive to outliers.
    - **Usage:** Used for preliminary understanding of CO2 and temperature relationship.
        - Advantages: Clear coefficient interpretability; computationally efficient.
        - Limitations: Assumes linearity; sensitive to outliers and high leverage points.

    """)

    # Parametric Methods
    st.markdown("###### 2. Parametric Methods:")
    st.write("""
    - **Description:** Assumes specific functional form of data.
    - **Advantages:** Simplicity; efficiency; interpretability.
    - **Limitations:** Assumption dependency; limited complexity.
    - **Model:** SARIMA - A time series model that captures trends, seasonality, and autocorrelation in data.
        - Advantages: Effective for data with trends and seasonality; interpretable parameters.
        - Limitations: Assumes linearity; relies on the validity of its assumptions.
    """)

    # Supervised Machine Learning Models
    st.markdown("###### 3. Supervised Machine Learning Models:")
    st.write("""
    - **Description:** Trained with labeled data.
    - **Advantages:** Versatility; accuracy; variety of algorithms.
    - **Limitations:** Needs labeled data; risk of overfitting.
    - **Models:** 
        - Linear Regression: Models the linear relationship between a dependent and one or more independent variables.
            - Advantages: Simple, interpretable, and widely used.
            - Limitations: Assumes a linear relationship; sensitive to outliers.
        - Elastic Net: Combines L1 and L2 regularization from Lasso and Ridge regression.
            - Advantages: Handles multicollinearity; performs feature selection.
            - Limitations: Requires tuning of hyperparameters.
        - SVR: Uses support vectors to find a hyperplane that best predicts continuous values.
            - Advantages: Effective for non-linear data; robust to outliers.
            - Limitations: Computationally intensive; requires hyperparameter tuning.


    """)

    # Ensemble Methods
    st.markdown("###### 4. Ensemble Methods:")
    st.write("""
    - **Description:** Combines multiple model decisions.
    - **Advantages:** Improved accuracy; robustness; feature insights.
    - **Limitations:** Complexity; less interpretability; computational intensity.
    - **Models:** 
        - Random Forests: Constructs multiple decision trees during training and outputs the average prediction of individual trees for regression tasks.
            - Advantages: Handles non-linear data; provides feature importance.
            - Limitations: Less interpretable than single trees; can be computationally heavy.
        - Gradient Boosting: Builds trees sequentially, where each tree corrects the errors of its predecessor.
            - Advantages: Often achieves higher accuracy than other methods.
            - Limitations: Sensitive to noisy data; can overfit if not well-tuned.            
    """)

    # Deep Learning & Neural Nets
    st.markdown("###### 5. Deep Learning & Neural Nets:")
    st.write("""
    - **Description:** Recognizes patterns via multi-layered neural networks.
    - **Advantages:** High performance; flexibility; adaptability.
    - **Limitations:** Needs large data; computationally heavy; black box nature.
    - **Model:** Time-Series Modeling with a Long Short-Term Memory Neural Network (LSTM) Model
        - A type of Recurrent Neural Network (RNN) that can remember patterns over long sequences.
        - Advantages: Captures long-term dependencies in sequential data.
        - Limitations: Requires large datasets; computationally intensive; harder to interpret.
    """)


    st.markdown("***")


    # Modeling Scope
    # Just global
    st.markdown('#### Modeling Iterations')
    st.markdown('Two iterations with different scopes and features have been included in the modeling. Depending on the analysis / modeling approach, both iteration steps or just one of them has been utilized.')

    dict_modeling_scope = {
        'Modeling iteration': [1, 2],
        'Features': [
            'Aggregated cumulative production-based CO2 emissions',
            "cumulative_cement_co2, cumulative_coal_co2, cumulative_gas_co2, cumulative_luc_co2, cumulative_oil_co2,\npopulation",
        ],
        'Number of features': [1, 6],
        'Temperature change data source': ['NASA', 'NASA'],
        'OLS': ['yes', 'yes'],
        'Supervised machine learning and ensemble models': ['yes', 'yes'],
        'SARIMA': ['yes', 'no'],
        'Long Short-Term Memory Neural Network (LSTM) model': ['yes', 'yes']
    }

    df_modeling_scope = pd.DataFrame(dict_modeling_scope)
    df_modeling_scope = df_modeling_scope.set_index('Modeling iteration')

    st.table(df_modeling_scope)


    st.markdown("""
    The two iterations serve different purposes: 
    - The **first iteration**, using **only aggregated cumulative CO2** as a features, provides a **broad overview of 
    the relationship** between CO2 emissions and temperature change. 
    - The **second iteration** offers a detailed analysis of the impact of individual emission sources. 
    
    By approaching the problem in this staged manner, we can ensure that we **capture both the macro and micro-level relationships** 
    in the data, leading to a comprehensive understanding of the factors driving temperature change.
    """)

    # Version 4 iterations
    # st.subheader('Modeling Scope')
    # st.markdown('Four iterations with different scopes and features have been included in the modeling. Depending on the analysis / modeling approach, all iteration steps or just a part of them has been utilized.')

    # dict_modeling_scope = {
    #     'Modeling iteration': [1, 2, 3, 4],
    #     'Scope / Data input': ['Global (Aggregated world)', 'Global (Aggregated world)', 'Local (country-based)', 'Local (country-based)'],
    #     'Features': [
    #         'Aggregated cumulative production-based CO2 emissions',
    #         "Cumulative CO2 emissions by emission source ('cumulative_cement_co2', 'cumulative_coal_co2', 'cumulative_gas_co2', 'cumulative_luc_co2', 'cumulative_oil_co2')\npopulation",
    #         'Aggregated cumulative production-based CO2 emissions',
    #         "Cumulative CO2 emissions by emission source ('cumulative_cement_co2', 'cumulative_coal_co2', 'cumulative_gas_co2', 'cumulative_luc_co2', 'cumulative_oil_co2')\npopulation"
    #     ],
    #     'Number of features': [1, 6, 1, 6],
    #     'Temperature change data source': ['NASA', 'NASA', 'FAO', 'FAO'],
    #     'OLS': ['yes', 'yes', 'no', 'no'],
    #     'Supervised machine learning and ensemble models': ['yes', 'yes', 'yes', 'yes'],
    #     'SARIMA': ['yes', 'no', 'no', 'no'],
    #     'Long Short-Term Memory Neural Network (LSTM) model': ['yes', 'yes', 'yes', 'yes']
    # }

    # df_modeling_scope = pd.DataFrame(dict_modeling_scope)
    # df_modeling_scope = df_modeling_scope.set_index('Modeling iteration')

    # st.table(df_modeling_scope)


    # st.markdown("""
    # By training models on both global and local scales, we hope to capture **overarching trends** and **local details**. 
    # Using varied CO2 emission sources helps **identify major model contributors** to temperature change prediction."
    # """)


if page == 'Ordinary Least Squares Regression':
    st.markdown(
        """
        <style>
        .centered-title {
            font-size: 28px;
            text-align: center;
            border-top: 2px solid black;
            border-bottom: 2px solid black;
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<h1 class="centered-title">Ordinary Least Squares Regression</h1>', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True) 

    st.markdown("""
    To generate **first high-level insights into the relationship of cumulative CO2 and temperature change**, 
    an Ordinary Least Squares Regression (OLS) has been computed, focusing on the global level.
    """)
    st.write("<br>", unsafe_allow_html=True)

    # User selection from the selectbox
    option = st.selectbox("Choose the feature set:", ["CO2", "all"])

    # Depending on the user selection, display the images
    if option == "CO2":
        st.markdown("#### **OLS CO2 Regression Results**")
        st.image("OLS_CO2_regression_summary.png", use_column_width=True)
        st.write("<br>", unsafe_allow_html=True)
        st.markdown("#### **OLS CO2 Regression Plot**")
        st.image("OLS_CO2_regression_plot.png", use_column_width=True)
        # st.image("OLS_CO2_residuals_vs_fitted_plot.png", caption="OLS CO2 Residuals vs Fitted Plot", use_column_width=True)
        # st.image("OLS_CO2_normal_q-q_plot.png", caption="OLS CO2 Normal Q-Q Plot", use_column_width=True)
        st.markdown("#### **OLS CO2 Scale-Location Plot**")
        st.image("OLS_CO2_scale_location_plot.png", use_column_width=True)
        # st.image("OLS_CO2_leverage_vs_residuals_squared_plot.png", caption="OLS CO2 Leverage vs Residuals Squared Plot", use_column_width=True)
        st.markdown("#### **Interpretation**")
        st.markdown("""
        Examining the results shows the following:
        - The model suggests that **89.9% of the variation** in temperature change can be attributed to changes in cumulative CO2 levels.
        - Without any CO2, the expected temperature change would be -0.273. Each unit increase in cumulative_co2 corresponds to a temperature change **increase of 7.262e−7** units.
        - The model's significance is evident from the **near-zero F-statistic p-value**.
        - The p-values for Omnibus and JB Test are greater than 0.05, suggesting that the residuals are **normally distributed**
        - The Durbin-Watson value of 0.920 hints at **potential positive autocorrelation**, which is a concern in time-series data. 
        Also, the **scale-location plot** indicates **heteroscedascity of the residuals** (no random distribution, but **funnel-shape**)
        This suggests that the model may not have captured all the underlying patterns or trends in the data, 
        and **specialized time-series modeling techniques**, like SARIMA, might be more appropriate.
        
        In essence, while there's a strong relationship between cumulative CO2 levels and temperature change, 
        the time-dependent nature of the data raises concerns about autocorrelation, 
        which may require more specialized modeling approaches.
        """)



    elif option == "all":
        st.markdown("#### **OLS all Features Regression Results**")
        st.image("OLS_all_regression_summary.png", use_column_width=True)
        st.write("<br>", unsafe_allow_html=True)
        st.markdown("#### **OLS all Features Partial Regression Plots**")
        st.image("OLS_all_partial_regression_plots.png", caption="OLS All Residuals vs Fitted Plot", use_column_width=True)
        # st.image("OLS_all_residuals_vs_fitted_plot.png", caption="OLS All Residuals vs Fitted Plot", use_column_width=True)
        # st.image("OLS_all_normal_q-q_plot.png", caption="OLS All Normal Q-Q Plot", use_column_width=True)
        st.markdown("#### **OLS all Features Scale-Location Plot**")
        st.image("OLS_all_scale_location_plot.png", use_column_width=True)
        # st.image("OLS_all_leverage_vs_residuals_squared_plot.png", caption="OLS All Leverage vs Residuals Squared Plot", use_column_width=True)
        st.markdown("#### **Interpretation**")
        st.markdown("""
        Examining the results shows the following:
        - **Model Fit**: The model accounts for **91.6% of the variability** in y, suggesting a strong fit.
        - **Model Significance**: The overall regression is **statistically significant**, implying at least one predictor is useful in predicting y.
        - **Coefficients**:
            - x2 (cumulative coal co2), x4 (cumulative luc co2), and x6 (population) have a **clear significant** effect on temperature change.
            - x1 (cumulative cement co2) and x5 (cumulative oil co2) show **marginal significance**.
            - x3 (cumulative gas co2) does **not significantly affect** temperature change.
        - **Autocorrelation**: Durbin-Watson value indicates **potential positive autocorrelation**, which can affect model reliability.
        - **Residuals**: Tests suggest residuals are likely normally distributed, which is a good sign.      
        - **Multicollinearity**: The high condition number suggests **potential collinearity** among predictors.
        
        Based on these results, next steps may include:
        - **Investigate potential sources of autocorrelation** and consider methods to correct for it, e.g., 
        introducing lag variables or using specialized models like ARIMA if time series data.
        - Given the high condition number, further **investigate potential multicollinearity** among predictors, for instance by 
        applying Variance Inflation Factor (VIF) analysis.
        - **Consider removing non-significant variables** or introducing interaction terms or polynomial terms based on domain knowledge.
        """)


# Supervised ML

if page == "Supervised machine learning and ensemble models":
    st.markdown(
        """
        <style>
        .centered-title {
            font-size: 28px;
            text-align: center;
            border-top: 2px solid black;
            border-bottom: 2px solid black;
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    

    st.markdown('<h1 class="centered-title">Supervised Machine Learning and Ensemble Models</h1>', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    import streamlit as st
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    import joblib
    # import sklearn
    # st.write(sklearn.__version__)

    @st.cache_data
    def load_csv_data(feature_set):
        # Create a mapping for the file prefix based on the choices
        feature_prefix = "CO2" if feature_set == "CO2" else "all"
        
        # Construct CSV path based on choices
        csv_path = f"CML_Glob_{feature_prefix}_results.csv"
        data = pd.read_csv(csv_path)
        return data

    # With countries
    # @st.cache_data
    # def load_csv_data(location, feature_set):
    #     # Create a mapping for the file prefix based on the choices
    #     location_prefix = "Glob" if location == "Global" else "Country"
    #     feature_prefix = "CO2" if feature_set == "CO2" else "all"
        
    #     # Construct CSV path based on choices
    #     csv_path = f"CML_{location_prefix}_{feature_prefix}_results.csv"
    #     data = pd.read_csv(csv_path)
    #     return data

    @st.cache_data
    def load_coefficients():
        return pd.read_csv("CML_Glob_all_model_coefficients.csv")


    @st.cache_data  # <- This will cache the image loading
    def load_image(plot_path):
        return mpimg.imread(plot_path)

    @st.cache_data  # Adding cache for the model loading
    def load_model(feature_set, model_name):
        # location_prefix = "Glob" if location == "Global" else "Country"
        feature_prefix = "CO2" if feature_set == "CO2" else "all"
        model_path = f"CML_Glob_{feature_prefix}_best_{model_name}_model.joblib"
        return joblib.load(model_path)

    # @st.cache_data  # Adding cache for the model loading
    # def load_model(location, feature_set, model_name):
    #     location_prefix = "Glob" if location == "Global" else "Country"
    #     feature_prefix = "CO2" if feature_set == "CO2" else "all"
    #     model_path = f"CML_{location_prefix}_{feature_prefix}_best_{model_name}_model.joblib"
    #     return joblib.load(model_path)

    # Prediction option 2, just linear model Glob Co2
    # def load_model():
    #     # Load the saved linear regression model
    #     return joblib.load("CML_Glob_CO2_best_linear_regression_model.joblib")



    def main():

        st.markdown("""
        This section outlines the modeling and training approach for supervised machine learning and ensemble methods and discusses its outcome.
        """)

        # Modeling preparation
        with st.expander("### **Modeling Preparation and Training**"):
            st.markdown("""
            We applied the following steps to prepare and train the selected supervised machine learning models:    
            Data Loading and Preprocessing:
            - Loading the relevant datasets: NASA for global temperature change modeling, OWID for CO2 and population data.            
            - All zero values in the dataset are replaced with NaN (missing values) to avoid potential pitfalls in the analysis.
            - Only rows with non-missing temperature change values are retained to avoid bias and keep data integrity in the target variable.
            - The data is split into training and test sets based on the year, with data up to the year 2000 used for training and data after 2000 used for testing to account for the time-dependent nature of the data. Considering the limited amount of data especially on the global level, splitting the data at the year 2000 provides a reasonable amount of observations for training (120) and testing (21) the models.
            

            Feature Engineering:
            - Data preprocessing includes two main steps: imputation and scaling. 
            - Missing values are imputed using the IterativeImputer, which models each feature with missing values as a function of other features. 
            - StandardScaler is then used to standardize the features.
            
            Model Selection:
            - A variety of regression models, including Random Forest, Gradient Boosting, SVM, ElasticNet, and Linear Regression, are chosen for evaluation.
            - Each model is paired with its hyperparameter grid for tuning.
            
            Model Training and Evaluation:
            - To account for the time-dependent nature of the data, TimeSeriesSplit is employed for cross-validation. Considering the limited amount of observation, a 2-fold split is applied
            - For each model, a grid search is performed to find the best hyperparameters using negative mean squared error as the scoring metric.
            - The performance of each model is evaluated on both the training and test datasets.
                """)

        st.write("<br>", unsafe_allow_html=True)

        st.markdown("""
        Choose a location and a feature set to see the results of the analysis for respective trained model:

        """)
        # st.write("<br>", unsafe_allow_html=True)

        # # Create a selectbox for location selection (Global or Country)
        # location = st.selectbox("Choose a location:", ["Global", "Country"])

        # Create a selectbox for feature selection (CO2 or All Features)
        feature_set = st.selectbox("Choose a feature set:", ["CO2", "All Features"])

        # Load the CSV data based on the selected location and feature set
        data = load_csv_data(feature_set)

        # # Load the CSV data based on the selected location and feature set
        # data = load_csv_data(location, feature_set)

        # Create a mapping for model selection
        model_mapping = {
            'Linear Regression': 'linear_regression',
            'Elastic Net Regression': 'elastic_net',
            'Gradient Boosting Regression': 'gradient_boosting',
            'Random Forest': 'random_forest',
            'Support Vector Regression': 'svm'
        }
        selected_model_name = st.selectbox("Choose a model:", list(model_mapping.keys()))
        selected_model = model_mapping[selected_model_name]

        # Filter the dataframe for the selected model and display the result
        st.write("<br>", unsafe_allow_html=True)        
        st.markdown('#### Performance Metrics')        
        model_data = data[data['Model'] == selected_model]
        st.table(model_data)

        # Construct the path for the prediction plot based on the choices
        st.markdown('#### Prediction Plot')
        # location_prefix = "Glob" if location == "Global" else "Country"
        feature_prefix = "CO2" if feature_set == "CO2" else "all"
        plot_path = f"CML_Glob_{feature_prefix}_{selected_model}_plot.png"
        
        try:
            image = load_image(plot_path)  # <- Call the cached function
            st.image(image, use_column_width=True, caption=f"{selected_model_name} Prediction Plot")
        except FileNotFoundError:
            st.write("The selected plot does not exist.")
        
        # Display Feature Importance Plot for tree-based models
        tree_based_models = ['gradient_boosting', 'random_forest', 'svm']
        if  feature_prefix == "all":
            
            if selected_model in tree_based_models:
                st.markdown('#### Feature importances')
                importance_plot_path = f"CML_Glob_{feature_prefix}_{selected_model}_feature_importance_plot.png"
                # importance_plot_path = f"CML_{location_prefix}_{feature_prefix}_{selected_model}_feature_importance_plot.png"
                try:
                    importance_image = load_image(importance_plot_path)
                    st.image(importance_image, use_column_width=True, caption=f"{selected_model_name} Feature Importance Plot")
                except FileNotFoundError:
                    st.write("Feature importance plot for the selected model does not exist.")
    

            # Display coefficients for Elastic Net and Linear Regression
            regression_models = ['elastic_net', 'linear_regression']
            if selected_model in regression_models:
                st.markdown('#### Coefficients')
                coeffs = load_coefficients()
                features = coeffs.iloc[:, 0]  # First column contains the feature names
                model_coeffs = coeffs[selected_model]
                selected_coeffs = pd.DataFrame({
                    'Feature': features,
                    'Coefficient': model_coeffs
                })
                selected_coeffs = selected_coeffs.sort_values(by = 'Coefficient')
                st.table(selected_coeffs)

        # PREDICTION WITH SELECTED MODEL
        if feature_prefix == 'CO2':
            st.write("<br>", unsafe_allow_html=True)        
            st.markdown('#### Model Prediction')
            st.markdown(f"Predict Temperature Change in Million tonnes based on CO2 Emissions with {selected_model_name}")

            co2_value = st.number_input("Enter CO2 emissions value:", value=1, step=1)

            if st.button("Predict"):
                model = load_model(feature_set, selected_model)
                # model = load_model(location, feature_set, selected_model)
                prediction = model.predict([[co2_value + 1e6]])
                st.write(f"Predicted temperature change for CO2 emissions value {co2_value} is: {prediction[0]}")


        # Option 2, just linear model Glob CO2
        # Button to trigger prediction
        # if st.button("Predict"):
        #     model = load_model()
        #     prediction = model.predict([[co2_value]])  # Model expects 2D array input
        #     st.write(f"Predicted temperature change for CO2 emissions value {co2_value} is: {prediction[0]}")

        st.write("<br>", unsafe_allow_html=True)                
        st.markdown('#### Interpretation')
        st.markdown("""
        Based on these metrics, the following models show the best performance: 
        1. **Linear Regression with 'Cumulative CO2' feature set**: This model has the highest test R2 and low error metrics (MAE, MSE, RMSE) 
        for both training and testing. This makes it the top-performing model among those provided.
        2. **SVM with ' Cumulative CO2' feature set**: Although the test performance is poor, its training performance is 
        close to the Linear Regression model. However, the significant discrepancy between training and test performance 
        indicates overfitting.
        3. **ElasticNet with 'Cumulative CO2' feature set**: Like SVM, the training performance is good, but it struggles on the test data. Again, 
        this suggests overfitting.
        4. Many of the other models, especially the more complex ones like Random Forest and Gradient Boosting, appear to be 
        overfitting the training data, as evidenced by their high training R2 values but poor test performance. 

        It's noteworthy to mention here again that the dataset utilized for modeling at the global level was relatively small. 
        Such a **limited dataset size can often pose challenges**, especially for non-linear models, leading to potential overfitting, 
        as was observed with Random Forest and Gradient Boosting.  With regards to **future modeling**, **regularization**, **feature selection**, 
        or **more data** might help in improving their generalization.
        """)



    if __name__ == "__main__":
        main()


# SARIMA
if page == "Time-series modeling with SARIMA":
    st.markdown(
        """
        <style>
        .centered-title {
            font-size: 28px;
            text-align: center;
            border-top: 2px solid black;
            border-bottom: 2px solid black;
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    

    st.markdown('<h1 class="centered-title">Time-series modeling with SARIMA</h1>', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)    

    st.markdown("""
    To address the **time-dependent nature of the data** in a more targeted manner, a **SARIMA** was computed and interpreted with the purpose 
    to account better for the temporal nature of the data at hand. For the SARIMA, the **"Cumulative CO2" feature set** has been chosen. 
    This ensures a pragmatic first approach in SARIMA modeling by **reducing model complexity**, ensuring **interpretability**, 
    and **mitigating potential multicollinearity issues** inherent in analyzing multiple emission sources.  
    
    The following figure visualizes the time series for both Cumulative 
    CO2 and Temperature Change:
    """)

    # Time-series visualization
    st.image("SARIMA_CumCo2andTempChange.png", use_column_width=True)
    st.markdown("""
        Given that we **observe seasonality in the global temperature anomaly**, it might be more appropriate to use a 
        **SARIMA** (Seasonal AutoRegressive Integrated Moving Average) model, which **can handle seasonality**, 
        as opposed to the simpler ARIMA model.
        """)
    st.write("<br>", unsafe_allow_html=True)

    st.markdown("***")
    
    # Model preparation
    with st.expander("**Modeling Preparation and Training**"):
        st.markdown("""
        Building the model, we considered the following steps:
        - Use the **Augmented Dickey-Fuller (ADF) test** to check for **stationarity** and apply **differencing** if needed
        - Consider **seasonality** (as observed in temperature change): Given that the data might have a yearly seasonality, 
        we'll consider a **seasonal order of 12** for the SARIMA model.
        - **Split the data** into training and test set using the year 2000 as a threshold, 
        resulting in 120 observations in the training and 21 observations in the test set
        - To identify the **best parameters** for the SARIMA model, we'll perform a **grid search** over a range of possible values 
        for p,  d,  q,  P,  D, and  Q (where  p,  d, and  q are the non-seasonal parameters, and  P,  D, and  Q are the seasonal 
        parameters).
            - P/p = (Seasonal) autoregressive order
            - D/d = (Seasonal) differencing order
            - Q/q = (Seasonal) moving average order
        """)
    # Insert a blank space
    st.write("<br>", unsafe_allow_html=True)

    st.markdown("***")


    # SARIMA results summary
    st.markdown("#### **Results summary**")    
    st.image("SARIMA_results_summary.png")
    st.markdown("""
    Looking at the results yields the following insights:
    - **Model**: A SARIMAX(1, 1, 1) was used, indicating one autoregressive term, one differencing term, 
    and one moving average term, without a seasonal component.
    - **Coefficients**: All coefficients are statistically significant. An increase in Cumulative CO2 leads to a rise in the global temperature anomaly.
    - **Residuals**: Residuals are independently distributed (Ljung-Box p-value: 0.25) and show no significant heteroskedasticity.
    - **Normality**: The data is approximately normally distributed (Jarque-Bera p-value: 0.23) with slight negative skewness and fewer extreme outliers.
    - **Model Fit**: The AIC and BIC values suggest a decent model fit, with lower values being better.

    In essence, the **model fits the data well**, with **Cumulative CO2 having a positive impact on global temperature anomaly**, 
    and the **residuals showing desirable properties**.

    """)

    st.write("<br>", unsafe_allow_html=True)

    st.markdown("***")


    # Performance Metrics
    st.markdown("#### **Model Performance Metrics**")

    SARIMA_performance_metrics = pd.read_csv('results_sarima_glob_cum_co2.csv', usecols=lambda column: column not in ['Unnamed: 0'])
    st.table(SARIMA_performance_metrics)
    st.markdown("""
    The performance metrics indicate a variety of things:
    - The SARIMA model **performs well on the training data**, capturing about **80.6%** of the variance. However, 
    its performance on the **test data** is **not as strong**, explaining **only 25.8%** of the variance. 
    - The **error metrics** (MAE, MSE, RMSE) are also **higher for the test set** compared to the training set, indicating 
    **potential overfitting** or the model's difficulty in generalizing to new data.
    """)

    st.write("<br>", unsafe_allow_html=True)

    st.markdown("***")


    # Actual vs Foreceast
    st.markdown("#### **Actual vs Forecast**")   
    st.markdown("""
    This chart visualizes the training data, the test data and the SARIMA forecast data of the temperature change variable.
    """) 
    st.image("SARIMA_ActualvsForeceast.png", caption="SARIMA Results Summary", use_column_width=True)
    st.markdown("""
    The plots grants the following key insights:
    - **SARIMA Forecast**: The **red line** represents the SARIMA model's forecasts for the test set. 
    The forecasts seem to **capture the general upward trend** observed in the training data and **align reasonably well with the actual values** in the test set.
    - **Confidence Intervals**: The **shaded pink region** represents the 95% confidence intervals for the forecasts. 
    For the most part, the **actual values from the test set fall within these confidence intervals**, 
    suggesting that the **model's forecasts are reasonably accurate**.
    """)
    st.markdown("""
    This suggests that the SARIMA model, with the given parameters, is a **suitable model for this dataset** and can 
    be used for future forecasts with a reasonable degree of confidence. However, while the model captures the 
    relationship between CO2 levels and the target variable in the training data, there might be other factors or 
    complexities in the test data that the model hasn't accounted for. **Regular model re-evaluation** and potential 
    **inclusion of other relevant features** might **improve its predictive accuracy** on unseen data.

    """)


# LSTM
if page == "Time-series modeling with LSTM":
    st.markdown(
        """
        <style>
        .centered-title {
            font-size: 28px;
            text-align: center;
            border-top: 2px solid black;
            border-bottom: 2px solid black;
            padding: 10px;
        }
        .linkedin-logo {
            width: 30px;
            height: 30px;
            cursor: pointer;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<h1 class="centered-title">Time-Series Modeling with a Long Short-Term Memory Neural Network (LSTM) Model</h1>', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    from tensorflow.keras.models import load_model

    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg

    @st.cache_data
    def load_image(image_path):
        return mpimg.imread(image_path)

    @st.cache_data
    def load_csv(csv_path):
        return pd.read_csv(csv_path, usecols=lambda column: column not in [' ','Unnamed: 0'])

    @st.cache_data
    def load_lstm_model(model_path):
        return load_model(model_path)

    def main():
        # st.markdown("<h3 style='text-align: center;'>Time-Series Modeling with a Long Short-Term Memory Neural Network (LSTM) Model</h3>", unsafe_allow_html=True)

        # st.write("<br>", unsafe_allow_html=True)

        st.markdown("""
        This section describes the steps for preparing and training a Long Short-Term Memory Neural Network 
        on the project data and shows the modeling results.
        """)

        with st.expander("### **Modeling Preparation and Training**"):
            st.markdown("""
            We applied the following steps for model preparation and training:
            
            **Data Preprocessing**:
            - Loading the relevant datasets: NASA for global temperature change modeling, OWID for CO2 and population data.
            - All zero values in the dataset are replaced with NaN (missing values) to avoid potential pitfalls in the analysis.
            - Only rows with non-missing temperature change values are retained to avoid bias and keep data integrity in the target variable.
            - The data is split into training and test sets based on the year, with data up to the year 2000 used for training and data after 2000 used for testing to account for the time-dependent nature of the data. Considering the limited amount of data especially on the global level, splitting the data at the year 2000 provides a reasonable amount of observations for training (120) and testing (21) the models.
            - Feature Engineering:
                - Created a pipeline to handle missing values using iterative imputation and standardized features using the StandardScaler.
                - Reshaping for LSTM: Reshaped the training data to create sequences of 10 n_steps (set to 10), which is necessary for LSTM to 
            operate on time-series data
            
            **Model Training and Hyperparameter Optimization**:
            - Hyperparameter Space: 
                - Defined a space for units (number of LSTM units) ranging from 32 to 256, with a step size of 32.
                - Defined possible activation functions: 'relu', 'tanh', and 'sigmoid'
            - Model Architecture: 
                - Designed a two-layer LSTM model followed by a dense layer for prediction. 
                - A two-layer LSTM can capture complex patterns in the data, and the dense layer provides the final prediction. 
                - This architecture balances complexity with computational efficiency.
            - Optimization Technique:
                - Employed a Bayesian optimization approach with the Optuna framework for efficient and effective hyperparameter 
                optimization, focusing on minimizing the Mean Squared Error (MSE) during cross-validation. 
                - TimeSeriesSplit was used for the validation strategy, ensuring that data integrity was maintained throughout 
                the optimization process. This is crucial for time-series data as it maintains the temporal structure during 
                validation The set was split into two folds to account for the limited data available in the Global runs
                - Conducted 50 trials to search for the best hyperparameters
            """)

        # User choices
        # location_choice = st.selectbox("Select Location:", ["Global", "Country"])
        feature_choice = st.selectbox("Select Feature Set:", ["CO2", "all features"])

        # Construct the path for the prediction plot based on the choices
        # location_prefix = "Glob" if location_choice == "Global" else "Country"
        feature_prefix = "CO2" if feature_choice == "CO2" else "all"

        # Base file path
        base_path = f"LSTM_Glob_{feature_prefix}"

        # Base file path with countries
        # base_path = f"LSTM_{location_prefix}_{feature_prefix}"

        st.markdown("***")


        # Display architecture image
        st.write("<br>", unsafe_allow_html=True)
        st.markdown("#### **Model Architecture**")   
        st.markdown("""
        The following plot visualizes the model architecture of the best performing LSTM of the specific scope with its best performing hyperparameters:
        """)
        architecture_image_path = f"{base_path}_best_model_architecture.png"
        st.image(load_image(architecture_image_path), caption="Model Architecture")
        st.markdown("""
        The architecture entails the following elements:
        - **Input Layer**: The model **receives sequences of data points as input**. 
        Each data point is a vector containing values for the features included in the modeling
        - **LSTM Layers**: This layer processes the sequences of the aforementioned features. The layer **captures the temporal 
        dependencies and relationships between the included featues** and how they might have historically influenced temperature changes. The LSTM's ability to maintain memory allows 
        the model to recognize patterns over time, such as how a surge in cumulative_oil_co2 in a prior period might correlate with temperature changes.
        - **Dense Layers**: The architecture concludes with a dense layer. 
        This layer **provides the final prediction**. Given the continuous nature of temperature values, 
        a dense layer is appropriate for regression tasks. It aggregates the features recognized 
        by the LSTM layers and produces a singular, continuous output.
        """)

        st.markdown("***")


        # Display results csv
        st.write("<br>", unsafe_allow_html=True)
        st.markdown("#### **Performance Metrics**")
        # st.markdown("The following table provides the performance metrics for the LSTM models trained:")
        results_csv_path = f"{base_path}_results.csv"
        st.write(load_csv(results_csv_path))
        st.write("<br>", unsafe_allow_html=True)

        st.markdown("***")


        # Display predictions image
        st.markdown("#### **Prediction plot**")
        # st.markdown("The following plot plots the actual vs the predicted values of the best performing LSTM model:")
        predictions_image_path = f"{base_path}_Predictions.png"
        st.image(load_image(predictions_image_path), caption="Predictions", use_column_width=True)

        st.markdown("***")

        # If user chose "all", display feature importance
        if feature_choice == "all features":
            st.markdown("#### **Feature importance plot**")
            st.markdown("""
            The feature importance been analyzed using **Permutation Feature Importance** (PFI). 
            PFI is a model-agnostic method used to estimate the importance of individual features in a predictive model. 
            The central idea is to evaluate the importance of a feature by **randomly shuffling its values and measuring how much 
            the model's performance drops**. If the performance remains largely unchanged, the feature is deemed unimportant. 
            Conversely, if the model's performance drops significantly, the feature is considered important.
            """)
            feature_importance_image_path = f"{base_path}_best_model_aggregated_importances_plot.png"
            st.image(load_image(feature_importance_image_path), caption="Feature Importances", use_column_width=True)

        # CO2 PREDICTION
        # Load the LSTM model
        if feature_choice == 'CO2':
            model_path = f"{base_path}_best_model.h5"
            model = load_lstm_model(model_path)

            # User input and prediction
            st.markdown('#### Model Prediction')
            st.markdown("""
            Predict Temperature Change in Million tonnes based on CO2 Emissions with the best performing model of trained 
            with cumulative CO2 as a feature.
            """)
            user_input = st.text_input("Enter the desired CO2 value to predict the temperature change:")
            if user_input:
                try:
                    input_value = np.array([[float(user_input)]])  # Convert the input to a 2D array
                    prediction = model.predict(input_value)
                    st.write(f"Predicted target value is: {prediction[0][0]}")
                except ValueError:
                    st.write("Please enter a valid number.")    
       
        st.markdown("***")
     
        # Summary
        st.markdown("#### **LSTM Summary**")
        st.markdown("""
        The analysis of the trained LSTM models grants the following insights:
        - **All models seem to overfit to the training data**, as indicated by the drop in performance from training to testing datasets. 
        The **limited size of the dataset** used in the modeling might play a central role in this regard, making it **difficult for the LSTM to capture complex, 
        non-linear relationships in the data** 
        - Models trained with the **all features set perform better** than models trained only with the CO2 feature. 
        This suggests that the additional features provide meaningful information that helps the model.
        - **"LSTM Global all"** stands out as the **best-performing model**, but there's **still significant room for improvement**, 
        given the negative R2 test values.
        - The **models' performance on the test data is not satisfactory**, with all models having negative R2 test values. 
        - The limited dataset size emerged as a tangible constraint, especially for models designed to discern non-linear relationships
        
        Looking into the future, further **feature engineering**, **widening the hyperparameter search space**, **increasing the training steps**, **reviewing the data preprocessing stage** for further optimization opportunities, 
        and **considerably increasing the size of the input data** might help improve the prediction power of LSTM models for the problem at hand. Also, **reducing 
        the batch size** might help improve the model performance given the size of the data we have at hand.
        """)

    if __name__ == "__main__":
        main()




###### Conclusion

if page == "Conclusion":
    st.markdown(
        """
        <style>
        .centered-title {
            font-size: 28px;
            text-align: center;
            border-top: 2px solid black;
            border-bottom: 2px solid black;
            padding: 10px;
        }
        .linkedin-logo {
            width: 30px;
            height: 30px;
            cursor: pointer;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<h1 class="centered-title">Conclusion</h1>', unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)

    # st.title("Conclusion")
    
    st.markdown("""
    The conducted research provides **critical insights** into the **relationship between CO2 emissions and temperature changes**, 
    answering important questions that steer the trajectory of our understanding and predictive capabilities.
    """)
    st.write("<br>", unsafe_allow_html=True)

    st.markdown("##### RQ 1 Historical Trend Analysis: *How have CO2 emissions and global temperatures changed over time?*") 
    st.markdown("""
    Our analysis revealed: 
    - A **clear upward trend in both global temperatures and CO2 emissions**, 
    with a notable surge in emissions post-1950. This holds true particularly for the Northern Hemisphere. 
    - It's also worth noting that **different countries** have shown **varied patterns of change** over time. 
    - Historically, high-income countries were the leading contributors to CO2 emissions, but now, 
    **upper-middle-income countries have overtaken them in total emissions**. However, when we consider emissions on a **per capita** basis, 
    **high-income countries still lead**. 
    """)
    st.write("<br>", unsafe_allow_html=True)

    st.markdown("##### RQ 2 Exploratory Relationship Analysis: *What is the nature of the relationship between CO2 emissions and global temperature changes?*") 
    st.markdown("""
    Our exploration revealed:
    - A **clear correlation between CO2 emissions and global temperature changes**. 
    - The Linear Regression model, particularly when trained on the 'CO2' feature, underscored this link, highlighting that **as 
    cumulative CO2 emissions increase, there's a corresponding rise in global temperatures**. 
    - This correlation not only **reaffirms the influential role of CO2 in global temperature dynamics** but also suggests 
    that other factors might be in play, given the observed variances in the models.

    """)
    st.write("<br>", unsafe_allow_html=True)

    st.markdown("##### RQ 3 Predictive Modeling: *Can we accurately predict future temperature changes based on the data included in the modeling?*")  
    st.markdown("""
    Summing up, based on the considered performance metrics:
    - **Most models** have shown signs of **overfitting**, indicated by high training  R2 values but negative test R2 values.
    - The **Linear Regression** model trained on the 'CO2' feature has provided the **most balanced performance**.
    - The **SARIMA** model has shown a **promising prediction performance**.
    - The **limited dataset size** emerged as a **tangible constraint**, especially for models designed to capture **non-linear relationships**. 
    Such models, including **SVR**, **Random Forest**, **Gradient Boosting**, and **LSTM**, exhibited tendencies of overfitting, illuminating the challenges of capturing intricate patterns with limited data.
    """)
    st.write("<br>", unsafe_allow_html=True)

    st.markdown("***")


    st.markdown("##### Limitations and Future Research and Projects")  
    st.markdown("""
    Future modeling endeavors could greatly benefit from **regularization**, **feature selection**, and, most critically, 
    the **inclusion of a more extensive dataset**. Incorporating **polynomial** or **interaction terms** and employing **transformations** 
    (e.g. log transformation or differencing) could further refine the models, enabling them to capture potential non-linearities 
    and interactions in the data more effectively.
    """)

    st.write("<br>", unsafe_allow_html=True)

    st.markdown("""
    In sum, while our current models **provide valuable insights and a foundational understanding**, 
    there lies a clear **avenue for enhancement**. By integrating more climate-relevant data and continuously 
    refining modeling techniques and **optimizing hyperparameters**, we can expect to bolster the performance of 
    even the more complex models, driving more accurate and nuanced forecasts in the future.
    """)  
