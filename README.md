# Asyncio API Fetcher

## Project Overview
This program uses `asyncio` and `aiohttp` to fetch data from multiple API sources asynchronously and save the results to a `results.json` file. It demonstrates how `asyncio` can efficiently handle multiple requests simultaneously.

## How to Use

### Install Required Libraries
```sh
pip install aiohttp
```

### Run the Program
```sh
python main.py
```

## How It Works
1. The program creates a `ClientSession` to use `aiohttp` for fetching data from predefined URLs.
2. It utilizes `asyncio.gather()` to execute multiple requests concurrently.
3. The results are saved to `results.json`.
4. The total execution time is displayed to highlight the efficiency of asynchronous programming.

## Expected Outcome
- Fetching data concurrently is significantly faster than synchronous requests.
- Demonstrates how `asyncio` effectively manages I/O-bound tasks.

This project provides a simple yet effective way to understand asynchronous programming in Python! 🚀

