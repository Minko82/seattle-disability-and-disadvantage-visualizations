import pandas as pd
import altair as alt

# Load data
seattle = "https://gist.githubusercontent.com/evanpeck/cf2a657e1d5007d037a5fe18fb3613f7/raw/56000b199945a52490ac01f84ccd4bc7bb966ed1/gistfile1.txt"

data = alt.Data(url=seattle, format=alt.DataFormat(property="features", type="json"))


# Plotting Socioeconomics vs Health in Seattle

alt.Chart(data).mark_circle().encode(
    x = alt.X("properties.SOCIOECON_DISADV_SCORE:Q", title="Socioeconomic Disadvantage Score"),
    y = alt.Y("properties.HEALTH_DISADV_SCORE:Q", title="Health Disadvantage Score"),
    size = alt.Size("properties.PCT_ADULT_WITH_DISABILITY:Q", title="% Adults with Disability").scale(zero=False),
    color = "properties.PCT_ADULT_WITH_DISABILITY:Q"
).properties(
    title = "Disadvantage and Disability in Seattle",
).interactive()


# Dropdown Menu

input_dropdown = alt.binding_select(options=[None, 'Lowest', 'Second Lowest', 'Middle', 'Second Highest', 'Highest Equity Priority'], name='Race, ELL, & Origins Quintile ')

selection = alt.selection_point(fields=['properties.RACE_ELL_ORIGINS_QUINTILE'], bind=input_dropdown)

opacity_rule = alt.condition(selection, alt.value(0.7), alt.value(0.1))

alt.Chart(data).mark_circle().encode(
    x = alt.X("properties.SOCIOECON_DISADV_SCORE:Q", title="Socioeconomic Disadvantage Score"),
    y = alt.Y("properties.HEALTH_DISADV_SCORE:Q", title="Health Disadvantage Score"),
    size = alt.Size("properties.PCT_ADULT_WITH_DISABILITY:Q", title="% Adults with Disability").scale(zero=False),
    opacity = opacity_rule
).properties(
    title = "Disadvantage and Disability in Seattle",
).add_params(
    selection
)


# Apply Selections to Multiple Charts

input_dropdown = alt.binding_select(options=[None, 'Lowest', 'Second Lowest', 'Middle', 'Second Highest', 'Highest Equity Priority'], name='Race, ELL, & Origins Quintile ')

selection = alt.selection_point(fields=['properties.RACE_ELL_ORIGINS_QUINTILE'], bind=input_dropdown)

disadvantage_and_disability = alt.Chart(data).mark_circle().encode(
    x = alt.X("properties.SOCIOECON_DISADV_SCORE:Q", title="Socioeconomic Disadvantage Score"),
    y = alt.Y("properties.HEALTH_DISADV_SCORE:Q", title="Health Disadvantage Score"),
    size = alt.Size("properties.PCT_ADULT_WITH_DISABILITY:Q", title="% Adults with Disability").scale(zero=False),
    opacity = alt.condition(selection, alt.value(0.7), alt.value(0.1))
).properties(
    title = "Disadvantage and Disability in Seattle",
).add_params(
    selection
)

obesity_vs_asthma = alt.Chart(data).mark_circle().encode(
    x = alt.X("properties.PCT_ADULT_WITH_OBESITY:Q", title="% Adults with Obesity").scale(zero=False),
    y = alt.Y("properties.PCT_ADULT_WITH_ASTHMA:Q", title="% Adults with Asthma").scale(zero=False),
    size = alt.Size("properties.PCT_ADULT_WITH_DISABILITY:Q", title="% Adults with Disability").scale(zero=False),
    opacity = alt.condition(selection, alt.value(0.7), alt.value(0.1))
).properties(
    title = "Obesity vs. Asthma",
).add_params(
    selection
)

disadvantage_and_disability | obesity_vs_asthma


# Brush and Link - Multiple Selections

brush = alt.selection_interval(empty=False)

