
import pandas as pd
import pydeck as pdk

# Read property data from Excel file
property_data = pd.read_excel('ValuePerAcre2.xlsx')

# Calculate property values divided by acres
property_data['ValuePerAcre'] = (property_data['CURR_VAL'] / property_data['ACRES'])/100

# Set up PyDeck 3D map visualization
view = pdk.data_utils.compute_view(property_data[['LONG', 'LAT']])
layer = pdk.Layer(
    'HexagonLayer',
    data=property_data,
    get_position=['LONG', 'LAT'],
    get_elevation='ValuePerAcre',
    radius=1000,
    elevation_scale=50,
    elevation_range=[0, 1000],
    get_fill_color='[255, 255 - (ValuePerAcre / 100), 0]',
    auto_highlight=True,
    pickable=True,
    coverage=1,
    extruded=True,
)

# Create a PyDeck map with the defined layer and view
r = pdk.Deck(layers=[layer], initial_view_state=view)

# Render the map
r.to_html('property_map.html')

print("Your map is ready!")

# Make sure to replace 'property_values.xlsx' with the path to your Excel file containing
# the property data. The Excel file should have columns named 'Longitude', 'Latitude', 'Value',
# and 'Acres' to represent the respective property attributes.

# NAD_1983_StatePlane_Georgia_West_FIPS_1002_Feet

# The code calculates the value per acre by dividing the property value by the number of acres
# and then visualizes it using a 3D map with PyDeck's ColumnLayer. The resulting map is saved
# as an HTML file named 'property_map.html'.

# Note: You'll need to install the required dependencies (pandas, pydeck) if you haven't already.