camera_ip = "192.168.X.XXX" # IP Address inbetween ""  i.e. 192.168.1.123 or 10.0.0.1 etc
camera_user = "XXXXXXXXXXXXX" # Username inbetween  "" i.e. MyUserName
camera_password = "XXXXXXXX" # Password inbetween ""  i.e. "Password"

from mipc_camera_client import MipcCameraClient

# Initialize the camera client
c = MipcCameraClient(camera_ip)
c.login(camera_user, camera_password)

# Get the RTMP stream URL
stream_url = c.get_rtmp_stream()
print("RTMP Stream URL:", stream_url)
