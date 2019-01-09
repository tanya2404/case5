import urllib.request

with open('input.txt', 'r') as f_in:
    links = f_in.readlines()
with open('output.txt', 'w') as f_out:
    for url in links:
        f = urllib.request.urlopen(url)
        text = str(f.read())
        part_name = text.find("player-name")
        name = text[text.find('>',part_name)+1:text.find('&',part_name)]
        player_totals = text.find('player-totals')
        stat = text[text.find('TOTAL',player_totals)+5:text.find('</tr>',player_totals)]
        trans_in = 'tdn\/<>'
        trans_out = '       '
        trans = ''.maketrans(trans_in, trans_out)
        stat = stat.translate(trans).split()
        f_out.write("{:20}{:7}{:7}{:10}{:7}{:7}{:7}\n".format(name, stat[0], stat[1], stat[3], stat[5], stat[6], stat[9]))
