import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set_style("whitegrid")
# notice that the imports are not in alphabetical order
sns.set_style("whitegrid")


def some_function_with_trailing_whitespaces() -> None:
    """Function that returns the string "Hello World!"""
    print("Hello World!")


x = np.random.randint(0, 100, 100)
df = pd.DataFrame({"x": x})
plt.plot(df.x)



