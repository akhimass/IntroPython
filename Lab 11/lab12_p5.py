# Problem #5

# Read the contents of a coal data file and return the data in a dictionary format.
def read_data_file(filename):
    data_file = open(filename, "r")
    header_line = data_file.readline() # Read the header line of the file to extract years

    years = header_line.strip().split(",")[1:] # Extract the years from the header line

    # Initialize an empty dictionary to store the data
    data_dict = {}

    # Iterate over each line in the data file
    for line in data_file:

        # Remove leading and trailing whitespaces, and split the line into a list using commas
        line = line.strip().split(",")
        # Create a nested dictionary for each country in the data_dict
        data_dict[line[0]] = {} 

        # Iterate over the years and assign the corresponding values to the data_dict
        for i in range(0,len(years)):
            data_dict[line[0]][int(years[i])] = line[i+1]

     # Close the file
    data_file.close()

    # Return the final data dictionary
    return data_dict

print(read_data_file("coal_production.csv"))

def calculate_total_production(coal_production):
    total_production = {}
    while coal_production:
        county, production = coal_production.popitem()
        if county in total_production:
            total_production[county] += production
        else:
            total_production[county] = production
    return total_production

coal_production_data = read_data_file("coal_production.csv")
total_production_by_county = calculate_total_production(coal_production_data)
print(total_production_by_county)