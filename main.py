import os

from icrawler.builtin import GoogleImageCrawler


def crawl_images(key, dir, max_num):
    google_crawler = GoogleImageCrawler(
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=4,
        storage={'root_dir': dir})

    google_crawler.crawl(keyword=key, language='vi', max_num=max_num, file_idx_offset='auto')


if __name__ == '__main__':
    normal_dir = './normal'
    malicious_dir = './malicious'

    if not os.path.exists(normal_dir):
        os.mkdir(normal_dir)

    if not os.path.exists(malicious_dir):
        os.mkdir(malicious_dir)

    max_count = 100

    normal_keys = [
        'học sinh',
        'giáo dục',
        'trường học',
        'gia đình',
        'dã ngoại',
        'đi chơi',
        'từ thiện',
        'nội trợ',
        'hội thảo',
    ]

    malicious_keys = [
        'máu me',
        'kinh dị',
        'hủy hoại bản thân',
        'hành hạ',
        'sex',
        'sexy',
        'ảnh nhạy cảm',
        'tai nạn giao thông',
        'đánh nhau',
        'giang hồ',
    ]

    max_count_per_key = max_count // len(normal_keys)
    for key in normal_keys:
        crawl_images(key, normal_dir, max_count_per_key)

    max_count_per_key = max_count // len(malicious_keys)
    for key in malicious_keys:
        crawl_images(key, malicious_dir, max_count_per_key)
