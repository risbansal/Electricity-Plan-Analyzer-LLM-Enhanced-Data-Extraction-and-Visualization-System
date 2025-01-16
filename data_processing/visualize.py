import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

def visualize(input_file):
    # Load the CSV file
    
    data = pd.read_csv(input_file)

    save_path = "output\plot.png"
    
    data["Plan"] = data["Company Name"] + " - " + data["Plan Name"] # combining plan and company name
    
    #Handle numeric data
    data['Base Charge'] = pd.to_numeric(data['Base Charge'], errors='coerce')
    data["Base Charge"].fillna(0, inplace=True)
    
    data['Energy Charge'] = pd.to_numeric(data['Energy Charge'], errors='coerce')
    data["Energy Charge"].fillna(0, inplace=True)
    
    width = 0.4
    l = np.arange(len(data["Plan"]))
    # l = [5] * len(data["Plan"])
    
    plt.bar(l - width/2, data["Base Charge"],width, label="Base Charge($)", color="cyan")
    plt.bar(l + width/2, data["Energy Charge"], width, label="Energy Charge(cents)", color="purple")

    
    plt.xlabel("Company and Plan")
    plt.ylabel("Charges")
    plt.xticks(l, data["Plan"], rotation=45)
    plt.title("Base Charge vs. Energy Charge by Plan")
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()


if __name__ == '__main__':
    file_path = "output\plans.csv"  
    visualize(file_path)

