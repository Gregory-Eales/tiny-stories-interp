import plotly.graph_objects as go

def draw_rectangles(h, l, colors, img_num=0, title=''):
    # Initialize the figure
    fig = go.Figure()

    # Add title
    fig.update_layout(title_text=title)

    # set background black
    fig.update_layout(
        plot_bgcolor='black',
        paper_bgcolor='black',
    )

    # make text white
    fig.update_layout(font=dict(color='white'))

    mult_factor = 0.75

    # Assuming each rectangle has a width and height of 1 for simplicity
    for i in range(h):
        for j in range(l):
            # Calculate the positions of the current rectangle
            x0, y0 = mult_factor*j+(0.01) + 1, mult_factor*i+(0.01) + 2# bottom left corner
            x1, y1 = mult_factor*j+0.2 + 1, mult_factor*i+0.2 + 2# top right corner
            
            # make color value int 1-255 for RGB
            color = int(colors[j][i])
            # Add the rectangle to the figure
            fig.add_shape(type="rect",
                          x0=x0, y0=y0, x1=x1, y1=y1,
                          line=dict(color=f"rgb({255},{255},{255})", width=0.1),
                          fillcolor=f"rgb({color},{color},{color})"
                          )

    # Adjust the axes to fit the rectangles
    fig.update_xaxes(range=[0, l], showgrid=False)
    fig.update_yaxes(range=[0, h], showgrid=False)

    # save imaage in img folder
    fig.write_image("img/rectangles_{}.png".format(img_num))

# # Example usage
# h = 16  # Number of rectangles vertically
# l = 8  # Number of rectangles horizontally
# draw_rectangles(h, l, [[255 for _ in range(h)] for _ in range(l)])