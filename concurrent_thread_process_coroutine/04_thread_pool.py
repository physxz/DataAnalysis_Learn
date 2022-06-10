import concurrent.futures
import blog_spider

# craw
with concurrent.futures.ThreadPoolExecutor() as pool: # 线程池个数未设定时默认是max_workers = min(32, (os.cpu_count() or 1) + 4)
    htmls = pool.map(blog_spider.craw, blog_spider.urls)
    htmls = list(zip(blog_spider.urls, htmls))
    for url, html in htmls:
        print(url, len(html))

print('craw over')

# parse

with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = {}
    for url, html in htmls:
        future = pool.submit(blog_spider.parse, html)
        futures[future] = url

    # for future, url in futures.items():
    #     print(url, future.result())

    for future in concurrent.futures.as_completed(futures):
        url = futures[future]
        print(url, future.result())