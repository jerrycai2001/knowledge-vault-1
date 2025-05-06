import altair as alt

def build_chart(df):
    return alt.Chart(df).mark_line().encode(
        x='x',
        y='y'
    )
