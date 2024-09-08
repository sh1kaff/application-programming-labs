from icrawler.builtin import GoogleImageCrawler

base_dir = "images"

def download_images(keyword, num=10, dir="images"):
    root_dir = f"{base_dir}\\{dir}"
    google_crawler = GoogleImageCrawler(
        storage={"root_dir": root_dir},
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=4
    )

    google_crawler.crawl(keyword=keyword, max_num=num)

    return root_dir

if __name__ == "__main__":
    download_images("snake2")