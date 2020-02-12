# The code is from https://www.geeksforgeeks.org/youtube-data-api-for-handling-videos-set-3/
# importing library
from apiclient.discovery import build

# Arguments that need to passed
# to the build function
DEVELOPER_KEY = "API_key"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# creating Youtube Resource Object
youtube_object = build(YOUTUBE_API_SERVICE_NAME,
                       YOUTUBE_API_VERSION,
                       developerKey=DEVELOPER_KEY)


def youtube_video_categories():

    # calling the videoCategory.list method
    # to retrieve youtube video categories result
    video_category = youtube_object.videoCategories(
    ).list(part='snippet', regionCode='IN').execute()

    # extracting the results
    # from video_category response
    results = video_category.get("items", [])

    # empty list to store video category metadata
    videos_categories = []

    # extracting required info
    # from each result object
    for result in results:

        # video_categories result object
        videos_categories.append("% s, (% s % s)"
                                 % (result["id"],
                                    result["snippet"]["title"],
                                     result["snippet"]["assignable"]))

    print("Video_Category_Id Catgeory_Name     Assignable :\n",
          "\n".join(videos_categories), "\n")


if __name__ == "__main__":
    youtube_video_categories()
