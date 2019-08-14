import sys
from env import test
from googleapiclient.discovery import build

if __name__ == "__main__":
    # status = sys.argv[1]
    # print(f"Updating status to: {status}")
    print(test)
    service = build()

    build(serviceName, version, http=None, discoveryServiceUrl=DISCOVERY_URI, developerKey=None, model=None, requestBuilder=HttpRequest, credentials=None, cache_discovery=True, cache=None)