disadvantage_and_disability_brush = alt.Chart(data).mark_circle().encode(
    x = alt.X("properties.SOCIOECON_DISADV_SCORE:Q", title="Socioeconomic Disadvantage Score"),
    y = alt.Y("properties.HEALTH_DISADV_SCORE:Q", title="Health Disadvantage Score"),
    size = alt.Size("properties.PCT_ADULT_WITH_DISABILITY:Q", title="% Adults with Disability").scale(zero=False),
    opacity = alt.condition(selection, alt.value(0.7), alt.value(0.1)),
    color = alt.condition(brush, alt.value('orange'), alt.value('steelblue'))
).properties(
    title = "Disadvantage and Disability in Seattle",
).add_params(
    selection,
    brush
)

obesity_vs_asthma_brush = alt.Chart(data).mark_circle().encode(
    x = alt.X("properties.PCT_ADULT_WITH_OBESITY:Q", title="% Adults with Obesity").scale(zero=False),
    y = alt.Y("properties.PCT_ADULT_WITH_ASTHMA:Q", title="% Adults with Asthma").scale(zero=False),
    size = alt.Size("properties.PCT_ADULT_WITH_DISABILITY:Q", title="% Adults with Disability").scale(zero=False),
    opacity = alt.condition(selection, alt.value(0.7), alt.value(0.1)),
    color = alt.condition(brush, alt.value('orange'), alt.value('steelblue'))
).properties(
    title = "Obesity vs. Asthma",
).add_params(
    selection,
    brush
)

disadvantage_and_disability_brush | obesity_vs_asthma_brush


# Interactive Legend

legend_select = alt.selection_point(fields=['properties.RACE_ELL_ORIGINS_QUINTILE'], bind='legend')


alt.Chart(data).mark_circle().encode(
    x = alt.X("properties.SOCIOECON_DISADV_SCORE:Q", title="Socioeconomic Disadvantage Score"),
    y = alt.Y("properties.HEALTH_DISADV_SCORE:Q", title="Health Disadvantage Score"),
    color = alt.Color("properties.RACE_ELL_ORIGINS_QUINTILE:N", scale=alt.Scale(scheme='brownbluegreen', domain=['Lowest', 'Second Lowest', 'Middle', 'Second Highest', 'Highest Equity Priority'])),
    opacity = alt.condition(legend_select, alt.value(1), alt.value(0.05))
).properties(
    title = "Disadvantage and Disability in Seattle"
).add_params(
    legend_select
)


# Strip Plots + Brushing

brush_selection = alt.selection_interval(empty=False)


disadvantage_and_disability_linked = alt.Chart(data).mark_circle().encode(
    x = alt.X('properties.SOCIOECON_DISADV_SCORE:Q', title="Socioeconomic Disadvantage Score", axis=None),
    y = alt.Y('properties.HEALTH_DISADV_SCORE:Q', title="Health Disadvantage Score", axis=None),
    size = alt.Size('properties.PCT_ADULT_WITH_DISABILITY:Q', title="% Adults with Disability").scale(zero=False),
    color = alt.condition(brush_selection, alt.value('orange'), alt.value('steelblue')),
).add_selection(
    brush_selection
).properties(
    title = "Disadvantage and Disability in Seattle"
).add_params(
    brush_selection
)



left_strip_plot = alt.Chart(data).mark_tick().encode(
    y = alt.Y('properties.HEALTH_DISADV_SCORE:Q', title='Health Disadvantage Score'),
    color = alt.condition(brush_selection, alt.value('orange'), alt.value('steelblue'))
).add_params(
    brush_selection
)

bottom_strip_plot = alt.Chart(data).mark_tick().encode(
    x = alt.X('properties.SOCIOECON_DISADV_SCORE:Q', title='Socioeconomic Disadvantage Score'),
    color = alt.condition(brush_selection, alt.value('orange'), alt.value('steelblue'))
).add_params(
    brush_selection
)


left_strip_plot | disadvantage_and_disability_linked & bottom_strip_plot

# Visualization 4 Redesigned

# - Double encoded the points with values that are unbiased
#     - Color blind friendly palette 
#     - No color biases in the color associations
# - Tooltip to help define outliers in the visualization
# - Regression line to help draw the viewer’s attention to trends

