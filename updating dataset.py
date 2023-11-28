import pandas as pd 
import random

dataset=pd.read_csv("C:\\Users\\Hp\\Desktop\\forest fire detection\\Forest_fire.csv")
def generate_data(num_examples=200):
    oxygen = [random.randint(1,60) for _ in range(num_examples)]
    temperature = [random.randint(1, 60) for _ in range(num_examples)]
    humidity = [random.randint(1, 100) for _ in range(num_examples)]
    fire_occurrence = [random.choice([0, 1]) for _ in range(num_examples)]

    data = {
        "Oxygen": oxygen,
        "Temperature": temperature,
        "Humidity": humidity,
        "Fire Occurrence": fire_occurrence,
    }

    df = pd.DataFrame(data)
    return df

dataset = generate_data(200)
dataset = dataset.drop(columns=['Area'], errors='ignore')
dataset.to_csv('modified_dataset.csv', index=False)
print(dataset)