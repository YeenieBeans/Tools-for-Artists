import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Define the size of the cube
size = 10

# Define colors
colors = {
    "lavender": "#9876B6",
    "obsidian": "#222326",
    "desaturated_cream": "#E6E7C9",  # More desaturated cream
    "lime": "#D6DC82",
    "cherry": "#DE6072",
    "gray_fill": "#CFCFCF",
    "user_point": "#3D2FD0",  # Default User point color
    "friend_point": "#B469C4"  # Default Friend point color
}

# Initial Plot Setup
def create_initial_plot():
    fig = go.Figure()

    # Add axes
    fig.add_trace(go.Scatter3d(x=[0, size], y=[0, 0], z=[0, 0],
        mode='lines', line=dict(color=colors['lavender'], width=4), hoverinfo="none"))
    fig.add_trace(go.Scatter3d(x=[0, -size], y=[0, 0], z=[0, 0],
        mode='lines', line=dict(color=colors['lavender'], width=4), hoverinfo="none"))
    fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, size], z=[0, 0],
        mode='lines', line=dict(color=colors['lime'], width=4), hoverinfo="none"))
    fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, -size], z=[0, 0],
        mode='lines', line=dict(color=colors['lime'], width=4), hoverinfo="none"))
    fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, 0], z=[0, size],
        mode='lines', line=dict(color=colors['cherry'], width=4), hoverinfo="none"))
    fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, 0], z=[0, -size],
        mode='lines', line=dict(color=colors['cherry'], width=4), hoverinfo="none"))

    # Add cube edges
    cube_vertices = [
        [-size, -size, -size], [-size, -size, size], [-size, size, -size], [-size, size, size],
        [size, -size, -size], [size, -size, size], [size, size, -size], [size, size, size]
    ]
    cube_edges = [
        [0, 1], [1, 3], [3, 2], [2, 0],
        [4, 5], [5, 7], [7, 6], [6, 4],
        [0, 4], [1, 5], [2, 6], [3, 7]
    ]

    for edge in cube_edges:
        fig.add_trace(go.Scatter3d(
            x=[cube_vertices[edge[0]][0], cube_vertices[edge[1]][0]],
            y=[cube_vertices[edge[0]][1], cube_vertices[edge[1]][1]],
            z=[cube_vertices[edge[0]][2], cube_vertices[edge[1]][2]],
            mode='lines', line=dict(color=colors['desaturated_cream'], width=2), hoverinfo="none"
        ))

    # Add hyperplanes
    # X-Y plane
    fig.add_trace(go.Surface(
        x=np.array([[-size, -size], [0, 0]]),
        y=np.array([[-size, size], [-size, size]]),
        z=np.zeros((2, 2)),
        colorscale=[[0, 'rgba(152, 118, 182, 0.85)'], [1, 'rgba(152, 118, 182, 0.85)']],
        opacity=0.85, showscale=False, hoverinfo="none"
    ))

    fig.add_trace(go.Surface(
        x=np.array([[0, 0], [size, size]]),
        y=np.array([[-size, size], [-size, size]]),
        z=np.zeros((2, 2)),
        colorscale=[[0, 'rgba(211, 211, 211, 0.85)'], [1, 'rgba(211, 211, 211, 0.85)']],
        opacity=0.85, showscale=False, hoverinfo="none"
    ))

    # Y-Z plane
    fig.add_trace(go.Surface(
        x=np.zeros((2, 2)),
        y=np.array([[-size, -size], [0, 0]]),
        z=np.array([[-size, size], [-size, size]]),
        colorscale=[[0, 'rgba(214, 220, 130, 0.85)'], [1, 'rgba(214, 220, 130, 0.85)']],
        opacity=0.85, showscale=False, hoverinfo="none"
    ))

    fig.add_trace(go.Surface(
        x=np.zeros((2, 2)),
        y=np.array([[0, 0], [size, size]]),
        z=np.array([[-size, size], [-size, size]]),
        colorscale=[[0, 'rgba(211, 211, 211, 0.85)'], [1, 'rgba(211, 211, 211, 0.85)']],
        opacity=0.85, showscale=False, hoverinfo="none"
    ))

    # X-Z plane
    fig.add_trace(go.Surface(
        x=np.array([[-size, size], [-size, size]]),
        y=np.zeros((2, 2)),
        z=np.array([[-size, -size], [0, 0]]),
        colorscale=[[0, 'rgba(222, 96, 114, 0.85)'], [1, 'rgba(222, 96, 114, 0.85)']],
        opacity=0.85, showscale=False, hoverinfo="none"
    ))

    fig.add_trace(go.Surface(
        x=np.array([[-size, size], [-size, size]]),
        y=np.zeros((2, 2)),
        z=np.array([[0, 0], [size, size]]),
        colorscale=[[0, 'rgba(211, 211, 211, 0.85)'], [1, 'rgba(211, 211, 211, 0.85)']],
        opacity=0.85, showscale=False, hoverinfo="none"
    ))

    # Add text annotations above the hyperplanes
    fig.add_trace(go.Scatter3d(
        x=[size, -size, 0, 0, 0, 0],
        y=[0, 0, size, -size, 0, 0],
        z=[0, 0, 0, 0, size, -size],
        mode='text',
        text=['Realistic', 'Cartoony', 'Anthro', 'Feral', 'Detailed', 'Simple'],
        textfont=dict(family='Arial, sans-serif', size=18, color=colors['desaturated_cream']),  # Updated color
        textposition='top center',  # Centered above the hyperplanes
        hoverinfo="none"
    ))

    # Layout settings
    fig.update_layout(
        title=dict(
            text='<b>3D Representation of Artistic Styles</b>',
            font=dict(size=30, color=colors['desaturated_cream']),
            x=0.5, y=0.95, xanchor='center', yanchor='top'
        ),
        scene=dict(
            xaxis=dict(nticks=4, range=[-size, size], showbackground=False,
                       title_text='<b>Realistic — Cartoony</b>', title_font=dict(size=18, color=colors['desaturated_cream']),
                       tickvals=[-10, 10], ticktext=['', ''], tickfont=dict(color=colors['desaturated_cream']),
                       showticklabels=False
                       ),
            yaxis=dict(nticks=4, range=[-size, size], showbackground=False,
                       title_text='<b>Feral — Anthro</b>', title_font=dict(size=18, color=colors['desaturated_cream']),
                       tickvals=[-10, 10], ticktext=['', ''], tickfont=dict(color=colors['desaturated_cream']),
                       showticklabels=False
                       ),
            zaxis=dict(nticks=4, range=[-size, size], showbackground=False,
                       title_text='<b>Simple — Detailed</b>', title_font=dict(size=18, color=colors['desaturated_cream']),
                       tickvals=[-10, 10], ticktext=['', ''], tickfont=dict(color=colors['desaturated_cream']),
                       showticklabels=False
                       ),
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.5), projection=dict(type='perspective')),
            dragmode='orbit',
            bgcolor=colors['obsidian']
        ),
        annotations=[
            dict(
                text='Made by <a href="https://x.com/yeeniebeans" style="color:#9876B6; size=18"><b>YeenieBeans</b></a>',
                x=0.5, y=0.01,  # Adjusted to be slightly below the title
                xref='paper', yref='paper',
                showarrow=False,
                font=dict(size=14, color='#fafae9'),
                align='center'
            )
        ],
        width=1280,
        height=720,
        margin=dict(r=3, l=3, b=3, t=3),
        showlegend=False,
    )
    return fig

