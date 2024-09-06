# OLAP vs OLTP Project with PostgreSQL

## Description
This project demonstrates the differences between Online Analytical Processing (OLAP) and Online Transaction Processing (OLTP) using PostgreSQL. It includes an ETL (Extract, Transform, Load) process that transfers data from an OLTP database to an OLAP database, showcasing the structural and functional differences between these two database paradigms.

## Features
- OLTP database schema for a simple e-commerce system
- OLAP database schema with star model for analytical processing
- Python-based ETL script to transfer data from OLTP to OLAP
- Sample data generation for testing and demonstration

## Prerequisites
- Python 3.7+
- PostgreSQL 12+
- psycopg2 library

## Installation

1. Clone the repository:

git clone https://github.com/yourusername/olap-vs-oltp-project.git
cd olap-vs-oltp-project
text

2. Set up a virtual environment (optional but recommended):

python -m venv myenv
source myenv/bin/activate # On Windows use myenv\Scripts\activate
text

3. Install the required Python packages:

pip install psycopg2
text

4. Set up PostgreSQL databases:
- Create two databases: `oltp_db` and `olap_db`
- Run the SQL scripts in `oltp_schema.sql` and `olap_schema.sql` to set up the respective schemas

## Usage

1. Populate the OLTP database with sample data:

psql -d oltp_db -f sample_data.sql
text

2. Run the ETL script:

python OLAP_VS_OLTP.py
text

3. Verify the data in the OLAP database:

psql -d olap_db
text

## Project Structure
- `OLAP_VS_OLTP.py`: Main Python script for ETL process
- `oltp_schema.sql`: SQL script for creating OLTP database schema
- `olap_schema.sql`: SQL script for creating OLAP database schema
- `sample_data.sql`: SQL script for inserting sample data into OLTP database

## Database Schemas

### OLTP Schema
- customers (customer_id, name, email, created_at)
- products (product_id, name, price, stock_quantity)
- orders (order_id, customer_id, order_date, total_amount)
- order_items (order_item_id, order_id, product_id, quantity, price)

### OLAP Schema
- dim_customer (customer_key, customer_id, name, email, created_at)
- dim_product (product_key, product_id, name, price)
- dim_date (date_key, date, day, month, year, quarter)
- fact_sales (sales_key, order_id, customer_key, product_key, date_key, quantity, total_amount)

## Contributing
Contributions to this project are welcome. Please feel free to submit a Pull Request.

## License
This project is open source and available under the [MIT License](LICENSE).

## Contact
For any queries regarding this project, please open an issue on GitHub.

