from flask import Flask, render_template, request, session
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import folium

from reference_table import obd_ii_codes


app = Flask(__name__)
app.secret_key = 'secret_key'


# Load the data into a pandas DataFrame
df = pd.read_csv("https://apmonitor.com/pds/uploads/Main/auto_iowa.txt")
df.dropna(how='all', inplace=True)
plt.switch_backend('Agg')

@app.route("/", methods=['GET', 'POST'])
def index():

    # Check if "Time (sec)" or "time" column exists
    if "Time (sec)" in df.columns:
        x_col = "Time (sec)"
    elif "time" in df.columns:
        x_col = "time"
    else:
        x_col = None

    # Get the number of columns in the DataFrame
    n_cols = len(df.columns) - 1

    if 'counter' not in session:
        session['counter'] = 0
    counter = session['counter']

    if request.method == 'POST':
        if request.form.get('action1') == 'PREVIOUS':
            session['counter'] = max(0, counter - 1)
        elif request.form.get('action2') == 'NEXT':
            session['counter'] = min(n_cols - 1, counter + 1)
        counter = session['counter']

    # Create the plot
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 6))
    if x_col is not None:
        ax.plot(df[x_col], df[df.columns[counter + 1]], label=df.columns[counter + 1])
        ax.set_title(df.columns[counter + 1])
    else:
        # plot with respect to n'th row if there is no time in the graph
        ax.plot(df.index, df[df.columns[counter + 1]], label=df.columns[counter + 1])
        ax.set_title(df.columns[counter + 1] + " (Index)")

    # Save the plot to a buffer
    buf = io.BytesIO()
    plt.savefig(buf, format="png")

    # Encode the buffer to base64
    image_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")


    # Display the PID and description of the plot
    if df.columns[counter + 1] in obd_ii_codes:
        pid = obd_ii_codes[df.columns[counter + 1]]['PID']
        description = obd_ii_codes[df.columns[counter + 1]]['Description:']
    else:
        pid = None
        description = None

    return render_template("index.html", image_base64=image_base64, pid=pid, description=description)

@app.route("/map")
def show_map():
    

    if " Latitude (deg)" in df.columns and " Longitude (deg)" in df.columns:
        y_axis = " Latitude (deg)"
        x_axis = " Longitude (deg)"
    elif "Latitude" in df.columns and "Longitude" in df.columns:
        y_axis = "Latitude"
        x_axis = "Longitude"
    elif "latitude" in df.columns and "longitude" in df.columns:
        y_axis = "latitude"
        x_axis = "longitude"
    else:
        error = "Error: Latitude or longitude does not exist in the dataset."
        return render_template("map.html", error=error)
            


    # Create a map centered on the mean latitude and longitude of the data
    mean_lat = df[y_axis].mean()
    mean_lon = df[x_axis].mean()
    map = folium.Map(location=[mean_lat, mean_lon], zoom_start=12)

    # Plot each lat-lon pair as a point on the map
    for lat, lon in zip(df[y_axis], df[x_axis]):
        folium.CircleMarker(location=[lat, lon], radius=2).add_to(map)

    # Save the map html
    map_html = map.get_root().render()

    return render_template("map.html", map_html=map_html)


@app.route("/about")
def show_about():

    return render_template("about.html")


if __name__ == "__main__":
    app.run(port=5001)