# Initialize the plot
plot = create_initial_plot()

# Streamlit App Setup
st.title("3D Artistic Alignment Plot")
st.markdown("""
Welcome to the 3D Artistic Alignment Plot! This tool helps you visualize where you and your friends align in a three-dimensional artistic space based on realism, ferality, and detail. Adjust the sliders to find your place in the style spectrum, and see how you compare to others!
""")

# SECTION ONE: Discover Your Artistic Alignment
st.header("Discover Your Artistic Alignment")
st.markdown("Use the sliders to determine your position on the style spectrum and see where you align in the 3D space.")

# User name and color input on one line
col1, col2 = st.columns([3, 1])
username = col1.text_input("Name", "")
user_color = col2.color_picker("Pick a color", value=colors['user_point'])

# Sliders on a new line
x_value = st.slider("Realistic — Cartoony", -10, 10, 0, format=" ",
                    help="Your level of realistic vs. cartoon style")
st.write(f"**Current Value:** {x_value}")

y_value = st.slider("Feral — Anthro", -10, 10, 0, format=" ",
                    help="Your level of feral vs. anthro style")
st.write(f"**Current Value:** {y_value}")

z_value = st.slider("Simple — Detailed", -10, 10, 0, format=" ",
                    help="Your level of simplicity vs. detail")
