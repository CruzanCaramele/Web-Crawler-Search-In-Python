def get_page(url):
    # get_page procedure so that as to test the
    # code on  pages 
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""


def get_next_target(page):
    start_link = page.find('<a href=',0)
    
    #find the 1st quote using start_link value as the starting point for the search
    if start_link != -1:
        start_quote = page.find('"',start_link)
    
        #find the end quote of the url
        end_quote = page.find('"', start_quote + 1)
    
        #url link is character after star quote plus one until end quote
        url = page[start_quote+1:end_quote]
        return url, end_quote

    elif start_link == -1:
        return None, 0



def get_all_links(page):

    #variable to keep track of links on page
    links = []

    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]

        else:
            break
    return links



def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)



def add_to_index(index,keyword,url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]
        
    
    



def loop_up(index,keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None





def add_page_to_index(index,url,content):
    
    wording = content.split()
    for a_word in wording:
        add_to_index(index, a_word, url)




def crawl_web(seed_link):
    #variable that contains links to crawl
    to_crawl = [seed_link]

    #variable that keeps track of crawled links
    crawled = []

    #an emty dictionary variable tracking the links
    index = {}

    #a graph variable which is dictionary containing url's as keys
    #and mapped to nodes (values) which are lists of links to that page
    graph = {}

    while to_crawl:
        page = to_crawl.pop() #get the last link from to_crawl

        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            out_links = get_all_links(content)
            graph[page] = [out_links]
            union(to_crawl,out_links)
            crawled.append(page)
    return index, graph



def compute_ranks(graph):
    d = 0.8 # damping factor (probability of selecting the current page)
    num_loops = 10

    ranks = {}
    #number of pages obtainable from the graph
    num_pages = len(graph)#number of nodes = number of pages crawled

    for page in graph:
        rank[page] = 1.0 / num_pages

    for num in range(0, num_loops):
        new_ranks = {}
        for page in graph:
            new_rank = (1 - d) / num_pages
            for node in graph:
                if page in graph[node]:
                    new_rank = new_ranks + d * (ranks[node] / len(graph[node]))
            new_ranks[page] = new_rank
        ranks = new_ranks
    return ranks


print crawl_web("http://www.udacity.com")

















