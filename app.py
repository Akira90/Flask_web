from flask import Flask, render_template, request
import pytube

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email == "nhassim01@gmail.com" and password == "nas":
            return render_template('hex_sit.html')

        elif email == "marwan@gmail.com" and password == "marwan":
            return render_template('success.html')
        else:
            error_message = "Invalid email or password. Please try again."
            return render_template('login.html', error=error_message)
    else:
        return render_template('login.html')

@app.route('/download', methods=['GET', 'POST'])
def download():
    if request.method == 'POST':
        url = request.form['url']
        try:
            # Use PyTube to get the video stream
            yt = pytube.YouTube(url)
            stream = yt.streams.filter(progressive=True).first()
            stream.download()
            download_message = f"Video downloaded successfully! Check your downloads folder."
            return render_template('download.html', message=download_message)
        except Exception as e:
            error_message = f"Error downloading video: {e}"
            return render_template('download.html', error=error_message)
    else:
        return render_template('download.html')

if __name__ == '__main__':
    app.run(debug=True)
