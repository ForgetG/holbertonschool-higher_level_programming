#!/usr/bin/python3
"""Module task_02_requests"""
import requests
import csv


def fetch_and_print_posts():
    """Fetches and prints all posts from JSON Placeholder
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {r.status_code}")

    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """Fetches and saves all posts from a JSON placeholder
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')

    if r.status_code == 200:
        posts = r.json()
        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for post in posts:
                writer.writerow({'id': post['id'], 'title': post['title'],
                                 'body': post['body']})
