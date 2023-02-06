from flask import Flask, render_template, request, session
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route("/", methods=['GET', 'POST'])
def index():
    # Load the data into a pandas DataFrame
    df = pd.read_csv("https://apmonitor.com/pds/uploads/Main/auto_iowa.txt")
    df.dropna(how='all', inplace=True)
    plt.switch_backend('Agg') 

    # Check if "Time (sec)" column exists
    if "Time (sec)" in df.columns:
        time_col = "Time (sec)"
    elif "time" in df.columns:
        time_col = "time"
    else:
        raise ValueError("Neither 'Time (sec)' nor 'time' column exists")

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
    ax.plot(df[time_col], df[df.columns[counter + 1]], label=df.columns[counter + 1])
    ax.set_title(df.columns[counter + 1])

    # Save the plot to a buffer
    buf = io.BytesIO()
    plt.savefig(buf, format="png")

    # Encode the buffer to base64
    image_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")

    return render_template("index.html", image_base64=image_base64)

if __name__ == "__main__":
    app.run(port=5001)
