#!/usr/bin/env python3
"""
Wayback Machine Checker
Checks if URLs are archived in the Wayback Machine
Usage: cat urls.txt | python3 wayback_checker.py
       or: echo "https://example.com" | python3 wayback_checker.py
"""

import sys
import requests
import json
from urllib.parse import quote
import time
from datetime import datetime

class WaybackChecker:
    def __init__(self):
        self.base_url = "https://archive.org/wayback/available"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def check_url(self, url):
        """Check if a URL is available in the Wayback Machine"""
        try:
            params = {'url': url}
            response = self.session.get(self.base_url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                archived_snapshots = data.get('archived_snapshots', {})
                closest = archived_snapshots.get('closest', {})
                
                if closest and closest.get('available'):
                    return {
                        'url': url,
                        'available': True,
                        'archived_url': closest.get('url'),
                        'timestamp': closest.get('timestamp'),
                        'status': closest.get('status')
                    }
                else:
                    return {
                        'url': url,
                        'available': False,
                        'archived_url': None,
                        'timestamp': None,
                        'status': None
                    }
            else:
                return {
                    'url': url,
                    'available': False,
                    'error': f'HTTP {response.status_code}'
                }
        except requests.exceptions.RequestException as e:
            return {
                'url': url,
                'available': False,
                'error': str(e)
            }
    
    def format_timestamp(self, timestamp):
        """Format timestamp to readable date"""
        if not timestamp:
            return "N/A"
        try:
            dt = datetime.strptime(timestamp, "%Y%m%d%H%M%S")
            return dt.strftime("%Y-%m-%d %H:%M:%S")
        except:
            return timestamp
    
    def print_result(self, result):
        """Print formatted result"""
        url = result['url']
        if result['available']:
            archived_url = result['archived_url']
            timestamp = self.format_timestamp(result['timestamp'])
            status = result.get('status', 'Unknown')
            
            print(f"✓ ARCHIVED: {url}")
            print(f"  └─ Archive URL: {archived_url}")
            print(f"  └─ Archived on: {timestamp}")
            print(f"  └─ Status: {status}")
            print()
        else:
            error = result.get('error', 'Not archived')
            print(f"✗ NOT FOUND: {url}")
            print(f"  └─ Reason: {error}")
            print()

def main():
    if sys.stdin.isatty():
        print("Usage: cat urls.txt | python3 wayback_checker.py")
        print("       or: echo 'https://example.com' | python3 wayback_checker.py")
        sys.exit(1)
    
    checker = WaybackChecker()
    
    print("🔍 Checking URLs in Wayback Machine...")
    print("=" * 60)
    
    total_urls = 0
    archived_count = 0
    
    try:
        for line in sys.stdin:
            url = line.strip()
            if url and url.startswith(('http://', 'https://')):
                total_urls += 1
                result = checker.check_url(url)
                checker.print_result(result)
                
                if result['available']:
                    archived_count += 1
                
                # Small delay to be respectful to the API
                time.sleep(0.5)
    
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        sys.exit(0)
    
    print("=" * 60)
    print(f"📊 Summary: {archived_count}/{total_urls} URLs found in Wayback Machine")
    
    if archived_count > 0:
        print(f"\n💡 Tip: You can visit the archived URLs directly in your browser!")

if __name__ == "__main__":
    main() 
