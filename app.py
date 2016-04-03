from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)

@app.route("/call", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
    # resp.say("Dial VG. Press 5 to shoot and 9 to jump. Press two, four, six or eight to move. 3 is start.")
 
    # Say a command, and listen for the caller to press a key. When they press
    # a key, redirect them to /handle-key.
    resp.gather(numDigits=1, action="/handle-key", method="POST", timeout=1000)
    return str(resp)


@app.route("/handle-key", methods=['GET', 'POST'])
def handle_key():
    """Handle key press from a user."""
 
    # Get the digit pressed by the user
    digit_pressed = request.values.get('Digits', None)

    if digit_pressed == "1":
        with open('button.txt', 'w') as f:
            f.write("S")

    if digit_pressed == "9":
        with open('button.txt', 'w') as f:
            f.write("A")

    if digit_pressed == "2":
        with open('button.txt', 'w') as f:
            f.write("up")

    if digit_pressed == "4":
        with open('button.txt', 'w') as f:
            f.write("left")

    if digit_pressed == "6":
        with open('button.txt', 'w') as f:
            f.write("right")

    if digit_pressed == "8":
        with open('button.txt', 'w') as f:
            f.write("down")

    if digit_pressed == "3":
        with open('button.txt', 'w') as f:
            f.write("start")

    if digit_pressed == "5":
        with open('button.txt', 'w') as f:
            f.write("B")

    return redirect("/call")

 
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0') # open to anyone
