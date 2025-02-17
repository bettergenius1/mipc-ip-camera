camera_ip = "192.168.1.197"
camera_user = "1jfiegbqo356a"
camera_password = "turbo54"

from mipc_camera_client import MipcCameraClient

# Initialize the camera client
c = MipcCameraClient(camera_ip)
c.login(camera_user, camera_password)

# Get the RTMP stream URL
stream_url = c.get_rtmp_stream()
print("RTMP Stream URL:", stream_url)
