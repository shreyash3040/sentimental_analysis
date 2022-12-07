def reviews_breakdown(positives,negatives,neutrals):
    return f"""
    <div class="my_main">
    <div class="positive">      
        <p class="title">Positive reviews</p>
        <p class="number" id="pos">{positives}</p>
    </div>
    <div class="negative">
        <p class="title">Negative reviews</p>
        <p class="number" id="neg">{negatives}</p>
    </div>
    <div class="neutral">
        <p class="title">Neutral reviews</p>
        <p class="number">{neutrals}</p>
    </div>
    </div>"""

def recommended():
    return """
    <div class="alert alert-success text-center" role="alert">
        The product is recommended
    </div>"""

def highly_recommended():
    return """
    <div class="alert alert-success text-center" role="alert">
        The product is highly recommended!!!
    </div>"""

def not_recommended():
    return """
    <div class="alert alert-warning text-center" role="alert">
        The product is not recommended!!!
    </div>"""


def component_rating(component,comp_rating):
    if comp_rating<2:
        color='red'
    elif comp_rating<3:
        color='yellow'
    elif comp_rating<4:
        color='palegreen'
    else:
        color='green'

    return f"""<div class="progress_bar {color}">
    <p class="rating">{comp_rating}</p>
    <p class="component">{component}</p>
    </div>"""

def group_component_rating(all_components,all_ratings):
    component1=all_components[0]
    component2=all_components[1]
    component3=all_components[2]
    rating1=all_ratings[0]
    rating2=all_ratings[1]
    rating3=all_ratings[2]

    if rating1<2:
        color1='red'
    elif rating1<3:
        color1='yellow'
    elif rating1<4:
        color1='palegreen'
    else:
        color1='green'

    if rating2<2:
        color2='red'
    elif rating2<3:
        color2='yellow'
    elif rating2<4:
        color2='palegreen'
    else:
        color2='green'

    if rating3<2:
        color3='red'
    elif rating3<3:
        color3='yellow'
    elif rating3<4:
        color3='palegreen'
    else:
        color3='green'

    return f"""
    <div class="group">
        <div class="component1 circle {color1}">
        <p class="rating">{rating1}</p>
        <p class="component">{component1}</p>
        </div>
        <div class="component2 circle {color2}">
        <p class="rating">{rating2}</p>
        <p class="component">{component2}</p>
        </div>
        <div class="component3 circle {color3}">
        <p class="rating">{rating3}</p>
        <p class="component">{component3}</p>
        </div>
    </div>
    """

def project_title():
    return """
    <div class="project_title text-center">
        Sentimental analysis of product reviews and Recommendation
    </div>"""