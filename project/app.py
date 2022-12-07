import pandas as pd
import streamlit as st
import markup
from analyzer import analyze
import graph
data=pd.read_csv('new.csv')


st.markdown(markup.project_title(),unsafe_allow_html=True)
with open('style.css') as file:
    st.markdown(f'<style>{file.read()}</style>',unsafe_allow_html=True)
st.markdown("""<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">"""
            ,unsafe_allow_html=True)


products=data.product_title.unique()
print(products)
product=st.selectbox(options=products,label="Select a Product: ")
st.write('Selected Product: ',product)


prod_reviews=data.loc[data['product_title'] == product]
prod_reviews.to_csv('product.csv',index=False)


def overall(all_components)->list:
    all_ratings=[]
    for component in all_components:
        component_data = analyze(component)
        count_rates = component_data['star_ratings']['ones'] + component_data['star_ratings']['twos'] + \
                        component_data['star_ratings']['threes'] \
                        + component_data['star_ratings']['fours'] + component_data['star_ratings']['fives']
        total_rates = component_data['star_ratings']['ones'] + component_data['star_ratings']['twos'] * 2 + \
                        component_data['star_ratings']['threes'] * 3 \
                        + component_data['star_ratings']['fours'] * 4 + component_data['star_ratings']['fives'] * 5
        average_rating=round(total_rates/count_rates,1)
        all_ratings.append(average_rating)

    st.markdown(markup.group_component_rating(all_components,all_ratings),unsafe_allow_html=True)
    return all_ratings

def display_component(component):
    st.write('Selected component: ',component)
    component_data = analyze(component)
    graph.bar_graph(component_data['positive_reviews'], component_data['negative_reviews'])
    st.image('image.png')
    count_rates = component_data['star_ratings']['ones'] + component_data['star_ratings']['twos'] + \
                  component_data['star_ratings']['threes'] \
                  + component_data['star_ratings']['fours'] + component_data['star_ratings']['fives']
    total_rates = component_data['star_ratings']['ones'] + component_data['star_ratings']['twos'] * 2 + \
                  component_data['star_ratings']['threes'] * 3 \
                  + component_data['star_ratings']['fours'] * 4 + component_data['star_ratings']['fives'] * 5
    st.markdown(markup.reviews_breakdown(component_data['positive_reviews'], component_data['negative_reviews']
                                         , component_data['neutral_reviews']), unsafe_allow_html=True)


    if(count_rates!=0):
        comp_rating = round(total_rates / count_rates, 1)
        st.markdown(f"<p style=font-size:1.25rem>Star rating of {component} (out of 5):</p>",unsafe_allow_html=True)
        st.markdown(markup.component_rating(component, comp_rating), unsafe_allow_html=True)
    else:
        st.write('component not found')
    st.write(f'Advanced analysis of {component}:')
    st.write(component_data)


#change::::::
if(len(product)):
    graph.draw_star_graph()
    st.image('image.png')   
    st.markdown(f"<p class=text-center style=font-size:1.25rem;>{product}</p>",unsafe_allow_html=True)
    component=st.text_input(label="Enter a component",placeholder="Name of component here")
    component=component.lower()
    

    if len(component):
        display_component(component)
        component=''    #

    all_components=['sound','battery','design']


    show_overall=st.button("Show overall")
    if show_overall:
        all_rating=overall(all_components)
        overall_rating=all_rating[0]+all_rating[1]+all_rating[2]
        overall_rating=overall_rating/3

        # st.write(overall_rating)
        if(overall_rating>4.25):
            st.markdown(markup.highly_recommended(),unsafe_allow_html=True)
        elif overall_rating>4:
            st.markdown(markup.recommended(),unsafe_allow_html=True)
        else:
            st.markdown(markup.not_recommended(),unsafe_allow_html=True)

