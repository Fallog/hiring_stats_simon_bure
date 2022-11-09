import pandas as pd
import matplotlib.pyplot as plt


def createHist(num_seq: list, column: str):
    plt.figure(figsize=(5, 5))  # creating a new pyplot figure
    # plt.subplots(2, 2)  # adding 2 axis
    plt.grid(visible=False)  # removing the grid
    plt.title("Histogram of" + column)  # titling figure
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.hist(x=num_seq, color="royalblue")
    plt.show()


if __name__ == "__main__":
    df = pd.DataFrame(
        {
            "eyes": ["Bleu", "Vert", "Marron", "Bleu", "Bleu", "Marron"],
            "nb_people": [35, 12, 54, 27, 25, 48],
        }
    )
    createHist([35, 12, 54, 27, 25, 48], "Number of people")
