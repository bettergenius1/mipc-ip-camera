from flask import Flask, jsonify
from mipc_camera_client import MipcCameraClient

app = Flask(__name__)

# Camera credentials
camera_ip = "192.168.X.XXX" # IP Address inbetween ""  i.e. 192.168.1.123 or 10.0.0.1 etc
camera_user = "XXXXXXXXXXXXX" # Username inbetween  "" i.e. MyUserName
camera_password = "XXXXXXXX" # Password inbetween ""  i.e. "Password"

def get_rtmp_url():
    """Fetch the latest RTMP stream URL from the camera."""
    c = MipcCameraClient(camera_ip)
    c.login(camera_user, camera_password)
    return c.get_rtmp_stream()

@app.route('/get_rtmp', methods=['GET'])
def get_rtmp():
    """Provide the latest RTMP URL in JSON format."""
    try:
        rtmp_url = get_rtmp_url()
        return jsonify({"rtmp_url": rtmp_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
