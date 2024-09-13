import matplotlib, string
import matplotlib.pyplot

def main(values, categories=[]):
    # Create bar chart
    if len(categories) == 0:
        categories = list(string.ascii_uppercase[:len(values)])
    matplotlib.pyplot.bar(categories, values)

    # Add title and labels
    matplotlib.pyplot.title("Pravda: Bar Chart")
    matplotlib.pyplot.xlabel("Categories")
    matplotlib.pyplot.ylabel("Values")

    # Show the plot
    matplotlib.pyplot.show()
