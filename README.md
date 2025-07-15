# Wayback Machine Checker

A Python tool that checks if URLs are archived in the Wayback Machine. Perfect for checking if discovered files from reconnaissance are still accessible in archived form.

## Features

- ✅ Accepts URLs via pipe input
- ✅ Checks Wayback Machine availability
- ✅ Shows archive dates and direct links
- ✅ Colorful output with summary statistics
- ✅ Respectful API usage with delays

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Make the script executable (already done):
```bash
chmod +x wayback_checker.py
```

## Usage

### Basic usage with your discovered files:

```bash
cat subdomains.httpx.gau.httpx.404 | grep -E '\.xls|\.xml|\.xlsx|\.json|\.pdf|\.sql|\.doc|\.docx|\.pptx|\.txt|\.zip|\.tar\.gz|\.tgz|\.bak|\.7z|\.rar|\.log|\.cache|\.secret|\.db|\.backup|\.yml|\.gz|\.config|\.csv|\.yaml|\.md|\.md5|\.exe|\.dll|\.bin|\.ini|\.bat|\.sh|\.tar|\.deb|\.rpm|\.iso|\.img|\.apk|\.msi|\.dmg|\.tmp|\.crt|\.pem|\.key|\.pub|\.asc' | python3 wayback_checker.py
```

### Or with a simple file list:

```bash
echo "https://example.com/ads.txt" | python3 wayback_checker.py
```

```bash
cat urls.txt | python3 wayback_checker.py
```

## Output Example

```
🔍 Checking URLs in Wayback Machine...
============================================================
✓ ARCHIVED: https://example.com/ads.txt
  └─ Archive URL: https://web.archive.org/web/20231201123456/https://example.com/ads.txt
  └─ Archived on: 2023-12-01 12:34:56
  └─ Status: 200

✗ NOT FOUND: https://example.com/nonexistent.pdf
  └─ Reason: Not archived

============================================================
📊 Summary: 1/2 URLs found in Wayback Machine

💡 Tip: You can visit the archived URLs directly in your browser!
```

## What it checks

The tool uses the Wayback Machine API to check if URLs are archived and provides:
- ✅ Whether the URL is archived
- 📅 When it was archived
- 🔗 Direct link to archived version
- 📊 HTTP status code of archived page

## Tips

1. **Use with grep**: Filter for specific file types as shown in the examples
2. **Rate limiting**: The tool includes a 0.5-second delay between requests to be respectful to the API
3. **Interruption**: Press Ctrl+C to stop the tool at any time
4. **Large lists**: The tool works well with large lists of URLs

## File Types Supported

Works with any URL, but particularly useful for checking archived versions of:
- Documents: `.pdf`, `.doc`, `.docx`, `.pptx`, `.txt`
- Data files: `.json`, `.xml`, `.csv`, `.sql`, `.db`
- Archives: `.zip`, `.tar.gz`, `.7z`, `.rar`
- Configuration: `.yml`, `.yaml`, `.config`, `.ini`
- Security files: `.key`, `.pem`, `.crt`
- And many more! 
