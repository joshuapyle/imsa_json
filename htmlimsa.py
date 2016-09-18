import json, requests
#from prettytable import *

#r = open("imsa_data.json","r") # read local file to avoid web hits
#r = r.read()

# Fetch the IMSA scoring json file and remove the leading and trailing characters to make a valid JSON file
r = requests.get("http://multimedia.netstorage.imsa.com/scoring_data/RaceResults_JSONP.json")
r = r.content.replace("jsonpRaceResults(","")
r = r.replace(");","")

data = json.loads(r)

# This section is to output the results, uncomment line 3, 36, and 40 to see results in the console
#racetable = PrettyTable(['Overall', 'In Class','Class','Behind Leader','Behind Next POS','Car #','Car Type','Driver','Last Lap','Best Lap','Pit Stops'])
#racetable.align = "r"
#racetable.align['Overall'] = "l"
#racetable.align['In Class'] = "l"
#racetable.align['Class'] = "l"
#racetable.align['Pit Stops'] = "c"

item_dict = json.loads(r)
r_max = len(item_dict['B']) - 2 # removing the last two entries as they are saftey cars

f = open('imsa.html', 'w')

print >> f, "<link rel=\"stylesheet\" type=\"text/css\" href=\"css\\css.css\">"
print >> f, "<link rel=\"stylesheet\" href=\"css\\css2.css\">"
print >> f, "<table class=\"pure-table pure-table-horizontal\"><tr><td>Car</td><td>Pos</td><td>Pos In Class</td><td>Car</td><td>Behind Leader</td><td>Behind Next Pos</td><td>Car #</td><td>Type</td><td>Driver</td><td>Last Lap</td><td>Best Lap</td><td>Pit Stops</td></tr>"

i = 1
for x in range(0, r_max):
	if data['B'][x]['C'] <> "PC":  # removing the PC class from the results
		print >> f, ("<tr  class=\"pure-table-odd\">" if i % 2 == 0 else "<tr>") + "<td><img src=images\\" + str(data['B'][x]['N']) + ".png width=223 height=75></img></td><td>" + str(x+1) + "</td><td>" + str(data['B'][x]['PIC']) + "</td><td>" +  str(data['B'][x]['C']) + "</td><td>" +  str(data['B'][x]['D']) + "</td><td>" +  str(data['B'][x]['G']) + "</td><td>" +  " #" + str(data['B'][x]['N']) + "</td><td>" +  str(data['B'][x]['V']) + "</td><td>" + str(data['B'][x]['F']) + "</td><td>" + str(data['B'][x]['LL']) + "</td><td>" + str(data['B'][x]['BL']) + "</td><td>" + str(data['B'][x]['PS'])+"</td></tr>"
		#racetable.add_row([str(x+1), str(data['B'][x]['PIC']), data['B'][x]['C'], data['B'][x]['D'], data['B'][x]['G'], " #" + data['B'][x]['N'], data['B'][x]['V'], data['B'][x]['F'], data['B'][x]['LL'],data['B'][x]['BL'],data['B'][x]['PS']])
		i = i+1 
f.close()

#print racetable