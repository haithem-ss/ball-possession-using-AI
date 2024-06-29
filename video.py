from IPython.display import HTML
from base64 import b64encode

def display_video(file_path):
    # Read video file
    with open(file_path, "rb") as file:
        video_encoded = b64encode(file.read()).decode("utf-8")

    video_tag = f"""<video controls>
                        <source src="data:video/mp4;base64,{video_encoded}" type="video/mp4">
                    </video>"""

    # Display video
    return HTML(video_tag)
