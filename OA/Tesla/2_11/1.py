class UrlBuilder:

    def __init__(self):
        self.scheme = "http"
        self.hostStr = None
        self.portNum = None
        self.pathStr = None
        self.queryParams = None

    def https(self):
        self.scheme = "https"
        return self

    def http(self):
        self.scheme = "http"
        return self

    def host(self, hostInp):
        self.hostStr = hostInp
        return self

    def port(self, portInp):
        self.portNum = portInp
        return self

    def path(self, pathInp):
        self.pathStr = pathInp
        return self

    def queryParam(self, paramsInp):
        if paramsInp:
            self.queryParams = "&".join([f"{k}={v}" for k, v in paramsInp.items()])
        return self

    def build(self):
        url = f"{self.scheme}://"
        if self.hostStr:
            url += self.hostStr
        if self.portNum:
            url += f":{str(self.portNum)}"
        if self.pathStr:
            url += f"{self.pathStr}"
        if self.queryParams:
            url += f"?{self.queryParams}"
        return url


u = (
    UrlBuilder()
    .https()
    .host("www.google.com")
    .port(8080)
    .path("search")
    .queryParam({"q": "hello"})
    .build()
)
print(type(u))
url = (
    UrlBuilder()
    .https()
    .host("www.google.com")
    .port(8080)
    .path("/search")
    .queryParam({"q": "hello"})
    .build()
)
print(url)
print(
    UrlBuilder().port(8080).host("codility.com").https().build()
)  # https://codility.com:8080)
