"""

Given a URL startUrl and an interface HtmlParser, implement a Multi-threaded web crawler to crawl all links that are under the same hostname as startUrl.

Return all URLs obtained by your web crawler in any order.

Your crawler should:

Start from the page: startUrl
Call HtmlParser.getUrls(url) to get all URLs from a webpage of a given URL.
Do not crawl the same link twice.
Explore only the links that are under the same hostname as startUrl.

As shown in the example URL above, the hostname is example.org. For simplicity's sake, you may assume all URLs use HTTP protocol without any port specified. For example, the URLs http://leetcode.com/problems and http://leetcode.com/contest are under the same hostname, while URLs http://example.org/test and http://example.com/abc are not under the same hostname.

The HtmlParser interface is defined as such:

interface HtmlParser {
  // Return a list of all urls from a webpage of given url.
  // This is a blocking call, that means it will do HTTP request and return when this request is finished.
  public List<String> getUrls(String url);
}
Note that getUrls(String url) simulates performing an HTTP request. You can treat it as a blocking function call that waits for an HTTP request to finish. It is guaranteed that getUrls(String url) will return the URLs within 15ms. Single-threaded solutions will exceed the time limit so, can your multi-threaded web crawler do better?

Below are two examples explaining the functionality of the problem. For custom testing purposes, you'll have three variables urls, edges and startUrl. Notice that you will only have access to startUrl in your code, while urls and edges are not directly accessible to you in code.

 

Example 1:



Input:
urls = [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.google.com",
  "http://news.yahoo.com/us"
]
edges = [[2,0],[2,1],[3,2],[3,1],[0,4]]
startUrl = "http://news.yahoo.com/news/topics/"
Output: [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.yahoo.com/us"
]
Example 2:



Input: 
urls = [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.google.com"
]
edges = [[0,2],[2,1],[3,2],[3,1],[3,0]]
startUrl = "http://news.google.com"
Output: ["http://news.google.com"]
Explanation: The startUrl links to all other pages that do not share the same hostname.


https://leetcode.com/problems/web-crawler-multithreaded
"""


class Solution {
    
    private ExecutorService executor = Executors.newFixedThreadPool(6);
    private AtomicInteger activeTasks = new AtomicInteger();
    private HtmlParser htmlParser;
    private final Set<String> visited = Collections.synchronizedSet(new HashSet<>());
    private String domain;
    

    private class Task implements Runnable {
        
        String url;
        public Task(String url) {
            this.url = url;
        }
        
        @Override
        public void run() {
            for(String link : htmlParser.getUrls(url)) {

                if(link.split("/")[2].equals(domain) && visited.add(link)) {
                    activeTasks.incrementAndGet();
                    executor.execute(new Task(link));
                }

            }

            activeTasks.decrementAndGet();
        }
    }

    
    public List<String> crawl(String startUrl, HtmlParser htmlParser) {

         
        this.htmlParser = htmlParser;
        this.domain = startUrl.split("/")[2];


        visited.add(startUrl);
        activeTasks.set(1);
        executor.execute(new Task(startUrl));


        while(activeTasks.get() > 0) {
           try {
             Thread.sleep(80);
           } catch (Exception e) {
    
           }
        }


        executor.shutdownNow();
        return new ArrayList<>(visited);
    }
    
}