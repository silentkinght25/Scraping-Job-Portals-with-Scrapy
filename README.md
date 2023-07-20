# Scraping-Job-Portals-with-Scrapy
<br>
Scarped simplyhired.com, foundit.com and hirist.com<br>

<ol>
  <li><strong>Hirist.com: </strong> Hirist uses api for job listing. Api scraped using scrapy more than 17,000 jobs scraped in           various categories. Start url consist of list of categories scraped.
  </li>
  <li><strong>Simplyhired.com: </strong> Scraped very few categories. Basically this websites has a limit on the request to             protect its content from scrapping. To handle the 429 status code (Too Many Requests) and avoid hitting the websites too                   frequently, I have used some of the methods they are listed below:<br>
      <ul>
        <li><strong>Rotate User Agents: </strong> Instead of randomly selecting a user-agent for each request, I have rotated the user-                  agent after a certain number of requests(5 in my case). This helps to mimic different browsers and reduce the chances of                   getting blocked. You can maintain a list of user-agents and use them in a sequential order.
        </li>
        <li><strong>Delay Requests: </strong>Introduce a delay between consecutive requests to simulate human-like behavior. Make sure               you have the AutoThrottle extension enabled in your settings, and it should handle the delay between requests for you. If                you're still experiencing issues with the 429 status code, you can try increasing the AUTOTHROTTLE_MAX_DELAY value to allow              for even longer delays between requests.
        </li>
        <li>
          <strong>Monitor Response Status: </strong>Check the response status codes returned by the website. If you consistently receive 429 status codes (Too Many Requests), it indicates that you are making too many requests in a short period. In such cases, you need to adjust the crawling speed, reduce the number of concurrent requests, or increase the delays between requests. In my case I have set it to 0.6 (i.e scrapy by default send 16 requests now it will send only 60% of this request so 9-10 requests will be sent concurrently).
        </li>
        <li>
          <strong>Request prioritization: </strong> In Scrapy, you can use the priority feature of Scrapy's Request objects. By assigning different priority values to your requests, you can control the order in which they are processed by the crawler.
        </li>
      </ul>   
  </li>
<li> <strong>Foundit.com: </strong>Foundit uses ip detection technique to protect against web scrapping. To scrape its content you cam use proxies and multiple user agent.
</li>
</ol>
<br>All the scraped files are attached in the folder. Also the proxies are replaced by default proxies.<br><br>

>**Please note that it's essential to respect the website's terms of service and robots.txt directives while scraping. Excessive scraping or ignoring rate limits can lead to IP blocking or other consequences.**

>**Remember, each website may have different anti-scraping mechanisms in place, and there is no one-size-fits-all solution. It's an ongoing process of experimentation and adjusting your spider's behavior to avoid detection and ensure successful scraping.**
