from icrawler.builtin import GoogleImageCrawler

base_dir = "images"

def download_images(keyword: str, num: int = 10, dir: str = "images") -> str:
    """
    Function for downloading images from Google using icrawler.

    Parameters:
    keyword (str): what are you search.
    num (int): number of photos you want download.
    dir (str): directory to save.

    Returns:
    str: path to directory where files save.
    """

    root_dir = f"{base_dir}\\{dir}"
    google_crawler = GoogleImageCrawler(
        storage={"root_dir": root_dir},
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=4
    )

    google_crawler.crawl(keyword=keyword, max_num=num)

    return root_dir