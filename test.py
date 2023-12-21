# # Import Tecton and other libraries
# import logging
# import os
# import tecton
# import pandas as pd
# import snowflake.connector
# from datetime import datetime, timedelta
# from pprint import pprint

# # The following two lines log only warnings to the console. To log all events to the console, remove the two lines.
# logging.getLogger('snowflake.connector').setLevel(logging.WARNING)
# logging.getLogger('snowflake.snowpark').setLevel(logging.WARNING)

# # connection_parameters assumes the Snowflake connection credentials are stored in the environment
# # variables `SNOWFLAKE_USER`,`SNOWFLAKE_PASSWORD` and `SNOWFLAKE_ACCOUNT`.
# # Uncomment the "authenticator" parameter below, only if authenticating through a browser.
# # If the "authenticator" parameter is included, do not include the password parameter below.
# connection_parameters = {
#     "user": 'Guest', # Your username in the Snowflake account that you're using with Tecton
#     "password": 'Password123', # Your password in the Snowflake account that you're using with Tecton. Not needed if using the authenticator parameter above.
#     "account": 'https://tv70595.central-us.azure.snowflakecomputing.com', # The Snowflake account you're using with Tecton (takes the form \<SNOWFLAKE_ACCOUNT\>.snowflakecomputing.com
#     "warehouse": "FEATURESTORE_WH",
#     # Database and schema are required to create various temporary objects by tecton
#     "database": "FEATURESTORE_DB",
#     "schema": "FEATURESTORE_SCHEMA"
# }
# conn = snowflake.connector.connect(**connection_parameters)
# tecton.snowflake_context.set_connection(conn) # Tecton will use this Snowflake connection for all interactive queries

# # Quick helper function to query snowflake from a notebook
# # Make sure to replace with the appropriate connection details for your own account
# def query_snowflake(query):
#     df = conn.cursor().execute(query).fetch_pandas_all()
#     return df

# # Set the compute mode to snowflake
# tecton.conf.set("TECTON_COMPUTE_MODE", "snowflake")

# tecton.version.summary()


# Import libraries
import logging
import os
from datetime import datetime, timedelta
import tecton
import pandas as pd
import snowflake.connector

# Set logging levels
logging.getLogger('snowflake.connector').setLevel(logging.WARNING)
logging.getLogger('snowflake.snowpark').setLevel(logging.WARNING)

# Connection parameters
connection_parameters = {
    "user": 'Guest',  # Your username in the Snowflake account that you're using with Tecton
    "password": 'Password123',  # Your password in the Snowflake account that you're using with Tecton. Not needed if using the authenticator parameter above.
    "account": 'https://tv70595.central-us.azure.snowflakecomputing.com',  # The Snowflake account you're using with Tecton
    "warehouse": "FEATURESTORE_WH",
    "database": "FEATURESTORE_DB",
    "schema": "FEATURESTORE_SCHEMA"
}

# Connect to Snowflake
conn = snowflake.connector.connect(**connection_parameters)
tecton.snowflake_context.set_connection(conn)

# Helper function to query Snowflake
def query_snowflake(query):
    df = conn.cursor().execute(query).fetch_pandas_all()
    return df

# Set compute mode to Snowflake
tecton.conf.set("TECTON_COMPUTE_MODE", "snowflake")

# Display Tecton version summary
tecton.version.summary()