input_dropdown = alt.binding_select(options=[None, 'Lowest', 'Second Lowest', 'Middle', 'Second Highest', 'Highest Equity Priority'], name='Race, ELL, & Origins Quintile ')
selection = alt.selection_point(fields=['properties.RACE_ELL_ORIGINS_QUINTILE'], bind=input_dropdown)
brush = alt.selection_interval(empty=False)

disadvantage_and_disability_brush = alt.Chart(data).mark_circle().encode(
    x=alt.X("properties.SOCIOECON_DISADV_SCORE:Q", title="Socioeconomic Disadvantage Score"),
    y=alt.Y("properties.HEALTH_DISADV_SCORE:Q", title="Health Disadvantage Score"),
    size=alt.Size("properties.PCT_ADULT_WITH_DISABILITY:Q", title="% Adults with Disability").scale(zero=False),
    color=alt.condition(
        brush,
        alt.value('#1f77b4'),  
        alt.Color("properties.PCT_ADULT_WITH_DISABILITY:Q", title="% Adults with Disability", scale=alt.Scale(scheme="paired"))
    ),
    opacity=alt.condition(
        brush & selection,  
        alt.value(0.8),     
        alt.value(0.2)      
    ),
    tooltip=[
        alt.Tooltip("properties.SOCIOECON_DISADV_SCORE:Q", title="Socioeconomic Disadvantage Score"),
        alt.Tooltip("properties.HEALTH_DISADV_SCORE:Q", title="Health Disadvantage Score"),
        alt.Tooltip("properties.PCT_ADULT_WITH_DISABILITY:Q", title="% Adults with Disability")
    ]
).properties(
    title="Disadvantage and Disability in Seattle"
).add_params(
    selection,
    brush
)

# Add regression line to Disadvantage and Disability Chart
disadvantage_and_disability_regression = alt.Chart(data).transform_regression(
    "properties.SOCIOECON_DISADV_SCORE", "properties.HEALTH_DISADV_SCORE"
).mark_line(color='red').encode(
    x="properties.SOCIOECON_DISADV_SCORE:Q",
    y="properties.HEALTH_DISADV_SCORE:Q"
)

disadvantage_and_disability_layer = disadvantage_and_disability_brush + disadvantage_and_disability_regression

obesity_vs_asthma_brush = alt.Chart(data).mark_circle().encode(
    x=alt.X("properties.PCT_ADULT_WITH_OBESITY:Q", title="% Adults with Obesity").scale(zero=False),
    y=alt.Y("properties.PCT_ADULT_WITH_ASTHMA:Q", title="% Adults with Asthma").scale(zero=False),
    size=alt.Size("properties.PCT_ADULT_WITH_DISABILITY:Q", title="% Adults with Disability").scale(zero=False),
    color=alt.condition(
        brush,
        alt.value('#1f77b4'),
        alt.Color("properties.PCT_ADULT_WITH_DISABILITY:Q", title="% Adults with Disability", scale=alt.Scale(scheme="paired"))
    ),
    opacity=alt.condition(
        brush & selection, 
        alt.value(0.8),     
        alt.value(0.2)      
    ),
    tooltip=[
        alt.Tooltip("properties.PCT_ADULT_WITH_OBESITY:Q", title="% Adults with Obesity"),
        alt.Tooltip("properties.PCT_ADULT_WITH_ASTHMA:Q", title="% Adults with Asthma"),
        alt.Tooltip("properties.PCT_ADULT_WITH_DISABILITY:Q", title="% Adults with Disability")
    ]
).properties(
    title="Obesity vs. Asthma"
).add_params(
    selection,
    brush
)

# Add regression line to Obesity vs. Asthma Chart
obesity_vs_asthma_regression = alt.Chart(data).transform_regression(
    "properties.PCT_ADULT_WITH_OBESITY", "properties.PCT_ADULT_WITH_ASTHMA"
).mark_line(color='red').encode(
    x="properties.PCT_ADULT_WITH_OBESITY:Q",
    y="properties.PCT_ADULT_WITH_ASTHMA:Q"
)


obesity_vs_asthma_layer = obesity_vs_asthma_brush + obesity_vs_asthma_regression


disadvantage_and_disability_layer | obesity_vs_asthma_layer