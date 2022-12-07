import pandas as pd
from rake_nltk import Rake
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#
# data=pd.read_csv('appl_1_amazon_pc.csv')
# data=data[['product_title','review_body','star_rating']]
# data.to_csv('new.csv',mode='w')
#change...

sid=SentimentIntensityAnalyzer()
# for index in data.index:

def analyze(component)->dict:
    data=pd.read_csv('product.csv')
    data=data[['review_body','star_rating']]
    component_data={'pos':0,'neg':0,'compound':0,'positive_reviews':0,'negative_reviews':0,'neutral_reviews':0,
          'star_ratings':{'ones':0,'twos':0,'threes':0,'fours':0,'fives':0}}
    for index in data.index:
    # for index in range(10442):
        review=data['review_body'][index]
        review=review.lower()
        # print(review)
        star=data['star_rating'][index]
        # print(review,'\n')
        is_included=False
        r = Rake()
        r.extract_keywords_from_text(review)
        phrase_df=pd.DataFrame(r.get_ranked_phrases_with_scores(),columns=['score','phrase'])
        phrase_df = phrase_df.loc[phrase_df.score > 2]
        list = phrase_df['phrase']
        # print(phrase_df)
        # print(list)
        if len(list):
            for element in list:
                if component in element:
                    # print(element)
                    is_included=True
                    value=sid.polarity_scores(element)
                    component_data['pos']+=value['pos']
                    component_data['neg']+=value['neg']
                    component_data['compound']+=value['compound']
                    if value['compound'] >= 0.05:
                        component_data['positive_reviews'] += 1
                    elif value['compound'] <= -0.05:
                        component_data['negative_reviews'] += 1
                    else:
                        component_data['neutral_reviews'] += 1
            # print(is_included)
        if is_included:
            if star==1:
                component_data['star_ratings']['ones']+=1
            elif star==2:
                component_data['star_ratings']['twos']+=1
            elif star==3:
                component_data['star_ratings']['threes']+=1
            elif star==4:
                component_data['star_ratings']['fours']+=1
            else:
                component_data['star_ratings']['fives']+=1
            # print('star value',component_data['star_ratings'])
            # print(component_data)
    return component_data



# print(data['review_body'][0])
# print(type(data.index))