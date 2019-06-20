from imggrabber import imgScrape  # todo
# Search term
search = 'fidget spinner'
savename = 'fidget spinner imggrab'
fType = ''  # if you want all the files them make it empty string
debug = False

html = imgScrape.browser(imgScrape.build_url(search), debug)
data = imgScrape.imageLink(html)
imgScrape.saveImages(data, savename, fType)