st.write(f"**Current Value:** {z_value}")

st.markdown("")

if st.button("Submit"):
    plot.add_trace(go.Scatter3d(
        x=[x_value], y=[y_value], z=[z_value],
        mode='markers+text',
        marker=dict(size=8, color=user_color),  # Use selected color
        text=[f"{username}"],
        textposition='top center',
        hoverinfo="none"
    ))
    st.write(f"Your alignment is ({x_value}, {y_value}, {z_value}).")

st.markdown("---")

# SECTION TWO: Add Your Friends
st.header("Add Your Friends")
st.markdown("Add your friends to the artistic style alignment plot.")

# Friend name and color input on one line
friend_col1, friend_col2 = st.columns([3, 1])
friend_name = friend_col1.text_input("Friend's Name")
friend_color = friend_col2.color_picker("Pick a color", value=colors['friend_point'])

# Friend axes inputs on a new line
friend_x = st.number_input("Realistic — Cartoony", value=0)
friend_y = st.number_input("Feral — Anthro", value=0)
friend_z = st.number_input("Simple — Detailed", value=0)

friend_data = st.empty()  # Placeholder for friend data

# Store friend data
if 'friends' not in st.session_state:
    st.session_state['friends'] = []

if st.button("Add Friend"):
    st.session_state['friends'].append((friend_name, friend_x, friend_y, friend_z, friend_color))
    # Display friend data as a list
    friend_data.write([f"{f[0]} ({f[1]}, {f[2]}, {f[3]})" for f in st.session_state['friends']])

    plot.add_trace(go.Scatter3d(
        x=[friend_x], y=[friend_y], z=[friend_z],
        mode='markers+text',
        marker=dict(size=6, color=friend_color),  # Use selected color
        text=[f"{friend_name}"],
        textposition='top center',
        hoverinfo="none"
    ))

# Display current friend data and allow removal by double-clicking
st.write("Current Friends:")
friend_box = st.multiselect("", [f"{f[0]} ({f[1]}, {f[2]}, {f[3]})" for f in st.session_state['friends']])

# Remove friend on double-click
for selected in friend_box:
    selected_name = selected.split(" ")[0]
    st.session_state['friends'] = [f for f in st.session_state['friends'] if f[0] != selected_name]
    # Redraw the plot without the removed friend's point
    plot = create_initial_plot()
    plot.add_trace(go.Scatter3d(
        x=[x_value], y=[y_value], z=[z_value],
        mode='markers+text',
        marker=dict(size=8, color=user_color),
        text=[f"{username}"],
        textposition='top center',
        hoverinfo="none"
    ))
    for friend in st.session_state['friends']:
        plot.add_trace(go.Scatter3d(
            x=[friend[1]], y=[friend[2]], z=[friend[3]],
            mode='markers+text',
            marker=dict(size=6, color=friend[4]),
            text=[f"{friend[0]}"],
            textposition='top center',
            hoverinfo="none"
        ))

st.markdown("---")

# SECTION THREE: Artistic Style Alignment
st.header("Artistic Style Alignment")
st.markdown("This is an interactive plot you can drag around! View options are in the upper-right corner.")
st.plotly_chart(plot, use_container_width=True)
