import matplotlib.pyplot as plt
from view.corpus_app import CorpusApp


plt.rcParams.update({'font.size': 8})

if __name__ == "__main__":
    app = CorpusApp()
    app.mainloop()
