from flask import Flask, send_file
import matplotlib.pyplot as plt
import io
import time
app = Flask(__name__)
@app.route('/')
def home():
    return """
    <h1>Docker Data Dashboard</h1>
    <p>This page is being served from inside a Docker container!</p>
    <img src="/plot.png" alt="Random Trend">
    <p><a href="/plot.png">Refresh Plot</a></p>
    """
@app.route('/plot.png')
def plot_png():
    # Generate a random plot
    plt.figure(figsize=(5,4))
    plt.plot([1,2,3,4],[1,4,9,16], 'r-o')
    plt.title("Sample Trend (Generated in container)")

    # Save plot to buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    # Listen on all interfaces (0.0.0.0) so we can access it from outside
    app.run(host='0.0.0.0',port=5000)
