from bs4 import BeautifulSoup
import json
import logging
import re
import requests

PATH_TO_EXPORT = 'data'
DATA_FILENAME = "next_launch_data.json"
SCRIPT_NAME = 'Next_Launch_Scraper'

logging.basicConfig(level=logging.INFO)


def scrape_next_launch_data():

    logging.info(f'{SCRIPT_NAME} - Searching for upcoming launch data..')

    def make_soup(url):
        response = requests.get(url)
        return BeautifulSoup(response.text, 'html.parser')

    # MAIN PAGE:
    card = make_soup('https://nextspaceflight.com/launches/?search=').select_one('div.mdl-cell')  # UPCOMING
    # card = make_soup('https://nextspaceflight.com/launches/past/?search=').select_one('div.mdl-cell')  # PAST
    next_launch_data = []

    organisation = card.select_one('span').text.strip()
    rocket = card.select_one('h5').text.strip()
    date = card.select_one('span[id^="localized"]').text

    default_image_link = 'https://storage.googleapis.com/nextspaceflight/media/rockets/default.jpg'
    regex_image_link = re.search(r'url\((.*)\)', card.select_one('style').text).group(1)
    image_link = regex_image_link if regex_image_link != default_image_link else None

    details_link = card.find_all('button')[0].get('onclick').split("'")[1]
    try:
        video_link = re.search(r"'(https://?\S+)'", card.find_all('button')[1].get('onclick')).group(1)
    except (IndexError, AttributeError):
        video_link = None

    # DETAILS PAGE:
    details = make_soup(url=f'https://nextspaceflight.com{details_link}')

    # GET MISSION DETAIL
    all_h3 = details.find_all('h3', class_='section--center mdl-grid title')
    for title in all_h3:
        if 'Mission Details' in title:
            all_paragraphs = title.find_all_next('div', class_='mdl-grid a')
            for paragraph in all_paragraphs:
                if paragraph.find_all_next('p'):
                    mission_detail = ''.join([block.string for block in paragraph.find_all('p')])
                    break
            break
    else:
        mission_detail = None

    # GET PRICE
    all_mdl_cell = details.find_all('div', class_='mdl-cell mdl-cell--6-col-desktop mdl-cell--12-col-tablet')

    for cell in all_mdl_cell:
        match = re.search(r'Price: \$(\d+\.\d+)', cell.string)
        if match:
            price = match.group(1)
            break
    else:
        price = None

    # GET NUMBER MISSION TOTAL AND NUMBER MISSION YEAR
    main_break = False
    for title in all_h3:
        if 'Stats' in title:
            subtitles_stat = title.find_all_next('h4', class_='mdl-card__title-text')
            if subtitles_stat:
                for subtitle in subtitles_stat:
                    if organisation in subtitle:
                        all_desc_stats = subtitle.find_all_next('div',
                                                                class_='mdl-cell mdl-cell--4-col-desktop mdl-cell--10-col-tablet')
                        if len(all_desc_stats) >= 2:
                            regex = r'(\d+)(?:th|st|nd|rd)'
                            total_mission, total_mission_year = (
                                re.match(regex, all_desc_stats[0].text) and re.match(regex, all_desc_stats[0].text).group(1),
                                re.match(regex, all_desc_stats[1].text) and re.match(regex, all_desc_stats[1].text).group(1),
                            )
                            main_break = True
                            break
            if main_break:
                break
    else:
        total_mission, total_mission_year = None, None

    # EXPORT DATA:
    next_launch_data.append(
        {
            'NEXT LAUNCH': date,
            'ORGANISATION': organisation,
            'ROCKET': rocket,
            'IMAGE': image_link,
            'VIDEO': video_link,
            'MISSION DETAIL': mission_detail,
            'PRICE': price,
            'TOTAL MISSION': total_mission,
            'TOTAL MISSION YEAR': total_mission_year
        }
    )
    # with open(fr'{PATH_TO_EXPORT}/{DATA_FILENAME}', 'w', encoding='utf-8') as json_file:
    #     json.dump(next_launch_data, json_file, ensure_ascii=False, indent=4)

    logging.info(f'{SCRIPT_NAME} - {DATA_FILENAME} updated!')

    return next_launch_data
