import pandas as pd
import selenium
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Create a new instance of the Chrome driver
driver = selenium.webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# List to video titles
video_titles = []

# List to video views
video_views = []

# List to video upload dates
video_upload_dates = []

# List to video links
video_links = []

# List to video descriptions
video_descriptions = []

# List to video channels
video_channels = []

# List to video channel links
video_channel_links = []

# List to video channel subscribers
video_channel_subscribers = []

# List to video channel upload dates
video_channel_upload_dates = []

# List to video likes
video_likes = []

# List to video dislikes
video_dislikes = []

# List to video comments
video_comments = []

# List to video tags
video_tags = []

# List to video duration
video_duration = []

# List to video category
video_category = []

# List to video category links
video_category_links = []

driver.get('https://youtu.be/A8MO7fkZc5o')

# Get the page source
page_source = driver.page_source

# Parse the page source
soup = BeautifulSoup(page_source, 'html.parser')

# Get the video titles
titles = soup.find_all('a', {'id': 'video-title'})

# Get the video views
views = soup.find_all('span', {'class': 'style-scope ytd-grid-video-renderer'})

# Get the video upload dates
upload_dates = soup.find_all('span', {'class': 'style-scope ytd-grid-video-renderer'})

# Get the video links
links = soup.find_all('a', {'id': 'video-title'})

# Get the video descriptions
descriptions = soup.find_all('yt-formatted-string', {'id': 'description-text'})

# Get the video channels
channels = soup.find_all('a', {'id': 'channel-name'})

# Get the video channel links
channel_links = soup.find_all('a', {'id': 'channel-name'})

# Get the video channel subscribers
channel_subscribers = soup.find_all('yt-formatted-string', {'id': 'owner-sub-count'})

# Get the video channel upload dates
channel_upload_dates = soup.find_all('yt-formatted-string', {'id': 'text'})

# Get the video likes
likes = soup.find_all('yt-formatted-string', {'id': 'text'})

# Get the video dislikes
dislikes = soup.find_all('yt-formatted-string', {'id': 'text'})

# Get the video comments
comments = soup.find_all('yt-formatted-string', {'id': 'text'})

# Get the video tags
tags = soup.find_all('yt-formatted-string', {'id': 'text'})

# Get the video duration
duration = soup.find_all('span', {'class': 'style-scope ytd-thumbnail-overlay-time-status-renderer'})

# Get the video category
category = soup.find_all('a', {'id': 'text'})

# Get the video category links
category_links = soup.find_all('a', {'id': 'text'})

# Get the video titles
for title in titles:
    video_titles.append(title.text)

# Get the video views
for view in views:
    video_views.append(view.text)

# Get the video upload dates
for upload_date in upload_dates:
    video_upload_dates.append(upload_date.text)

# Get the video links
for link in links:
    video_links.append('https://www.youtube.com' + link.get('href'))

# Get the video descriptions
for description in descriptions:
    video_descriptions.append(description.text)

# Get the video channels
for channel in channels:
    video_channels.append(channel.text)

# Get the video channel links
for channel_link in channel_links:
    video_channel_links.append('https://www.youtube.com' + channel_link.get('href'))

# Get the video channel subscribers
for channel_subscriber in channel_subscribers:
    video_channel_subscribers.append(channel_subscriber.text)

# Get the video channel upload dates
for channel_upload_date in channel_upload_dates:
    video_channel_upload_dates.append(channel_upload_date.text)

# Get the video likes
for like in likes:
    video_likes.append(like.text)

# Get the video dislikes
for dislike in dislikes:
    video_dislikes.append(dislike.text)

# Get the video comments
for comment in comments:
    video_comments.append(comment.text)

# Get the video tags
for tag in tags:
    video_tags.append(tag.text)

# Get the video duration
for time in duration:
    video_duration.append(time.text)

# Get the video category
for cat in category:
    video_category.append(cat.text)

# Get the video category links
for cat_link in category_links:
    video_category_links.append('https://www.youtube.com' + cat_link.get('href'))

a = {'Video Title': video_titles, 'Video Views': video_views, 'Video Upload Date': video_upload_dates, 'Video Link': video_links, 'Video Description': video_descriptions, 'Video Channel': video_channels, 'Video Channel Link': video_channel_links, 'Video Channel Subscribers': video_channel_subscribers, 'Video Channel Upload Date': video_channel_upload_dates, 'Video Likes': video_likes, 'Video Dislikes': video_dislikes, 'Video Comments': video_comments, 'Video Tags': video_tags, 'Video Duration': video_duration, 'Video Category': video_category, 'Video Category Link': video_category_links}

# Create a dataframe
df = pd.DataFrame.from_dict(a, orient='index')

# Save the dataframe to a csv file
df.to_csv('youtube.csv', index=False)

# Close the driver
driver.close()

# Print the dataframe
print(df)

# Print the number of rows and columns
print(df.shape)

# Print the number of rows
print(df.shape[0])

# Print the number of columns
print(df.shape[1])

# Print the column names
print(df.columns)

# Print the column names
for column in df.columns:
    print(column)
