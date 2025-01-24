# NextSpaceFlight Next Launch Scraper

**NSF Next Launch Scraper** is a Python package designed to scrape and export the latest upcoming space launch data from [Next Spaceflight](https://nextspaceflight.com/). It supports exporting data **locally** or to an **AWS S3 bucket**, making it flexible for various use cases.

---

## Features

- Scrapes detailed information about the next space launch:
  - Date, Organization, Rocket, Mission Details, and more.
- Supports **local export** *(JSON file)* and **AWS S3 integration**.
- Easily configurable via environment variables (`ENV`).

---

## Installation

Clone the repository and install the package:

```bash
pip install git+https://github.com/Tanguy9862/Next-Launch-Scraper.git
```

---

## Usage

### 1. Setup Configuration
Create a `.env` file in the directory where you’ll run the scraper. Specify the environment:

- `ENV=local` (default): Export to a local JSON file.
- `ENV=aws`: Export to an S3 bucket (requires proper IAM permissions).

Example `.env`:

```bash
ENV=local
```

### 2. Run the Scraper
Import and call the main function:

```python
from next_launch_scraper.scraper import scrape_next_launch_data

scrape_next_launch_data()
```

- **Local Mode**: Exports data to a `data/` folder in the current directory.
- **AWS Mode**: Uploads the data to your specified S3 bucket (requires IAM setup).

### 3. Example Integration
This scraper can be seamlessly integrated into pipelines. See [Space-App](https://github.com/Tanguy9862/Space-App) for a practical example:
- A Lambda function calls this scraper to update data in an S3 bucket.
- The [Space-App](https://github.com/Tanguy9862/Space-App) consumes the data for visualization.

---

## AWS Integration

If using `ENV=aws`, ensure:
1. Your AWS credentials are configured in your environment or via `.aws/credentials`.
2. The Lambda function or local user has appropriate permissions:
   - `s3:PutObject`
   - `s3:GetObject`

