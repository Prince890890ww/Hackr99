from flask import Flask, request, render_template
import requests

app = Flask(__name__)

def get_profile_name(access_token):
    url = "https://graph.facebook.com/me"
    params = {'access_token': access_token}
    response = requests.get(url, params=params)
    data = response.json()
    if 'name' in data:
        return data['name']
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    profile_name = None
    error_message = None

    if request.method == 'POST':
        access_token = request.form['access_token']
        profile_name = get_profile_name(access_token)
        if profile_name is None:
            error_message = "Invalid access token. Please try again."

    return render_template('index.html', profile_name=profile_name, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)

<div class="container">
    <h1>Facebook Token Checker</h1>
    <form method="post">
        <input type="text" name="access_token" placeholder="Input_Token" style="border: 2px solid white; padding: 6px;" required="Input_Token">
        <br />
        <button  class="btn"type="submit">CHECK TOKEN</button>
    </form>
    
    {% if error_message %}
        <p class="error">{{ error_message }}</p>
    {% elif profile_name %}
        <p>Your Profile Name: {{ profile_name }}</p>
    {% endif %}
    
    <footer>
        <h2>MAKE BY ARYAN</h2>
    </footer>
</div>




        <!-- Add more random images and links here as needed -->
    </div>

    <footer class="footer">
        


    </footer>
</body>
</html>
