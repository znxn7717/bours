import requests, time, datetime
import pandas as pd
start = datetime.datetime.now()

def main():

    def time(id):
        req = requests.get(f'http://www.tsetmc.com/tsev2/data/instinfofast.aspx?{id}').text
        time = req.split(';')[0].split(',')[0]
        return time
    def price(id):
        req = requests.get(f'http://www.tsetmc.com/tsev2/data/instinfofast.aspx?{id}').text
        price = float(req.split(';')[0].split(',')[3])
        return price
    def lprice(id):
        req = requests.get(f'http://www.tsetmc.com/tsev2/data/instinfofast.aspx?{id}').text
        lprice = float(req.split(';')[0].split(',')[5])
        return lprice
    table = [['foulad', 11949, time('i=46348559193224090&c=27'), price('i=46348559193224090&c=27'), lprice('i=46348559193224090&c=27')], 
    ['palayesh', 100235, time('i=67675656072510693&c=68%20&e=1'), price('i=67675656072510693&c=68%20&e=1'), lprice('i=67675656072510693&c=68%20&e=1')],
    ['parsan', 40228, time('i=23441366113375722&c=44'), price('i=23441366113375722&c=44'), lprice('i=23441366113375722&c=44')],
    ['ariyan', 11100, time('i=6506179926371994&c=56'), price('i=6506179926371994&c=56'), lprice('i=6506179926371994&c=56')],
    ['fmeli', 8804, time('i=35425587644337450&c=27'), price('i=35425587644337450&c=27'), lprice('i=35425587644337450&c=27')],
    ['vsepehr', 12236, time('i=114312662654155&c=56'), price('i=114312662654155&c=56'), lprice('i=114312662654155&c=56')],
    ['shtran', 10011, time('i=51617145873056483&c=23'), price('i=51617145873056483&c=23'), lprice('i=51617145873056483&c=23')],
    ['bgilan', 24301, time('i=71068313834275501&c=40'), price('i=71068313834275501&c=40'), lprice('i=71068313834275501&c=40')],
    ['vbmellat', 5164, time('i=778253364357513&c=57'), price('i=778253364357513&c=57'), lprice('i=778253364357513&c=57')],
    ['vtousam', 9145, time('i=17528249960294496&c=56'), price('i=17528249960294496&c=56'), lprice('i=17528249960294496&c=56')],
    ['vtejarat', 3939, time('i=63917421733088077&c=57'), price('i=63917421733088077&c=57'), lprice('i=63917421733088077&c=57')],
    ['vpars', 4395, time('i=33293588228706998&c=57'), price('i=33293588228706998&c=57'), lprice('i=33293588228706998&c=57')],
    ['vbsader', 4405, time('i=28320293733348826&c=57'), price('i=28320293733348826&c=57'), lprice('i=28320293733348826&c=57')],
    ['ap', 18464, time('i=55254206302462116&c=72'), price('i=55254206302462116&c=72'), lprice('i=55254206302462116&c=72')],
    ['chkarn', 10825, time('i=53113471126689455&c=21'), price('i=53113471126689455&c=21'), lprice('i=53113471126689455&c=21')],
    ]
    df = pd.DataFrame(table, columns=['symbol', 'purched price', 'time', 'last price', 'l price'])
    df['PNL%'] = ((df['last price'] - df['purched price']) / df['purched price'] * 100).round(3)
    df['lPNL%'] = ((df['l price'] - df['purched price']) / df['purched price'] * 100).round(3)
    df['l2PNL%'] = (df['PNL%'] - df['lPNL%']).round(3)
    df = df.sort_values(by=['PNL%'], ignore_index=True)
    print(df[['symbol', 'last price', 'time', 'PNL%']])


if __name__ == '__main__':
    while True:
        try:
            main()
            print('\nRun time: ', (datetime.datetime.now() - start))
        except Exception as e:
            print(e)
            time.sleep(1)