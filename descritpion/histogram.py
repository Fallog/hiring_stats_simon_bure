import pandas as pd
import matplotlib.pyplot as plt


def createHist(sequence: list, name: str):
    """Displays an histogram description the given sequence using matplotlib.pyplot package.
    Histogram is titled using the name argument.

    Args:
        sequence (list): list of int, float, str or char
        name (str): name of the sequence used for the labelling of the histogram
    """
    plt.figure(figsize=(6.5, 6.5))  # creating a new pyplot figure of a certain size
    plt.grid(visible=False)  # removing the grid
    plt.title("Histogram of " + name)  # titling figure
    plt.xlabel(name)  # titling x axis
    plt.ylabel("Frequency")  # titling y axis
    plt.hist(x=sequence, color="royalblue")
    plt.show()  # display the histogram


# The following lines are executed only if you run specifically histogram.py and are used to test the code above
if __name__ == "__main__":
    df = pd.DataFrame(
        {
            "eyes": ["Bleu", "Vert", "Marron", "Bleu", "Bleu", "Marron"],
            "nb_people": [35, 12, 54, 27, 25, 48],
        }
    )
    createHist([35, 12, 54, 27, 25, 48], "Number of people")  # Function is working
