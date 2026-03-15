/*
Create Database and Schemas 
This script creates a new database named 'DataWarehouse' after checking if it already exists. If such database exists, 
it is dropped and recreated. This script also creates three schemas: 'bronze', 'silver', and 'gold'. 
*/

-- Drop and recreate schemas for each layer
DROP SCHEMA IF EXISTS bronze CASCADE;
DROP SCHEMA IF EXISTS silver CASCADE;
DROP SCHEMA IF EXISTS gold CASCADE;

-- Create Schemas
CREATE SCHEMA bronze;
CREATE SCHEMA silver;
CREATE SCHEMA gold;