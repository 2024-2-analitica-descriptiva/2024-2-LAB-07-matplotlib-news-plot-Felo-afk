"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import matplotlib.pyplot as plt
import os


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    def read_data(dir):
        df = pd.read_csv(dir, index_col=0)
        return df

    def create_plot(df, output_dir, filename):
        plt.figure()
        colors = {
            "Television": "dimgray",
            "Newspaper": "grey",
            "Internet": "tab:blue",
            "Radio": "lightgrey",
        }
        zorder = {
            "Television": 1,
            "Newspaper": 1,
            "Internet": 2,
            "Radio": 1,
        }
        linewidths = {
            "Television": 2,
            "Newspaper": 2,
            "Internet": 3,
            "Radio": 2,
        }
        for col in df.columns:
            plt.plot(
                df[col],
                label=col,
                color=colors[col],
                zorder=zorder[col],
                linewidth=linewidths[col],
            )
        plt.title("How people get their news", fontsize=16)
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["left"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.gca().axes.get_yaxis().set_visible(False)
        for col in df.columns:
            first_year = df.index[0]
            plt.scatter(
                x=first_year,
                y=df[col][first_year],
                color=colors[col],
                zorder=zorder[col],
            )

            last_year = df.index[-1]
            plt.scatter(
                x=last_year, y=df[col][last_year], color=colors[col], zorder=zorder[col]
            )

        plt.legend(loc="upper right")
        plt.tight_layout()
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, filename))
        plt.close()
        plt.show

    df = read_data(r"files\input\news.csv")
    create_plot(df, r"files\plots", "news.png")


pregunta_01()  # Running
