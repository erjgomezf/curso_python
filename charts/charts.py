import matplotlib.pyplot as plt

def generate_pie_chart():
    """
    Generates a pie chart from the provided data and labels.

    Parameters:
    - data: A list of numerical values for the pie chart.
    - labels: A list of labels corresponding to the data.
    - title: The title of the pie chart.

    Returns:
    - None
    """
    labels = ['A', 'B', 'C', 'D']
    values = [10, 20, 30, 40]
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    plt.savefig('pie_chart.png')
    plt.close()