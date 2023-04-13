import requests
import os

api_key = os.environ['GOOGLE_CUSTOM_SEARCH_API_KEY']
search_engine_id = os.environ['GOOGLE_CUSTOM_SEARCH_ENGINE_ID']
QUERY = "Dog"

# response = requests.get(f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={QUERY}&searchType=image&num=10", timeout=10)

# data = response.json()
# for x, item in enumerate(data['items']):
#     # print(item['link'])
#     response = requests.get(item['link'])
#     with open("Dog" + str(x) + ".jpg", "wb") as f:
#         f.write(response.content)

# import requests

# API_KEY = "YOUR_API_KEY"
# SEARCH_ENGINE_ID = "YOUR_SEARCH_ENGINE_ID"
# QUERY = "YOUR_QUERY"
NUM_PER_REQUEST = 10
NUM_REQUESTS = 100
SAVE_DIR = "images"

def download_images():
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

    total = 0
    for i in range(NUM_REQUESTS):
        print(f"Downloading images {total+1}-{total+NUM_PER_REQUEST}")
        response = requests.get(f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={QUERY}&searchType=image&num={NUM_PER_REQUEST}&start={i*NUM_PER_REQUEST+1}")
        data = response.json()

        for j, item in enumerate(data['items']):
            try:
                response = requests.get(item['link'], timeout=10)
                content_type = response.headers.get('Content-Type')
                if "image" not in content_type:
                    print(f"Skipping non-image {item['link']}")
                    continue

                with open(f"{SAVE_DIR}/{total+j+1}.jpg", "wb") as f:
                    f.write(response.content)
            except:
                print(f"Failed to download {item['link']}")

        total += NUM_PER_REQUEST
        if total >= 1000:
            break

if __name__ == '__main__':
    download_images()