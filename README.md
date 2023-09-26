# US House Price Analysis

### Web application of House Price Index

Analyzing the Influence of Various Social and Economic Factors on US Housing Prices

The analysis is structured across three distinct notebooks:

1. **[Data Gathering]**: In this notebook, data is acquired from publicly accessible online sources and processed into a clean and usable format using the pandas library. Multiple data sources are integrated to create consolidated dataframes that serve as the foundation for subsequent analyses. The combined datasets are also stored in a designated data directory for easy access in other notebooks.

2. **Exploratory Data Analysis (EDA)**: This notebook focuses on exploratory data analysis, presenting visualizations that elucidate relationships between various dataset features. EDA provides insights into patterns, trends, and potential correlations within the data.

3. **Model Building**: In this notebook, a Linear Regressor model is trained and evaluated using the acquired data. The results of this model help us comprehend how different factors influence the prices of single households in the US. Notably, the S&P/Case-Shiller U.S. National Home Price Index is employed as a proxy for home prices in this analysis.

The S&P/Case-Shiller Home Price Indices are instrumental in monitoring changes in the prices of single-family residential homes across the United States. These indices rely on sales pairs that have undergone at least two arm's length transactions, employing the repeat-sales method to mitigate the challenge of accounting for price variations due to differing home characteristics. Consequently, these indices measure fluctuations in single household prices over time while holding quality attributes constant. As a result, no quality-related variables such as the number of bedrooms, bathrooms, or furnishings have been considered in this analysis.

How to Navigate:
Simply click on the file you wish to explore:
- Data Gathering
- EDA
- Model Building

Powered by raw.githack.com

To Execute:
1. Clone the repository or download the ZIP file.
2. Unzip the downloaded file into an empty directory.
3. Utilize Jupyter Notebook or Jupyter Lab to open the .ipynb files for exploration and analysis.


Effect on supply and demand factors in the housing market:

1. **spend**: Increased government spending can stimulate demand for housing by boosting the economy.

2. **permits**: A higher number of permits indicates increased supply as more construction projects are initiated.

3. **permit_val**: A higher permit value suggests larger and more expensive construction projects, potentially impacting supply and demand.

4. **starts**: More housing starts can increase supply, potentially moderating price growth.

5. **completions**: Completed units can affect supply dynamics, potentially influencing prices.

6. **manufactured**: Manufactured homes can provide more affordable housing options, increasing supply and demand.

7. **new_for_sale**: A higher number of new homes for sale can impact both supply and demand.

8. **months_supply**: More months' supply suggests greater supply, potentially reducing prices.

9. **emratio**: A strong employment ratio can boost demand for housing.

10. **pop_level**: A growing population can increase demand for homes.

11. **gdp**: A growing GDP can stimulate demand for housing due to economic prosperity.

12. **mortgage_rate**: Lower mortgage rates can increase demand by making homeownership more affordable.

13. **fed_fund_rate**: Changes in the federal funds rate can influence mortgage rates and overall demand.

14. **disp_income**: Higher disposable income can boost demand by increasing purchasing power.

15. **pm_save**: Personal savings can impact down payment capabilities, affecting demand.

16. **consump_durable**: Increased spending on durable goods can reflect consumer confidence and affect demand.

17. **new_sold**: More newly sold homes can indicate a competitive market and increased demand.

18. **rent_vacancy**: A high rental vacancy rate can impact rental income and demand for investment properties.

19. **owner_vacancy**: Higher owner vacancy rates can affect supply and demand dynamics.

20. **week_earning**: Higher weekly earnings can increase demand for housing.

21. **delinquent_rate**: A high delinquency rate on loans can signal financial instability, affecting demand.

22. **hor**: A higher Housing Opportunity Index indicates better affordability, potentially attracting more buyers.

23. **hp_idx_qtr**: A rising Home Price Index reflects property value appreciation, impacting demand and supply dynamics.

Each of these factors plays a role in shaping the supply and demand balance in the housing market, ultimately influencing housing prices.