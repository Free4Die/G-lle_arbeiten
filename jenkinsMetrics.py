import urllib, json, sys

metrics = {}
JENKINS_URL = "CHANGE IT"
PLUGIN_KEY = "CHANGE IT"

def denormalize(data, keyname):
    for d in data.keys():
        if isinstance(data[d], dict):
            denormalize(data[d], u"%s%s." % (keyname, d))
        else:
            metrics[u"%s%s" % (keyname, d)] = data[d]

if __name__ == "__main__":

    response = urllib.urlopen("%s/metrics/%s/metrics" % (JENKINS_URL, PLUGIN_KEY));
    data = json.loads(response.read())

    denormalize(data, u"")

    if len(sys.argv) > 1 :
        print metrics[str(sys.argv[1])]
    else:
        for m in metrics:
            print "%s=%s" % (m, metrics[m])
