import pandas as pd
import matplotlib.pyplot as plt


def draw_star_graph():
    data = pd.read_csv('product.csv')
    ones = data[data['star_rating'] == 1]
    twos = data[data['star_rating'] == 2]
    threes = data[data['star_rating'] == 3]
    fours = data[data['star_rating'] == 4]
    fives = data[data['star_rating'] == 5]

    x = [1,2,3,4,5]

    print(len(ones))
    y = [len(ones),len(twos),len(threes),len(fours),len(fives)]

    plt.plot(x,y,marker='o',markerfacecolor='green',linestyle='dashed')
    plt.xlabel('Stars')
    plt.ylabel('No. of reviews')
    plt.title('Star Rating Graph')
    plt.savefig('image.png')
    plt.close()

def bar_graph(pos,neg):
    x=['Positive','Negative']
    y=[pos,neg]
    plt.bar(x,y,color=['green','red'],width=0.5)
    plt.ylabel('Number of reviews')
    plt.savefig('image.png')
    plt.close()