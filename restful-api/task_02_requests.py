import requests
import csv

# Function to fetch and print posts
def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
        print("Failed to retrieve data.")

# Function to fetch and save posts to a CSV file
def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        # Extract relevant data: id, title, body
        data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

        # Write data to CSV
        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(data)
        print("Posts saved to posts.csv.")
    else:
        print("Failed to retrieve data.")
