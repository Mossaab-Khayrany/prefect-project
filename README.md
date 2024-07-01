# Prefect data orchestration | real world example of data analysis project

![Static Badge](https://img.shields.io/badge/-prefect-wite?logo=prefect&logoColor=eaeaea&color=gray) ![Static Badge](https://img.shields.io/badge/-python-wite?logo=python&logoColor=eaeaea&color=blue) ![Static Badge](https://img.shields.io/badge/-SQL-wite?logo=postgresql&logoColor=white&color=green) ![Static Badge](https://img.shields.io/badge/-PowerBI-wite?logo=powerbi&logoColor=white&color=red)

<div style="overflow: hidden; border-radius: 15px; width: fit-content;">
    <img src="https://raw.githubusercontent.com/Mossaab-Khayrany/prefect-project/19e786dee466f25623dcd120e3ca9a0eb90ca5b6/gifs/dashboard.gif" alt="Markdownify Screenshot" width="600"/>
</div>

## Project Overview

<div style="overflow: hidden; border-radius: 15px; width: fit-content;">
    <img src="https://raw.githubusercontent.com/Mossaab-Khayrany/prefect-project/main/gifs/1.jpg" alt="Markdownify Screenshot" width="600"/>
</div>

This project demonstrates a real-world example of constructing a Power BI dashboard from raw data using Prefect for data orchestration. As a data analyst working for an analytics company, my objective was to create an analytics dashboard for both "Brands" investors and "Restaurants" clients. the company offers a digital presence application to restaurants, allowing them to connect their receipt printers to the app. This app collects data and builds dashboards and insights for restaurant owners. Additionally, the company provides market analytics to brand investors, offering insights into the restaurants and brands market.

## Project Workflow

1. **Data Collection:**

   - Collected raw data from 10 restaurants that are clients of the analytics company.
   - The raw data is dumped into a PostgreSQL server in a table called `raw_data` within a database named `database_one`.
   - The `raw_data` table contains two columns:
     - `id`: The ID of the printed receipt in a specific restaurant.
     - `tickets`: A string column containing JSON formatted inputs representing the content in every order/ticket printed.

2. **Data Orchestration using Prefect:**

   - **Fetch Raw Data:**
     - Constructed tasks using Python functions that fetch raw data from the PostgreSQL database using credentials.
   - **Data Transformation:**
     - Transformed the raw data into Pandas datasets.
     - Ran a similarity algorithm to enrich the raw data, providing context and additional features from a preclassified dataset called `food`.
     - Fetched `stores` data from the database during this workflow.
   - **Data Construction:**
     - Constructed `orders` and `enriched_ordersdetails` datasets from the raw data.
     - Sent the processed data back to the PostgreSQL database.

3. **Power BI Dashboard Construction:**
   - Used the processed and enriched data to construct a Power BI dashboard.
   - The dashboard serves the analytics needs of both restaurant owners and brand investors.
   - Restaurant owners can track their business performance through the admin dashboard.
   - Brand investors gain insights into the market and their competition.

## Detailed Steps

### 1. Setting Up the Environment

- Installed necessary libraries such as `Prefect`, `pandas`, and `sqlalchemy`.
- Configured database credentials and connections.

### 2. Fetching Raw Data

- Defined Prefect tasks to connect to the PostgreSQL database.
- Fetched raw data from the `raw_data` table.

### 3. Data Transformation

- Loaded raw data into Pandas DataFrames.
- Applied data cleaning and transformation techniques.
- Implemented a similarity algorithm to enrich the data using the `food` dataset.
- Extracted and processed additional `stores` data.

### 4. Constructing Datasets

- Combined and enriched the raw data to create `orders` and `enriched_ordersdetails` datasets.
- Uploaded the processed datasets back to the PostgreSQL database.

### 5. Building the Power BI Dashboard

- Imported the processed datasets into Power BI.
- Created visualizations to display key metrics and insights for restaurant owners and brand investors.
- Designed an interactive dashboard to facilitate data-driven decision-making.

## Conclusion

This project showcases the power of Prefect for data orchestration and Power BI for data visualization. By automating the data pipeline and creating an insightful dashboard, we can provide valuable analytics to both restaurant owners and brand investors, helping them make informed decisions and stay competitive in the market.

## Tools and Technologies Used

- **Prefect**: For orchestrating data workflows.
- **Python**: For data fetching, transformation, and enrichment.
- **PostgreSQL**: For storing raw and processed data.
- **Pandas**: For data manipulation and transformation.
- **Power BI**: For creating interactive dashboards and visualizations.

## How to Run the Project

1. Clone the repository.
2. Set up the PostgreSQL database and insert the raw data.
3. Configure the database credentials in the Prefect tasks.
4. Run the Prefect flow to fetch, transform, and enrich the data.
5. Load the processed data into Power BI and build the dashboard.

## Repository Structure

- `README.md`: Project documentation.
- `prefect_flows/`: Prefect flow definitions.
- `data/`: Sample raw data and processed datasets.
- `powerbi_dashboard/`: Power BI dashboard files.

Feel free to explore the repository and reach out if you have any questions or need further assistance!

---

This content provides a comprehensive overview of the project, including the steps taken, tools used, and instructions for running the project. You can modify and expand upon this template to better fit your specific needs and details.
