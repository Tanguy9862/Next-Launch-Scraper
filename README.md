# Next-Launch-Scraper

## Overview

This Python package is designed to scrape real-time and upcoming space launch data. It is part of a larger project, [Space-App](https://github.com/Tanguy9862/Space-App), which visualizes various aspects of space exploration.

## Features

- **Real-Time Data**: Scrapes data about the next upcoming space launch, including the launch vehicle, launch site, mission details, live video, timing, etc.
- **Detailed Information**: Provides comprehensive data such as the launch organization, rocket type, mission objectives, and cost.
- **Data Transformation**: Transforms the scraped data into a JSON format for easy consumption.
- **Error Handling**: Robust error handling to ensure data integrity.
- **Logging**: Detailed logging for debugging and monitoring.

## Installation

To install this package, run:

```bash
pip install git+https://github.com/Tanguy9862/Next-Launch-Scraper.git
```

## Usage

After installation, you can import the package and use the `scrape_next_launch_data()` function to scrape the data.

```python
from next_launch_scraper import scraper

# Scrape next launch data
scraper.scrape_next_launch_data()
```

## Dependencies

- Python 3.x
- BeautifulSoup
- Requests
- Pandas

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Related Projects

- [Space-App](https://github.com/Tanguy9862/Space-App)
- [Wikipedia_Space_Scraper](https://github.com/Tanguy9862/Wikipedia_Space_Scraper)
- [NextSpaceFlight-Scrapper](https://github.com/Tanguy9862/NextSpaceFlight-Scrapper)
