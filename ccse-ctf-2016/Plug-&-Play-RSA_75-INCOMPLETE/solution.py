c = 'BX\xdc\xbcW\xd6\x02\xbd\\\xfb3&j\xa7>Ip\x02\x17\x8f_\x88\x83p\xaa&\x12j3\xf7\x12d\x87\xd7\xa5\xa5\xf1S\x8b\xad+\xb1\x8fs9\x1e\x1d\xdf\x97\xd7\x80\x982\xea\xca\xbaf\x19<!-\x8a\xa8P\x9b\xfb\xd1-T\x95\xbc\xc3\xb6\xc5A\x07aO\xd9%\xf9\x07\xe5J\xb5\x08n\x04N\xd7r\x89\x9e\xe1\x8c\xaa\x82@\x01DV\xe4\xc6\x13|\x89O\x9dR\xf1\xd3\x16\xc3|u\th\xf0\xc2\x02J\xb9R\xa6\xa0\xa3Q\xf7'

d = 24069549728215324577453307851521297949516475963050722703759362398862028631743382629854663003280168784010920627026063536479810282659439197543562907784279792726629500074357017285309193668857272383477490233966425871848873115363634986614342967222755431648953799658739091041422709670844736241145311803853079346241

p = 39175905369894602545622564633688109576881300396190403606195825113075511243224444388917515593723333063130647408827621922969525762377395782239885003810998225334414753

q = 2295782035886409121799876810984786026144067511904018840862463797635128365911123969631134191840510337863136189433062429033320846858767824087921423

n = p*q

print hex(d)[2:-1]
c = int(c.encode("hex"), 16)

m = pow(c, d, n)
print hex(m)[2:-1].decode("hex")